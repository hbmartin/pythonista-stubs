# Created on July, 07 2025 by o-murphy <https://github.com/o-murphy>
"""pythonista `_cb` module type annotations
according to [pythonista.cb docs](https://omz-software.com/pythonista/docs/ios/cb.html)
and references to pythonista built-in `_cb` module help
>>> import _cb
>>> help(_cb)
"""

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
)

CM_STATE_UNKNOWN: int = 0
CM_STATE_RESETTING: int = 1
CM_STATE_UNSUPPORTED: int = 2
CM_STATE_UNAUTHORIZED: int = 3
CM_STATE_POWERED_OFF: int = 4
CM_STATE_POWERED_ON: int = 5

CH_PROP_BROADCAST: int = 1
CH_PROP_READ: int = 2
CH_PROP_WRITE_WITHOUT_RESPONSE: int = 4
CH_PROP_WRITE: int = 8
CH_PROP_NOTIFY: int = 16
CH_PROP_INDICATE: int = 32
CH_PROP_AUTHENTICATED_SIGNED_WRITES: int = 64
CH_PROP_EXTENDED_PROPERTIES: int = 128
CH_PROP_NOTIFY_ENCRYPTION_REQUIRED: int = 256
CH_PROP_INDICATE_ENCRYPTION_REQUIRED: int = 512

class Characteristic:
    properties: int
    value: bytes | None
    uuid: str  # hex
    notifying: bool

class Service:
    characteristics: list[Characteristic]
    primary: bool
    uuid: str  # hex

class Peripheral:
    manufacturer_data: bytes
    name: str | None
    uuid: str  # hex
    state: int
    services: list[Service]

    def discover_services(self) -> None: ...
    def discover_characteristics(self, service: Service) -> None: ...
    def set_notify_value(
        self,
        characteristic: Characteristic,
        flag: bool = True,
    ) -> None: ...
    def write_characteristic_value(
        self,
        characteristic: Characteristic,
        data: bytes,
        with_response: bool,
    ) -> None: ...
    def read_characteristic_value(self, characteristic: Characteristic) -> None: ...

class CentralManager:
    state: int

    def __init__(self) -> None: ...
    def scan_for_peripherals(self) -> None: ...
    def stop_scan(self) -> None: ...
    def connect_peripheral(self, p: Peripheral) -> None: ...
    def cancel_peripheral_connection(self, p: Peripheral) -> None: ...
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
