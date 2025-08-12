"""This is a stub file for the `linguistictagger` module, providing type hints for
its functions and their parameters, to be used for static analysis and
autocompletion.
"""

from typing import Literal, TypeAlias

# -----------------------------------------------------------------------------
# Constants
# -----------------------------------------------------------------------------
SCHEME_TOKEN_TYPE: str = ...
SCHEME_LEXICAL_CLASS: str = ...
SCHEME_NAME_TYPE: str = ...
SCHEME_NAME_TYPE_OR_LEXICAL_CLASS: str = ...
SCHEME_LEMMA: str = ...
SCHEME_LANGUAGE: str = ...
SCHEME_SCRIPT: str = ...

# -----------------------------------------------------------------------------
# Functions
# -----------------------------------------------------------------------------
_Scheme: TypeAlias = Literal[
    "Token Type",
    "Lexical Class",
    "Name Type",
    "Name Type or Lexical Class",
    "Lemma",
    "Language",
    "Script",
]

def tag_string(
    string: str,
    scheme: _Scheme,
) -> list[tuple[str, str, tuple[int, int]]]:
    """Tag a given string according to the scheme.

    Args:
        string (str): The text to be tagged.
        scheme (str): The tagging scheme to use.

    Returns:
        List[Tuple[str, str, Tuple[int, int]]]: A list of (tag, substring, range)
            tuples.

    """
    ...
