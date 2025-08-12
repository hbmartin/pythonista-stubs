"""Utilities for bridging Objective-C APIs.

This module provides a "bridge" for using Objective-C APIs from Python.
Based on ctypes and the Objective-C runtime library, objc_util allows
you to "wrap" existing Objective-C classes in a way that automatically
converts Python method calls to corresponding Objective-C messages.
"""

import ctypes
from collections.abc import Callable
from contextlib import AbstractContextManager
from typing import (
    Any,
    TypeVar,
    overload,
)

# A type variable for the decorator to preserve function signatures.
F = TypeVar("F", bound=Callable)

class ObjCClass:
    """Wrapper for an Objective-C class.

    Acts as a proxy for calling Objective-C class methods. Method calls are
    converted to Objective-C messages on-the-fly. This is done by replacing
    underscores in the method name with colons in the selector name, and
    using the selector and arguments for a call to the low-level objc_msgSend()
    function.

    Example:
        Calling `NSDictionary.dictionaryWithObject_forKey_(obj, key)` in Python is
        translated to `[NSDictionary dictionaryWithObject:obj forKey:key]`
        in Objective-C.

    Args:
        name: The name of the Objective-C class as a string.

    """

    def __init__(self, name: str) -> None: ...

class ObjCInstance:
    """Wrapper for a pointer to an Objective-C object.

    Acts as a proxy for sending messages to the object. Method calls are converted
    to Objective-C messages on-the-fly.

    Example:
        Calling `obj.setFoo_withBar_(foo, bar)` in Python is translated to
        `[obj setFoo:foo withBar:bar]` in Objective-C.

    Args:
        ptr: A pointer to the Objective-C object.

    """

    def __init__(self, ptr: int | ctypes.c_void_p | None) -> None: ...

    # Collection-like behavior for NSArray, NSDictionary, NSSet
    def __len__(self) -> int: ...
    def __getitem__(self, key: Any) -> ObjCInstance: ...
    def __setitem__(self, key: Any, value: Any) -> None: ...
    def __iter__(self) -> Any: ...
    def __contains__(self, item: Any) -> bool: ...

class ObjCBlock:
    """Wrapper for Objective-C blocks (closures).

    Note:
        Block support is experimental.

    Args:
        func: The Python function to wrap as a block.
        restype: The return type of the block (e.g., `NSInteger`).
        argtypes: A list of argument types for the block.

    """

    def __init__(
        self,
        func: Callable,
        restype: type[ctypes._SimpleCData] | None = None,
        argtypes: list[type[ctypes._SimpleCData]] | None = None,
    ) -> None: ...

def autoreleasepool() -> AbstractContextManager[None]:
    """A context manager for NSAutoreleasePool.

    This acts as a wrapper for `NSAutoreleasePool` (similar to
    `@autoreleasepool {...}` in Objective-C).

    Usage:
        with objc_util.autoreleasepool():
            # do stuff...

    Returns:
        A context manager for an autorelease pool.

    """
    ...

def create_objc_class(
    name: str,
    superclass: ObjCClass = ...,
    methods: list[Callable] | None = None,
    classmethods: list[Callable] | None = None,
    protocols: list[str] | None = None,
    debug: bool = True,
) -> ObjCClass:
    """Create and return a new ObjCClass.

    The selector name is derived from the name of the function. The return and
    argument types are inferred automatically from the superclass or protocols
    if possible.

    Args:
        name: The name of the class to create.
        superclass: The ObjCClass object from which the new class inherits.
        methods: A list of functions for instance methods.
        classmethods: A list of functions for class methods.
        protocols: A list of protocol names (strings) for type hinting.
        debug: If `True`, a new name will be chosen automatically if a class
            with `name` already exists.

    Returns:
        A new ObjCClass object.

    """
    ...

def load_framework(name: str) -> None:
    """Load the system framework with the given name.

    Args:
        name: The name of the framework (e.g., 'SceneKit').

    """
    ...

@overload
def ns(obj: str) -> ObjCInstance: ...
@overload
def ns(obj: float) -> ObjCInstance: ...
@overload
def ns(obj: list) -> ObjCInstance: ...
@overload
def ns(obj: dict) -> ObjCInstance: ...
@overload
def ns(obj: set) -> ObjCInstance: ...
@overload
def ns(obj: bytes | bytearray) -> ObjCInstance: ...
@overload
def ns(obj: Any) -> ObjCInstance:
    """Convert a Python object to its Objective-C equivalent.

    Converts `str` to `NSString`, `list` to `NSMutableArray`, `dict` to
    `NSMutableDictionary`, etc. Nested structures are supported.

    Args:
        obj: The Python object to convert.

    Returns:
        The Objective-C equivalent of the input object, wrapped in an
        ObjCInstance if applicable.

    """
    ...

