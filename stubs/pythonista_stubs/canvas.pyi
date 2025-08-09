"""
This is a stub file for the `canvas` module, providing type hints for its
functions and their parameters, to be used for static analysis and autocompletion.
"""

from typing import Optional, Tuple

# -----------------------------------------------------------------------------
# Blend Modes (Constants)
# -----------------------------------------------------------------------------
BLEND_NORMAL: int = ...
BLEND_MULTIPLY: int = ...
BLEND_SCREEN: int = ...
BLEND_OVERLAY: int = ...
BLEND_DARKEN: int = ...
BLEND_LIGHTEN: int = ...
BLEND_COLOR_DODGE: int = ...
BLEND_COLOR_BURN: int = ...
BLEND_SOFT_LIGHT: int = ...
BLEND_HARD_LIGHT: int = ...
BLEND_DIFFERENCE: int = ...
BLEND_EXCLUSION: int = ...
BLEND_HUE: int = ...
BLEND_SATURATION: int = ...
BLEND_COLOR: int = ...
BLEND_LUMINOSITY: int = ...
BLEND_CLEAR: int = ...
BLEND_COPY: int = ...
BLEND_SOURCE_IN: int = ...
BLEND_SOURCE_OUT: int = ...
BLEND_SOURCE_ATOP: int = ...
BLEND_DESTINATION_OVER: int = ...
BLEND_DESTINATION_ATOP: int = ...
BLEND_XOR: int = ...
BLEND_PLUS_DARKER: int = ...
BLEND_PLUS_LIGHTER: int = ...

# -----------------------------------------------------------------------------
# Functions
# -----------------------------------------------------------------------------
# Configuration
def clear() -> None:
    """Clears the canvas."""
    ...

def get_size() -> Tuple[float, float]:
    """Return the size of the canvas as a tuple of width and height."""
    ...

def set_size(width: float, height: float) -> None:
    """Set the size of the canvas and reset all graphics state."""
    ...

def begin_updates() -> None:
    """Begins a group of drawing operations to improve performance."""
    ...

def end_updates() -> None:
    """Forces all buffered drawing to be displayed on the screen."""
    ...

def save_png(filename: str) -> None:
    """Save the current content of the canvas to a PNG file."""
    ...

# Setting Drawing Parameters
def set_aa_enabled(flag: bool) -> None:
    """Enables or disables antialiasing."""
    ...

def set_alpha(alpha: float) -> None:
    """Sets the global alpha value."""
    ...

def set_blend_mode(mode: int) -> None:
    """Sets the active blend mode."""
    ...

def set_fill_color(r: float, g: float, b: float, a: float = 1.0) -> None:
    """Sets the fill color (RGB or RGBA)."""
    ...

def set_line_width(width: float) -> None:
    """Sets the line width."""
    ...

def set_stroke_color(r: float, g: float, b: float, a: float = 1.0) -> None:
    """Sets the active stroke color (RGB or RGBA)."""
    ...

# Vector Drawing Functions
def add_curve(
    cp1x: float, cp1y: float, cp2x: float, cp2y: float, x: float, y: float
) -> None:
    """Adds a cubic bezier curve to the current path."""
    ...

def add_ellipse(x: float, y: float, width: float, height: float) -> None:
    """Adds an ellipse to the current path."""
    ...

def add_line(x: float, y: float) -> None:
    """Adds a straight line to the current path."""
    ...

def add_quad_curve(cpx: float, cpy: float, x: float, y: float) -> None:
    """Adds a quadratic bezier curve to the current path."""
    ...

def add_rect(x: float, y: float, width: float, height: float) -> None:
    """Adds a rectangle to the current path."""
    ...

def begin_path() -> None:
    """Begins a new path."""
    ...

def clip() -> None:
    """Clips subsequent drawing to the current path."""
    ...

def close_path() -> None:
    """Closes the current path."""
    ...

def draw_ellipse(x: float, y: float, width: float, height: float) -> None:
    """Draws an ellipse in a rectangle."""
    ...

def draw_line(x1: float, y1: float, x2: float, y2: float) -> None:
    """Draws a line between two points."""
    ...

def draw_path() -> None:
    """Draws the outline of the current path."""
    ...

def draw_rect(x: float, y: float, width: float, height: float) -> None:
    """Draws the outline of a rectangle."""
    ...

def fill_ellipse(x: float, y: float, width: float, height: float) -> None:
    """Fills an ellipse in a rectangle."""
    ...

def fill_path() -> None:
    """Fills the current path."""
    ...

def fill_pixel(x: float, y: float) -> None:
    """Fills a pixel with the current fill color."""
    ...

def fill_rect(x: float, y: float, width: float, height: float) -> None:
    """Fills a rectangle."""
    ...

def move_to(x: float, y: float) -> None:
    """Moves the 'pen' to a given point."""
    ...

# Transforms
def restore_gstate() -> None:
    """Restores the graphics state from the stack."""
    ...

def rotate(angle: float) -> None:
    """Rotates the current transformation matrix."""
    ...

def save_gstate() -> None:
    """Pushes a copy of the current graphics state onto the stack."""
    ...

def scale(sx: float, sy: float) -> None:
    """Scales the current transformation matrix."""
    ...

def translate(tx: float, ty: float) -> None:
    """Translates the current transformation matrix."""
    ...

# Drawing Bitmap Images
def draw_image(
    image_name: str,
    x: float,
    y: float,
    width: Optional[float] = None,
    height: Optional[float] = None,
) -> None:
    """Draws the image with the given name in a rectangle."""
    ...

def draw_clipboard(x: float, y: float, width: float, height: float) -> None:
    """Draw the image in the clipboard in a given rectangle."""
    ...

def get_clipboard_size() -> Tuple[float, float]:
    """Return the size of the image in the clipboard in points."""
    ...

def get_image_size(image_name: str) -> Tuple[float, float]:
    """Returns the size of the image with the given name in points."""
    ...

# Drawing Text
def draw_text(
    text: str,
    x: float,
    y: float,
    font_name: str = "Helvetica",
    font_size: float = 16.0,
) -> None:
    """Draw a single line of text at a given point."""
    ...

def get_text_size(
    text: str, font_name: str = "Helvetica", font_size: float = 16.0
) -> Tuple[float, float]:
    """Get the size of a line of text as a tuple of (width, height)."""
    ...
