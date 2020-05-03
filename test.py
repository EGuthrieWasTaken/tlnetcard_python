# test.py
# Ethan Guthrie
# 04/30/2020
# Tests that all tlnetcard_python modules run.

import pytest
from glob import glob

def test_run():
    files = glob("./tlnetcard_python/**/*.py", recursive=True)
    for i in files:
        if i[-11:] != "__init__.py":
            exec(open(i, "r").read())
