"""Data test."""
import glob
import json
import os
import unittest

from linkml_runtime.loaders import JSONLoader
from src.celltag_schema.datamodel.celltag_schema import CxGMetaSchema

ROOT = os.path.join(os.path.dirname(__file__), '..')
DATA_DIR = os.path.join(ROOT, "src", "data", "examples")

EXAMPLE_FILES = glob.glob(os.path.join(DATA_DIR, '*.json'))


class TestData(unittest.TestCase):
    """Test data and datamodel."""

    def test_data(self):
        """Validation test."""
        loader = JSONLoader()
        for path in EXAMPLE_FILES:
            with open(path, 'r') as file:
                data = json.load(file)
                for item in data["meta"]:
                    obj = loader.load(item, target_class=CxGMetaSchema)
                    assert obj
