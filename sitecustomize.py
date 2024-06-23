"""This file is executed before every script so performance is critical.

Most scrips will never call the hooks below, so we install them lazily
only when they are needed. Lazy imports & installs limit the total
overhead of this file to the microseconds scale.
"""

import sys
import threading
from typing import Any


def install_powertrace() -> None:
    import powertrace

    powertrace.install_traceback_hooks()


def excepthook(*args: Any) -> None:
    install_powertrace()
    sys.excepthook(*args)


def threading_excepthook(*args: Any) -> None:
    install_powertrace()
    threading.excepthook(*args)


sys.excepthook = excepthook
threading.excepthook = threading_excepthook
