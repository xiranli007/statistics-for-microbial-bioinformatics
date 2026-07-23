"""Validate that every chapter listed in _quarto.yml exists."""

from pathlib import Path

import yaml


def listed_chapters(config: dict) -> list[str]:
    """Return all file paths declared in the book chapter tree."""
    paths: list[str] = []
    for item in config["book"]["chapters"]:
        if isinstance(item, str):
            paths.append(item)
        elif isinstance(item, dict):
            paths.extend(item.get("chapters", []))
    return paths


def missing_chapters(root: Path) -> list[str]:
    """Return configured chapter paths that do not exist."""
    config = yaml.safe_load((root / "_quarto.yml").read_text())
    return [path for path in listed_chapters(config) if not (root / path).is_file()]


if __name__ == "__main__":
    project_root = Path(__file__).resolve().parents[1]
    missing = missing_chapters(project_root)
    if missing:
        raise SystemExit("Missing chapters:\n" + "\n".join(missing))
    print("Curriculum structure is complete.")

