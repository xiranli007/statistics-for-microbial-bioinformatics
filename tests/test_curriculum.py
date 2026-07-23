from pathlib import Path

from scripts.validate_curriculum import missing_chapters


def test_all_configured_chapters_exist() -> None:
    assert missing_chapters(Path(__file__).resolve().parents[1]) == []

