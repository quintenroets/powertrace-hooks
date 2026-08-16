"""
Executed before every script, so performance is critical.

The script resolves the hooks and extra builtins lazily to limit the total
overhead to microseconds.
"""

import sys
import threading
from types import TracebackType


def install_powertrace() -> None:
    import powertrace  # noqa: PLC0415

    powertrace.install_traceback_hooks()


def excepthook(
    type_: type[BaseException],
    value: BaseException,
    traceback: TracebackType | None,
) -> None:
    install_powertrace()
    sys.excepthook(type_, value, traceback)


def threading_excepthook(args: threading.ExceptHookArgs) -> None:
    install_powertrace()
    threading.excepthook(args)


sys.excepthook = excepthook
threading.excepthook = threading_excepthook
