"""
This is a stub file for the `sound` module, providing type hints for its
functions and their parameters, to be used for static analysis and autocompletion.
"""

from typing import Callable, Optional, Tuple

# -----------------------------------------------------------------------------
# Functions
# -----------------------------------------------------------------------------
def play_effect(
    name: str,
    volume: float = 1.0,
    pitch: float = 1.0,
    pan: float = 0.0,
    looping: bool = False,
) -> Optional["Effect"]:
    """Play the sound effect with the given name.
    Args:
        name (str): The name of the sound effect or a file path.
        volume (float, optional): The volume of the effect (0.0-1.0).
        pitch (float, optional): The pitch of the effect. Defaults to 1.0.
        pan (float, optional): The stereo position (-1.0 to 1.0). Defaults to 0.0.
        looping (bool, optional): Whether the effect should loop. Defaults to False.
    Returns:
        Optional[Effect]: An Effect object, or None if too many effects are playing.
    """
    ...

def stop_all_effects() -> None:
    """Stop all sound effects that are currently playing."""
    ...

def stop_effect(effect: "Effect") -> None:
    """Stop playback of the given sound effect."""
    ...

def set_volume(vol: float) -> None:
    """Sets the default volume for all sound effects (0.0 to 1.0)."""
    ...

def set_honors_silent_switch(flag: bool) -> None:
    """Determines whether the silent switch is honored when playing sounds."""
    ...

# -----------------------------------------------------------------------------
# Effect Class
# -----------------------------------------------------------------------------
class Effect:
    """Represents a sound effect that is currently playing.
    Effect objects are returned from `play_effect()`.
    """
    def stop(self) -> None:
        """Stop playback of the sound effect."""
        ...

    @property
    def looping(self) -> bool: ...
    @looping.setter
    def looping(self, value: bool) -> None: ...
    @property
    def pan(self) -> float: ...
    @pan.setter
    def pan(self, value: float) -> None: ...
    @property
    def pitch(self) -> float: ...
    @pitch.setter
    def pitch(self, value: float) -> None: ...
    @property
    def position(self) -> Tuple[float, float, float]: ...
    @position.setter
    def position(self, value: Tuple[float, float, float]) -> None: ...
    @property
    def volume(self) -> float: ...
    @volume.setter
    def volume(self, value: float) -> None: ...

# -----------------------------------------------------------------------------
# Player Class
# -----------------------------------------------------------------------------
class Player:
    """Provides an interface for playing audio files from disk."""
    def __init__(self, file_path: str): ...
    def play(self) -> None:
        """Start playing audio."""
        ...

    def stop(self) -> None:
        """Stop playing audio and reset the playback position."""
        ...

    def pause(self) -> None:
        """Stop playing audio, but keep the current playback position."""
        ...

    current_time: float
    """The current playback position in seconds."""
    duration: float
    """The duration of the audio track (read-only)."""
    finished_handler: Optional[Callable[[], None]]
    """A function that is called when the player finishes playing."""
    number_of_loops: int
    """The number of times the audio track should be repeated."""
    playing: bool
    """A boolean indicating whether the audio player is playing."""
    pan: float
    """The stereo positioning of the played sound (-1.0 to 1.0)."""

# -----------------------------------------------------------------------------
# Recorder Class
# -----------------------------------------------------------------------------
class Recorder:
    """High-level methods for recording audio files from the microphone."""
    def __init__(self, file_path: str): ...
    def record(self, duration: Optional[float] = None) -> None:
        """Start recording audio from the microphone.
        Args:
            duration (float, optional): The number of seconds to record.
        """
        ...

    def stop(self) -> None:
        """Stop recording audio."""
        ...

    def pause(self) -> None:
        """Pause recording audio."""
        ...

    current_time: float
    """The current duration of the active recording."""
    recording: bool
    """Whether the recorder is currently recording."""
    meters: dict
    """The current average and peak power (read-only).
    Example: {'average': (-35.3, -30.1), 'peak': (-5.2, -8.2)}
    """

# -----------------------------------------------------------------------------
# MIDIPlayer Class
# -----------------------------------------------------------------------------
class MIDIPlayer:
    """Simple playback functions for MIDI (.mid) files."""
    def __init__(self, file_path: str, sound_bank_path: Optional[str] = None): ...
    def play(self) -> None:
        """Start playback."""
        ...

    def stop(self) -> None:
        """Stop playback."""
        ...

    current_time: float
    """The current playback position."""
    duration: float
    """The duration of the loaded MIDI file."""
    rate: float
    """The playback rate."""
