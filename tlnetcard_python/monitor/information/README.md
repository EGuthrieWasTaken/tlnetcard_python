# [information.py](information.py)

## Important Note

The functions in this file are not part of a class, and can be used independently of the rest of the API.

|                                                                                                                   Function Header                                                                                                                   |                            Quick Description                             |
|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| [``get_with_snmp(host, snmp_ids, snmp_user=None, snmp_auth_key=None, snmp_priv_key=None, timeout=10)``](#get_with_snmphost-str-snmp_ids-liststr-snmp_user-str--none-snmp_auth_key-str--none-snmp_priv_key-str--none-timeout-float--100---liststr) |            Gets the provided SNMP values from their SNMP IDs.            |
|                             [``scrape_with_selenium(host, element_ids, url, session=None timeout=10)``](#scrape_with_seleniumhost-str-element_ids-liststr-url-str-session-session--none-timeout-float--100---liststr)                             | Scrapes the provided web elements by their ID from the provided webpage. |

## get_with_snmp(host: str, snmp_ids: List[str], snmp_user: str = None, snmp_auth_key: str = None, snmp_priv_key: str = None, timeout: float = 10.0) -> List[str]

|        Name         |  Type  | Required | Default Value |                                   Description                                   |
|:-------------------:|:------:|:--------:|:-------------:|:-------------------------------------------------------------------------------:|
|     ``host``      | String |   Yes    |      N/A      |                   The host which will sending out SNMP data.                    |
|   ``snmp_ids``    |  List  |   Yes    |      N/A      |         A list of SNMP IDs for which the function will retrieve values.         |
|   ``snmp_user``   | String |    No    |  ``None``   |                       A SNMP user with read permissions.                        |
| ``snmp_auth_key`` | String |    No    |  ``None``   |                      The auth key for the ``snmp_user``.                      |
| ``snmp_priv_key`` | String |    No    |  ``None``   |                      The priv key for the ``snmp_user``.                      |
|    ``timeout``    | Float  |    No    |   ``10``    | The maximum time the function may wait for a response from the SNMP ``host``. |

Gets the values for each of the specified SNMP IDs and returns them in a list.  
Example:

``python
from tlnetcard_python.monitor.information.information import get_with_snmp

battery_status, battery_capacity = get_with_snmp("10.0.0.100", ["iso.3.6.1.2.1.33.1.2.1", "iso.3.6.1.2.1.33.1.2.4"], "sample_snmp_read_user", "sample_auth_key", "sample_priv_key")

if int(battery_status) == 1:
    print("Battery status unknown!")
elif int(battery_status)  >= 3:
    print("Battery low: " + battery_capacity + "%")
``

## scrape_with_selenium(host: str, element_ids: List[str], url: str, session: Session = None, timeout: float = 10.0) -> List[str]

|       Name        |       Type       | Required | Default Value |                                                Description                                                |
|:-----------------:|:----------------:|:--------:|:-------------:|:---------------------------------------------------------------------------------------------------------:|
|    ``host``     |      String      |   Yes    |      N/A      |                                    The host for the TLNET Supervisor.                                     |
| ``element_ids`` |       List       |   Yes    |      N/A      |                    A list of element IDs for which the function will retrieve values.                     |
|     ``url``     |      String      |   Yes    |      N/A      |                             The URL which Selenium will use to scrape values.                             |
|   ``session``   | requests.Session |    No    |  ``None``   | A requests session. When one is present, all cookies from it will be transferred to the Selenium session. |
|   ``timeout``   |      Float       |    No    |   ``10``    |        The maximum time the function may wait for all requested values to be populated in the URL.        |

Scrapes the values from the provided URL with the provided IDs and returns them in a list.  
Example:

``python
from tlnetcard_python import Login
from tlnetcard_python.monitor.information.information import scrape_with_selenium

battery_status, battery_capacity = scrape_with_selenium("10.0.0.100", ["UPS_BATTSTS", "UPS_BATTLEVEL"], "https://10.0.0.100//en/ups/info_battery.asp", Login("sample_username", "sample_password", "10.0.0.100", reject_invalid_certs=False).get_session())

if int(battery_status) == 1:
    print("Battery status unknown!")
elif int(battery_status)  >= 3:
    print("Battery low: " + battery_capacity + "%")
``

## Documentation Tree

* [tlnetcard_python](/tlnetcard_python)
  * [Monitor](/tlnetcard_python/monitor)
    * Information
      * [UPS Properties](/tlnetcard_python/monitor/information/ups_properties)
      * [Battery Parameters](/tlnetcard_python/monitor/information/battery_parameters)
      * [In/Out Parameters](/tlnetcard_python/monitor/information/in_out_parameters)
      * [Identification](/tlnetcard_python/monitor/information/identification)
      * [Status Indication](/tlnetcard_python/monitor/information/status_indication)
      * [Shutdown Agent](/tlnetcard_python/monitor/information/shutdown_agent)
    * [History](/tlnetcard_python/monitor/history)
      * [Event Log](/tlnetcard_python/monitor/history/event_log)
      * [Data Log](/tlnetcard_python/monitor/history/data_log)
      * [Configure](/tlnetcard_python/monitor/history/configure)
    * [Environment](/tlnetcard_python/monitor/environment)
      * [Information](/tlnetcard_python/monitor/environment/information)
      * [Configuration](/tlnetcard_python/monitor/environment/configuration)
    * [About](/tlnetcard_python/monitor/about)
      * [Information](/tlnetcard_python/monitor/about/information)
  * [Device](/tlnetcard_python/device)
    * [Management](/tlnetcard_python/device/management)
      * [Reaction](/tlnetcard_python/device/management/reaction)
      * [Configure](/tlnetcard_python/device/management/configure)
      * [Control](/tlnetcard_python/device/management/control)
      * [Weekly Schedule](/tlnetcard_python/device/management/weekly_schedule)
      * [Specific Schedule](/tlnetcard_python/device/management/specific_schedule)
      * [Event Level](/tlnetcard_python/device/management/event_level)
  * [System](/tlnetcard_python/system)
    * [Administration](/tlnetcard_python/system/administration)
      * [User Manager](/tlnetcard_python/system/administration/user_manager)
      * [TCP/IP](/tlnetcard_python/system/administration/tcp_ip)
      * [Web](/tlnetcard_python/system/administration/web)
      * [Console](/tlnetcard_python/system/administration/console)
      * [FTP](/tlnetcard_python/system/administration/ftp)
      * [Time Server](/tlnetcard_python/system/administration/time_server)
      * [Syslog](/tlnetcard_python/system/administration/syslog)
      * [Batch Configuration](/tlnetcard_python/system/administration/batch_configuration)
      * [Upgrade](/tlnetcard_python/system/administration/upgrade)
    * [Notification](/tlnetcard_python/system/notification)
      * [SNMP Access](/tlnetcard_python/system/notification/snmp_access)
      * [SNMPv3 USM](/tlnetcard_python/system/notification/snmpv3_usm)
      * [SNMP Trap](/tlnetcard_python/system/notification/snmp_trap)
      * [Mail Server](/tlnetcard_python/system/notification/mail_server)
      * [Wake On LAN](/tlnetcard_python/system/notification/wake_on_lan)
      * [Modbus TCP](/tlnetcard_python/system/notification/modbus_tcp)
