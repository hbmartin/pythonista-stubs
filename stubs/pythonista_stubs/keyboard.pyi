"""This is a stub file for the `keyboard` module, providing type hints for its
functions and their parameters, to be used for static analysis and autocompletion.
"""

from typing import Literal, TypeAlias

from .ui import View

# -----------------------------------------------------------------------------
# Functions
# -----------------------------------------------------------------------------
_Appearance: TypeAlias = Literal["dark", "light"]
_Mode: TypeAlias = Literal["current", "minimized", "expanded"]

def backspace(times: int = 1) -> None:
    """Delete backwards in the current document.

    Args:
        times (int, optional): The number of characters to delete. Defaults to 1.

    """
    ...

def get_appearance() -> _Appearance:
    """Return the current appearance of the keyboard ('dark' or 'light')."""
    ...

def get_document_id() -> str:
    """Return a unique identifier (UUID) for the current document."""
    ...

def get_input_context() -> tuple[str, str]:
    """Return a 2-tuple with the text immediately before and after the cursor."""
    ...

def get_selected_text() -> str:
    """Return the currently selected text or an empty string."""
    ...

def get_text_replacements() -> list[tuple[str, str]] | None:
    """Return a list of text replacements.

    Returns:
        list[tuple[str, str]] | None: A list of (phrase, shortcut) tuples,
        or None if not running in the keyboard.

    """
    ...

def has_full_access() -> bool:
    """Return True if 'Full Access' is enabled for the keyboard."""
    ...

def has_text() -> bool:
    """Return True if the document being edited contains any text."""
    ...

def insert_text(text: str) -> None:
    """Insert text in the current document."""
    ...

def is_keyboard() -> bool:
    """Return True if the script is running in the custom Pythonista keyboard."""
    ...

def move_cursor(offset: int) -> None:
    """Move the cursor by a specified offset."""
    ...

def play_input_click() -> None:
    """Play an input click sound."""
    ...

def set_view(view: View | None = None, mode: _Mode = "current") -> None:
    """Sets a custom ui.View as the keyboard's UI.

    Args:
        view (ui.View, optional): The view to display. Pass None to close.
        mode (str, optional): The presentation mode, one of 'minimized',
            'expanded', or 'current'.

    """
    ...
