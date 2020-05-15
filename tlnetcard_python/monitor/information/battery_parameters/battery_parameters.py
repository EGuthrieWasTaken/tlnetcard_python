# battery_parameters.py
# Ethan Guthrie
# 05/14/2020
""" Allows battery parameters to be read. """

# Related third-party library.
from pysnmp.hlapi import getCmd, SnmpEngine, UsmUserData, UdpTransportTarget
from pysnmp.hlapi import ContextData, ObjectType, ObjectIdentity
#from selenium import webdriver

class BatteryParameters:
    """ Class for the Battery_Parameters object. """
    def __init__(self, login_object):
        """ Initializes the Battery_Parameters object. """
        self._login_object = login_object
        self._get_url = login_object.get_base_url() + "/en/ups/info_battery.asp"
        # Selenium webdriver is required to scrape information from this page.
    def get_battery_status(self):
        """ Gets battery status information. """
    def get_battery_measurements(self, snmp=True, snmp_user=None,
                                 snmp_auth_key=None, snmp_priv_key=None):
        """ Gets information about battery capacity, temperature, and voltage. """
        if snmp:
            # SNMP will be used to get the value. This is the preferred method.
            # Generating SNMP value-->key dictionary.
            snmp_dict = {
                'Battery Capacity': 'iso.3.6.1.2.1.33.1.2.4',
                'Voltage': 'iso.3.6.1.2.1.33.1.2.5', # In decivolts (i.e. divide this value by 10).
                'Temperature': 'iso.3.6.1.2.1.33.1.2.7',
                'Remaining Minutes': 'iso.3.6.1.2.1.33.1.2.3',
                'Remaining Hours': 'iso.3.6.1.2.1.33.1.2.2'
            }
            # Initializing output dictionary.
            battery_measurements = {}

            # Iterating through dictionary to get values.
            for i in snmp_dict:
                error_indication, error_status, error_index, var_binds = next(
                    getCmd(SnmpEngine(),
                           UsmUserData(snmp_user, authKey=snmp_auth_key, privKey=snmp_priv_key),
                           UdpTransportTarget((self._login_object.get_host(), 161),
                                              timeout=0.5, retries=1),
                           ContextData(),
                           ObjectType(ObjectIdentity(snmp_dict[i])))
                )

                if error_indication:
                    print(error_indication)
                    return -1
                elif error_status:
                    print('%s at %s' % (error_status.prettyPrint(),
                                        error_index and var_binds[int(error_index) - 1][0] or '?'))
                    return -1
                else:
                    battery_measurements[i] = var_binds[0].split()[-1]

            return {

            }
        else:
            # Selenium will be used to scrape the value. This method is much slower than using SNMP.
            return 0
    def get_last_replacement_date(self):
        """ Gets the last date the UPS battery was changed. """
    def get_next_replacement_date(self):
        """ Gets the next date the UPS battery should be changed. """
