from PIL import Image
from typing_extensions import Literal

def get() -> str: ...
def set(string: str) -> None: ...
def get_image(idx: int = 0) -> Image: ...
def set_image(
    image: Image, format: Literal["jpeg", "png"] = "png", jpeg_quality: float = 0.75
) -> None: ...
