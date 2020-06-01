# tcp_ip.py
# Ethan Guthrie
# 05/04/2020
""" Allows TCP/IP settings for IPv4/IPv6 to be configured. """

# Standard library.
from typing import Any, Dict
# Required internal classes/functions.
from tlnetcard_python.login import Login

class TcpIp:
    """ Class for the TcpIp object. """
    def __init__(self, login_object: Login) -> None:
        """ Initializes the TcpIp object. """
        self._login_object = login_object
        self._get_url = login_object.get_base_url() + "/en/adm_ipconfig.asp"
        self._post_url = login_object.get_base_url() + "/delta/adm_ipconfig"
    def disable_autonegotiation(self) -> None:
        """ Disables link speed autonegotiation. """
        # Generating payload.
        ip_data = {
            "SYS_AUTONEG": "0"
        }

        # Uploading TCP/IP configuration and requesting system config renewal.
        self._login_object.get_session().post(self._post_url, data=ip_data,
                                              timeout=self._login_object.get_timeout(),
                                              verify=self._login_object.get_reject_invalid_certs()
                                              ).raise_for_status()
        self._login_object.request_system_config_renewal()
    def disable_ipv4_dhcp(self) -> None:
        """ Disables DHCP for IPv4. """
        # Generating payload.
        ip_data = {
            "SYS_DHCP": "0"
        }

        # Uploading TCP/IP configuration and requesting system config renewal.
        self._login_object.get_session().post(self._post_url, data=ip_data,
                                              timeout=self._login_object.get_timeout(),
                                              verify=self._login_object.get_reject_invalid_certs()
                                              ).raise_for_status()
        self._login_object.request_system_config_renewal()
    def disable_ipv6_dhcp(self) -> None:
        """ Disables DHCP for IPv6. """
        ip_data = {
            "SYS_V6DHCP": "0"
        }

        # Uploading TCP/IP configuration and requesting system config renewal.
        self._login_object.get_session().post(self._post_url, data=ip_data,
                                              timeout=self._login_object.get_timeout(),
                                              verify=self._login_object.get_reject_invalid_certs()
                                              ).raise_for_status()
        self._login_object.request_system_config_renewal()
    def enable_autonetogiation(self) -> None:
        """ Enables link speed negotiation. """
        # Generating payload.
        ip_data = {
            "SYS_AUTONEG": "1"
        }

        # Uploading TCP/IP configuration and requesting system config renewal.
        self._login_object.get_session().post(self._post_url, data=ip_data,
                                              timeout=self._login_object.get_timeout(),
                                              verify=self._login_object.get_reject_invalid_certs()
                                              ).raise_for_status()
        self._login_object.request_system_config_renewal()
    def enable_ipv4_dhcp(self) -> None:
        """ Enables DHCP for IPv4. """
        # Generating payload.
        ip_data = {
            "SYS_DHCP": "1"
        }

        # Uploading TCP/IP configuration and requesting system config renewal.
        self._login_object.get_session().post(self._post_url, data=ip_data,
                                              timeout=self._login_object.get_timeout(),
                                              verify=self._login_object.get_reject_invalid_certs()
                                              ).raise_for_status()
        self._login_object.request_system_config_renewal()
    def enable_ipv6_dhcp(self) -> None:
        """ Enables DHCP for IPv6. """
        ip_data = {
            "SYS_V6DHCP": "1"
        }

        # Uploading TCP/IP configuration and requesting system config renewal.
        self._login_object.get_session().post(self._post_url, data=ip_data,
                                              timeout=self._login_object.get_timeout(),
                                              verify=self._login_object.get_reject_invalid_certs()
                                              ).raise_for_status()
        self._login_object.request_system_config_renewal()
    def get_ipv4_info(self) -> Dict[str, str]:
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

        # GETing system config.
        system_config = self._login_object.get_system_config()

        # Parsing list for required values.
        for line in system_config:
            format_line = line.split("=")
            if format_line[0] in pretty:
                out[pretty[format_line[0]]] = str(format_line[1])
        return out
    def get_ipv6_info(self) -> Dict[str, Any]:
        """ GETs info on how IPv6 is configured. """
        # Generating dictionary of items to search for and initializing out dictionary.
        pretty = {
            "V6 DHCP": "DHCP Status",
            "V6 IP": "IP Address",
            "V6 Gateway": "Gateway IP",
            "V6 DNS": "DNS IP",
        }
        out = {}

        # GETing system config.
        system_config = self._login_object.get_system_config()

        # Parsing list for required values.
        for line in system_config:
            format_line = line.split("=")
            if format_line[0] in pretty:
                out[pretty[format_line[0]]] = str(format_line[1])
        out["Prefix Length"] = int(out["IP Address"].split("/")[1])
        out["IP Address"] = out["IP Address"].split("/")[0]
        return out
    def get_system_info(self) -> Dict[str, str]:
        """ GETs info on the system and its location. """
        # Generating dictionary of items to search for and initializing out dictionary.
        pretty = {
            "Name": "Host Name",
            "Contact": "System Contact",
            "Location": "System Location"
        }
        out = {}

        # GETing system config.
        system_config = self._login_object.get_system_config()

        # Parsing list for required values.
        for line in system_config:
            format_line = line.split("=")
            if format_line[0] in pretty:
                out[pretty[format_line[0]]] = str(format_line[1])
        return out
    def set_ipv4_info(self, ip_addr: str, mask: str = "255.255.255.0", gateway: str = "",
                      dns_ip: str = "", domain: str = "") -> None:
        """ Sets info on how IPv4 is configured. """
        # Generating payload.
        ip_data = {
            "SYS_DHCP": "0",
            "SYS_IP": ip_addr,
            "SYS_MASK": mask,
            "SYS_GATE": gateway,
            "SYS_DNS": dns_ip,
            "SYS_DOMAIN": domain
        }

        # Uploading TCP/IP configuration and requesting system config renewal.
        self._login_object.get_session().post(self._post_url, data=ip_data,
                                              timeout=self._login_object.get_timeout(),
                                              verify=self._login_object.get_reject_invalid_certs()
                                              ).raise_for_status()
        self._login_object.request_system_config_renewal()
    def set_ipv6_info(self, ip_addr: str, prefix_len: int = 64,
                      gateway: str = "::", dns_ip: str = "::") -> None:
        """ Sets info on how IPv6 is configured. """
        # Generating payload.
        ip_data = {
            "SYS_V6DHCP": "0",
            "SYS_V6IP": ip_addr,
            "SYS_V6LEN": prefix_len,
            "SYS_V6GW": gateway,
            "SYS_V6DNS": dns_ip,
        }

        # Uploading TCP/IP configuration and requesting system config renewal.
        self._login_object.get_session().post(self._post_url, data=ip_data,
                                              timeout=self._login_object.get_timeout(),
                                              verify=self._login_object.get_reject_invalid_certs()
                                              ).raise_for_status()
        self._login_object.request_system_config_renewal()
    def set_system_info(self, name: str = "TLNET", contact: str = "", location: str = "") -> None:
        """ Sets info on the system and its location. """
        # Generating payload.
        ip_data = {
            "SYS_NAM": name,
            "SYS_CON": contact,
            "SYS_LOC": location,
        }

        # Uploading TCP/IP configuration and requesting system config renewal.
        self._login_object.get_session().post(self._post_url, data=ip_data,
                                              timeout=self._login_object.get_timeout(),
                                              verify=self._login_object.get_reject_invalid_certs()
                                              ).raise_for_status()
        self._login_object.request_system_config_renewal()
    def use_10m_link_speed(self) -> None:
        """ Sets the link speed to 10M. """
        # Generating payload.
        ip_data = {
            "SYS_SPEED": "0"
        }

        # Uploading TCP/IP configuration and requesting system config renewal.
        self._login_object.get_session().post(self._post_url, data=ip_data,
                                              timeout=self._login_object.get_timeout(),
                                              verify=self._login_object.get_reject_invalid_certs()
                                              ).raise_for_status()
        self._login_object.request_system_config_renewal()
    def use_100m_link_speed(self) -> None:
        """ Sets the link speed to 100M. """
        # Generating payload.
        ip_data = {
            "SYS_SPEED": "1"
        }

        # Uploading TCP/IP configuration and requesting system config renewal.
        self._login_object.get_session().post(self._post_url, data=ip_data,
                                              timeout=self._login_object.get_timeout(),
                                              verify=self._login_object.get_reject_invalid_certs()
                                              ).raise_for_status()
        self._login_object.request_system_config_renewal()
    def use_full_duplex(self) -> None:
        """ Sets the duplex for the link to full. """
        # Generating payload.
        ip_data = {
            "SYS_DUPLEX": "1"
        }

        # Uploading TCP/IP configuration and requesting system config renewal.
        self._login_object.get_session().post(self._post_url, data=ip_data,
                                              timeout=self._login_object.get_timeout(),
                                              verify=self._login_object.get_reject_invalid_certs()
                                              ).raise_for_status()
        self._login_object.request_system_config_renewal()
    def use_half_duplex(self) -> None:
        """ Sets the duplex for the link to half. """
        # Generating payload.
        ip_data = {
            "SYS_DUPLEX": "0"
        }

        # Uploading TCP/IP configuration and requesting system config renewal.
        self._login_object.get_session().post(self._post_url, data=ip_data,
                                              timeout=self._login_object.get_timeout(),
                                              verify=self._login_object.get_reject_invalid_certs()
                                              ).raise_for_status()
        self._login_object.request_system_config_renewal()
