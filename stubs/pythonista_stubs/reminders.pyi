"""This is a stub file for the `reminders` module, providing type hints for its
functions and their parameters, to be used for static analysis and autocompletion.
"""

import datetime
from typing import Literal

# -----------------------------------------------------------------------------
# Alarm Objects
# -----------------------------------------------------------------------------
class Alarm:
    """Alarm objects represent an alarm associated with a reminder."""

    date: datetime.datetime | None
    """The absolute date when the alarm is triggered."""
    location: tuple[str, float, float] | tuple[str, float, float, float] | None
    """The title, coordinates, and radius for a geo-location-based alarm.
    Represented as a 3- or 4-tuple: (title, latitude, longitude[, radius]).
    """
    proximity: Literal["enter", "leave", "none"]
    """Determines if a location-based alarm is triggered when entering or
    leaving the specified area.
    """

# -----------------------------------------------------------------------------
# Reminder Objects
# -----------------------------------------------------------------------------
class Reminder:
    """Reminder objects represent a single reminder in a list."""

    def __init__(self, calendar: Calendar | None = None): ...

    alarms: list[Alarm]
    """A list of Alarm objects associated with this reminder."""
    completed: bool
    """Whether the reminder has been completed (checked off) yet."""
    completion_date: datetime.datetime | None
    """The date when the reminder was completed, or None if not completed."""
    due_date: datetime.datetime | None
    """The due date of the reminder."""
    notes: str
    """Additional notes for the reminder."""
    priority: int
    """Priority of the reminder (0 = no priority, 1 = highest, 9 = lowest)."""
    title: str
    """The title of the reminder."""
    url: str
    """A URL associated with the reminder."""

    def save(self) -> None:
        """Save changes to the database."""
        ...

# -----------------------------------------------------------------------------
# Calendar Objects
# -----------------------------------------------------------------------------
class Calendar:
    """Calendar objects represent lists of reminders."""

    title: str
    """The title of the list of reminders."""
    identifier: str
    """The unique identifier of the calendar (readonly)."""

    def save(self) -> None:
        """Save changes to the database."""
        ...

# -----------------------------------------------------------------------------
# Functions
# -----------------------------------------------------------------------------
def get_reminders(
    calendar: Calendar | None = None,
    completed: bool | None = None,
) -> list[Reminder]:
    """Return all reminders in the given Calendar (or all calendars).

    Args:
        calendar (Calendar, optional): The calendar to get reminders from.
            Defaults to None.
        completed (bool, optional): Filters reminders by completion status.
            Defaults to None (all reminders).

    Returns:
        list[Reminder]: A list of Reminder objects.

    """
    ...

def get_all_calendars() -> list[Calendar]:
    """Return a list of all available Calendar objects."""
    ...

def get_default_calendar() -> Calendar:
    """Return the Calendar that is used for new reminders by default."""
    ...

def get_calendar(calendar_id: str) -> Calendar | None:
    """Return a specific Calendar by its unique identifier.

    Args:
        calendar_id (str): The unique identifier of the calendar.

    Returns:
        Calendar | None: The Calendar object, or None if not found.

    """
    ...

def delete_reminder(reminder: Reminder) -> bool:
    """Remove a Reminder from the database.

    Args:
        reminder (Reminder): The Reminder object to remove.

    Returns:
        bool: True if the removal was successful, False otherwise.

    """
    ...

def delete_calendar(calendar: Calendar) -> bool:
    """Remove a Calendar from the database.

    Args:
        calendar (Calendar): The Calendar object to remove.

    Returns:
        bool: True if the removal was successful, False otherwise.

    """
    ...
