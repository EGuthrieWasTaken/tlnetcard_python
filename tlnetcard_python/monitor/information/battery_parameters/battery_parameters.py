# battery_parameters.py
# Ethan Guthrie
# 05/14/2020
""" Allows battery parameters to be read. """

# Related third-party library.
from pysnmp.hlapi import getCmd, SnmpEngine, UsmUserData, UdpTransportTarget
from pysnmp.hlapi import ContextData, ObjectType, ObjectIdentity
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

class BatteryParameters:
    """ Class for the Battery_Parameters object. """
    def __init__(self, login_object):
        """ Initializes the Battery_Parameters object. """
        self._login_object = login_object
        self._get_url = login_object.get_base_url() + "/en/ups/info_battery.asp"
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
                    battery_measurements[i] = str(var_binds[0]).split("=")[-1]

            # Generating out payload.
            hour = int(battery_measurements['Remaining Hours'])
            mins = int(battery_measurements['Remaining Minutes'])
            out = {
                'Battery Capacity (%)': int(battery_measurements['Battery Capacity']),
                'Voltage (V)': float(int(battery_measurements['Voltage'])/10),
                'Temperature (°C)': int(battery_measurements['Temperature']),
                'Remaining Time (HH:MM)': '{hour:02d}:{mins:02d}'.format(hour=hour, mins=mins)
            }
            return out
        else:
            # Selenium will be used to scrape the value. This method is much slower than using SNMP.
            # Configuring Selenium to run headless (i.e. without a GUI).
            browser_options = Options()
            browser_options.add_argument("--headless")
            browser = webdriver.Chrome(options=browser_options)
            # Configuring browser timeouts.
            browser.set_page_load_timeout(10)
            browser.implicitly_wait(10)
            # Getting card login page.
            browser.get(self._login_object.get_base_url())
            # Adding cookies from requests session to "login".
            requests_cookies = self._login_object.get_session().cookies.get_dict()
            for cookie in requests_cookies:
                browser.add_cookie({'name': cookie, 'domain': self._login_object.get_host(), 'value': requests_cookies[cookie]})
            # Getting webpage again now that cookies are installed.
            browser.get(self._get_url)
            
            # Getting out values.
            out = {}
            out['Battery Capacity (%)'] = browser.find_element_by_id("UPS_BATTLEVEL").text
            out['Voltage (V)'] = browser.find_element_by_id("UPS_BATTVOLT").text
            out['Temperature (°C)'] = browser.find_element_by_id("UPS_TEMP").text
            out['Remaining Time (HH:MM)'] = browser.find_element_by_id("UPS_BATTREMAIN").text

            return out
    def get_last_replacement_date(self):
        """ Gets the last date the UPS battery was changed. """
    def get_next_replacement_date(self):
        """ Gets the next date the UPS battery should be changed. """
