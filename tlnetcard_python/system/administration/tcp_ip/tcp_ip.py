# tcp_ip.py
# Ethan Guthrie
# DATE TBD
""" Allows TCP/IP settings for IPv4/IPv6 to be configured. """

class TcpIp:
    """ Class for the TcpIp object. """
    def __init__(self, login_object):
        """ Initializes the TcpIp object. """
    def disable_autonegotiation(self):
        """ Disables link speed autonegotiation. """
    def disable_dhcp(self, protocol="IPv4"):
        """ Disables DHCP for the provided protocol. """
    def enable_autonetogiation(self):
        """ Enables link speed negotiation. """
    def enable_dhcp(self, protocol="IPv4"):
        """ Enables DHCP for the provided protocol. """
    def get_dns_ip(self, protocol="IPv4"):
        """ GETs the DNS IP for the provided protocol. """
    def get_gateway_ip(self, protocol="IPv4"):
        """ GETs the Gateway IP for the provided protocol. """
    def get_ip_addr(self, protocol="IPv4"):
        """ GETs the IP address for the provided protocol. """
    def get_prefix_len(self):
        """ GETs the IPv6 prefix length. """
    def get_search_domain(self):
        """ GETs the IPv4 search domain. """
    def get_subnet_mask(self):
        """ GETs the IPv4 subnet mask. """
    def set_dns_ip(self, ip, protocol="IPv4"):
        """ Sets the DNS IP for the provided protocol. """
    def set_gateway_ip(self, ip, protocol="IPv4"):
        """ Sets the Gateway IP for the provided protocol. """
    def set_ip_addr(self, ip, protocol="IPv4"):
        """ Sets the IP address for the provided protocol. """
    def set_prefix_len(self, length):
        """ Sets the IPv6 prefix length. """
    def set_search_domain(self, domain):
        """ Sets the IPv4 search domain. """
    def set_subnet_mask(self, mask):
        """ Sets the IPv4 subnet mask. """
