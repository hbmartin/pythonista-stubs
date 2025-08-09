"""
This is a stub file for the `motion` module, providing type hints for its
functions and their parameters, to be used for static analysis and autocompletion.
"""

from typing import Tuple

# -----------------------------------------------------------------------------
# Functions
# -----------------------------------------------------------------------------
def start_updates() -> None:
    """Start monitoring the device's motion sensors."""
    ...

def stop_updates() -> None:
    """Stop monitoring the device's motion sensors."""
    ...

def get_gravity() -> Tuple[float, float, float]:
    """Return the gravity vector (x, y, z)."""
    ...

def get_user_acceleration() -> Tuple[float, float, float]:
    """Return the acceleration the user is giving to the device."""
    ...

def get_attitude() -> Tuple[float, float, float]:
    """Return the attitude of the device (roll, pitch, yaw)."""
    ...

def get_magnetic_field() -> Tuple[float, float, float, float]:
    """Return the magnetic field vector with respect to the device (x, y, z, accuracy)."""
    ...
