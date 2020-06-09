"""
tlnetcard_python.monitor.history.event_log.event_log
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This module provides a ``EventLog`` object to provide the functionality of TLNET Supervisor ->
Monitor -> History -> Event Log.
"""

# Required internal classes/functions.
from tlnetcard_python.login import Login

class EventLog:
    """
    A TLNET Supervisor ``EventLog`` object. Provides the functionality of the equivalent webpage
    TLNET Supervisor -> Monitor -> History -> Event Log.

    Basic Usage:

    >>> from tlnetcard_python import Login
    >>> from tlnetcard_python.monitor.history import EventLog
    >>> # As always, a tlnetcard_python.Login object must first be created. Then the Login object
    >>> # can be passed to the tlnetcard_python.monitor.history.EventLog object.
    >>> card = Login(user="admin", passwd="password", host="10.0.0.100")
    >>> card_event_log = EventLog(card)
    >>> # Now that the EventLog object has been created, functions belonging to the EventLog class
    >>> # can be used. For example, downloading the event log:
    >>> card_event_log.download_event_log()
    """
    def __init__(self, login_object: Login) -> None:
        """
        Initializes the ``EventLog`` object. Returns ``None``.

        :param login_object: A valid ``tlnetcard_python.Login`` object.
        :rtype: ``None``
        """
        self._login_object = login_object
