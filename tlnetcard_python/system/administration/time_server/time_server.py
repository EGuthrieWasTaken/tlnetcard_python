# time_server.py
# Ethan Guthrie
# 04/17/2020
""" Allows TimeServer to be updated or removed (i.e. switch to manual time). """

# Required internal classes/functions.
from tlnetcard_python.login import Login

class TimeServer:
    """ Class for the TimeServer object. """
    def __init__(self, login_object: Login) -> None:
        """ Initializes the TimeServer object. """
        self._login_object = login_object
        self._get_url = login_object.get_base_url() + "/en/adm_time.asp"
        self._post_url = login_object.get_base_url() + "/delta/adm_time"
    def disable_daylight_savings(self) -> None:
        """ Disables daylight savings for SNTP. """
        # Generating payload.
        time_server_data = {
            "NTP_MANU": "0",
            "NTP_DLS_EN": "0"
        }

        # Uploading time server configuration and requesting system config renewal.
        self._login_object.get_session().post(self._post_url, data=time_server_data,
                                              timeout=self._login_object.get_timeout(),
                                              verify=self._login_object.get_reject_invalid_certs()
                                              ).raise_for_status()
        self._login_object.request_system_config_renewal()
    def disable_sntp(self) -> None:
        """ Disables SNTP. """
        # Generating payload.
        time_server_data = {
            "NTP_MANU": "1"
        }

        # Uploading time server configuration and requesting system config renewal.
        self._login_object.get_session().post(self._post_url, data=time_server_data,
                                              timeout=self._login_object.get_timeout(),
                                              verify=self._login_object.get_reject_invalid_certs()
                                              ).raise_for_status()
        self._login_object.request_system_config_renewal()
    def enable_daylight_savings(self, start_date: str = "04/01", end_date: str = "11/01") -> None:
        """ Enables daylight savings from the start date to the end date for SNTP. """
        # Generating payload.
        time_server_data = {
            "NTP_MANU": "0",
            "NTP_DLS_EN": "1",
            "NTP_DLS_SDATE": start_date,
            "NTP_DLS_EDATE": end_date
        }

        # Uploading time server configuration and requesting system config renewal.
        self._login_object.get_session().post(self._post_url, data=time_server_data,
                                              timeout=self._login_object.get_timeout(),
                                              verify=self._login_object.get_reject_invalid_certs()
                                              ).raise_for_status()
        self._login_object.request_system_config_renewal()
    def enable_sntp(self) -> None:
        """ Enables SNTP. """
        # Generating payload.
        time_server_data = {
            "NTP_MANU": "0"
        }

        # Uploading time server configuration and requesting system config renewal.
        self._login_object.get_session().post(self._post_url, data=time_server_data,
                                              timeout=self._login_object.get_timeout(),
                                              verify=self._login_object.get_reject_invalid_certs()
                                              ).raise_for_status()
        self._login_object.request_system_config_renewal()
    def get_primary_server(self) -> str:
        """ GETs the primary time server for SNTP and returns it. """
        # GETing system config.
        system_config = self._login_object.get_system_config()

        # Parsing config for primary SNTP server.
        for line in system_config:
            if line.find("Server1") != -1:
                return line.split("=")[1]
        return ""
    def get_secondary_server(self) -> str:
        """ GETs the secondary time server for SNTP and returns it. """
        # GETing system config.
        system_config = self._login_object.get_system_config()

        # Parsing config for secondary SNTP server.
        for line in system_config:
            if line.find("Server2") != -1:
                return line.split("=")[1]
        return ""
    def set_manual_time(self, date: str = "01/01/2000", time: str = "00:00:00") -> None:
        """ Sets the time manually. """
        # Generating payload.
        time_server_data = {
            "NTP_MANU": "1",
            "NTP_USE_PCTIME": "0",
            "NTP_SYSDATE": date,
            "NTP_SYSTIME": time
        }

        # Uploading time server configuration and requesting system config renewal.
        self._login_object.get_session().post(self._post_url, data=time_server_data,
                                              timeout=self._login_object.get_timeout(),
                                              verify=self._login_object.get_reject_invalid_certs()
                                              ).raise_for_status()
        self._login_object.request_system_config_renewal()
    def set_primary_server(self, server: str) -> None:
        """ Sets the primary time server for SNTP. """
        # Generating payload.
        time_server_data = {
            "NTP_MANU": "0",
            "NTP_IP1": server
        }

        # Uploading time server configuration and requesting system config renewal.
        self._login_object.get_session().post(self._post_url, data=time_server_data,
                                              timeout=self._login_object.get_timeout(),
                                              verify=self._login_object.get_reject_invalid_certs()
                                              ).raise_for_status()
        self._login_object.request_system_config_renewal()
    def set_secondary_server(self, server: str) -> None:
        """ Sets the secondary time server for SNTP. """
        # Generating payload.
        time_server_data = {
            "NTP_MANU": "0",
            "NTP_IP2": server
        }

        # Uploading time server configuration and requesting system config renewal.
        self._login_object.get_session().post(self._post_url, data=time_server_data,
                                              timeout=self._login_object.get_timeout(),
                                              verify=self._login_object.get_reject_invalid_certs()
                                              ).raise_for_status()
        self._login_object.request_system_config_renewal()
    def set_time_zone(self, offset: str = "GMT") -> int:
        """ Sets the time zone for SNTP. """
        # Converting string to list value.
        offsets = ["GMT-12", "GMT-11", "GMT-10", "GMT-09", "GMT-08", "GMT-07",
                   "GMT-06", "GMT-05", "GMT-04", "GMT-03:30", "GMT-03", "GMT-02",
                   "GMT-01", "GMT", "GMT+01", "GMT+02", "GMT+03", "GMT+03:30",
                   "GMT+04", "GMT+05", "GMT+05:30", "GMT+06", "GMT+07", "GMT+08",
                   "GMT+09", "GMT+10", "GMT+11", "GMT+12"]
        zone = -1
        for i in range(0, len(offsets)):
            if offset == offsets[i]:
                zone = i
                break

        # Checking if zone value was set (otherwise an improper offset value was provided).
        if zone == -1:
            print("Invalid time zone specified!")
            return -1

        # Generating payload.
        time_server_data = {
            "NTP_MANU": "0",
            "NTP_ZONE": str(zone)
        }

        # Uploading time server configuration and requesting system config renewal.
        self._login_object.get_session().post(self._post_url, data=time_server_data,
                                              timeout=self._login_object.get_timeout(),
                                              verify=self._login_object.get_reject_invalid_certs()
                                              ).raise_for_status()
        self._login_object.request_system_config_renewal()
        return 0
    def use_local_time(self) -> None:
        """ Sets the manual time to this PC's time. """
        # Generating payload.
        time_server_data = {
            "NTP_MANU": "1",
            "NTP_USE_PCTIME": "1"
        }

        # Uploading time server configuration and requesting system config renewal.
        self._login_object.get_session().post(self._post_url, data=time_server_data,
                                              timeout=self._login_object.get_timeout(),
                                              verify=self._login_object.get_reject_invalid_certs()
                                              ).raise_for_status()
        self._login_object.request_system_config_renewal()
