from __future__ import annotations

import logging

from rich.logging import RichHandler

FORMAT="%(message)s"
logging.basicConfig(
    format=FORMAT, datefmt="[%X] ", handlers=[RichHandler()], level=logging.INFO
)

from . import cli
from . import poker

__version__ = "0.1"