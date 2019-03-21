from typing import Optional, List, Tuple
from datetime import datetime

def get_reminders(
    calendar: Optional[Calendar], completed=Optional[bool]
) -> List[Reminder]: ...
def get_all_calendars() -> List[Calendar]: ...
def get_default_calendar() -> Calendar: ...
def get_calendar(calendar_id: str) -> Optional[Calendar]: ...
def delete_reminder(reminder: Reminder) -> bool: ...
def delete_calendar(calendar: Calendar) -> bool: ...

class Alarm:
    date: datetime
    location: Tuple[str, float, float, Optional[float]]
    proximity: str

class Calendar:
    title: str
    identifier: str
    def save(self) -> None: ...

class Reminder:
    title: str
    notes: str
    completed: bool
    completion_date: Optional[datetime]
    due_date: Optional[datetime]
    alarms: List[Alarm]
    def __init__(self, calendar: Optional[Calendar]) -> None: ...
    def save(self) -> None: ...
