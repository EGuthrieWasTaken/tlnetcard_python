# in_out_parameters.py
# Ethan Guthrie
# DATE TBD
""" Allows UPS input and output power levels to be read. """

# Required internal classes/functions.
from tlnetcard_python.login import Login
from tlnetcard_python.monitor.information.information import get_with_snmp, scrape_with_selenium

class InOutParameters:
    """ Class for the InOutParameters object. """
    def __init__(self, login_object: Login) -> None:
        """ Initializes the InOutParameters object. """
        self._login_object = login_object
        self._get_url = login_object.get_base_url() + "/en/ups/info_io.asp"
    def get_bypass_measurements(self, snmp: bool = True, snmp_user: str = None,
                                snmp_auth_key: str = None, snmp_priv_key: str = None,
                                timeout: int = 10) -> Dict[str, Any]:
        """ Gets battery bypass measurements. """
        if snmp:
            # SNMP will be used to get values. This is the preferred method.
            # Generating SNMP ID dictionary.
            snmp_dict = {
                'Frequency (Hz)': 'iso.3.6.1.2.1.33.1.5.1',
                'Voltage (V)': 'iso.3.6.1.2.1.33.1.5.3.1.2.1',
                'Current (A)': 'iso.3.6.1.2.1.33.1.5.3.1.3.1', # In deciamps (i.e. divide this value by 10).
                'Power (Watt)': 'iso.3.6.1.2.1.33.1.5.3.1.4.1'
            }

            # Getting values.
            freq, volts, curr, power = get_with_snmp(self._login_object.get_host(),
                                                     [snmp_dict[i] for i in snmp_dict], snmp_user,
                                                     snmp_auth_key, snmp_priv_key, timeout)

            # Generating out dictionary.
            out = {
                'Frequency (Hz)': float(freq),
                'Voltage (V)': float(volts),
                'Current (A)': float(int(curr)/10),
                'Power (Watt)': int(power)
            }
        else:
            # Selenium will be used to scrape values. This method is slower than using SNMP.
            # Getting values.
            freq, volts, curr, power = scrape_with_selenium(self._login_object.get_host(),
                                                            ["UPS_BYFREQ1", "UPS_BYVOLT1",
                                                             "UPS_BYAMP1", "UPS_BYPOWER1"],
                                                            self._get_url,
                                                            self._login_object.get_session(),
                                                            timeout)

            # Generating out dictionary.
            out = {
                'Frequency (Hz)': float(freq),
                'Voltage (V)': float(volts),
                'Current (A)': float(curr),
                'Power (Watt)': int(power)
            }
        return out
