"""This is a stub file for the `editor` module, providing type hints for its
functions and their parameters, to be used for static analysis and autocompletion.
"""

from typing import Literal, TypeAlias

# We'll use a minimal stub for the ui.View type from the ui module.
class View: ...

def get_path() -> str | None:
    """Returns the absolute path of the script that is currently open in the editor.

    Returns:
        str | None: The absolute file path, or None if no script is open.

    """
    ...

def get_text() -> str:
    """Returns the entire text of the script that is currently being edited.

    Returns:
        str: The full text content of the editor.

    """
    ...

def get_selection() -> tuple[int, int] | None:
    """Returns the selected range as a tuple of the form (start, end).

    The `start` and `end` values are character indices.

    Returns:
        tuple[int, int] | None: The start and end indices of the selection,
            or None if no file is currently open.

    """
    ...

def get_line_selection() -> tuple[int, int] | None:
    """Returns the range of all lines that are part of the current selection.

    Returns:
        tuple[int, int] | None: The start and end indices of the line selection,
            or None if no file is currently open.

    """
    ...

def set_selection(start: int, end: int | None = None, scroll: bool = False) -> None:
    """Sets the selected range in the editor.

    Args:
        start (int): The starting character index of the selection.
        end (int | None, optional): The ending character index of the selection.
            If None, the caret is positioned at `start` with no text selected.
        scroll (bool, optional): If True, scrolls the view to make the selection
            visible. Defaults to False.

    """
    ...

def replace_text(start: int, end: int, replacement: str) -> None:
    """Replaces the text in the given range with a new string.

    To insert/append text, a zero-length range can be used. All changes can be
    undone by the user (using the regular undo key).

    Args:
        start (int): The starting character index of the range to replace.
        end (int): The ending character index of the range to replace.
        replacement (str): The new text to insert.

    """
    ...

def make_new_file(name: str | None = None, content: str | None = None) -> None:
    """Creates a new file and opens it in the editor.

    If a file with the given name already exists, a numeric suffix is
    automatically appended.

    Args:
        name (str | None, optional): The desired name for the new file.
            Defaults to None.
        content (str | None, optional): The initial content of the new file.
            If omitted, an empty file is created. Defaults to None.

    """
    ...

def open_file(name: str, new_tab: bool = False) -> None:
    """Opens the file with the given name in the editor.

    Args:
        name (str): The path to the file. It can be relative to the script
            library's root directory or an absolute path. The .py extension
            can be omitted.
        new_tab (bool, optional): If True, the file is opened in a new tab.
            Defaults to False.

    """
    ...

def apply_ui_theme(ui_view: View, theme_name: str | None = None) -> None:
    """Styles a ui.View (and its descendants) with the given UI theme.

    Args:
        ui_view (ui.View): The view to be styled.
        theme_name (str | None, optional): The name of the theme. If None,
            the currently selected theme is used. Defaults to None.

    """
    ...

def present_themed(
    ui_view: View,
    theme_name: str | None = None,
    **kwargs,  # noqa: ANN003
) -> None:
    """Styles a ui.View and presents it.

    This function combines `apply_ui_theme()` and `ui.View.present()`.
    Keyword arguments are passed on to `ui.View.present()`.

    Args:
        ui_view (ui.View): The view to be styled and presented.
        theme_name (str | None, optional): The name of the theme. If None,
            the currently selected theme is used. Defaults to None.
        **kwargs: Keyword arguments are passed on to ui.View.present(),
            except for title_bar_color and title_color, which are set
            automatically based on the theme.



    """
    ...

_AnnotationStyle: TypeAlias = Literal["success", "warning", "error"]

def annotate_line(
    lineno: int,
    text: str = "",
    style: _AnnotationStyle = "warning",
    expanded: bool = True,
    filename: str | None = None,
    scroll: bool = False,
) -> None:
    """Annotates a line of code in the editor with a label.

    Args:
        lineno (int): The 1-based line number to annotate.
        text (str, optional): The text of the annotation. Defaults to ''.
        style (Literal['success', 'warning', 'error'], optional): The style of
            the annotation. Defaults to 'warning'.
        expanded (bool, optional): If False, only an icon is shown; tapping
            shows the text. Defaults to True.
        filename (str | None, optional): The path to the file to annotate.
            If None, the file currently open in the editor is used.
            Defaults to None.
        scroll (bool, optional): If True, scrolls to the annotated line.
            Defaults to False.

    """
    ...

def clear_annotations(filename: str | None = None) -> None:
    """Removes all annotations that were added via `annotate_line()`.

    Args:
        filename (str | None, optional): The path to the file from which to
            clear annotations. If None, the file currently open is used.
            Defaults to None.

    """
    ...
