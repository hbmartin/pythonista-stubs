from typing import Optional, Tuple
from typing_extensions import Literal

from stubs import ui


def get_path() -> Optional[str]:
    ...


def get_text() -> str:
    ...


def get_selection() -> Optional[Tuple[int, int]]:
    ...


def get_line_selection() -> Optional[Tuple[int, int]]:
    ...


def set_selection(start: int, end: Optional[int] = None, scroll: bool = False) -> None:
    ...


def replace_text(start: int, end: int, replacement: str) -> None:
    ...


def make_new_file(name: str, content: Optional[str], new_tab: Optional[bool]) -> None:
    ...


def open_file(name: str, new_tab: Optional[bool] = False) -> None:
    ...


def reload_files() -> None:
    ...  # undocumented


def apply_ui_theme(ui_view: ui.View, theme_name: Optional[str] = None) -> None:
    ...


def present_themed(
    ui_view: ui.View, theme_name: Optional[str] = None, **kwargs
) -> None:
    ...


def annotate_line(
    lineno: int,
    text: str = "",
    style: Literal["success", "warning", "error"] = "warning",
    expanded: bool = True,
    filename: Optional[str] = None,
    scroll: bool = False,
) -> None:
    ...


def clear_annotations(filename: Optional[str] = None) -> None:
    ...
