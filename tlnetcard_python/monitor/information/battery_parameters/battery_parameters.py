# battery_parameters.py
# Ethan Guthrie
# 05/14/2020
""" Allows battery parameters to be read. """

class BatteryParameters:
    """ Class for the Battery_Parameters object. """
    def __init__(self, login_object):
        """ Initializes the Battery_Parameters object. """
        self._login_object = login_object
        self._get_url = login_object.get_base_url() + "/en/ups/info_battery.asp"
    def get_battery_status(self):
        """ GETs battery status information. """
    def get_battery_measurements(self):
        """ GETs information about battery capacity, temperature, and voltage. """
    def get_last_replacement_date(self):
        """ GETs the last date the UPS battery was changed. """
    def get_next_replacement_date(self):
        """ GETs the next date the UPS battery should be changed. """
