"""This is a stub file for the `appex` module, providing type hints for its
functions and their parameters, to be used for static analysis and autocompletion.
"""

from typing import Any, Literal, overload

from PIL.Image import Image as PILImage

# These are imported from the `ui` module, which is part of Pythonista.
from .ui import Image as UIImage
from .ui import View

# -----------------------------------------------------------------------------
# General Functions
# -----------------------------------------------------------------------------
def is_running_extension() -> bool:
    """Return True if the script is running within an app extension (share
    extension or widget), False otherwise.
    """
    ...

def is_widget() -> bool:
    """Return True if the script is running within the Today widget, False
    otherwise.
    """
    ...

def finish(js: str | None = None) -> None:
    """Close the share sheet extension.

    Args:
        js (str, optional): A piece of JavaScript code to be evaluated in the
            context of the current web page (only relevant in Safari).

    """
    ...

# -----------------------------------------------------------------------------
# Share Extension Functions
# -----------------------------------------------------------------------------
def get_attachments(uti: str = "public.data") -> list[Any]:
    """Return a list of attachments that match the given type identifier.

    Args:
        uti (str, optional): The type identifier to match. Defaults to 'public.data'.

    Returns:
        list[Any]: A list of attachments.

    """
    ...

@overload
def get_images() -> list[PILImage]: ...
@overload
def get_images(image_type: Literal["pil"]) -> list[PILImage]: ...
@overload
def get_images(image_type: Literal["ui"]) -> list[UIImage]: ...
@overload
def get_image() -> PILImage | None: ...
@overload
def get_image(image_type: Literal["pil"]) -> PILImage | None: ...
@overload
def get_image(image_type: Literal["ui"]) -> UIImage | None: ...
def get_image_data() -> bytes | None:
    """Return raw image data for the first image in the share sheet's input.

    Returns:
        bytes | None: The raw image data as a byte string, or None.

    """
    ...

def get_images_data() -> list[bytes]:
    """Return raw image data for all images in the share sheet's input.

    Returns:
        list[bytes]: A list of byte strings, or an empty list.

    """
    ...

def get_text() -> str | None:
    """Return text input of the share sheet.

    Returns:
        str | None: The text as a unicode string, or None.

    """
    ...

def get_urls() -> list[str]:
    """Return a list of URLs in the share sheet's input.

    Returns:
        list[str]: A list of URLs, or an empty list.

    """
    ...

def get_url() -> str | None:
    """Return the first URL in the share sheet's input.

    Returns:
        str | None: The first URL, or None.

    """
    ...

def get_file_paths() -> list[str]:
    """Return a list of file paths in the share sheet's input.

    Returns:
        list[str]: A list of file paths, or an empty list.

    """
    ...

def get_file_path() -> str | None:
    """Return the first file path in the share sheet's input.

    Returns:
        str | None: The first file path, or None.

    """
    ...

def get_vcards() -> list[str]:
    """Return a list of VCard records in the share sheet's input.

    Returns:
        list[str]: A list of VCard records as strings, or an empty list.

    """
    ...

def get_vcard() -> str | None:
    """Return the first VCard record in the share sheet's input.

    Returns:
        str | None: The first VCard record as a string, or None.

    """
    ...

def get_web_page_info() -> dict[str, str]:
    """When the share sheet is shown in Safari, return information about the
    currently loaded page.

    Returns:
        dict[str, str]: A dictionary with page information, or an empty dict.

    """
    ...

# -----------------------------------------------------------------------------
# Today Widget Functions
# -----------------------------------------------------------------------------
def get_widget_view() -> View | None:
    """Return the view that is currently shown in the Today widget.

    Returns:
        ui.View | None: The current view, or None.

    """
    ...

def set_widget_view(view: View | None) -> None:
    """Set the widget's view to a ui.View object.

    Args:
        view (ui.View | None): The view to set, or None to remove the current view.

    """
    ...
