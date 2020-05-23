# ratscience: Python Additional Packages

[![made-with-Markdown](https://img.shields.io/badge/Made%20with-Markdown-2d2d2d.svg)](http://commonmark.org)
[![License: Unlicense](https://img.shields.io/badge/License-Unlicense-green.svg)](https://unlicense.org/)

This repository contains `requirements.txt` file with a periodically updated list of packages and their versions.
The main task of this repository is to instantly synchronize packages and versions between different projects or team members.

**This file is updated as a [rolling release](https://ru.wikipedia.org/wiki/Rolling_release) ASAP. Please see Usage section for freeze current requirements.**

Provides:

* [black](https://github.com/psf/black)
* [colorama](https://github.com/tartley/colorama)
* [flake8](https://github.com/pycqa/flake8)
* [isort](https://github.com/timothycrosley/isort)
* [numpy](https://github.com/numpy/numpy)
* [pip-check](https://github.com/bartTC/pip-check)
* [pipreqs](https://github.com/bndr/pipreqs)
* [pre-commit](https://github.com/pre-commit/pre-commit)
* [psutil](https://github.com/giampaolo/psutil)
* [pur](https://github.com/alanhamlett/pip-update-requirements)
* [pydocstyle](https://github.com/PyCQA/pydocstyle)
* [pylint](https://github.com/PyCQA/pylint)
* [pytest](https://github.com/pytest-dev/pytest)
* [pyyaml](https://github.com/yaml/pyyaml)
* [requests](https://github.com/psf/requests)
* [rope](https://github.com/python-rope/rope)
* [tabulate](https://github.com/astanin/python-tabulate)
* [toml](https://github.com/uiri/toml)
* [tqdm](https://github.com/tqdm/tqdm)

## Usage

### Install

#### Method 1. Install directly from url raw file

Run this script:

```bash
pip install --user -U -r https://raw.githubusercontent.com/ratscience/python-additional/master/requirements.txt
```

or if you use [virtualenv](https://github.com/pypa/virtualenv):

```bash
pip install -U -r https://raw.githubusercontent.com/ratscience/python-additional/master/requirements.txt
```

#### Method 2. Clone repo

Clone this repository as `git clone https://github.com/ratscience/python-additional.git`, then go to the repo directory and run:

```bash
pip install --user -U -r requirements.txt
```

or if you use [virtualenv](https://github.com/pypa/virtualenv):

```bash
pip install -U -r requirements.txt
```

### Update

For update, simply re-run any of install scripts. If you clone git repo, please run `git pull` first.

## Acknowledgements

This project is actively uses this awesome packages:

* [pur](https://github.com/alanhamlett/pip-update-requirements)
* [pip-check](https://github.com/bartTC/pip-check)
* [pre-commit](https://github.com/pre-commit/pre-commit)

## License

This project is licensed under the terms of the [Unlicense](https://unlicense.org/) (see [LICENSE](<https://github.com/ratscience/python-base/blob/master/LICENSE>) file).
