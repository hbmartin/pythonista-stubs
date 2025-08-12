"""This is a stub file for the `notification` module, providing type hints for its
functions and their parameters, to be used for static analysis and autocompletion.
"""

from typing import TypeAlias

# -----------------------------------------------------------------------------
# Functions
# -----------------------------------------------------------------------------
_Action: TypeAlias = dict[str, str | bool]
_Trigger: TypeAlias = dict[str, int | float | bool]

def schedule(
    message: str | None = None,
    delay: float = 0,
    sound_name: str | None = None,
    action_url: str | None = None,
    title: str | None = None,
    subtitle: str | None = None,
    attachments: list[str] | None = None,
    trigger: _Trigger | None = None,
    actions: list[_Action] | None = None,
    identifier: str | None = None,
) -> str:
    """Schedule a notification.

    Args:
        message (str, optional): The main text of the notification.
        delay (float, optional): The time in seconds until delivery. Defaults to 0.
        sound_name (str, optional): The sound to play. Use 'default' for the
            default sound or None for silent.
        action_url (str, optional): The URL to launch when the notification is tapped.
        title (str, optional): The title of the notification.
        subtitle (str, optional): The subtitle of the notification.
        attachments (list[str], optional): A list of file paths to attach.
        trigger (dict, optional): A dictionary for more complex triggers.
        actions (list[dict], optional): Definitions for custom action buttons.
        identifier (str, optional): An optional identifier for the notification.

    Returns:
        str: The identifier of the scheduled notification.

    """
    ...

def cancel(identifier: str) -> None:
    """Cancel a previously scheduled notification.

    Args:
        identifier (str): The identifier of the notification to cancel.

    """
    ...

def cancel_all() -> None:
    """Cancel all previously scheduled notifications."""
    ...

def get_scheduled() -> list[str]:
    """Return a list of scheduled notification identifiers."""
    ...

def remove_delivered(identifier: str) -> None:
    """Remove a specific delivered notification from Notification Center.

    Args:
        identifier (str): The identifier of the notification to remove.

    """
    ...

def remove_all_delivered() -> None:
    """Remove all delivered notifications from Notification Center."""
    ...
