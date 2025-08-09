"""
This is a stub file for the `speech` module, providing type hints for its
functions and their parameters, to be used for static analysis and autocompletion.
"""

from typing import Dict, List, Optional, Tuple

# -----------------------------------------------------------------------------
# Functions
# -----------------------------------------------------------------------------
def get_synthesis_languages() -> List[str]:
    """Return a list of all language/locale identifiers available for
    speech synthesis.
    """
    ...

def get_recognition_languages() -> List[str]:
    """Return a list of all language/locale identifiers available for
    speech recognition.
    """
    ...

def say(text: str, language: Optional[str] = None, rate: float = 0.5) -> None:
    """Speak the given text.
    Args:
        text (str): The text to be spoken.
        language (str, optional): The language as a BCP-47 code (e.g. 'en-US').
        rate (float, optional): The speech rate (0.0 slowest, 1.0 fastest).
    """
    ...

def stop() -> None:
    """Stop any speech synthesis currently in progress."""
    ...

def is_speaking() -> bool:
    """Return True if the synthesizer is currently speaking, False otherwise."""
    ...

def recognize(
    file_path: str, language: Optional[str] = None
) -> List[Tuple[str, List[Dict]]]:
    """Transcribe spoken text in the given audio file.
    Args:
        file_path (str): The path to the audio file.
        language (str, optional): The locale identifier (e.g. 'en-US').
    Returns:
        List[Tuple[str, List[Dict]]]: A list of possible transcriptions.
    Raises:
        RuntimeError: If speech recognition fails.
        ValueError: If the language parameter is invalid.
        IOError: If the audio file cannot be read.
    """
    ...
