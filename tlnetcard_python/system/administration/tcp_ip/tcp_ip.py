# tcp_ip.py
# Ethan Guthrie
# 05/04/2020
""" Allows TCP/IP settings for IPv4/IPv6 to be configured. """

class TcpIp:
    """ Class for the TcpIp object. """
    def __init__(self, login_object):
        """ Initializes the TcpIp object. """
        self._login_object = login_object
        self._get_url = login_object.get_base_url() + "/en/adm_ipconfig.asp"
        self._post_url = login_object.get_base_url() + "/delta/adm_ipconfig"
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
        # GETing TCP/IP page.
        resp = self._login_object.get_session().get(self._get_url)

        # Initializing list to get values.
        element_names = ["SYS_IP", "SYS_MASK", "SYS_GATE", "SYS_DNS", "SYS_DOMAIN"]

        # Checking if DHCP in enabled for IPv4.
        addr = str(resp.text).upper().find("NAME=\"SYS_DHCP\"")
        if str(resp.text).upper().find(">") > str(resp.text).upper().find("CHECKED"):
            info = [True]
        else:
            info = [False]

        # Parsing response for value.
        for name in element_names:
            addr = str(resp.text).upper().find("NAME=\"" + name + "\"")
            start_index = str(resp.text).upper().find("VALUE=", addr) + 7
            end_index = str(resp.text).upper().find("\"", start_index)
            info.append(resp.text[start_index:end_index])

        # Generating out dictionary.
        out = {
            "DHCP Enabled": info[0],
            "IP Address": info[1],
            "Subnet Mask": info[2],
            "Gateway IP": info[3],
            "DNS IP": info[4],
            "Search Domain": info[5]
        }
        return out
    def get_ipv6_info(self):
        """ GETs info on how IPv6 is configured. """

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
