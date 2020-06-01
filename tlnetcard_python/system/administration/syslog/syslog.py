# syslog.py
# Ethan Guthrie
# 04/16/2020
""" Allows syslog servers to be added or removed. """

# Standard library.
from typing import List
# Required internal classes/functions.
from tlnetcard_python.login import Login

class Syslog:
    """ Class for the syslog object. """
    def __init__(self, login_object: Login) -> None:
        """ Initializes the Syslog object. """
        self._login_object = login_object
        self._get_url = login_object.get_base_url() + "/en/adm_syslog.asp"
        self._post_url = login_object.get_base_url() + "/delta/adm_syslog"
    def add_server(self, server: str) -> int:
        """ Adds a syslog server. """
        # Quitting if four servers are already listed.
        curr_servers = self.get_servers()
        if len(curr_servers) >= 4:
            return -1

        # Returning success if server is already in use.
        if server in curr_servers:
            return 0

        # Adding current servers to payload.
        syslog_data = {}
        i = 0   # Setting i to 0 here prevents error if curr_servers is empty.
        for i in range(0, len(curr_servers)):
            syslog_data["SLG_SERVER" + str(i + 1)] = curr_servers[i]

        # Adding new server to payload.
        syslog_data["SLG_SERVER" + str(i + 2)] = server

        # Adding empty server lines to payload.
        for j in range(i + 2, 4):
            syslog_data["SLG_SERVER" + str(j + 1)] = ""

        # Uploading syslog configuration and requesting system config renewal.
        self._login_object.get_session().post(self._post_url, data=syslog_data,
                                              timeout=self._login_object.get_timeout(),
                                              verify=self._login_object.get_reject_invalid_certs()
                                              ).raise_for_status()
        self._login_object.request_system_config_renewal()
        return 0
    def clear_servers(self) -> None:
        """ Clears all syslog servers. """
        # Generating payload.
        syslog_data = {}
        for i in range(0, 4):
            syslog_data["SLG_SERVER" + str(i + 1)] = ""

        # Uploading syslog configuration and requesting system config renewal.
        self._login_object.get_session().post(self._post_url, data=syslog_data,
                                              timeout=self._login_object.get_timeout(),
                                              verify=self._login_object.get_reject_invalid_certs()
                                              ).raise_for_status()
        self._login_object.request_system_config_renewal()
    def disable_syslog(self) -> None:
        """ Disables syslog servers. """
        # Generating payload.
        syslog_data = {
            'SLG_SLG': 0
        }

        # Uploading syslog configuration and requesting system config renewal.
        self._login_object.get_session().post(self._post_url, data=syslog_data,
                                              timeout=self._login_object.get_timeout(),
                                              verify=self._login_object.get_reject_invalid_certs()
                                              ).raise_for_status()
        self._login_object.request_system_config_renewal()
    def enable_syslog(self) -> None:
        """ Enables syslog servers. """
        # Generating payload.
        syslog_data = {
            'SLG_SLG': 1
        }

        # Uploading syslog configuration and requesting system config renewal.
        self._login_object.get_session().post(self._post_url, data=syslog_data,
                                              timeout=self._login_object.get_timeout(),
                                              verify=self._login_object.get_reject_invalid_certs()
                                              ).raise_for_status()
        self._login_object.request_system_config_renewal()
    def get_servers(self) -> List[str]:
        """ GETs syslog servers and returns them in a list. """
        # GETing system config.
        system_config = self._login_object.get_system_config()

        servers = []
        # Parsing config for syslog servers.
        for line in system_config:
            if line.find("SysLog Server") != -1 and line.split("=")[1] != "":
                servers.append(line.split("=")[1])
        return servers
    def remove_server(self, server: str) -> int:
        """ Removes a syslog server. """
        # Quitting if server isn't listed.
        curr_servers = self.get_servers()
        if server not in curr_servers:
            return -1

        # Removing server from list.
        curr_servers.remove(server)

        # Adding remaining servers to payload.
        syslog_data = {}
        for i in range(0, len(curr_servers)):
            syslog_data["SLG_SERVER" + str(i + 1)] = curr_servers[i]

        # Adding empty server lines to payload.
        for j in range(i + 1, 4):
            syslog_data["SLG_SERVER" + str(j + 1)] = ""

        # Uploading syslog configuration and requesting system config renewal.
        self._login_object.get_session().post(self._post_url, data=syslog_data,
                                              timeout=self._login_object.get_timeout(),
                                              verify=self._login_object.get_reject_invalid_certs()
                                              ).raise_for_status()
        self._login_object.request_system_config_renewal()
        return 0
