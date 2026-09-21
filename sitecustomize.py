"""
Lazy imports let this module be part of sitecustomize.
"""

import _thread
import atexit
import sys

TYPE_CHECKING = False

if TYPE_CHECKING:
    import threading
    from types import TracebackType


def excepthook(
    type_: type[BaseException],
    value: BaseException,
    traceback: "TracebackType | None",
) -> None:
    # importing libraries clears interpreter's interrupt exit status
    if not issubclass(type_, KeyboardInterrupt):
        import powertrace  # noqa: PLC0415

        powertrace.excepthook(type_, value, traceback)


def threading_excepthook(args: "threading.ExceptHookArgs") -> None:
    import powertrace  # noqa: PLC0415

    powertrace.threading_excepthook(args)


def exit_if_failed() -> None:
    if "powertrace" in sys.modules:
        import powertrace  # noqa: PLC0415

        powertrace.exit_if_failed()


sys.excepthook = excepthook
atexit.register(exit_if_failed)

if "threading" in sys.modules:
    import threading

    threading.excepthook = threading_excepthook
else:
    # threading copies _thread._excepthook into its excepthook at import time
    _thread._excepthook = threading_excepthook  # noqa: SLF001
