# Steps to configure this template:
# 8) Trim trailing whitespace from all lines, ensure no line exceedes 100 characters, and delete
#    these instructions. You're on your own, kid.
"""
tlnetcard_python.monitor.information.identification.identification
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This module provides a ``Identification`` object to provide the functionality of TLNET Supervisor ->
Monitor -> Information -> Identification.
"""
# Standard library.
from typing import Dict
# Required internal classes/functions.
from tlnetcard_python.login import Login
from tlnetcard_python.monitor.information.information import get_with_snmp, scrape_with_selenium

class Identification:
    """
    A TLNET Supervisor ``Identification`` object. Provides the functionality of the equivalent
    webpage TLNET Supervisor -> Monitor -> Information -> Identification. This functionality is
    provided through either SNMP or Selenium per the user's choice. While Selenium requires no
    additional arguments at runtime, it does require Google Chrome to be installed as well as the
    associated WebDriver (see the README.md for more details), as well as suffering from
    greatly-reduced speeds. As such, it is only recommended that Selenium be used on smaller
    workloads (if you must use it at all). Alternatively, SNMP can be used to retrieve values at a
    much greater speed, although this will require more arguments (SNMP user, auth key, and priv key
    as applicable), all of which can be retrieved using the
    ``tlnetcard_python.system.notification.Snmpv3Usm`` object.

    Basic Usage:

    >>> from tlnetcard_python import Login
    >>> from tlnetcard_python.monitor.information import Identification
    >>> # As always, a tlnetcard_python.Login object must first be created. Then the Login object
    >>> # can be passed to the tlnetcard_python.monitor.information.Identification object.
    >>> card = Login(user="admin", passwd="password", host="10.0.0.100")
    >>> card_identification = Identification(card)

    At this point, functions can either be run using SNMP:

    >>> card_identification.get_identification_info(snmp_user="admin", snmp_auth_key="imadethisup",
    >>>                                             snmp_priv_key="imadethisuptoo")

    Or they can be run using Selenium:

    >>> card_identification.get_identification_info(snmp=False)

    """
    def __init__(self, login_object: Login) -> None:
        """
        Initializes the ``Identification`` object. Returns ``None``.

        :param login_object: A valid ``tlnetcard_python.Login`` object.
        :rtype: ``None``
        """
        self._login_object = login_object
        self._get_url = login_object.get_base_url() + "/en/ups/info_ident.asp"
    def get_identification_info(self, snmp: bool = True, snmp_user: str = "",
                                snmp_auth_key: str = "", snmp_priv_key: str = "") -> Dict[str, str]:
        """
        Returns UPS identifying information as a dictionary.

        :param snmp: (optional) Whether SNMP should be used or not. Setting this value to ``False``
        will result in Selenium being used.
        :param snmp_user: (optional) The SNMP user to connect with.
        :param snmp_auth_key: (optional) The SNMP auth key to connect with.
        :param snmp_priv_key: (optional) The SNMP priv key to connect with.
        :rtype: ``Dict[str, str]``
        """
        if snmp:
            # SNMP will be used to get values. This is the preferred method.
            # Generating SNMP ID dictionary.
            snmp_dict = {
                'Model': 'iso.3.6.1.2.1.33.1.1.2',
                'UPS Firmware': 'iso.3.6.1.2.1.33.1.1.3',
                'Interface Firmware': 'iso.3.6.1.2.1.33.1.1.4',
                'UPS Serial Number': 'iso.3.6.1.4.1.850.100.1.1.2',
                'Interface Serial Number': 'iso.3.6.1.4.1.850.100.1.1.4',
                'MAC Address': 'iso.3.6.1.2.1.2.2.1.6.2'
            }

            # Getting values.
            host = self._login_object.get_host()
            timeout = self._login_object.get_timeout()
            model, ups_firm, int_firm, ups_ser, int_ser, mac = get_with_snmp(host,
                                                                             [snmp_dict[i] for i in
                                                                             snmp_dict], snmp_user,
                                                                             snmp_auth_key,
                                                                             snmp_priv_key, timeout)

            # Generating out dictionary.
            out = {
                'Model': model,
                'Type': 'On line',
                'UPS Firmware': ups_firm,
                'Interface Firmware': int_firm,
                'UPS Serial Number': ups_ser,
                'Interface Serial Number': int_ser,
                'MAC Address': mac
            }
        else:
            # Selenium will be used to scrape values. This method is slower than using SNMP.
            # Getting values.
            host = self._login_object.get_host()
            session = self._login_object.get_session()
            timeout = self._login_object.get_timeout()
            # For some reason the values on this page don't have IDs so Xpaths will be used instead.
            # pylint: disable=line-too-long
            xpaths = ["/html/body/table/tbody/tr[5]/td[3]/table/tbody/tr[3]/td[1]/div/table/tbody/tr[2]/td[2]/div/table/tbody/tr[1]/td[2]",
                      "/html/body/table/tbody/tr[5]/td[3]/table/tbody/tr[3]/td[1]/div/table/tbody/tr[2]/td[2]/div/table/tbody/tr[3]/td[2]",
                      "/html/body/table/tbody/tr[5]/td[3]/table/tbody/tr[3]/td[1]/div/table/tbody/tr[2]/td[2]/div/table/tbody/tr[4]/td[2]",
                      "/html/body/table/tbody/tr[5]/td[3]/table/tbody/tr[3]/td[1]/div/table/tbody/tr[2]/td[2]/div/table/tbody/tr[5]/td[2]",
                      "/html/body/table/tbody/tr[5]/td[3]/table/tbody/tr[3]/td[1]/div/table/tbody/tr[2]/td[2]/div/table/tbody/tr[6]/td[2]",
                      "/html/body/table/tbody/tr[5]/td[3]/table/tbody/tr[3]/td[1]/div/table/tbody/tr[2]/td[2]/div/table/tbody/tr[7]/td[2]"]
            # pylint: enable=line-too-long
            model, ups_firm, int_firm, ups_ser, int_ser, mac = scrape_with_selenium(host,
                                                                                    xpaths,
                                                                                    self._get_url,
                                                                                    session,
                                                                                    timeout)

            # Generating out dictionary.
            out = {

                'Type': 'On line'
            }
        return out
