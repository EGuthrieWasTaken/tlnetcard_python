# [ftp.py](ftp.py)

|                          Function Header                           |       Quick Description       |
|:------------------------------------------------------------------:|:-----------------------------:|
| [``__init__(login_object)``](#__init__login_object-login---none) |  Initializes the Ftp object.  |
|             [``disable_ftp()``](#disable_ftp---none)             |         Disables FTP.         |
|              [``enable_ftp()``](#enable_ftp---none)              |         Enables FTP.          |
|            [``get_ftp_port()``](#get_ftp_port---int)             | GETs the port in use for FTP. |
|  [``set_ftp_port(port=21)``](#set_ftp_portport-int--21---none)   | Sets the port for use by FTP. |

## \_\_init__(login_object: Login) -> None

|        Name        |                        Type                       | Required | Default Value | Description                                                               |
|:------------------:|:-------------------------------------------------:|----------|---------------|---------------------------------------------------------------------------|
| ``login_object`` | Login from [login.py](/tlnetcard_python/login.py) | Yes      | N/A           | A valid login object generated by [login.py](/tlnetcard_python/login.py). |

Initializes the Ftp object. If ``login_object`` is a valid Login object, then this object will be capable of performing all other functions built into the object.

## disable_ftp() -> None

Disables FTP.  
Example:

```python
from tlnetcard_python import Login
from tlnetcard_python.system.administration import Ftp

# Initialize the login object.
card = Login("sample_username", "sample_password", "10.0.0.100", reject_invalid_certs=False)

# Disable FTP.
card_ftp = Ftp(card)
card_ftp.disable_ftp()

# Continue configuring card.
...

# Then logout the session.
card.logout()
```

## enable_ftp() -> None

Enables FTP with currently configured port. FTP will be enabled automatically when the FTP port is changed using [set_ftp_port()](#set_ftp_portport), so there is no need to use these two functions together.  
Example:

```python
from tlnetcard_python import Login
from tlnetcard_python.system.administration import Ftp

# Initialize the login object.
card = Login("sample_username", "sample_password", "10.0.0.100", reject_invalid_certs=False)

# Enable FTP.
card_ftp = Ftp(card)
card_ftp.enable_ftp()

# Continue configuring card.
...

# Then logout the session.
card.logout()
```

## get_ftp_port() -> int

GETs the FTP port.  
Example:

```python
from tlnetcard_python import Login
from tlnetcard_python.system.administration import Ftp

# Initialize the login object.
card = Login("sample_username", "sample_password", "10.0.0.100", reject_invalid_certs=False)

# Get FTP port.
card_ftp = Ftp(card)
ftp_port = card_ftp.get_ftp_port()

# Continue configuring card.
...

# Then logout the session.
card.logout()
```

## set_ftp_port(port: int = 21) -> None

|    Name    |   Type  | Required | Default Value |        Description       |
|:----------:|:-------:|:--------:|:-------------:|:------------------------:|
| ``port`` | Integer |    No    |    ``21``   | The FTP port to be used. |

Sets the FTP port. When the FTP port is set using this function, FTP is automatically enabled.  
Example:

```python
from tlnetcard_python import Login
from tlnetcard_python.system.administration import Ftp

# Initialize the login object.
card = Login("sample_username", "sample_password", "10.0.0.100", reject_invalid_certs=False)

# Set FTP port.
card_ftp = Ftp(card)
card_ftp.set_ftp_port(2121)

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
      * FTP
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
