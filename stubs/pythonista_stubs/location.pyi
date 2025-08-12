"""This is a stub file for the `location` module, providing type hints for its
functions and their parameters, to be used for static analysis and autocompletion.
"""

from typing import Literal, TypeAlias

# These are imported from the `ui` module, which is part of Pythonista.
from .ui import Image

# -----------------------------------------------------------------------------
# Functions
# -----------------------------------------------------------------------------
_MapType: TypeAlias = Literal["standard", "satellite", "hybrid"]

def get_location() -> dict[str, float] | None:
    """Return the most recently obtained location data.

    Returns:
        dict[str, float] | None: A dictionary with 'longitude', 'latitude',
        and 'timestamp' keys, or None.

    """
    ...

def start_updates() -> None:
    """Start updating location data."""
    ...

def stop_updates() -> None:
    """Stop updating location data."""
    ...

def geocode(address: dict[str, str]) -> list[dict[str, float]]:
    """Convert an address dictionary to geo-coordinates.

    Args:
        address (Dict[str, str]): A dictionary with address components (e.g.,
        'Street', 'City', 'Country').

    Returns:
        List[Dict[str, float]]: A list of dictionaries with 'longitude' and
        'latitude' keys.

    """
    ...

def render_map_snapshot(
    lat: float,
    lng: float,
    width: float = 1000.0,
    height: float = 1000.0,
    map_type: _MapType = "standard",
    show_poi: bool = True,
    img_width: int = 240,
    img_height: int = 240,
    img_scale: int = 0,
) -> Image:
    """Render a snapshot image of the given map region.

    Args:
        lat (float): Latitude of the map's center.
        lng (float): Longitude of the map's center.
        width (float, optional): Width of the map region in meters.
        height (float, optional): Height of the map region in meters.
        map_type (str, optional): Map type ('standard', 'satellite', or 'hybrid').
        show_poi (bool, optional): Whether to show points of interest.
        img_width (int, optional): Width of the returned image in points.
        img_height (int, optional): Height of the returned image in points.
        img_scale (int, optional): Scale factor of the image (0 for device scale).

    Returns:
        ui.Image: The rendered map snapshot.

    """
    ...

def reverse_geocode(location: dict[str, float]) -> list[dict[str, str]]:
    """Convert geo-coordinates to a human-readable address.

    Args:
        location (Dict[str, float]): A dictionary with 'longitude' and
        'latitude' keys.

    Returns:
        List[Dict[str, str]]: A list of possible address dictionaries.

    """
    ...

def is_authorized() -> bool:
    """Returns True if access to location data is currently allowed."""
    ...
