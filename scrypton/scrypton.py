import argparse
import os

from jinja2 import Environment, FileSystemLoader
from slugify import slugify

scrypton_folder = os.path.dirname(__file__)
template_folder = os.path.join(scrypton_folder, "templates")


def parse_args() -> argparse.Namespace:
    """
    Parse the arguments.

    Returns:
        argparse.Namespace: The parsed arguments.
    """
    parser = argparse.ArgumentParser(
        description="Generate a python script."
    )
    parser.add_argument(
        "path",
        type=str,
        help="The path of the script you wanna gen."
    )
    parser.add_argument(
        "--description",
        type=str,
        default="",
        help="A simple description of the script."
    )
    args = parser.parse_args()
    return args


def main() -> None:
    """
    """
    args = parse_args()
    path = args.path
    description = args.description
    environment = Environment(loader=FileSystemLoader(template_folder))
    template = environment.get_template("script.py")
    content = template.render(
        slug=slugify(os.path.basename(path)),
        description=description
    )
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)


if __name__ == "__main__":
    main()