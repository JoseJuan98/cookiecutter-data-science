
# -*- coding: utf-8 -*-
"""Logger utils.

This module contains the logger utilities to be used in the project.
"""

import logging


class Color:
    """A class for terminal color codes."""

    BOLD = "\033[1m"
    BLUE = "\033[94m"
    WHITE = "\033[97m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    RED = "\033[91m"
    GREY = "\033[90m"
    BLACK = "\033[30m"
    BOLD_WHITE = BOLD + WHITE
    BOLD_BLUE = BOLD + BLUE
    BOLD_GREEN = BOLD + GREEN
    BOLD_YELLOW = BOLD + YELLOW
    BOLD_RED = BOLD + RED
    BOLD_BLACK = BOLD + BLACK
    BOLD_GREY = BOLD + GREY
    END = "\033[0m"


class ColorLogFormatter(logging.Formatter):
    """A class for formatting colored logs."""

    FORMAT = "%(prefix)s%(msg)s%(suffix)s"

    LOG_LEVEL_COLOR = {
        "DEBUG": {"prefix": "", "suffix": ""},
        "INFO": {"prefix": Color.BLACK, "suffix": Color.END},
        "WARNING": {"prefix": Color.BOLD_YELLOW, "suffix": Color.END},
        "ERROR": {"prefix": Color.BOLD_RED, "suffix": Color.END},
        "CRITICAL": {"prefix": Color.BOLD_RED, "suffix": Color.END},
    }

    def format(self, record):
        """Format log records with a default prefix and suffix to terminal color codes that corresponds to the log
        level name.
        """
        if not hasattr(record, "prefix"):
            record.prefix = self.LOG_LEVEL_COLOR.get(record.levelname.upper()).get(
                "prefix"
            )

        if not hasattr(record, "suffix"):
            record.suffix = self.LOG_LEVEL_COLOR.get(record.levelname.upper()).get(
                "suffix"
            )

        formatter = logging.Formatter(self.FORMAT)
        return formatter.format(record)


def get_logger(
    name: str = "main", level: int = logging.INFO, log: str = "main"
) -> logging.Logger:
    """Get the main logger.

    Args:
        name (str, optional): The logger name. Defaults to "main".
        level (int, optional): The logger level. Defaults to logging.INFO.
        log (str, optional): The log file name. Defaults to "main".
    """
    logger = logging.getLogger(name)
    logger.setLevel(level=level)

    logger.propagate = False

    if not logger.handlers:
        # FIXME
        log_dir = pathlib.Path(__file__).parent.parent.parent.parent / "artifacts" / "logs"

        # create the logs dir if it doesn't exist
        os.makedirs(log_dir, exist_ok=True)

        stream_handler = logging.StreamHandler()
        stream_handler.setFormatter(ColorLogFormatter())
        logger.addHandler(stream_handler)
        logger.addHandler(
            logging.FileHandler(filename=log_dir / f"{log}.log", mode="w"),
        )

    return logger


def log_tittle(msg: str, logger: logging.Logger = None) -> None:
    """Print the title message for an experiment.

    Args:
        msg (str): The message to print.
        logger (logging.Logger, optional): The logger to use. Defaults to None, so it creates a new one.
    """
    if logger is None:
        logger = get_logger()

    logger.info(f"\n\n{f' {msg} ':_^100}\n\n")
