[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://github.com/pre-commit/pre-commit)
[![codecov](https://codecov.io/gh/mashi/requirements-filter/branch/main/graph/badge.svg?token=HSSZFVCNOJ)](https://codecov.io/gh/mashi/requirements-filter)
[![CircleCI](https://circleci.com/gh/circleci/circleci-docs.svg?style=shield)](https://app.circleci.com/pipelines/github/mashi/requirements-filter?branch=main)


# Description
Removes private packages from a general `requirements.txt` file.


## Usage
An example of usage is installing private packages. My usual workflow consists of
1. changes in the source code,
1. `pip freeze > requirements.txt`
1. and `git add .` and `git commit -m "commit massage"`.
    However, my private packages were included and the CI build would fail because of
    the peculiar syntax required to install
    [private packages](https://docs.readthedocs.io/en/stable/guides/private-python-packages.html).
1. The private package was manually removed from the `requirements.txt` and another `commit` was executed.

This package was created to avoid this situation. Storing the private packages
in a different file (e.g., `requirements-private.txt`), it removes the
packages already presented inside `requirements-private.txt` from the `requirements.txt`
avoiding the manual deletion and the commit correcting the change.

The recommended use is adding in the `.pre-commit-config.yaml` file
```
  - repo: https://github.com/mashi/requirements-filter
    rev: v0.0.0  # replace by desired tag version
    hooks:
      - id: rqf
        args: [--filename1, requirements.txt, --filename2, requirements-private.txt]  # example with arguments
```

In this way, the packages are checked before the `commit` and prevents the inclusion in the version control.


## Instructions (Development)
Create a virtual environment and install the required packages with
```
python3 -m venv .venv
source .venv/bin/activate
pip install wheel
pip install -r requirements.txt
pre-commit install
```
