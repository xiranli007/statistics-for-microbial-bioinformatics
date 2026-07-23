"""Validate provenance records for versioned paper datasets."""

from __future__ import annotations

import hashlib
from pathlib import Path

import yaml


REQUIRED_ARTICLE_FIELDS = {"citation_key", "title", "journal", "year", "doi", "peer_reviewed"}
REQUIRED_DATA_FIELDS = {
    "repository",
    "repository_url",
    "source_commit",
    "source_path",
    "local_path",
    "source_sha256",
    "local_sha256",
    "license",
}
REQUIRED_DESIGN_FIELDS = {"organism", "response", "experimental_unit"}


def provenance_errors(root: Path) -> list[str]:
    """Return human-readable errors from the dataset registry."""
    registry_path = root / "data" / "datasets.yml"
    registry = yaml.safe_load(registry_path.read_text())
    datasets = registry.get("datasets", {})
    errors: list[str] = []

    if not datasets:
        return ["data/datasets.yml contains no dataset records"]

    bibliography = (root / "references.bib").read_text()

    for key, record in datasets.items():
        article = record.get("article", {})
        data = record.get("data", {})
        design = record.get("design", {})

        for field in sorted(REQUIRED_ARTICLE_FIELDS - article.keys()):
            errors.append(f"{key}: missing article.{field}")
        for field in sorted(REQUIRED_DATA_FIELDS - data.keys()):
            errors.append(f"{key}: missing data.{field}")
        for field in sorted(REQUIRED_DESIGN_FIELDS - design.keys()):
            errors.append(f"{key}: missing design.{field}")

        if article.get("peer_reviewed") is not True:
            errors.append(f"{key}: article.peer_reviewed must be true")

        citation_key = article.get("citation_key")
        if citation_key and f"{{{citation_key}," not in bibliography:
            errors.append(f"{key}: citation key {citation_key!r} is absent from references.bib")

        local_path = data.get("local_path")
        if local_path:
            file_path = root / local_path
            if not file_path.is_file():
                errors.append(f"{key}: local file {local_path!r} does not exist")
            else:
                observed = hashlib.sha256(file_path.read_bytes()).hexdigest()
                expected = data.get("local_sha256")
                if expected and observed != expected:
                    errors.append(
                        f"{key}: local checksum mismatch; expected {expected}, observed {observed}"
                    )

        for chapter in record.get("used_in", []):
            if not (root / chapter).is_file():
                errors.append(f"{key}: used_in path {chapter!r} does not exist")

    return errors


if __name__ == "__main__":
    project_root = Path(__file__).resolve().parents[1]
    errors = provenance_errors(project_root)
    if errors:
        raise SystemExit("Dataset provenance errors:\n" + "\n".join(errors))
    print("Dataset provenance is complete and checksums match.")
