# [user_manager.py](user_manager.py)

|                                                                                                                                                                                                                                                                                                                             Function Header                                                                                                                                                                                                                                                                                                                             |              Quick Description              |
|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------:|:-------------------------------------------:|
|                                                                                                                                                                                                                                                                                                   [``__init__(login_object)``](#__init__login_object-login---none)                                                                                                                                                                                                                                                                                                    |     Initializes the UserManager object.     |
|                                                                                                                                                                                                                                                                                                            [``disable_radius()``](#disable_radius---none)                                                                                                                                                                                                                                                                                                             |       Disables RADIUS authentication.       |
|                                                                                                                                                                                                                                                                                                             [``enable_radius()``](#enable_radius---none)                                                                                                                                                                                                                                                                                                              |       Enables RADIUS authentication.        |
|                                                                                                                                                                                                                                                                                  [``get_permissions(user="Administrator")``](#get_permissionsuser-str--administrator---dictstr-bool)                                                                                                                                                                                                                                                                                  | GETs the permissions for the provided user. |
|                                                                                                                                                                                                                                                                                                        [``get_server_info()``](#get_server_info---dictstr-any)                                                                                                                                                                                                                                                                                                        |  GETs information about the RADIUS server.  |
|                                                                                                                                                                                                                                                                                                   [``get_user()``](#get_useruser-str--administrator---dictstr-any)                                                                                                                                                                                                                                                                                                    |  GETs information about the provided user.  |
| [``set_permissions(user="Administrator", login_user=False, framed_user=False, callback_login=False, callback_framed=False, outbound=False, administrative=False, nas_prompt=False, authenticate_only=False, callback_nas_prompt=False, call_check=False, callback_administrative=False)``](#set_permissionsuser-str--administrator-login_user-bool--false-framed_user-bool--false-callback_login-bool--false-callback_framed-bool--false-outbound-bool--false-administrative-bool--false-nas_prompt-bool--false-authenticate_only-bool--false-callback_nas_prompt-bool--false-call_check-bool--false-callback_administrative-bool--false-selenium-bool--false---bool) |   Sets permissions for the provided user.   |
|                                                                                                                                                                                                                                                                               [``set_server_info(server, secret, port)``](#set_server_infoserver-str-secret-str-port-int--1812---none)                                                                                                                                                                                                                                                                                |   Sets information for the RADIUS server.   |
|                                                                                                                                                                                                                                                    [``set_user(username, passwd, wan_access=False, user="Administrator")``](#set_userusername-str-passwd-str-wan_access-int--false-user-str--administrator---bool)                                                                                                                                                                                                                                                    |   Sets information for the provided user.   |

## \_\_init__(login_object: Login) -> None

|        Name        |                        Type                       | Required | Default Value | Description                                                               |
|:------------------:|:-------------------------------------------------:|----------|---------------|---------------------------------------------------------------------------|
| ``login_object`` | Login from [login.py](/tlnetcard_python/login.py) | Yes      | N/A           | A valid login object generated by [login.py](/tlnetcard_python/login.py). |

Initializes the UserManager object. If ``login_object`` is a valid Login object, then this object will be capable of performing all other functions built into the object.

## disable_radius() -> None

Disables RADIUS authentication.  
Example:

```python
from tlnetcard_python import Login
from tlnetcard_python.system.administration import UserManager

# Initialize the login object.
card = Login("sample_username", "sample_password", "10.0.0.100", reject_invalid_certs=False)

# Disable RADIUS.
card_user_manager = UserManager(card)
card_user_manager.disable_radius()

# Continue configuring card.
...

# Then logout the session.
card.logout()
```

## enable_radius() -> None

Enables RADIUS authentication. RADIUS will be enabled automatically when server info is set using [set_server_info()](#set_server_infoserver-secret-port), so there is no need to use these two functions together.  
Example:

```python
from tlnetcard_python import Login
from tlnetcard_python.system.administration import UserManager

# Initialize the login object.
card = Login("sample_username", "sample_password", "10.0.0.100", reject_invalid_certs=False)

# Enable RADIUS.
card_user_manager = UserManager(card)
card_user_manager.enable_radius()

# Continue configuring card.
...

# Then logout the session.
card.logout()
```

## get_permissions(user: str = "Administrator") -> Dict[str, bool]

|    Name    |  Type  | Required |     Default Value     |            Description           |
|:----------:|:------:|:--------:|:---------------------:|:--------------------------------:|
| ``user`` | String |    No    | ``"Administrator"`` | The user to get permissions for. |

GETs permissions for the provided user. If ``user`` is not a valid value (``"Administrator"``, ``"Device Manager"``, ``"Read Only User"``), then this function will return ``-1``. Otherwise, a dictionary of user permissions will be returned. The dictionary keys are as follows: ``Login User``, ``Framed User``, ``Callback Login``, ``Callback Framed``, ``Outbound``, ``Administrative``, ``NAS Prompt``, ``Authenticate Only``, ``Callback NAS Prompt``, ``Call Check``, and ``Callback Administrative`` where each key contains a boolean for whether or not the permission is granted for that user type.  
Example:

```python
from tlnetcard_python import Login
from tlnetcard_python.system.administration import UserManager

# Initialize the login object.
card = Login("sample_username", "sample_password", "10.0.0.100", reject_invalid_certs=False)

# Get administrative permissions.
card_user_manager = UserManager(card)
admin_permissions = card_user_manager.get_permissions()
print(admin_permissions["Administrative"])

# Continue configuring card.
...

# Then logout the session.
card.logout()
```

Which may print, for example:

```python
True
```

## get_server_info() -> Dict[str, Any]

GETs information about the RADIUS server and returns it in a dictionary. The dictionary keys are as follows:  

* ``IP``: The IP of the RADIUS server.
* ``Secret``: The secret string for the RADIUS server.
* ``Port``: The port RADIUS is using.

Example:

```python
from tlnetcard_python import Login
from tlnetcard_python.system.administration import UserManager

# Initialize the login object.
card = Login("sample_username", "sample_password", "10.0.0.100", reject_invalid_certs=False)

# Get RADIUS server information.
card_user_manager = UserManager(card)
radius_server = card_user_manager.get_server_info()
print(radius_server["IP"])

# Continue configuring card.
...

# Then logout the session.
card.logout()
```

Which may print, for example:

```python
"10.0.0.200"
```

## get_user(user: str = "Administrator") -> Dict[str, Any]

|      Name      |   Type  | Required |     Default Value     |                 Description                 |
|:--------------:|:-------:|:--------:|:---------------------:|:-------------------------------------------:|
|   ``user``   |  String |    No    | ``"Administrator"`` |       The user to get information for.      |

GETs information about the provided user. If ``user`` is not a valid value (``"Administrator"``, ``"Device Manager"``, ``"Read Only User"``), then this function will return ``-1``. Otherwise, a dictionary of user information will be returned. The dictionary keys are as follows:  

* ``Type``: The type of user (this will be identical to the ``user`` parameter).
* ``Name``: The user's name.
* ``Password``: The user's password.
* ``WAN Access``: Whether the user can be accessed from outside of the LAN.

Example:

```python
from tlnetcard_python import Login
from tlnetcard_python.system.administration import UserManager

# Initialize the login object.
card = Login("sample_username", "sample_password", "10.0.0.100", reject_invalid_certs=False)

# Get user information.
card_user_manager = UserManager(card)
user_info = card_user_manager.get_user()
print(user_info["Name"])

# Continue configuring card.
...

# Then logout the session.
card.logout()
```

Which may print, for example:

```python
"10.0.0.200"
```

## set_permissions(user: str = "Administrator", login_user: bool = False, framed_user: bool = False, callback_login: bool = False, callback_framed: bool = False, outbound: bool = False, administrative: bool = False, nas_prompt: bool = False, authenticate_only: bool = False, callback_nas_prompt: bool = False, call_check: bool = False, callback_administrative: bool = False, selenium: bool = False) -> bool

|              Name             |   Type  | Required |     Default Value     |                               Description                              |
|:-----------------------------:|:-------:|:--------:|:---------------------:|:----------------------------------------------------------------------:|
|           ``user``          |  String |    No    | ``"Administrator"`` |                    The user to set permissions for.                    |
|        ``login_user``       | Boolean |    No    |      ``False``      |        Whether the user should have ``login_user`` permission.       |
|       ``framed_user``       | Boolean |    No    |      ``False``      |       Whether the user should have ``framed_user`` permission.       |
|      ``callback_login``     | Boolean |    No    |      ``False``      |      Whether the user should have ``callback_login`` permission.     |
|     ``callback_framed``     | Boolean |    No    |      ``False``      |     Whether the user should have ``callback_framed`` permission.     |
|         ``outbound``        | Boolean |    No    |      ``False``      |         Whether the user should have ``outbound`` permission.        |
|      ``administrative``     | Boolean |    No    |      ``False``      |      Whether the user should have ``administrative`` permission.     |
|        ``nas_prompt``       | Boolean |    No    |      ``False``      |        Whether the user should have ``nas_prompt`` permission.       |
|    ``authenticate_only``    | Boolean |    No    |      ``False``      |    Whether the user should have ``authenticate_only`` permission.    |
|   ``callback_nas_prompt``   | Boolean |    No    |      ``False``      |   Whether the user should have ``callback_nas_prompt`` permission.   |
|        ``call_check``       | Boolean |    No    |      ``False``      |        Whether the user should have ``call_check`` permission.       |
| ``callback_administrative`` | Boolean |    No    |      ``False``      | Whether the user should have ``callback_administrative`` permission. |
|         ``selenium``        | Boolean |    No    |      ``False``      |              Whether a selenium approach should be used.               |

Sets the permissions for the provided user. If ``user`` is not a valid value (``"Administrator"``, ``"Device Manager"``, ``"Read Only User"``), then this function will return ``False``. Otherwise, ``True`` will be returned.  
**It is recommended that ``selenium`` be set to ``True`` for speed, but it defaults to ``False`` for compatability. If you elect to use Selenium for this function, you will have to have [Google Chrome](https://www.google.com/chrome/) or [Chromium](https://www.chromium.org/getting-involved/download-chromium) installed on your system, as well as the corresponding version of Chrome/Chromium's [webdriver](https://sites.google.com/a/chromium.org/chromedriver/downloads) in your PATH. For more details on configuring Selenium, see [their PyPi page](https://pypi.org/project/selenium/).**  
Example:

```python
from tlnetcard_python import Login
from tlnetcard_python.system.administration import UserManager

# Initialize the login object.
card = Login("sample_username", "sample_password", "10.0.0.100", reject_invalid_certs=False)

# Setting user permissions.
card_user_manager = UserManager(card)
card_user_manager.set_permissions(user="Read Only", callback_nas_prompt=True, outbound=True)

# Continue configuring card.
...

# Then logout the session.
card.logout()
```

## set_server_info(server: str, secret: str, port: int = 1812) -> None

|     Name     |   Type  | Required | Default Value |              Description             |
|:------------:|:-------:|:--------:|:-------------:|:------------------------------------:|
| ``server`` |  String |    Yes   |      N/A      | The IP address of the RADIUS server. |
| ``secret`` |  String |    Yes   |      N/A      |  The RADIUS server's secret string.  |
|  ``port``  | Integer |    No    |   ``1812``  | The port the RADIUS server is using. |

Sets information for the RADIUS server.  
Example:

```python
from tlnetcard_python import Login
from tlnetcard_python.system.administration import UserManager

# Initialize the login object.
card = Login("sample_username", "sample_password", "10.0.0.100", reject_invalid_certs=False)

# Setting user permissions.
card_user_manager = UserManager(card)
card_user_manager.set_server_info("10.0.0.200", "Av43udHEk3uh2278eDss", 3333)

# Continue configuring card.
...

# Then logout the session.
card.logout()
```

## set_user(username: str, passwd: str, wan_access: int = False, user: str = "Administrator") -> bool

|       Name       |  Type   | Required |     Default Value     |                         Description                          |
|:----------------:|:-------:|:--------:|:---------------------:|:------------------------------------------------------------:|
|  ``username``  | String  |   Yes    |          N/A          |            The intended username for the account.            |
|   ``passwd``   | String  |   Yes    |          N/A          |            The intended password for the account.            |
| ``wan_access`` | Boolean |    No    |      ``False``      |    Whether the account should be accessible from the WAN.    |
|    ``user``    | String  |    No    | ``"Administrator"`` | The type of user (from which permissions will be inherited). |

Sets information for the provided user. If ``user`` is not a valid value (``"Administrator"``, ``"Device Manager"``, ``"Read Only User"``), then this function will return ``False``. Otherwise, ``True`` will be returned.  
Example:

```python
from tlnetcard_python import Login
from tlnetcard_python.system.administration import UserManager

# Initialize the login object.
card = Login("sample_username", "sample_password", "10.0.0.100", reject_invalid_certs=False)

# Setting user information.
card_user_manager = UserManager(card)
card_user_manager.set_server_info("manager", "imthecaptain", user="Device Manager")

# Continue configuring card.
...

# Then logout the session.
card.logout()
```

## Documentation Tree

* [tlnetcard_python](/tlnetcard_python)
  * [Monitor](/tlnetcard_python/monitor)
    * [Information](/tlnetcard_python/monitor/information)
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
      * User Manager
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
