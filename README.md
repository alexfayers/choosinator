# choosinator

An epic projected called choosinator, by alexfayers!

## Installation

To install the project you only need to clone the repo and run pip install:

```bash
git clone https://github.com/alexfayers/choosinator
cd choosinator
pip install .
```

If you like using virtual environments, you can easily install the project within one using [pipx](https://pypa.github.io/pipx/):

```bash
pipx install .
```

## Usage

You can use choosinator as an importable module:

```py
from project_name import BaseClass

app = BaseClass("config.yml")

app.logger.info(
    f"Hi, welcome to {app.config.INFO.NAME} by {app.config.INFO.AUTHOR}!"
)
```

Or as a command line interface:

```bash
$ python3 -m project_name
# or
$ project_name
```

## Documentation

Documentation for choosinator can be found at [https://alexfayers.github.io/choosinator](https://alexfayers.github.io/choosinator).
