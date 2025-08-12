"""This is a stub file for the `contacts` module, providing type hints for its
functions and their parameters, to be used for static analysis and autocompletion.
"""

import datetime

# -----------------------------------------------------------------------------
# Constants for multi-value attributes
# -----------------------------------------------------------------------------
HOME: str = ...
WORK: str = ...
OTHER: str = ...
IPHONE: str = ...
MAIN_PHONE: str = ...
HOME_FAX: str = ...
WORK_FAX: str = ...
OTHER_FAX: str = ...
PAGER: str = ...
FATHER: str = ...
MOTHER: str = ...
PARENT: str = ...
BROTHER: str = ...
SISTER: str = ...
CHILD: str = ...
FRIEND: str = ...
SPOUSE: str = ...
PARTNER: str = ...
ASSISTANT: str = ...
MANAGER: str = ...
HOMEPAGE: str = ...
STREET: str = ...
CITY: str = ...
STATE: str = ...
ZIP: str = ...
COUNTRY: str = ...
COUNTRY_CODE: str = ...

# -----------------------------------------------------------------------------
# Person Objects
# -----------------------------------------------------------------------------
class Person:
    """Person objects represent people in the address book."""

    address: list[tuple[str, dict[str, str]]]
    """Street address(es). The inner dictionary uses keys from the constants
    section (e.g., STREET, CITY).
    """
    birthday: datetime.datetime | None
    """Birthday as a datetime object."""
    creation_date: datetime.datetime
    """When the person was added (readonly)."""
    department: str
    """Department name."""
    email: list[tuple[str, str]]
    """Email address(es)."""
    first_name: str
    """First name."""
    first_name_phonetic: str
    """Phonetic first name."""
    full_name: str
    """The person's full name (readonly)."""
    id: int
    """The persistent identifier of the person record (readonly)."""
    image_data: bytes | None
    """The person's image data (e.g., PNG or JPEG) or None."""
    instant_message: list[tuple[str, dict[str, str]]]
    """Instant message accounts."""
    job_title: str
    """Job title."""
    kind: int
    """The kind of address book record (0 for person, 1 for organization)."""
    last_name: str
    """Last name."""
    last_name_phonetic: str
    """Phonetic last name."""
    middle_name: str
    """Middle name."""
    middle_name_phonetic: str
    """Phonetic middle name."""
    modification_date: datetime.datetime
    """When the person was last modified (readonly)."""
    nickname: str
    """Nickname."""
    note: str
    """Additional notes."""
    organization: str
    """Organization name."""
    phone: list[tuple[str, str]]
    """Phone number(s)."""
    prefix: str
    """Prefix (e.g., 'Sir')."""
    related_names: list[tuple[str, str]]
    """Related names."""
    social_profile: list[tuple[str, dict[str, str]]]
    """Social profile(s)."""
    suffix: str
    """Suffix (e.g., 'Jr.')."""
    url: list[tuple[str, str]]
    """URL(s)."""
    vcard: str
    """VCard representation of the person's data (readonly)."""

# -----------------------------------------------------------------------------
# Group Objects
# -----------------------------------------------------------------------------
class Group:
    """A Group object represents a group in the address book."""

    name: str
    """The group's name."""
    id: int
    """The persistent identifier of the group (readonly)."""

# -----------------------------------------------------------------------------
# Functions
# -----------------------------------------------------------------------------
def get_group(group_id: int) -> Group | None:
    """Return the Group with the given id, or None if not found."""
    ...

def get_all_groups() -> list[Group]:
    """Return a list of all Group objects in the address book."""
    ...

def add_group() -> Group:
    """Add a new Group to the address book.

    Returns:
        Group: The newly created Group object.

    """
    ...

def remove_group(group: Group) -> None:
    """Remove a Group from the address book."""
    ...

def add_person(person: Person) -> None:
    """Add a Person to the address book."""
    ...

def remove_person(person: Person) -> None:
    """Remove a Person from the address book."""
    ...

def find(name: str) -> list[Person]:
    """Do a prefix search for the given name and return a list of matches."""
    ...

def get_all_people() -> list[Person]:
    """Return a list of all people in the address book."""
    ...

def get_person(person_id: int) -> Person | None:
    """Return the Person with the given id, or None if not found."""
    ...

def save() -> None:
    """Save all pending changes in the contacts database."""
    ...

def revert() -> None:
    """Revert all pending changes in the contacts database."""
    ...

def localized_label(label: str) -> str:
    """Return a localized version of a label."""
    ...

def is_authorized() -> bool:
    """Returns True if access to the address book is currently allowed."""
    ...
