<div align="center">

<img
  src="docs/assets/logo.png"
  alt="Alt text"
  title="Optional title"
  style="display: inline-block; margin: 0 auto; width: 150px">

# Scrypton

**python scripts generation**

---

</div>

## About scrypton

Scrypton is a command line tool that generates python scripts. It creates a python script with a docstring, a logger, a main function and a `__name__ == "__main__"` block.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)

## Installation

1. clone this repo
2. cd into the repo
3. run `pip install -e .`

## Usage

Run `scrypton --help` to see the available commands.

To create a script called `hello.py` run `scrypton hello.py --description "This script is just an empty script example."`. This will create a file called `hello.py` in the current directory. The file contains the skeleton of a python script with:

- a docstring
- a logger
- a main function
- a `__name__ == "__main__"` block
