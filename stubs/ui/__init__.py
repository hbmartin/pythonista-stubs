from typing import Tuple, Union, Optional


class View:
    def __init__(
        self,
        frame: Tuple[int, int, int, int] = (0, 0, 100, 100),
        flex: str = "",
        background_color: Optional[
            Union[str, Tuple[int, int, int], Tuple[int, int, int, int], float]
        ] = None,
        name: Optional[str] = None,
    ) -> None: ...
