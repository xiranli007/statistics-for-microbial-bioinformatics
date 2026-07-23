from pathlib import Path

from scripts.validate_datasets import provenance_errors


def test_dataset_provenance_and_checksums() -> None:
    assert provenance_errors(Path(__file__).resolve().parents[1]) == []
