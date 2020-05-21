# tcp_ip.py
# Ethan Guthrie
# 05/04/2020
""" Allows TCP/IP settings for IPv4/IPv6 to be configured. """

# Standard library.
from os import remove
# Required internal class.
from tlnetcard_python.system.administration.batch_configuration import BatchConfiguration

class TcpIp:
    """ Class for the TcpIp object. """
    def __init__(self, login_object):
        """ Initializes the TcpIp object. """
        self._login_object = login_object
        self._get_url = login_object.get_base_url() + "/en/adm_ipconfig.asp"
        self._post_url = login_object.get_base_url() + "/delta/adm_ipconfig"
        self._batch_object = BatchConfiguration(self._login_object)
    def disable_autonegotiation(self):
        """ Disables link speed autonegotiation. """
        # Generating payload.
        ip_data = {
            "SYS_AUTONEG": "0"
        }

        # Uploading TCP/IP configuration.
        self._login_object.get_session().post(self._post_url, data=ip_data,
                                              verify=self._login_object.get_reject_invalid_certs())
    def disable_ipv4_dhcp(self):
        """ Disables DHCP for IPv4. """
        # Generating payload.
        ip_data = {
            "SYS_DHCP": "0"
        }

        # Uploading TCP/IP configuration.
        self._login_object.get_session().post(self._post_url, data=ip_data,
                                              verify=self._login_object.get_reject_invalid_certs())
    def disable_ipv6_dhcp(self):
        """ Disables DHCP for IPv6. """
        ip_data = {
            "SYS_V6DHCP": "0"
        }

        # Uploading TCP/IP configuration.
        self._login_object.get_session().post(self._post_url, data=ip_data,
                                              verify=self._login_object.get_reject_invalid_certs())
    def enable_autonetogiation(self):
        """ Enables link speed negotiation. """
        # Generating payload.
        ip_data = {
            "SYS_AUTONEG": "1"
        }

        # Uploading TCP/IP configuration.
        self._login_object.get_session().post(self._post_url, data=ip_data,
                                              verify=self._login_object.get_reject_invalid_certs())
    def enable_ipv4_dhcp(self):
        """ Enables DHCP for IPv4. """
        # Generating payload.
        ip_data = {
            "SYS_DHCP": "1"
        }

        # Uploading TCP/IP configuration.
        self._login_object.get_session().post(self._post_url, data=ip_data,
                                              verify=self._login_object.get_reject_invalid_certs())
    def enable_ipv6_dhcp(self):
        """ Enables DHCP for IPv6. """
        ip_data = {
            "SYS_V6DHCP": "1"
        }

        # Uploading TCP/IP configuration.
        self._login_object.get_session().post(self._post_url, data=ip_data,
                                              verify=self._login_object.get_reject_invalid_certs())
    def get_ipv4_info(self):
        """ GETs info on how IPv4 is configured. """
        # Generating dictionary of items to search for and initializing out dictionary.
        pretty = {
            "Bootp": "DHCP Status",
            "IP": "IP Address",
            "Mask": "Subnet Mask",
            "Gateway": "Gateway IP",
            "DNS IP": "DNS IP",
            "Domain": "Search Domain"
        }
        out = {}

        # GETing system configuration and writing lines to list.
        self._batch_object.download_system_configuration("system_config_temp.ini")
        with open("system_config_temp.ini", "r") as sys_config_file:
            sys_config = sys_config_file.readlines()

        # Parsing list for required values.
        for line in sys_config:
            format_line = line.split("=")
            if format_line[0] in pretty:
                out[pretty[format_line[0]]] = str(format_line[1]).rstrip('\n')
                
        # Cleaning up.
        remove("system_config_temp.ini")
        return out
    def get_ipv6_info(self):
        """ GETs info on how IPv6 is configured. """
        # Generating dictionary of items to search for and initializing out dictionary.
        pretty = {
            "V6 DHCP": "DHCP Status",
            "V6 IP": "IP Address",
            "V6 Gateway": "Gateway IP",
            "V6 DNS": "DNS IP",
        }
        out = {}

        # GETing system configuration and writing lines to list.
        self._batch_object.download_system_configuration("system_config_temp.ini")
        with open("system_config_temp.ini", "r") as sys_config_file:
            sys_config = sys_config_file.readlines()

        # Parsing list for required values.
        for line in sys_config:
            format_line = line.split("=")
            if format_line[0] in pretty:
                out[pretty[format_line[0]]] = str(format_line[1]).rstrip('\n')
        out["Prefix Length"] = int(out["IP Address"].split("/")[1])
        out["IP Address"] = out["IP Address"].split("/")[0]

        # Cleaning up.
        remove("system_config_temp.ini")
        return out
    def get_system_info(self):
        """ GETs info on the system and its location. """
    def set_ipv4_info(self):
        """ Sets info on how IPv4 is configured. """
    def set_ipv6_info(self):
        """ Sets info on how IPv6 is configured. """
    def set_system_info(self):
        """ Sets info on the system and its location. """
    def use_10m_link_speed(self):
        """ Sets the link speed to 10M. """
    def use_100m_link_speed(self):
        """ Sets the link speed to 100M. """
    def use_full_duplex(self):
        """ Sets the duplex for the link speed to full. """
    def use_half_duplex(self):
        """ Sets the duplex for the link speed to half. """
