# user_manager.py
# Ethan Guthrie
# 04/06/2020
""" Allows user and permission settings to be configured. """

class UserManager:
    """ Class for the UserManager object. """
    def __init__(self):
        """ Initializes the UserManager object. """
    def disable_radius(self):
        """ Disables RADIUS authentication. """
    def enable_radius(self):
        """ Enables RADIUS authentication. """
    def get_permissions(self, user="Administrator"):
        """ GETs the permissions for the provided user. """
    def get_server_info(self):
        """ GETs information about the user management server. """
    def get_user(self, user="Administrator"):
        """ GETs information about the provided user. """
    def set_permissions(self, user="Administrator", login_user=False,
                        framed_user=False, callback_login=False, callback_framed=False,
                        outbound=False, administrative=False, nas_prompt=False,
                        authenticate_only=False, callback_nas_prompt=False,
                        call_check=False, callback_administrative=False):
        """ Sets permissions for the provided user. """
    def set_server_info(self, server, secret, port):
        """ Sets information for the user management server. """
    def set_user(self, username, passwd, wan_access=False, user="Administrator"):
        """ Sets information about the provided user. """
