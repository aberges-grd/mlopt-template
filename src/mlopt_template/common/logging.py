"""Logging module"""

import logging
from functools import wraps
from rich.logging import RichHandler


logging.basicConfig(
    level="NOTSET", format="%(message)s", datefmt="[%X]", handlers=[RichHandler()]
)


def infolog(msg_before: str = "", msg_after: str = ""):
    """Decorator for arbitrary info before and after function call."""

    def decorator_infolog(func):
        """Actual decorator function"""

        @wraps(func)
        def inner(*args, **kwargs):
            if msg_before:
                logging.info(msg_before)
            result = func(*args, **kwargs)
            if msg_after:
                logging.info(msg_after)
            return result

        return inner

    return decorator_infolog
