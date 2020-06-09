"""
tlnetcard_python.monitor.history.data_log.data_log
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This module provides a ``DataLog`` object to provide the functionality of TLNET Supervisor ->
Monitor -> History -> Data Log.
"""

# Required internal classes/functions.
from tlnetcard_python.login import Login

class DataLog:
    """
    A TLNET Supervisor ``DataLog`` object. Provides the functionality of the equivalent webpage
    TLNET Supervisor -> Monitor -> History -> Data Log.

    Basic Usage:

    >>> from tlnetcard_python import Login
    >>> from tlnetcard_python.monitor.history import DataLog
    >>> # As always, a tlnetcard_python.Login object must first be created. Then the Login object
    >>> # can be passed to the tlnetcard_python.monitor.history.DataLog object.
    >>> card = Login(user="admin", passwd="password", host="10.0.0.100")
    >>> card_data_log = DataLog(card)
    >>> # Now that the DataLog object has been created, functions belonging to the DataLog class
    >>> # can be used. For example, downloading the data log.:
    >>> card_data_log.download_data_log()
    """
    def __init__(self, login_object: Login) -> None:
        """
        Initializes the ``DataLog`` object. Returns ``None``.

        :param login_object: A valid ``tlnetcard_python.Login`` object.
        :rtype: ``None``
        """
        self._login_object = login_object
