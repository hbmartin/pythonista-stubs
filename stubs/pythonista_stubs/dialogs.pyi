"""This is a stub file for the `dialogs` module, providing type hints for its
functions and their parameters, to be used for static analysis and autocompletion.
"""

import datetime
from collections.abc import Sequence
from typing import Any, Literal, Protocol, TypeAlias, TypeVar

from PIL.Image import Image as PILImage

# These are imported from the `console` module for convenience.
# We'll alias the types for clarity.
from .console import _HudIcon
from .ui import Image as UIImage

class TextField:
    AUTOCAPITALIZE_SENTENCES: int = ...
    # ... other autocapitalization types

class ListDataSource:
    items: list[dict[str, Any]] = ...

def alert(
    title: str,
    message: str = "",
    button1: str = "OK",
    button2: str | None = None,
    button3: str | None = None,
    hide_cancel_button: bool = False,
) -> int:
    """See console.alert()"""
    ...

def input_alert(
    title: str,
    message: str = "",
    input: str = "",
    ok_button_title: str = "OK",
    hide_cancel_button: bool = False,
) -> str:
    """See console.input_alert()"""
    ...

def password_alert(
    title: str,
    message: str = "",
    password: str = "",
    ok_button_title: str = "OK",
    hide_cancel_button: bool = False,
) -> str:
    """See console.password_alert()"""
    ...

def login_alert(
    title: str,
    message: str = "",
    login: str = "",
    password: str = "",
    ok_button_title: str = "OK",
) -> tuple[str, str]:
    """See console.login_alert()"""
    ...

def hud_alert(message: str, icon: _HudIcon = "success", duration: float = 1.8) -> None:
    """See console.hud_alert()"""
    ...

# -----------------------------------------------------------------------------
# Dialog Functions
# -----------------------------------------------------------------------------
class StrConvertible(Protocol):
    def __str__(self) -> str: ...

T = TypeVar('T', bound=StrConvertible)

def list_dialog(
    title: str = "",
    items: list[T] | None = None,
    multiple: bool = False,
) -> list[T] | None:
    """Presents a list of items and returns the one(s) that were selected.

    When the dialog is cancelled, None is returned. The `items` list can
    contain any kind of object that can be converted to a string. To get more
    control over how each item is displayed in the list, you can also use a
    list of dictionaries (see ui.ListDataSource.items for details).

    Args:
        title (str, optional): The title of the dialog. Defaults to "".
        items (Union[Sequence[Any], List[Dict[str, Any]]], optional):
            The list of items to display. Defaults to None.
        multiple (bool, optional): If True, allows multiple selections.
            Defaults to False.

    Returns:
        Optional[Union[Any, List[Any]]]: The selected item(s), or None if the
            dialog was canceled.

    """
    ...

def edit_list_dialog(
    title: str = "",
    items: Sequence[Any] | None = None,
    move: bool = True,
    delete: bool = True,
) -> list[Any] | None:
    """Presents a list of items that can be edited by the user.

    By default, the user can both rearrange the list and remove items; this
    behavior can be controlled with the `move` and `delete` parameters.

    Args:
        title (str, optional): The title of the dialog. Defaults to "".
        items (Sequence[Any], optional): The list of items to display.
            Defaults to None.
        move (bool, optional): If True, allows items to be rearranged.
            Defaults to True.
        delete (bool, optional): If True, allows items to be deleted.
            Defaults to True.

    Returns:
        Optional[List[Any]]: The modified list of items, or None if the
            dialog was cancelled.

    """
    ...

# Field dictionaries are complex, so we'll type-hint them with a specific type alias.
_FieldType: TypeAlias = Literal[
    "switch",
    "text",
    "url",
    "email",
    "password",
    "number",
    "check",
    "datetime",
    "date",
    "time",
]
_FieldDict: TypeAlias = dict[str, Any]
_SectionTuple: TypeAlias = tuple[str, list[_FieldDict], str | None]

