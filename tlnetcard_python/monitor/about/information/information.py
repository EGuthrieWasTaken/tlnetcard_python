# information.py
# Ethan Guthrie
# 05/13/2020
""" Allows the firmware version for the TLNETCARD to be retreived. """

# Required internal classes/functions.
from tlnetcard_python.login import Login

# pylint: disable=too-few-public-methods
class Information:
    """ Class for the Information object. """
    def __init__(self, login_object: Login) -> None:
        """ Initializes the BatchConfiguration object. """
        self._login_object = login_object
        self._get_url = login_object.get_base_url() + "/en/ups/about_info.asp"
    def get_firmware_version(self) -> str:
        """ GETs the current firmware version. """
        # GETing Information page.
        verify = self._login_object.get_reject_invalid_certs()
        resp = self._login_object.get_session().get(self._get_url,
                                                    timeout=self._login_object.get_timeout(),
                                                    verify=verify)
        resp.raise_for_status()

        # Parsing response for firmware version.
        start_index = str(resp.text).find("Version : ") + 10
        end_index = str(resp.text).find("\n", start_index)
        return resp.text[start_index:end_index]
