# test.py
# Ethan Guthrie
# 04/30/2020
# Tests that all tlnetcard_python modules run.

# Classes to actually run the tests.
import pytest
from glob import glob

# Importing classes that are used as types.
from requests import Session
from tlnetcard_python.login import Login
from typing import Any, Dict, List

def test_run():
    files = glob("./tlnetcard_python/**/*.py", recursive=True)
    for i in files:
        if i[-11:] != "__init__.py":
            exec(open(i, "r").read())
