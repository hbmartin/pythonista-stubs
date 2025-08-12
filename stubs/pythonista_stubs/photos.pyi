"""This is a stub file for the `photos` module, providing type hints for its
functions and their parameters, to be used for static analysis and autocompletion.
"""

import datetime
import io
from typing import Literal, TypeAlias, overload

from PIL.Image import Image as PILImage

from .ui import Image as UIImage

# -----------------------------------------------------------------------------
# Asset Class
# -----------------------------------------------------------------------------
class Asset:
    """Represents a single media item in the photo library."""

    def get_image(self, original: bool = False) -> PILImage:
        """Fetch the asset's image data as a PIL.Image object."""
        ...

    def get_image_data(self, original: bool = False) -> io.BytesIO:
        """Fetch the asset's image data as an io.BytesIO object."""
        ...

    def get_ui_image(
        self,
        size: tuple[int, int] | None = None,
        crop: bool = False,
    ) -> UIImage:
        """Fetch the asset's image data as a ui.Image object.

        Args:
            size (Optional[tuple[int, int]]): The desired size of the returned image,
                specified as a tuple of (width, height). If None, the original
                image dimensions are used.
            crop (bool): If True, the image will be cropped to fit the specified
                size while maintaining its aspect ratio. If False, the image will
                be resized and may be distorted. Defaults to False.

        Returns:
            UIImage: The asset's image data as a ui.Image object.

        """
        ...

    def edit_content(self, jpeg_path: str) -> None:
        """Replace the asset's image content with the given JPEG file."""
        ...

    def delete(self) -> None:
        """Delete the asset from the photo library."""
        ...

    def revert(self) -> None:
        """Revert the asset to its original state."""
        ...
    local_id: str
    """A unique identifier of this asset (read-only)."""
    pixel_width: int
    """The width of the asset in pixels (read-only)."""
    pixel_height: int
    """The height of the asset in pixels (read-only)."""
    media_type: Literal["image", "video"]
    """The asset's media type (read-only)."""
    media_subtypes: list[str]
    """The asset's media subtypes (read-only)."""
    creation_date: datetime.datetime
    """The asset's creation date (read-write)."""
    modification_date: datetime.datetime
    """The asset's modification date (read-write)."""
    hidden: bool
    """Whether the asset is hidden (read-write)."""
    favorite: bool
    """Whether the asset is a favorite (read-write)."""
    duration: float
    """The duration of a video asset in seconds (read-only)."""
    location: dict | None
    """The geo-location where the media was taken (read-write)."""
    can_edit_content: bool
    """Whether the asset's content can be modified (read-only)."""
    can_edit_properties: bool
    """Whether the asset's metadata can be modified (read-only)."""
    can_delete: bool
    """Whether the asset can be deleted (read-only)."""

# -----------------------------------------------------------------------------
# AssetCollection Class
# -----------------------------------------------------------------------------
class AssetCollection:
    """Represents a collection in the photo library (album or smart album)."""

    def delete(self) -> None:
        """Delete the asset collection from the photo library."""
        ...

    def add_assets(self, assets: list[Asset]) -> None:
        """Add a list of Asset objects to the album."""
        ...

    def remove_assets(self, assets: list[Asset]) -> None:
        """Remove a list of Asset objects from the album."""
        ...
    assets: list[Asset]
    """The assets that the collection contains (read-only)."""
    local_id: str
    """A unique identifier of this asset collection (read-only)."""
    title: str
    """The title of the asset collection (read-write)."""
    type: Literal["album", "smart_album", "moment"]
    """The type of the asset collection (read-only)."""
    subtype: str
    """The subtype of the asset collection (read-only)."""
    start_date: datetime.datetime
    """The earliest creation date of an asset in the collection (read-only)."""
    end_date: datetime.datetime
    """The latest creation date of an asset in the collection (read-only)."""
    can_delete: bool
    """Whether the collection can be deleted (read-only)."""
    can_add_assets: bool
    """Whether the collection allows adding assets (read-only)."""
    can_remove_assets: bool
    """Whether the collection allows removing assets (read-only)."""
    can_rename: bool
    """Whether the collection's title can be changed (read-only)."""

# -----------------------------------------------------------------------------
# Functions
# -----------------------------------------------------------------------------
_MediaType: TypeAlias = Literal["image", "video"]
_CameraType: TypeAlias = Literal["rear", "front"]
_MapType: TypeAlias = Literal["standard", "satellite", "hybrid"]

def capture_image(camera: _CameraType = "rear") -> PILImage | None:
    """Show a standard camera interface and return the captured image."""
    ...

def get_assets(
    media_type: _MediaType = "image",
    include_hidden: bool = False,
) -> list[Asset]:
    """Fetch and return a list of all assets in the library."""
    ...

def get_asset_with_local_id(local_id: str) -> Asset:
    """Fetch and return the asset with the given local identifier."""
    ...

def get_albums() -> list[AssetCollection]:
    """Return a list of all regular albums in the photo library."""
    ...

def get_smart_albums() -> list[AssetCollection]:
    """Return a list of all smart albums in the photo library."""
    ...

def get_moments() -> list[AssetCollection]:
    """Return a list of all 'moments' in the photo library."""
    ...

def get_favorites_album() -> AssetCollection:
    """Return the smart album containing all favorite assets."""
    ...

def get_recently_added_album() -> AssetCollection:
    """Return the smart album containing recently added assets."""
    ...

def get_selfies_album() -> AssetCollection:
    """Return the smart album containing all assets taken with the front camera."""
    ...

def get_screenshots_album() -> AssetCollection:
    """Return the smart album containing all screenshots."""
    ...

def batch_delete(assets: list[Asset]) -> None:
    """Delete multiple assets from the photo library."""
    ...

def batch_revert(assets: list[Asset]) -> None:
    """Revert multiple assets to their original state."""
    ...

def create_album(title: str) -> AssetCollection:
    """Create and return a new album in the photo library."""
    ...

def create_image_asset(image_path: str) -> Asset:
    """Create and return a new image asset from a file."""
    ...

@overload
def pick_asset(
    assets: list[Asset] | AssetCollection | None = ...,
    title: str = ...,
    multi: Literal[True] = ...,
) -> list[Asset] | None: ...
@overload
def pick_asset(
    assets: list[Asset] | AssetCollection | None = ...,
    title: str = ...,
    multi: Literal[False] = ...,
) -> Asset | None: ...
def pick_asset(
    assets: list[Asset] | AssetCollection | None = None,
    title: str = "",
    multi: bool = False,
) -> Asset | None | list[Asset]:
    """Show a dialog with a grid of thumbnails for the given assets."""
    ...
