"""This is a stub file for the `appex` module, providing type hints for its
functions and their parameters, to be used for static analysis and autocompletion.
"""

from typing import Any, Literal, TypeAlias

# These are imported from the `ui` module, which is part of Pythonista.
from .ui import View, Image

# Assuming 'PIL' is from the Pillow library.
try:
    from PIL.Image import Image as PilImage
except ImportError:
    PilImage: Any  # type: ignore[no-redef]

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
        List[Any]: A list of attachments.

    """
    ...

_ImageType: TypeAlias = Literal["ui", "pil"]

def get_images(image_type: _ImageType = "pil") -> list[Image | PilImage]:
    """Return a list of images in the input of the share sheet.

    Args:
        image_type (Literal['ui', 'pil'], optional): The desired image type.
            Defaults to 'pil'.

    Returns:
        List[Union[ui.Image, PIL.Image.Image]]: A list of images.

    """
    ...

def get_image(image_type: _ImageType = "pil") -> Image | PilImage | None:
    """Return the first image in the input of the share sheet.

    Args:
        image_type (Literal['ui', 'pil'], optional): The desired image type.
            Defaults to 'pil'.

    Returns:
        Optional[Union[ui.Image, PIL.Image.Image]]: The first image, or None.

    """
    ...

def get_image_data() -> bytes | None:
    """Return raw image data for the first image in the share sheet’s input.

    Returns:
        Optional[bytes]: The raw image data as a byte string, or None.

    """
    ...

def get_images_data() -> list[bytes]:
    """Return raw image data for all images in the share sheet’s input.

    Returns:
        List[bytes]: A list of byte strings, or an empty list.

    """
    ...

def get_text() -> str | None:
    """Return text input of the share sheet.

    Returns:
        Optional[str]: The text as a unicode string, or None.

    """
    ...

def get_urls() -> list[str]:
    """Return a list of URLs in the share sheet’s input.

    Returns:
        List[str]: A list of URLs, or an empty list.

    """
    ...

def get_url() -> str | None:
    """Return the first URL in the share sheet’s input.

    Returns:
        Optional[str]: The first URL, or None.

    """
    ...

def get_file_paths() -> list[str]:
    """Return a list of file paths in the share sheet’s input.

    Returns:
        List[str]: A list of file paths, or an empty list.

    """
    ...

def get_file_path() -> str | None:
    """Return the first file path in the share sheet’s input.

    Returns:
        Optional[str]: The first file path, or None.

    """
    ...

def get_vcards() -> list[str]:
    """Return a list of VCard records in the share sheet’s input.

    Returns:
        List[str]: A list of VCard records as strings, or an empty list.

    """
    ...

def get_vcard() -> str | None:
    """Return the first VCard record in the share sheet’s input.

    Returns:
        Optional[str]: The first VCard record as a string, or None.

    """
    ...

def get_web_page_info() -> dict[str, str]:
    """When the share sheet is shown in Safari, return information about the
    currently loaded page.

    Returns:
        Dict[str, str]: A dictionary with page information, or an empty dict.

    """
    ...

# -----------------------------------------------------------------------------
# Today Widget Functions
# -----------------------------------------------------------------------------
def get_widget_view() -> View | None:
    """Return the view that is currently shown in the Today widget.

    Returns:
        Optional[ui.View]: The current view, or None.

    """
    ...

def set_widget_view(view: View | None) -> None:
    """Set the widget’s view to a ui.View object.

    Args:
        view (Optional[ui.View]): The view to set, or None to remove the current view.

    """
    ...
