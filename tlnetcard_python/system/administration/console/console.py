# console.py
# Ethan Guthrie
# DATE TBD
""" Allows for console settings to be configured. """

class Console:
    """ Class for the Console object. """
    def __init__(self, login_object):
        """ Initializes the Console object. """
        self._login_object = login_object
        self._get_url = login_object.get_base_url() + "/en/adm_console.asp"
        self._post_url = login_object.get_base_url() + "/delta/adm_console"
    def disable_ssh(self):
        """ Disables SSH. """
    def disable_telnet(self):
        """ Disables Telnet. """
    def enable_ssh(self):
        """ Enables SSH. """
    def enable_telnet(self):
        """ Enables Telnet. """
    def get_ssh_port(self):
        """ GETs the port in use for SSH. """
    def get_telnet_port(self):
        """ GETs the port in use for Telnet. """
    def set_ssh_port(self, port=22):
        """ Sets the port for use by SSH. """
    def set_telnet_port(self, port=23):
        """ Sets the port for use by Telnet. """
    def upload_auth_public_key(self, key):
        """ Uploads the provided authentication public key. """
    def upload_dsa_host_key(self, key):
        """ Uploads the provided DSA host key. """
    def upload_rsa_host_key(self, key):
        """ Uploads the provided RSA host key. """
