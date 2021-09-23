"""Tests for `pydata_factory` package."""
import json
from pathlib import Path

from pydata_factory.class_model import create_model


def test_create_model():
    """Test the creation of a new model from a parquet file."""
    path = Path(__file__).parent / "data" / "schemas" / "fb2021.json"
    with open(path, "r") as f:
        content = f.read()
        result = create_model(json.loads(content))
    assert result != ""
