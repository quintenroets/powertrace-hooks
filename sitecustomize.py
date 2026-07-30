"""This file is executed before every script so performance is critical.

Most scrips will never call the hooks below, so we install them lazily
only when they are needed. Lazy imports & installs limit the total
overhead of this file to the microseconds scale.
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
