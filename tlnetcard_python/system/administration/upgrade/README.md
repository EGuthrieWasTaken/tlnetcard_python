# [upgrade.py](upgrade.py)

|                                                    Function Header                                                     |         Quick Description          |
|:----------------------------------------------------------------------------------------------------------------------:|:----------------------------------:|
|                           [``__init__(login_object)``](#__init__login_object-login---none)                           |  Initializes the Upgrade object.   |
|                              [``get_firmware_version()``](#get_firmware_version---str)                               | GETs the current firmware version. |
| [``upgrade_snmp_firmware(path="ups-tl-01_12_05c.bin")``](#upgrade_snmp_firmwarepath-str--ups-tl-01_12_05cbin---bool) |   Upgrades SNMP device firmware.   |

## \_\_init__(login_object: Login) -> None

|        Name        |                       Type                        | Required | Default Value |                                Description                                |
|:------------------:|:-------------------------------------------------:|:--------:|:-------------:|:-------------------------------------------------------------------------:|
| ``login_object`` | Login from [login.py](/tlnetcard_python/login.py) |   Yes    |      N/A      | A valid login object generated by [login.py](/tlnetcard_python/login.py). |

Initializes the Upgrade object. If ``login_object`` is a valid Login object, then this object will be capable of performing all other functions built into the object.  

## get_firmware_version() -> str

GETs the firmware version for the TLNETCARD. **Please note that this function is simply an alias to the function of the same name in [information.py](/tlnetcard_python/monitor/about/information) from /tlnetcard_python/monitor/about/information.**  
Example:

```python
from tlnetcard_python import Login
from tlnetcard_python.system.administration import Upgrade

# Initialize the login object.
card = Login("sample_username", "sample_password", "10.0.0.100", reject_invalid_certs=False)

# Get firmware version.
card_upgrade = Upgrade(card)
firmware_version = card_upgrade.get_firmware_version()

# Continue configuring card.
...

# Then logout the session.
card.logout()
```

## upgrade_snmp_firmware(path: str = "ups-tl-01_12_05c.bin") -> bool

|    Name    |  Type  | Required |        Default Value         |                       Description                        |
|:----------:|:------:|:--------:|:----------------------------:|:--------------------------------------------------------:|
| ``path`` | String |    No    | ``"ups-tl-01_12_05c.bin"`` | The upgrade ``.bin`` file, downloaded from Tripp Lite. |

Uploads the specified SNMP Device Firmware. If the specified (or default) configuration file does not exist, this function will return ``False``. Otherwise, ``True`` will be returned. Please note that the cards may not accept configuration files that do not use the  ``.bin`` file extension. Also, after upgrade files are uploaded, the card will become unresponsive for ~1 minute. Therefore, if further configuration is needed after uploading a file, you should pause your program before continuing.  
Example:

```python
from time import sleep
from tlnetcard_python import Login
from tlnetcard_python.system.administration import BatchConfiguration, Upgrade

# Initialize the login object.
card = Login("sample_username", "sample_password", "10.0.0.100", reject_invalid_certs=False)

# (Optional) Download current configuration as backup.
card_batch_config = BatchConfiguration(card)
card_batch_config.download_snmp_configuration()
card_batch_config.download_system_configuration()

# Upgrade SNMP Device Firmware.
card_upgrade = Upgrade(card)
card_upgrade.upgrade_snmp_firmware()

# Pause program before continuing.
sleep(60)

# Continue configuring card.
...

# Then logout the session.
card.logout()
```

## Documentation Tree

* [tlnetcard_python](/tlnetcard_python)
  * [Monitor](/tlnetcard_python/monitor)
    * [Information](/tlnetcard_python/monitor/information)
      * [Battery Parameters](/tlnetcard_python/monitor/information/battery_parameters)
      * [In/Out Parameters](/tlnetcard_python/monitor/information/in_out_parameters)
      * [Identification](/tlnetcard_python/monitor/information/identification)
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
      * Upgrade
    * [Notification](/tlnetcard_python/system/notification)
      * [SNMP Access](/tlnetcard_python/system/notification/snmp_access)
      * [SNMPv3 USM](/tlnetcard_python/system/notification/snmpv3_usm)
      * [SNMP Trap](/tlnetcard_python/system/notification/snmp_trap)
      * [Mail Server](/tlnetcard_python/system/notification/mail_server)
      * [Wake On LAN](/tlnetcard_python/system/notification/wake_on_lan)
      * [Modbus TCP](/tlnetcard_python/system/notification/modbus_tcp)
