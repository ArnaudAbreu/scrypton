"""
{{description}}
"""
import argparse
import logging
from logging.handlers import RotatingFileHandler


reset_color = "\x1b[0m"
dracula_cyan = "\x1b[38;5;159m"
dracula_green = "\x1b[38;5;120m"
dracula_orange = "\x1b[38;5;222m"
dracula_red = "\x1b[38;5;210m"
c_format_str = '%(name)s - [%(levelname)s] - %(message)s'

FORMATS = {
    logging.DEBUG: dracula_cyan + c_format_str + reset_color,
    logging.INFO: dracula_green + c_format_str + reset_color,
    logging.WARNING: dracula_orange + c_format_str + reset_color,
    logging.ERROR: dracula_red + c_format_str + reset_color,
    logging.CRITICAL: dracula_red + c_format_str + reset_color
}


class CustomFormatter(logging.Formatter):

    def format(self, record):
        log_fmt = FORMATS.get(record.levelno)
        formatter = logging.Formatter(log_fmt)
        return formatter.format(record)

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
file_formatter = logging.Formatter(
    "%(asctime)s :: %(levelname)s :: %(message)s", datefmt="%Y-%m-%d %H:%M:%S"
)
file_handler = RotatingFileHandler(
    "{{slug}}.log", "a", 1000000, 1
)  # 1Mo max, 1 backup
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
stream_handler = logging.StreamHandler()
stream_handler.setLevel(logging.DEBUG)
stream_handler.setFormatter(CustomFormatter())
logger.addHandler(stream_handler)


def parse_args() -> argparse.Namespace:
    """
    Parse the arguments.

    Returns:
        argparse.Namespace: The parsed arguments.
    """
    parser = argparse.ArgumentParser(
        description="{{description}}"
    )
    parser.add_argument(
        "--input",
        type=str,
        help="The input of this script."
    )
    parser.add_argument(
        "--output",
        type=str,
        help="The output of this script."
    )
    args = parser.parse_args()
    return args


def main() -> None:
    args = parse_args()
    pass


if __name__ == "__main__":
    main()