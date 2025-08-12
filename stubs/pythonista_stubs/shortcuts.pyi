"""This is a stub file for the `shortcuts` module, providing type hints for its
functions and their parameters, to be used for static analysis and autocompletion.
"""

from typing import Literal, TypeAlias

# -----------------------------------------------------------------------------
# Functions
# -----------------------------------------------------------------------------
_Action: TypeAlias = Literal["run", "open", "exec"]

def open_url(url: str) -> None:
    """Open a given URL using the system's default app.

    Args:
        url (str): The URL to open.

    """
    ...

def pythonista_url(
    path: str = "",
    action: _Action = "run",
    args: str | None = None,
    argv: list[str] | None = None,
) -> str:
    """Generates a pythonista3://... URL from a file name/path.

    Args:
        path (str, optional): Path to the script. Defaults to ''.
        action (_Action, optional): The action to perform ('run', 'open', 'exec').
            Defaults to 'run'.
        args (str, optional): A string of arguments to pass to the script.
        argv (List[str], optional): A list of arguments to pass to the script.

    Returns:
        str: The generated Pythonista URL.

    """
    ...

def open_shortcuts_app(name: str | None = None, shortcut_input: str = "") -> None:
    """Open the Apple Shortcuts app and optionally run a named shortcut.

    Args:
        name (str, optional): The name of the shortcut to run.
        shortcut_input (str, optional): Text input to pass to the shortcut.

    """
    ...
