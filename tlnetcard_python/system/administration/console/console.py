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
    
