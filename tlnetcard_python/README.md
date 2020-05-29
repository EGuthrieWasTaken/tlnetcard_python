# [login.py](login.py)

## Cheatsheet

|                                                                                                                      Function Header                                                                                                                       |                                                               Quick Description                                                               |
|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------------------------------:|
| [```__init__(user="admin", passwd="password", host="", save_passwd=False, ssl=True, reject_invalid_certs=True)```](#__init__user-str--admin-passwd-str--password-host-str---save_passwd-bool--false-ssl-bool--true-reject_invalid_certs-bool--true---none) |                                                         Initializes the Login object.                                                         |
|                                                                                                        [```get_base_url()```](#get_base_url---str)                                                                                                         |                                                  Returns the base URL for TLNET Supervisor.                                                   |
|                                                                                                            [```get_host()```](#get_host---str)                                                                                                             |                                                               Returns the host.                                                               |
|                                                                                            [```get_reject_invalid_certs()```](#get_reject_invalid_certs---bool)                                                                                            |                                               Returns the ```reject_invalid_certs``` attribute.                                               |
|                                                                                                       [```get_session()```](#get_session---session)                                                                                                        |                                                             Returns the session.                                                              |
|                                                                                     [```get_snmp_config(force=False)```](#get_snmp_configforce-bool--false---liststr)                                                                                      |                Triggers the API to pull a new version of SNMP config file if required and returns the configuration as a list.                |
|                                                                                   [```get_system_config(force=False)```](#get_system_configforce-bool--false---liststr)                                                                                    |               Triggers the API to pull a new version of system config file if required and returns the configuration as a list.               |
|                                                                                                              [```logout()```](#logout---none)                                                                                                              |                                                              Closes the session.                                                              |
|                                                                                              [```_perform_login(passwd)```](#_perform_loginpasswd-str---int)                                                                                               |                                                           Logs into a new session.                                                            |
|                                                                                         [```request_snmp_config_renewal()```](#request_snmp_config_renewal---none)                                                                                         |    Sets the _renew_snmp attribute to ```True``` so that the next call to get_snmp_config() will trigger a re-pull of the SNMP config file.    |
|                                                                                       [```request_system_config_renewal()```](#request_system_config_renewal---none)                                                                                       | Sets the _renew_system attribute to ```True``` so that the next call to get_system_config() will trigger a re-pull of the system config file. |
|                                                                                          [```set_host(host, passwd="")```](#set_hosthost-str-passwd-str-----none)                                                                                          |                                               Sets host and then calls ```_perform_login()```.                                                |

## \_\_init__(user: str = "admin", passwd: str = "password", host: str = "", save_passwd: bool = False, ssl: bool = True, reject_invalid_certs: bool = True) -> None

|            Name            |  Type   | Required |  Default Value   |                                                                          Description                                                                          |
|:--------------------------:|:-------:|:--------:|:----------------:|:-------------------------------------------------------------------------------------------------------------------------------------------------------------:|
|         ```user```         | String  |    No    |  ```"admin"```   |                                                                The TLNET Supervisor username.                                                                 |
|        ```passwd```        | String  |    No    | ```"password"``` |                                                                The TLNET Supervisor password.                                                                 |
|         ```host```         | String  |    No    |     ```""```     |                                                                 The address of the TLNETCARD.                                                                 |
|     ```save_passwd```      | Boolean |    No    |   ```False```    |       Determines whether or not the ```passwd``` value will be saved in the object. When set to ```False```, the ```passwd``` value will not be saved.        |
|         ```ssl```          | Boolean |    No    |    ```True```    | Determines whether or not the TLNET Supervisor at the host address has an SSL certificate i.e. does it use HTTPS. When set to ```True```, HTTPS will be used. |
| ```reject_invalid_certs``` | Boolean |    No    |    ```True```    |  Determines whether or not an invalid (i.e. a self-signed) SSL certificate will be rejected. When set to ```True```, invalid certificates will be rejected.   |

Initializes the Login object. A Login object is required by all classes in this repository.  
Example:

```python
from tlnetcard_python import Login

# Initialize the login object.
card = Login("sample_username", "sample_password", "10.0.0.100", reject_invalid_certs=False)

# Do whatever you need to do with the card.
...

# Then logout the session.
card.logout()
```

## get_base_url() -> str

Returns the ```self._base_url``` attribute. This attribute will be the fully-qualified URL of the TLNET Supervisor, usually in the form of ```https://<host>```, but can be in the form ```http://<host>``` if ```ssl``` was set to ```False``` in ```__init__()```. While this function is public, its primary function is to be called by other classes in this module.  
Example:

```python
from tlnetcard_python import Login

# Initialize the login object.
card = Login("sample_username", "sample_password", "10.0.0.100", reject_invalid_certs=False)

# Print the base_url.
print(card.get_base_url())

# Then logout the session.
card.logout()
```

Which would print:  

```text
https://10.0.0.100
```

## get_host() -> str

Returns the ```self._host``` attribute. This will be whatever was specified when initializing the object, or the most recent ```host``` argument passed to the ```set_host()``` function. Like the ```get_base_url()``` function, this function's primary function is to be called by other classes in this module.  
Example:

```python
from tlnetcard_python import Login

# Initialize the login object.
card = Login("sample_username", "sample_password", "10.0.0.100", reject_invalid_certs=False)

# Print the host's address.
print(card.get_host())

# Then logout the session.
card.logout()
```

Which would print:  

```python
10.0.0.100
```

## get_reject_invalid_certs() -> bool

Returns the ```self._reject_invalid_certs``` attribute. This will be whatever was specified when initializing the object. Like most other functions in this class, this function's primary function is to be used by other classes in this module.  
Example:

```python
from tlnetcard_python import Login

# Initialize the login object.
card = Login("sample_username", "sample_password", "10.0.0.100", reject_invalid_certs=False)

# Print whether the card rejects invalid certs.
print(card.get_reject_invalid_certs())

# Then logout the session.
card.logout()
```

Which would print:

```python
False
```

## get_session() -> Session

Returns the ```self._session``` attribute. This will be the logged-in session created after initializing the object, or after the most recent call of the  ```set_host()``` function. This will be a standards python [requests](https://requests-html.kennethreitz.org/) object which may be used to make GET or POST requests. For more information, see the documentation for [requests](https://requests-html.kennethreitz.org/). This function's primary function is to be called by other classes in this module.  
Example:

```python
from tlnetcard_python import Login

# Initialize the login object.
card = Login("sample_username", "sample_password", "10.0.0.100", reject_invalid_certs=False)

# Make a GET request with the session.
r = card.get_session().get("https://duckduckgo.com")
# Do whatever with the respose.
...

# Then logout the session.
card.logout()
```

## get_snmp_config(force: bool = False) -> List[str]

Triggers the API to pull a new version of SNMP config file if required and returns the configuration as a list. Many of the GET-style functions in this API use this function to pull configuration information, and this is the primary function of this function. The list returned should be the contents of the up-to-date configuration file, but for extra certainty that the file has been pulled recently the ```force``` parameter can be set to ```True```.  
Example:

```python
from tlnetcard_python import Login

# Initialize the login object.
card = Login("sample_username", "sample_password", "10.0.0.100", reject_invalid_certs=False)

# Pull card configuration information.
snmp_config, sys_config = card.get_snmp_config(force=True), card.get_system_config(force=True)

# Do whatever you need to do with the card.
...

# Then logout the session.
card.logout()
```

## get_system_config(force: bool = False) -> List[str]

Triggers the API to pull a new version of system config file if required and returns the configuration as a list. Many of the GET-style functions in this API use this function to pull configuration information, and this is the primary function of this function. The list returned should be the contents of the up-to-date configuration file, but for extra certainty that the file has been pulled recently the ```force``` parameter can be set to ```True```.  

Example:

```python
from tlnetcard_python import Login

# Initialize the login object.
card = Login("sample_username", "sample_password", "10.0.0.100", reject_invalid_certs=False)

# Pull card configuration information.
snmp_config, sys_config = card.get_snmp_config(force=True), card.get_system_config(force=True)

# Do whatever you need to do with the card.
...

# Then logout the session.
card.logout()
```

## logout() -> None

Closes the session saved as ```self._session```. This module should be called before your program terminates.  
Example:

```python
from tlnetcard_python import Login

# Initialize the login object.
card = Login("sample_username", "sample_password", "10.0.0.100", reject_invalid_certs=False)

# Do whatever you need to do with the card.
...

# Then logout the session.
card.logout()
```

## _perform_login(passwd: str) -> int

|     Name     |  Type  | Required | Default Value |           Description          |
|:------------:|:------:|:--------:|:-------------:|:------------------------------:|
| ```passwd``` | String |    Yes   |      N/A      | The TLNET Supervisor password. |

Creates a self._session object that is logged into TLNET Supervisor. This module was not meant to be called directly, so use it with caution, or simply call it indirectly using the ```set_hosts()``` function.  
Example:

```python
from tlnetcard_python import Login

# Initialize the login object.
card = Login("sample_username", "incorrect_password", "10.0.0.100", reject_invalid_certs=False)
# Tisk tisk, you put in the wrong password!
card.performLogin("correct_password")

# Do whatever you need to do with the card.
...

# Then logout the session.
card.logout()
```

## request_snmp_config_renewal() -> None

Sets the ```_renew_snmp``` attribute to ```True``` so that the next call to [```get_snmp_config()```](#get_snmp_configforce-bool--false---liststr) will trigger a re-pull of the SNMP config file. This function is called by any class function which makes a POST request to the TLNET Supervisor to edit any values in the SNMP config file. This is to ensure that the information returned by GET-style class functions will always be updated. Because the class functions in this API already make use of this function automatically, this function should never be called directly by the user. Should the user wish to guaruntee that a fresh configuration is retrieved from the TLNET Supervisor, they should instead use [```get_snmp_config(force=True)```](#get_snmp_configforce-bool--false---liststr).

## request_system_config_renewal() -> None

Sets the ```_renew_system``` attribute to ```True``` so that the next call to [```get_system_config()```](#get_system_configforce-bool--false---liststr) will trigger a re-pull of the system config file. This function is called by any class function which makes a POST request to the TLNET Supervisor to edit any values in the system config file. This is to ensure that the information returned by GET-style class functions will always be updated. Because the class functions in this API already make use of this function automatically, this function should never be called directly by the user. Should the user wish to guaruntee that a fresh configuration is retrieved from the TLNET Supervisor, they should instead use [```get_system_config(force=True)```](#get_system_configforce-bool--false---liststr).

## set_host(host: str, passwd: str = "") -> None

|     Name     |  Type  | Required | Default Value |          Description           |
|:------------:|:------:|:--------:|:-------------:|:------------------------------:|
|  ```host```  | String |   Yes    |      N/A      | The address of the TLNETCARD.  |
| ```passwd``` | String |    No    |   ```""```    | The TLNET Supervisor password. |

Sets the ```self._host``` attribute to ```host```, and calls ```logout()``` if a session was already running. Then, the ```performLogin()``` function is called using ```passwd``` if it was specified. If it was not specified, the ```self._passwd``` value will be used if it was specified. Otherwise, the user will be prompted to enter a password (which will then be saved if the ```self._save_passwd``` attribute is set to ```True```). This function is highly useful if you wish to configure multiple cards which share the same credentials.  
Example:

```python
from tlnetcard_python import Login

# Defining a list of TLNETCARD hostnames.
hosts = ["10.0.0.100", "10.0.0.101", "10.0.0.103"]
# Initializing a session-less Login object.
card = Login("admin", "sample_password", save_passwd=True)

# Logging into cards and performing tasks.
for i in hosts:
    card.set_host(i)

    # Do whatever you need to do with the cards.
    ...
# Then logout the last session.
card.logout()
```

## Documentation Tree

* tlnetcard_python
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
