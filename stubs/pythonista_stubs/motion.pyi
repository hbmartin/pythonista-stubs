"""This is a stub file for the `motion` module, providing type hints for its
functions and their parameters, to be used for static analysis and autocompletion.
"""

# -----------------------------------------------------------------------------
# Functions
# -----------------------------------------------------------------------------
def start_updates() -> None:
    """Start monitoring the device's motion sensors."""
    ...

def stop_updates() -> None:
    """Stop monitoring the device's motion sensors."""
    ...

def get_gravity() -> tuple[float, float, float]:
    """Return the gravity vector (x, y, z)."""
    ...

def get_user_acceleration() -> tuple[float, float, float]:
    """Return the acceleration the user is giving to the device."""
    ...

def get_attitude() -> tuple[float, float, float]:
    """Return the attitude of the device (roll, pitch, yaw)."""
    ...

def get_magnetic_field() -> tuple[float, float, float, float]:
    """Return the magnetic field vector with respect to the device:
    (x, y, z, accuracy).
    """
    ...
