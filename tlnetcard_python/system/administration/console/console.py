""" Allows for console settings to be configured. """

# Standard library.
from os.path import isfile
from warnings import warn
# Required internal classes/functions.
from tlnetcard_python.login import Login

class Console:
    """ Class for the Console object. """
    def __init__(self, login_object: Login) -> None:
        """ Initializes the Console object. """
        self._login_object = login_object
        self._get_url = login_object.get_base_url() + "/en/adm_console.asp"
        self._post_url = login_object.get_base_url() + "/delta/adm_console"
    def disable_ssh(self) -> None:
        """ Disables SSH. """
        # Generating payload.
        console_data = {
            "CON_SSH": "0"
        }

        # Uploading console configuration and requesting system config renewal.
        self._login_object.get_session().post(self._post_url, data=console_data,
                                              timeout=self._login_object.get_timeout(),
                                              verify=self._login_object.get_reject_invalid_certs()
                                              ).raise_for_status()
        self._login_object.request_system_config_renewal()
    def disable_telnet(self) -> None:
        """ Disables Telnet. """
        # Generating payload.
        console_data = {
            "CON_TELNET": "0"
        }

        # Uploading console configuration and requesting system config renewal.
        self._login_object.get_session().post(self._post_url, data=console_data,
                                              timeout=self._login_object.get_timeout(),
                                              verify=self._login_object.get_reject_invalid_certs()
                                              ).raise_for_status()
        self._login_object.request_system_config_renewal()
    def enable_ssh(self) -> None:
        """ Enables SSH. """
        # Generating payload.
        console_data = {
            "CON_SSH": "1"
        }

        # Uploading console configuration and requesting system config renewal.
        self._login_object.get_session().post(self._post_url, data=console_data,
                                              timeout=self._login_object.get_timeout(),
                                              verify=self._login_object.get_reject_invalid_certs()
                                              ).raise_for_status()
        self._login_object.request_system_config_renewal()
    def enable_telnet(self) -> None:
        """ Enables Telnet. """
        # Generating payload.
        console_data = {
            "CON_TELNET": "1"
        }

        # Uploading console configuration and requesting system config renewal.
        self._login_object.get_session().post(self._post_url, data=console_data,
                                              timeout=self._login_object.get_timeout(),
                                              verify=self._login_object.get_reject_invalid_certs()
                                              ).raise_for_status()
        self._login_object.request_system_config_renewal()
    def get_ssh_port(self) -> int:
        """ GETs the port in use for SSH. """
        # GETing system config.
        system_config = self._login_object.get_system_config()

        # Parsing config for SSH port.
        if "SSH Port" in system_config:
            return int(system_config["SSH Port"])
        return -1
    def get_telnet_port(self) -> int:
        """ GETs the port in use for Telnet. """
        # GETing system config.
        system_config = self._login_object.get_system_config()

        # Parsing config for telnet port.
        if "Telnet Port" in system_config:
            return int(system_config["Telnet Port"])
        return -1
    def set_ssh_port(self, port=22) -> None:
        """ Sets the port for use by SSH. """
        # Generating payload.
        console_data = {
            "CON_SSH": "1",
            "CON_PORT_SSH": str(port)
        }

        # Uploading console configuration and requesting system config renewal.
        self._login_object.get_session().post(self._post_url, data=console_data,
                                              timeout=self._login_object.get_timeout(),
                                              verify=self._login_object.get_reject_invalid_certs()
                                              ).raise_for_status()
        self._login_object.request_system_config_renewal()
    def set_telnet_port(self, port=23) -> None:
        """ Sets the port for use by Telnet. """
        # Generating payload.
        console_data = {
            "CON_TELNET": "1",
            "CON_PORT_TELNET": str(port)
        }

        # Uploading console configuration and requesting system config renewal.
        self._login_object.get_session().post(self._post_url, data=console_data,
                                              timeout=self._login_object.get_timeout(),
                                              verify=self._login_object.get_reject_invalid_certs()
                                              ).raise_for_status()
        self._login_object.request_system_config_renewal()
    def upload_auth_public_key(self, key: str) -> bool:
        """ Uploads the provided authentication public key. """
        # Testing if the file specified in path exists.
        if not isfile(key):
            warn("Specified key file does not exist!", FileNotFoundError)
            return False

        # Creating upload payload.
        upload_data = {
            'OK': 'Submit'
        }
        upload_file = {
            'CON_PUB': (key.split("/")[-1], open(key, 'rb'), 'multipart/form-data'),
        }

        # Uploading public authentication key.
        self._login_object.get_session().post(self._post_url, data=upload_data, files=upload_file,
                                              timeout=self._login_object.get_timeout(),
                                              verify=self._login_object.get_reject_invalid_certs()
                                              ).raise_for_status()
        return True
    def upload_dsa_host_key(self, key: str) -> bool:
        """ Uploads the provided DSA host key. """
        # Testing if the file specified in path exists.
        if not isfile(key):
            warn("Specified key file does not exist!", FileNotFoundError)
            return False

        # Creating upload payload.
        upload_data = {
            'OK': 'Submit'
        }
        upload_file = {
            'CON_DSA': (key.split("/")[-1], open(key, 'rb'), 'multipart/form-data'),
        }

        # Uploading DSA key.
        self._login_object.get_session().post(self._post_url, data=upload_data, files=upload_file,
                                              timeout=self._login_object.get_timeout(),
                                              verify=self._login_object.get_reject_invalid_certs()
                                              ).raise_for_status()
        return True
    def upload_rsa_host_key(self, key: str) -> bool:
        """ Uploads the provided RSA host key. """
        # Testing if the file specified in path exists.
        if not isfile(key):
            warn("Specified key file does not exist!", FileNotFoundError)
            return False

        # Creating upload payload.
        upload_data = {
            'OK': 'Submit'
        }
        upload_file = {
            'CON_RSA': (key.split("/")[-1], open(key, 'rb'), 'multipart/form-data'),
        }

        # Uploading DSA key.
        self._login_object.get_session().post(self._post_url, data=upload_data, files=upload_file,
                                              timeout=self._login_object.get_timeout(),
                                              verify=self._login_object.get_reject_invalid_certs()
                                              ).raise_for_status()
        return True
