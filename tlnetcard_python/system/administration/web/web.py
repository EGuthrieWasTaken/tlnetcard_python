""" Allows web host settings to be configured. """

# Standard library.
from os.path import isfile
from warnings import warn
# Required internal classes/functions.
from tlnetcard_python.login import Login

class Web:
    """ Class for the Web object. """
    def __init__(self, login_object: Login) -> None:
        """ Initializes the Web object. """
        self._login_object = login_object
        self._get_url = login_object.get_base_url() + "/en/adm_web.asp"
        self._post_url = login_object.get_base_url() + "/delta/adm_web"
    def disable_http(self) -> None:
        """ Disables HTTP access. """
        # Generating payload.
        web_data = {
            "WEB_HTTP": "0"
        }

        # Uploading web configuration and requesting system config renewal.
        self._login_object.get_session().post(self._post_url, data=web_data,
                                              timeout=self._login_object.get_timeout(),
                                              verify=self._login_object.get_reject_invalid_certs()
                                              ).raise_for_status()
        self._login_object.request_system_config_renewal()
    def disable_https(self) -> None:
        """ Disables HTTPS access. """
        # Generating payload.
        web_data = {
            "WEB_HTTPS": "0"
        }

        # Uploading web configuration and requesting system config renewal.
        self._login_object.get_session().post(self._post_url, data=web_data,
                                              timeout=self._login_object.get_timeout(),
                                              verify=self._login_object.get_reject_invalid_certs()
                                              ).raise_for_status()
        self._login_object.request_system_config_renewal()
    def enable_http(self) -> None:
        """ Enables HTTP access. """
        # Generating payload.
        web_data = {
            "WEB_HTTP": "1"
        }

        # Uploading web configuration and requesting system config renewal.
        self._login_object.get_session().post(self._post_url, data=web_data,
                                              timeout=self._login_object.get_timeout(),
                                              verify=self._login_object.get_reject_invalid_certs()
                                              ).raise_for_status()
        self._login_object.request_system_config_renewal()
    def enable_https(self) -> None:
        """ Enables HTTPS access. """
        # Generating payload.
        web_data = {
            "WEB_HTTPS": "1"
        }

        # Uploading web configuration and requesting system config renewal.
        self._login_object.get_session().post(self._post_url, data=web_data,
                                              timeout=self._login_object.get_timeout(),
                                              verify=self._login_object.get_reject_invalid_certs()
                                              ).raise_for_status()
        self._login_object.request_system_config_renewal()
    def get_http_port(self) -> int:
        """ GETs the port in use for HTTP. """
        # GETing system config.
        system_config = self._login_object.get_system_config()

        # Parsing config for HTTP port.
        if "HTTP Port" in system_config:
            return int(system_config["HTTP Port"])
        return -1
    def get_https_port(self) -> int:
        """ GETs the port in use for HTTPS. """
        # GETing system config.
        system_config = self._login_object.get_system_config()

        # Parsing config for HTTPS port.
        if "HTTPS Port" in system_config:
            return int(system_config["HTTPS Port"])
        return -1
    def get_web_refresh(self) -> int:
        """ GETs the web refresh time in seconds. """
        # GETing system config.
        system_config = self._login_object.get_system_config()

        # Parsing config for web refresh time.
        if "Web Refresh" in system_config:
            return int(system_config["Web Refresh"])
        return -1
    def set_http_port(self, port: int = 80) -> None:
        """ Sets the port for use by HTTP. """
        # Generating payload.
        web_data = {
            "WEB_HTTP": "1",
            "WEB_PORT_HTTP": str(port)
        }

        # Uploading web configuration and requesting system config renewal.
        self._login_object.get_session().post(self._post_url, data=web_data,
                                              timeout=self._login_object.get_timeout(),
                                              verify=self._login_object.get_reject_invalid_certs()
                                              ).raise_for_status()
        self._login_object.request_system_config_renewal()
    def set_https_port(self, port: int = 443) -> None:
        """ Sets the port for use by HTTPS. """
        # Generating payload.
        web_data = {
            "WEB_HTTPS": "1",
            "WEB_PORT_HTTPS": str(port)
        }

        # Uploading web configuration and requesting system config renewal.
        self._login_object.get_session().post(self._post_url, data=web_data,
                                              timeout=self._login_object.get_timeout(),
                                              verify=self._login_object.get_reject_invalid_certs()
                                              ).raise_for_status()
        self._login_object.request_system_config_renewal()
    def set_web_refresh(self, seconds: int = 10) -> bool:
        """ Sets the web refresh time to ```seconds``` seconds. """
        # Generating payload.
        web_data = {
            "WEB_REFRESH": str(seconds)
        }

        # Uploading web configuration and requesting system config renewal.
        self._login_object.get_session().post(self._post_url, data=web_data,
                                              timeout=self._login_object.get_timeout(),
                                              verify=self._login_object.get_reject_invalid_certs()
                                              ).raise_for_status()
        self._login_object.request_system_config_renewal()
    def upload_ssl_cert(self, path: str) -> int:
        """ Uploads the provided SSL certificate. """
        # Testing if the file specified in path exists.
        if not isfile(path):
            warn("Specified PEM file does not exist!", FileNotFoundError)
            return False

        # Creating upload payload.
        upload_data = {
            'OK': 'Submit'
        }
        upload_file = {
            'WEB_SSLCERT': (path.split("/")[-1], open(path, 'rb'), 'multipart/form-data'),
        }

        # Uploading SSL certificate.
        self._login_object.get_session().post(self._post_url, data=upload_data, files=upload_file,
                                              timeout=self._login_object.get_timeout(),
                                              verify=self._login_object.get_reject_invalid_certs()
                                              ).raise_for_status()
        return True
