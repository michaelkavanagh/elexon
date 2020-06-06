#!/usr/bin/env bash

# ensure all tests pass
# bump version in setup.py
# bump version in elexon/__init__.py

rm dist/*
python3 setup.py sdist bdist_wheel
python3 -m twine upload dist/*
