"""
This is a stub file for the `notification` module, providing type hints for its
functions and their parameters, to be used for static analysis and autocompletion.
"""

from typing import Dict, List, Optional, Union

# -----------------------------------------------------------------------------
# Functions
# -----------------------------------------------------------------------------
_Action = Dict[str, Union[str, bool]]
_Trigger = Dict[str, Union[int, float, bool]]

def schedule(
    message: Optional[str] = None,
    delay: float = 0,
    sound_name: Optional[str] = None,
    action_url: Optional[str] = None,
    title: Optional[str] = None,
    subtitle: Optional[str] = None,
    attachments: Optional[List[str]] = None,
    trigger: Optional[_Trigger] = None,
    actions: Optional[List[_Action]] = None,
    identifier: Optional[str] = None,
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
        attachments (List[str], optional): A list of file paths to attach.
        trigger (dict, optional): A dictionary for more complex triggers.
        actions (List[dict], optional): Definitions for custom action buttons.
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

def get_scheduled() -> List[str]:
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
