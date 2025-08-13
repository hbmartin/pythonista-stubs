"""`pythonista.cb` module type annotations
according to [pythonista.cb docs](https://omz-software.com/pythonista/docs/ios/cb.html)
"""

from typing import Protocol

from _cb import (
    CH_PROP_AUTHENTICATED_SIGNED_WRITES,
    CH_PROP_BROADCAST,
    CH_PROP_EXTENDED_PROPERTIES,
    CH_PROP_INDICATE,
    CH_PROP_INDICATE_ENCRYPTION_REQUIRED,
    CH_PROP_NOTIFY,
    CH_PROP_NOTIFY_ENCRYPTION_REQUIRED,
    CH_PROP_READ,
    CH_PROP_WRITE,
    CH_PROP_WRITE_WITHOUT_RESPONSE,
    CM_STATE_POWERED_OFF,
    CM_STATE_POWERED_ON,
    CM_STATE_RESETTING,
    CM_STATE_UNAUTHORIZED,
    CM_STATE_UNKNOWN,
    CM_STATE_UNSUPPORTED,
    CentralManager,
    Characteristic,
    Peripheral,
    Service,
)

__all__ = (
    "CH_PROP_AUTHENTICATED_SIGNED_WRITES",
    "CH_PROP_BROADCAST",
    "CH_PROP_EXTENDED_PROPERTIES",
    "CH_PROP_INDICATE",
    "CH_PROP_INDICATE_ENCRYPTION_REQUIRED",
    "CH_PROP_NOTIFY",
    "CH_PROP_NOTIFY_ENCRYPTION_REQUIRED",
    "CH_PROP_READ",
    "CH_PROP_WRITE",
    "CH_PROP_WRITE_WITHOUT_RESPONSE",
    "CM_STATE_POWERED_OFF",
    "CM_STATE_POWERED_ON",
    "CM_STATE_RESETTING",
    "CM_STATE_UNAUTHORIZED",
    "CM_STATE_UNKNOWN",
    "CM_STATE_UNSUPPORTED",
    "CentralManager",
    "Characteristic",
    "Peripheral",
    "Service",
    "SharedCentralManager",
    "cancel_peripheral_connection",
    "connect_peripheral",
    "get_state",
    "reset",
    "scan_for_peripherals",
    "set_central_delegate",
    "set_verbose",
    "shared_manager",
    "stop_scan",
)

class _CentralManagerDelegate(Protocol):
    def did_discover_peripheral(self, p: Peripheral) -> None: ...
    def did_connect_peripheral(self, p: Peripheral) -> None: ...
    def did_fail_to_connect_peripheral(
        self,
        p: Peripheral,
        error: str | None,
    ) -> None: ...
    def did_disconnect_peripheral(
        self,
        p: Peripheral,
        error: str | None,
    ) -> None: ...
    def did_discover_services(self, p: Peripheral, error: str | None) -> None: ...
    def did_discover_characteristics(
        self,
        s: Service,
        error: str | None,
    ) -> None: ...
    def did_write_value(self, c: Characteristic, error: str | None) -> None: ...
    def did_update_value(self, c: Characteristic, error: str | None) -> None: ...
    def did_update_state(self) -> None: ...

# Documented at https://github.com/hbmartin/pythonista-stubs/pull/11#issuecomment-3180673698
class SharedCentralManager(CentralManager):
    delegate: _CentralManagerDelegate | None
    verbose: bool = False
    def verbose_log(self) -> None: ...

shared_manager: SharedCentralManager | None = None

def set_central_delegate(delegate: _CentralManagerDelegate) -> None: ...
def set_verbose(flag: bool) -> None: ...
def scan_for_peripherals() -> None: ...
def stop_scan() -> None: ...
def connect_peripheral(p: Peripheral) -> None: ...
def cancel_peripheral_connection(p: Peripheral) -> None: ...
def get_state() -> int: ...
def reset() -> None: ...