def form_dialog(
    title: str = "",
    fields: list[_FieldDict] | None = None,
    sections: list[_SectionTuple] | None = None,
) -> dict[str, Any] | None:
    """Presents a form dialog with customizable data input fields.

    Args:
        title (str, optional): The title of the dialog. Defaults to "".
        fields (List[Dict[str, Any]], optional): A list of field dictionaries for
            a single-section form. Use `sections` for multiple sections.
            Defaults to None.
        sections (List[Tuple[str, List[Dict[str, Any]], Optional[str]]], optional):
            A list of tuples, where each tuple represents a section.
            Defaults to None.

    Returns:
        Optional[Dict[str, Any]]: A dictionary of values for each field,
            or None if the dialog was cancelled.

    """
    ...

def text_dialog(
    title: str = "",
    text: str = "",
    font: tuple[str, int] | tuple[str] | str = ("<system>", 16),
    autocorrection: bool | None = None,
    autocapitalization: int = ...,
    spellchecking: bool | None = None,
) -> str | None:
    """Shows a multi-line text editor sheet.

    Args:
        title (str, optional): The title of the dialog. Defaults to "".
        text (str, optional): The initial text in the editor. Defaults to "".
        font (Union[Tuple[str, int], Tuple[str], str], optional):
            The font and size. Defaults to ('<system>', 16).
        autocorrection (Optional[bool], optional): Whether auto-correction
            should be enabled. Defaults to None.
        autocapitalization (int, optional): The auto-capitalization behavior.
            Defaults to ui.AUTOCAPITALIZE_SENTENCES.
        spellchecking (Optional[bool], optional): Whether spell checking
            should be enabled. Defaults to None.

    Returns:
        Optional[str]: The edited text, or None if the dialog was cancelled.

    """
    ...

def date_dialog(title: str = "") -> datetime.datetime | None:
    """Shows a date picker dialog.

    Args:
        title (str, optional): The title of the dialog. Defaults to "".

    Returns:
        Optional[datetime.datetime]: A datetime.datetime object with the selected
            date, or None if the dialog was cancelled.

    """
    ...

def time_dialog(title: str = "") -> datetime.datetime | None:
    """Shows a time picker dialog.

    Args:
        title (str, optional): The title of the dialog. Defaults to "".

    Returns:
        Optional[datetime.datetime]: A datetime.datetime object with the selected
            time, or None if the dialog was cancelled.

    """
    ...

def datetime_dialog(title: str = "") -> datetime.datetime | None:
    """Shows a date and time picker dialog.

    Args:
        title (str, optional): The title of the dialog. Defaults to "".

    Returns:
        Optional[datetime.datetime]: A datetime.datetime object with the selected
            date and time, or None if the dialog was cancelled.

    """
    ...

def duration_dialog(title: str = "") -> float | None:
    """Shows a duration picker dialog (e.g. for a countdown timer).

    Args:
        title (str, optional): The title of the dialog. Defaults to "".

    Returns:
        Optional[float]: The selected duration in seconds, or None if the
            dialog was cancelled.

    """
    ...

# -----------------------------------------------------------------------------
# Sharing Functions
# -----------------------------------------------------------------------------

def share_image(img: UIImage | PILImage) -> None:
    """Shows the system sharing dialog for a given image.

    Args:
        img (ui.Image | PIL.Image.Image): The image to share.

    """
    ...

def share_text(text: str) -> None:
    """Shows the system sharing dialog for a given string.

    Args:
        text (str): The text to share.

    """
    ...

def share_url(url: str) -> None:
    """Shows the system sharing dialog for a given URL.

    Args:
        url (str): The URL to share.

    """
    ...

# -----------------------------------------------------------------------------
# Importing Files
# -----------------------------------------------------------------------------

def pick_document(types: list[str] = ["public.data"]) -> str | None:
    """Shows the system's document picker for importing a file.

    Args:
        types (List[str], optional): Universal Type Identifiers (UTIs) for
            file types that should be selectable. Defaults to ['public.data'].

    Returns:
        Optional[str]: The path to the selected temporary file, or None if
            the dialog was cancelled.

    """
    ...
