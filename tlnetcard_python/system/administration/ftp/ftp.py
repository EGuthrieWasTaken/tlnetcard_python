# ftp.py
# Ethan Guthrie
# 05/01/2020
""" Allows FTP settings to be configured. """

# Required internal classes/functions.
from tlnetcard_python.login import Login

class Ftp:
    """ Class for the Ftp object. """
    def __init__(self, login_object: Login) -> None:
        """ Initialize Ftp object. """
        self._login_object = login_object
        self._get_url = login_object.get_base_url() + "/en/adm_ftp.asp"
        self._post_url = login_object.get_base_url() + "/delta/adm_ftp"
    def disable_ftp(self) -> None:
        """ Disables FTP. """
        # Generating payload.
        ftp_data = {
            "FTP_FTP": "0",
        }

        # Uploading FTP configuration and requesting system config renewal.
        self._login_object.get_session().post(self._post_url, data=ftp_data,
                                              timeout=self._login_object.get_timeout(),
                                              verify=self._login_object.get_reject_invalid_certs()
                                              ).raise_for_status()
        self._login_object.request_system_config_renewal()
    def enable_ftp(self) -> None:
        """ Enables FTP. """
        # Generating payload.
        ftp_data = {
            "FTP_FTP": "1",
        }

        # Uploading FTP configuration and requesting system config renewal.
        self._login_object.get_session().post(self._post_url, data=ftp_data,
                                              timeout=self._login_object.get_timeout(),
                                              verify=self._login_object.get_reject_invalid_certs()
                                              ).raise_for_status()
        self._login_object.request_system_config_renewal()
    def get_ftp_port(self) -> int:
        """ GETs the port in use for FTP. """
        # GETing system config.
        system_config = self._login_object.get_system_config()

        # Parsing config for FTP port.
        if "FTP Port" in system_config:
            return int(system_config["FTP Port"])
        return -1
    def set_ftp_port(self, port: int = 21) -> None:
        """ Sets the port for use by FTP. """
        # Generating payload.
        ftp_data = {
            "FTP_FTP": "1",
            "FTP_PORT_FTP": str(port),
        }

        # Uploading FTP configuration and requesting system config renewal.
        self._login_object.get_session().post(self._post_url, data=ftp_data,
                                              timeout=self._login_object.get_timeout(),
                                              verify=self._login_object.get_reject_invalid_certs()
                                              ).raise_for_status()
        self._login_object.request_system_config_renewal()
