from typing import Literal, TypeAlias

_RenderingMode: TypeAlias = Literal["automatic", "always_original", "always_template"]

AUTOCAPITALIZE_NONE: int = ...
AUTOCAPITALIZE_WORDS: int = ...
AUTOCAPITALIZE_SENTENCES: int = ...
AUTOCAPITALIZE_ALL: int = ...

class Image:
    """Represents an image that can be displayed in the user interface."""

    @classmethod
    def from_data(cls, image_data: bytes, scale: float | None = None) -> "Image":
        """Create an image from binary image data.

        Args:
            image_data: Binary image data (PNG, JPEG, etc.)
            scale: Scale factor for high-resolution displays (optional)

        Returns:
            New Image object

        """
        ...

    @classmethod
    def named(cls, image_name: str) -> "Image" | None:
        """Create an image from a built-in or local image file.

        Args:
            image_name: Name of built-in image (no extension) or path to local file

        Returns:
            Image object, or None if image not found

        """
        ...

    @property
    def scale(self) -> float:
        """The scale factor of the image (readonly)."""
        ...

    @property
    def size(self) -> tuple[float, float]:
        """The dimensions of the image as (width, height) tuple (readonly)."""
        ...

    def clip_to_mask(self, x: float, y: float, width: float, height: float) -> None:
        """Use this image as a mask for subsequent drawing operations.

        Args:
            x: X coordinate of the clipping rectangle
            y: Y coordinate of the clipping rectangle
            width: Width of the clipping rectangle
            height: Height of the clipping rectangle

        """
        ...

    def draw(
        self,
        x: float | None = None,
        y: float | None = None,
        width: float | None = None,
        height: float | None = None,
    ) -> None:
        """Draw the image in the current drawing context.

        Args:
            x: X coordinate (optional)
            y: Y coordinate (optional)
            width: Width to draw (optional, uses image width if None)
            height: Height to draw (optional, uses image height if None)

        """
        ...

    def draw_as_pattern(self, x: float, y: float, width: float, height: float) -> None:
        """Fill a rectangle with this image as a repeating pattern.

        Args:
            x: X coordinate of the rectangle
            y: Y coordinate of the rectangle
            width: Width of the rectangle
            height: Height of the rectangle

        """
        ...

    def resizable_image(
        self,
        top: float,
        left: float,
        bottom: float,
        right: float,
    ) -> Image:
        """Create a 9-patch resizable version of this image.

        Args:
            top: Top inset
            left: Left inset
            bottom: Bottom inset
            right: Right inset

        Returns:
            New resizable Image object

        """
        ...

    def show(self) -> None:
        """Display the image in the console output."""
        ...

    def to_png(self) -> bytes:
        """Convert the image to PNG format.

        Returns:
            PNG image data as bytes

        """
        ...

    def with_rendering_mode(self, mode: _RenderingMode) -> Image:
        """Create a new image with the specified rendering mode.

        Args:
            mode: The rendering mode to use

        Returns:
            New Image object with the specified rendering mode

        """
        ...

class View:
    def __init__(
        self,
        frame: tuple[int, int, int, int] = (0, 0, 100, 100),
        flex: str = "",
        background_color: (
            str | tuple[int, int, int] | tuple[int, int, int, int] | float | None
        ) = None,
        name: str | None = None,
    ) -> None: ...
