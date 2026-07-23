# Contributing

## Chapter contract

Every statistical-method chapter should include:

1. biological questions the method can and cannot answer;
2. outcome and predictor types;
3. mathematical model with every term defined;
4. independent sampling unit and dependence structure;
5. assumptions, separated into design assumptions and distributional assumptions;
6. estimand and effect size;
7. corresponding inferential procedure and what its p-value or interval means;
8. diagnostic checks and remedies;
9. a traceable microbiology dataset from a real paper;
10. reproducible Python analysis and, when useful, an R equivalent;
11. plain-language interpretation and a reporting template;
12. common misuses and a short knowledge check.

## Dataset acceptance checklist

- Peer-reviewed microbiology article
- Stable paper DOI or full citation
- Stable raw-data accession or repository URL
- Reuse license checked
- Raw data not manually edited
- Download script and checksum
- Processing script from raw to analysis-ready data
- Data dictionary with units, missing-value codes, and sampling unit
- No human-identifiable data

Do not invent a synthetic replacement when a suitable paper dataset cannot be
found. Open a discussion with the repository owner, describe the missing data
need, and wait for approval before creating any simulated teaching observations.

## Development

```bash
pip install -r requirements-dev.txt
pytest
quarto render
```

Do not commit `_site/`, virtual environments, caches, or unlicensed raw data.
