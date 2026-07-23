# Statistics for Microbial Bioinformatics

A Python-first, paper-driven study guide for choosing, fitting, checking, and
interpreting statistical models used in microbiology and bioinformatics.
Selected R equivalents are included where the R ecosystem is especially strong.

## What makes this guide different

- Starts from biological questions and study design—not software menus.
- Uses microbiology examples and public data linked to real papers.
- Connects each model to its estimand, assumptions, significance test, effect
  size, diagnostics, and common failure modes.
- Distinguishes exploratory methods (for example, PCA) from inferential tests
  (for example, PERMANOVA).
- Treats repeated measures, random effects, compositionality, zero inflation,
  multiple testing, and batch effects as core topics.
- Compares frequentist and Bayesian reasoning using the same biological models.

## Status

The complete curriculum structure is present. Chapters are being filled
progressively. The orientation section, statistical foundations, and two-group
comparison chapter form the first paper-driven release.

## Read locally

1. Install [Quarto](https://quarto.org/docs/get-started/).
2. Create the Python environment:

   ```bash
   python -m venv .venv
   source .venv/bin/activate
   pip install -r requirements.txt
   ```

3. Render the book:

   ```bash
   quarto render
   ```

The rendered site is written to `_site/`.

## Curriculum map

| Part | Central question | Representative methods |
|---|---|---|
| Orientation | What am I trying to estimate? | estimands, design, decision workflow |
| Foundations | How do probability and sampling create uncertainty? | distributions, likelihood, CIs, resampling |
| Classical tests | Do predefined groups differ? | t tests, ANOVA, rank tests, contingency tests |
| Regression | How does an outcome change with predictors? | linear, logistic, Poisson, negative binomial |
| Mixed models | Which observations share a sampling unit? | random intercepts/slopes, GLMMs |
| Multivariate ecology | Do whole communities differ? | PCA, PCoA, NMDS, PERMANOVA, constrained ordination |
| Omics data | How should counts and compositions be modeled? | DE, offsets, transformations, FDR |
| Time and dependence | How do trajectories and autocorrelation matter? | longitudinal models, splines, time series |
| Prediction | How well can unseen samples be predicted? | regularization, trees, nested CV |
| Bayesian models | What changes when uncertainty is represented probabilistically? | priors, posterior intervals, hierarchical models |
| Reproducibility | Can another researcher rerun and audit the result? | environments, workflows, reporting |

## Data policy

Every worked example must use observations from a peer-reviewed microbiology
article. Synthetic teaching datasets are not allowed unless a proposed exception
is discussed with and approved by the repository owner before any data are
created.

Small source datasets may be versioned when their license permits redistribution.
Otherwise, raw data are downloaded by scripts. Every completed case study records
the article DOI, stable data location or accession, license, exact source file,
checksum, experimental unit, and preprocessing in
[`data/datasets.yml`](data/datasets.yml).

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md). Scientific corrections, microbiology
datasets with stable accessions, and Python/R parity improvements are welcome.
