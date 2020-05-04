# web.py
# Ethan Guthrie
# 05/04/2020
""" Allows web host settings to be configured. """

class Web:
    """ Class for the Web object. """
    def __init__(self):
        """ Initializes the Web object. """
    def disable_http(self):
        """ Disables HTTP access. """
    def disable_https(self):
        """ Disables HTTPS access. """
    def enable_http(self):
        """ Enables HTTP access. """
    def enable_https(self):
        """ Enables HTTPS access. """
    def get_http_port(self):
        """ GETs the port in use for HTTP. """
    def get_https_port(self):
        """ GETs the port in use for HTTPS. """
    def get_web_refresh(self):
        """ GETs the web refresh time in seconds. """
    def set_http_port(self, port=80):
        """ Sets the port for use by HTTP. """
    def set_https_port(self, port=443):
        """ Sets the port for use by HTTPS. """
    def set_web_refresh(self, seconds=10):
        """ Sets the web refresh time to ```seconds``` seconds. """
    def upload_ssl_cert(self, path):
        """ Uploads the provided SSL certificate. """