#!/usr/bin/env python

"""Smoke tests."""

import unittest


class TestSmoke(unittest.TestCase):
    """Some smoke tests."""

    def test_import_all(self):
        """Import all modules."""
        import black
        import colorama
        import flake8
        import isort
        import numpy
        import pipreqs
        import psutil
        import pydocstyle
        import pylint
        import pytest
        import requests
        import rope
        import tabulate
        import toml
        import tqdm
        import yaml

        return 0


if __name__ == "__main__":
    unittest.main()
