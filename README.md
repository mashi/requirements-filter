[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://github.com/pre-commit/pre-commit)
[![CircleCI](https://circleci.com/gh/circleci/circleci-docs.svg?style=shield)](https://app.circleci.com/pipelines/github/mashi/requirements-filter?branch=master)


# Description
This package filters the packages between two files. It was created as an exercise
about python packages, but I hope it can help someone else.

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
avoiding the manual delete and the commit correcting this change.


## Instructions (Development)
Create a virtual environment and install the required packages with
```
python3 -m venv .venv
source .venv/bin/activate
pip install wheel
pip install -r requirements.txt
pre-commit install
```
