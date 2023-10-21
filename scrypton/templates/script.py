"""
{{description}}
"""
import argparse
import logging
from logging.handlers import RotatingFileHandler

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
formatter = logging.Formatter(
    "%(asctime)s :: %(levelname)s :: %(message)s", datefmt="%Y-%m-%d %H:%M:%S"
)
file_handler = RotatingFileHandler(
    "{{slug}}.log", "a", 1000000, 1
)  # 1Mo max, 1 backup
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)
stream_handler = logging.StreamHandler()
stream_handler.setLevel(logging.DEBUG)
stream_handler.setFormatter(formatter)
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