def nsurl(url_or_path: str) -> ObjCInstance:
    """Convert a Python string to an NSURL object.

    Args:
        url_or_path: A string representing a URL or a file path.

    Returns:
        An `NSURL` object wrapped in an `ObjCInstance`.

    """
    ...

def nsdata_to_bytes(data: ObjCInstance) -> bytes:
    """Convert an NSData object to a Python byte string.

    Args:
        data: An `NSData` object wrapped in an `ObjCInstance`.

    Returns:
        A Python byte string.

    """
    ...

def uiimage_to_png(img: ObjCInstance) -> bytes:
    """Convert a UIImage object to a Python byte string with PNG data.

    Args:
        img: A `UIImage` object wrapped in an `ObjCInstance`.

    Returns:
        A Python byte string containing PNG data.

    """
    ...

def on_main_thread(func: F) -> F:
    """Decorator to call a function on the UIKit main thread.

    This is typically used to decorate another function, but can also be used
    ad-hoc for dispatching a function call to the main thread.

    Args:
        func: The function to be executed on the main thread.

    Returns:
        The decorated function.

    """
    ...

def sel(name: str) -> ctypes.c_void_p:
    """Convert a Python string to an Objective-C selector.

    Args:
        name: The name of the selector as a string.

    Returns:
        An Objective-C selector object.

    """
    ...

# Convenience class wrappers for common Objective-C types
# These are included as module-level objects for convenience.
class CGPoint(ctypes.Structure):
    """Core Graphics point structure."""

    _fields_ = [("x", ctypes.c_double), ("y", ctypes.c_double)]
    x: float
    y: float
    def __init__(self, x: float = 0.0, y: float = 0.0) -> None: ...

class CGSize(ctypes.Structure):
    """Core Graphics size structure."""

    _fields_ = [("width", ctypes.c_double), ("height", ctypes.c_double)]
    width: float
    height: float
    def __init__(self, width: float = 0.0, height: float = 0.0) -> None: ...

class CGVector(ctypes.Structure):
    """Core Graphics vector structure."""

    _fields_ = [("dx", ctypes.c_double), ("dy", ctypes.c_double)]
    dx: float
    dy: float
    def __init__(self, dx: float = 0.0, dy: float = 0.0) -> None: ...

class CGRect(ctypes.Structure):
    """Core Graphics rectangle structure."""

    _fields_ = [("origin", CGPoint), ("size", CGSize)]
    origin: CGPoint
    size: CGSize
    def __init__(
        self,
        origin: CGPoint | None = None,
        size: CGSize | None = None,
    ) -> None: ...

class CGAffineTransform(ctypes.Structure):
    """Core Graphics affine transformation matrix."""

    _fields_ = [("a", ctypes.c_double), ("b", ctypes.c_double), ("c", ctypes.c_double), ("d", ctypes.c_double), ("tx", ctypes.c_double), ("ty", ctypes.c_double)]
    a: float
    b: float
    c: float
    d: float
    tx: float
    ty: float
    def __init__(
        self,
        a: float = 1.0,
        b: float = 0.0,
        c: float = 0.0,
        d: float = 1.0,
        tx: float = 0.0,
        ty: float = 0.0,
    ) -> None: ...

class UIEdgeInsets(ctypes.Structure):
    """UIKit edge insets structure."""

    _fields_ = [("top", ctypes.c_double), ("left", ctypes.c_double), ("bottom", ctypes.c_double), ("right", ctypes.c_double)]
    top: float
    left: float
    bottom: float
    right: float
    def __init__(
        self,
        top: float = 0.0,
        left: float = 0.0,
        bottom: float = 0.0,
        right: float = 0.0,
    ) -> None: ...

class NSRange(ctypes.Structure):
    """Foundation range structure."""

    _fields_ = [("location", ctypes.c_int), ("length", ctypes.c_int)]
    location: int
    length: int
    def __init__(self, location: int = 0, length: int = 0) -> None: ...

class NSDictionary(ObjCClass): ...
class NSMutableDictionary(ObjCClass): ...
class NSArray(ObjCClass): ...
class NSMutableArray(ObjCClass): ...
class NSSet(ObjCClass): ...
class NSMutableSet(ObjCClass): ...
class NSString(ObjCClass): ...
class NSMutableString(ObjCClass): ...
class NSData(ObjCClass): ...
class NSMutableData(ObjCClass): ...
class NSNumber(ObjCClass): ...
class NSURL(ObjCClass): ...
class NSEnumerator(ObjCClass): ...

# Convenience functions for creating structures
def CGPointMake(x: float, y: float) -> CGPoint:
    """Create a CGPoint structure."""
    ...

def CGSizeMake(width: float, height: float) -> CGSize:
    """Create a CGSize structure."""
    ...

def CGRectMake(x: float, y: float, width: float, height: float) -> CGRect:
    """Create a CGRect structure."""
    ...

def NSMakeRange(location: int, length: int) -> NSRange:
    """Create an NSRange structure."""
    ...
