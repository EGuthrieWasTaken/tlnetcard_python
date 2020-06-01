# batch_configuration.py
# Ethan Guthrie
# 04/14/2020
""" Allows batch configurations for SNMP or system settings to be uploaded or downloaded. """

# Standard library.
from os.path import isfile
from pathlib import Path
from platform import system
# Required internal classes/functions.
from tlnetcard_python.login import Login

class BatchConfiguration:
    """ Class for the BatchConfiguration object. """
    def __init__(self, login_object: Login) -> None:
        """ Initializes the BatchConfiguration object. """
        self._login_object = login_object
        self._post_url = login_object.get_base_url() + "/delta/adm_batch"
    def download_snmp_configuration(self, path: str = None, no_write: bool = False) -> str:
        """ Downloads the SNMP configuration and saves it to the specified file. """
        # Setting path to downloads directory for operating system if no path was specified.
        if path is None and not no_write:
            path = str(Path.home())
            if system() == "Windows":
                path += "\\Downloads\\snmp_config.ini"
            else:
                path += "/Downloads/snmp_config.ini"

        # Creating download payload.
        download_data = {
            'DL_SNMP': 'Download'
        }

        # Submitting download request.
        verify = self._login_object.get_reject_invalid_certs()
        data = self._login_object.get_session().post(self._post_url, data=download_data,
                                                     port=self._login_object.get_port(),
                                                     timeout=self._login_object.get_timeout(),
                                                     verify=verify).raise_for_status()
        # Returning raw configuration data if no_write was set to True.
        if no_write:
            return data.text
        # Otherwise writing configuration data to file an returning the file path.
        with open(path, "w") as out_file:
            out_file.write(data.text)
        return path
    def download_system_configuration(self, path: str = None, no_write: bool = False) -> None:
        """ Downloads the system configuration and saves it to the specified file. """
        # Setting path to downloads directory for operating system if no path was specified.
        if path is None and not no_write:
            path = str(Path.home())
            if system() == "Windows":
                path += "\\Downloads\\system_config.ini"
            else:
                path += "/Downloads/system_config.ini"

        # Creating download payload.
        download_data = {
            'DL_SYSTEM': 'Download'
        }

        # Submitting download request.
        verify = self._login_object.get_reject_invalid_certs()
        data = self._login_object.get_session().post(self._post_url, data=download_data,
                                                     port=self._login_object.get_port(),
                                                     timeout=self._login_object.get_timeout(),
                                                     verify=verify).raise_for_status()
        # Returning raw configuration data if no_write was set to True.
        if no_write:
            return data.text
        # Otherwise writing configuration data to file an returning the file path.
        with open(path, "w") as out_file:
            out_file.write(data.text)
        return path
    def upload_snmp_configuration(self, path: str = "snmp_config.ini") -> int:
        """ Uploads the specified SNMP configuration file. """
        # Testing if the file specified in path exists.
        if not isfile(path):
            print("Specified configuration file does not exist!")
            return -1

        # Creating upload payload.
        upload_data = {
            'UL_SNMP': 'Upload'
        }
        upload_file = {
            'UL_F_SNMP': (path.split("/")[-1], open(path, 'rb'), 'multipart/form-data'),
        }

        # Uploading SNMP configuration and requesting SNMP config renewal.
        self._login_object.get_session().post(self._post_url, data=upload_data, files=upload_file,
                                              port=self._login_object.get_port(),
                                              timeout=self._login_object.get_timeout(),
                                              verify=self._login_object.get_reject_invalid_certs()
                                              ).raise_for_status()
        print("NOTE: The card at " + self._login_object.get_base_url()
              + " will be offline for approximately 10 seconds.")
        self._login_object.request_snmp_config_renewal()
        return 0
    def upload_system_configuration(self, path: str = "system_config.ini") -> int:
        """ Uploads the specified system configuration file. """
        # Testing if the file specified in path exists.
        if not isfile(path):
            print("Specified configuration file does not exist!")
            return -1

        # Creating upload payload.
        upload_data = {
            'UL_SYSTEM': 'Upload'
        }
        upload_file = {
            'UL_F_SYSTEM': (path.split("/")[-1], open(path, 'rb'), 'multipart/form-data'),
        }

        # Uploading system configuration and requesting system config renewal.
        self._login_object.get_session().post(self._post_url, data=upload_data, files=upload_file,
                                              port=self._login_object.get_port(),
                                              timeout=self._login_object.get_timeout(),
                                              verify=self._login_object.get_reject_invalid_certs()
                                              ).raise_for_status()
        print("NOTE: The card at " + self._login_object.get_base_url()
              + " will be offline for approximately 10 seconds.")
        self._login_object.request_system_config_renewal()
        return 0
