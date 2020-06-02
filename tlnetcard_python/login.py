# login.py
# Ethan Guthrie
# 02/17/2020
""" Creates a logged-in session to the specified TLNETCARD using the provided credentials. """

# Standard library.
from getpass import getpass
from hashlib import md5
from typing import Dict
from warnings import filterwarnings, warn
# Related third-party library.
from requests import Session
from urllib3.exceptions import InsecureRequestWarning
# Importing BatchConfiguration module to access configuration files.
# pylint: disable=line-too-long
import tlnetcard_python.system.administration.batch_configuration.batch_configuration as batch_configuration
# pylint: enable=line-too-long

class Login:
    """ Class for the login object. A login object is required by all classes in this repository."""
    # pylint: disable=too-many-arguments,too-many-instance-attributes
    def __init__(self, user: str = "admin", passwd: str = "password", host: str = "",
                 save_passwd: bool = False, ssl: bool = True,
                 reject_invalid_certs: bool = True, timeout: float = 10.0, port: int = None
                 ) -> None:
        """ Initializes the login object. """
        # Saving values which will be used independently.
        self._host = host
        self._user = user
        self._reject_invalid_certs = reject_invalid_certs
        self._save_passwd = save_passwd
        self._ssl = ssl
        self._timeout = timeout
        # Setting port.
        if self._ssl and port is None:
            self._port = 443
        elif not self._ssl and port is None:
            self._port = 80
        else:
            self._port = port
        # Checking to see if password should be saved.
        if self._save_passwd:
            self._passwd = passwd
        else:
            self._passwd = ""
        # Executing login if a host was specified.
        if self._host != "":
            self._perform_login(passwd)
        # Initializing system/snmp config list variables.
        self._snmp_config = {}
        self._system_config = {}
        self._renew_snmp = True
        self._renew_system = True
    def get_base_url(self) -> str:
        """ Returns the base URL for TLNET Supervisor. """
        # Generating base URL.
        if self._ssl:
            base_url = 'https://' + self._host + ":" + str(self._port)
        else:
            base_url = 'http://' + self._host + ":" + str(self._port)
        return base_url
    def get_host(self) -> str:
        """ Returns the host. """
        return self._host
    def get_port(self) -> int:
        """ Returns the port number. """
        return self._port
    def get_reject_invalid_certs(self) -> bool:
        """ Returns whether to accept invalid SSL certificates
        (i.e. self-signed SSL certificates). """
        return self._reject_invalid_certs
    def get_session(self) -> Session:
        """ Returns the session. """
        return self._session
    def get_snmp_config(self, force: bool = False) -> Dict[str, str]:
        """ Triggers the API to pull a new version of SNMP config file if required and returns the
        configuration as a dictionary. """
        # Checking if a snmp config is required or forced and returning if neither.
        if not self._renew_snmp and not force:
            return self._snmp_config
        # Otherwise initializing BatchConfiguration object pulling new SNMP config.
        batch_object = batch_configuration.BatchConfiguration(self)
        snmp_config = batch_object.download_snmp_configuration(no_write=True).split('\n')
        # Clearing existing SNMP config and writing new config.
        self._snmp_config.clear()
        for i in snmp_config:
            if "=" in i:
                info = i.split("+")
                self._snmp_config[info[0]] = info[1]
        # Resetting _renew_snmp variable to False.
        self._renew_snmp = False
        return self._snmp_config
    def get_system_config(self, force: bool = False) -> Dict[str, str]:
        """ Triggers the API to pull a new version of system config file if required and returns the
        configuration as a dictionary. """
        # Checking if a system config is required or forced and returning if neither.
        if not self._renew_system and not force:
            return self._system_config
        # Otherwise initializing BatchConfiguration object pulling new system config.
        batch_object = batch_configuration.BatchConfiguration(self)
        system_config = batch_object.download_system_configuration(no_write=True).split('\n')
        # Clearing existing system config and writing new config.
        self._system_config.clear()
        for i in system_config:
            if "=" in i:
                info = i.split("+")
                self._system_config[info[0]] = info[1]
        # Resetting _renew_system variable to False.
        self._renew_system = False
        return self._system_config
    def get_timeout(self) -> float:
        """ Returns the timeout value. """
        return self._timeout
    def logout(self) -> None:
        """ Closes the session. """
        # Restoring warnings in case reject_invalid_certs flag is used.
        filterwarnings("default", category=InsecureRequestWarning)
        self._session.close()
    def _perform_login(self, passwd: str) -> bool:
        """ Logs into a new session. """
        # Ignoring self-signed SSL certificate warning when reject_invalid_certs is False.
        if not self._reject_invalid_certs:
            filterwarnings("ignore", category=InsecureRequestWarning)

        # Setting login URLs for future use.
        login_get_url = self.get_base_url() + '/home.asp'
        login_post_url = self.get_base_url() + '/delta/login'

        # Initializing session (to provide login persistence).
        session = Session()

        # Getting login screen HTML (so that Challenge can be retrieved).
        login_screen = session.get(login_get_url, timeout=self._timeout,
                                   verify=self._reject_invalid_certs)
        login_screen.raise_for_status()

        # Retrieving challenge from HTML.
        challenge_loc = login_screen.text.find('name="Challenge"')
        challenge = str(login_screen.text[challenge_loc + 24:challenge_loc + 32])

        # Generating 'Response' value (see login screen HTML for more details).
        response_str = self._user + passwd + challenge
        response = md5(response_str.encode('utf-8')).hexdigest()

        # Creating login payload.
        login_data = {
            'Username': self._user,
            'password': passwd,
            'Submitbtn': '      OK      ',
            'Challenge': challenge,
            'Response': response
        }

        # Logging in.
        session.post(login_post_url, data=login_data, timeout=self._timeout,
                     verify=self._reject_invalid_certs).raise_for_status()

        # Checking if login was successful.
        login_response = session.get(login_get_url, timeout=self._timeout,
                                     verify=self._reject_invalid_certs)
        login_response.raise_for_status()
        if login_response.text.find("login_title") != -1:
            warn("login failed for host at URL " + self._host, RuntimeWarning)
            session.close()
            return False

        # Saving session.
        self._session = session
        return True
    def request_snmp_config_renewal(self) -> None:
        """ Sets the _renew_snmp attribute to True so that the next call to get_snmp_config() will
        trigger a re-pull of the SNMP config file. """
        self._renew_snmp = True
    def request_system_config_renewal(self) -> None:
        """ Sets the _renew_system attribute to True so that the next call to get_system_config()
        will trigger a re-pull of the system config file. """
        self._renew_system = True
    def set_host(self, host: str, passwd: str = "") -> None:
        """ Sets host and then calls _perform_login(). """
        # Closing previous session (if there was one).
        if self._host != "":
            self.logout()
        # Saving host value.
        self._host = host

        # Checking if password was provided or if password was saved, and then logging in.
        if passwd != "":
            self._perform_login(passwd)
        elif self._save_passwd:
            self._perform_login(self._passwd)
        else:
            passwd = getpass()
            if self._save_passwd:
                self._passwd = passwd
            self._perform_login(passwd)
