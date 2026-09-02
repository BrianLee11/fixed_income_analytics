# Fixed Income Analytics

This project explores the core concepts of bonds and interest-rate products through Python implementations. It starts with a simple bond object and aims to expand into cash flows, pricing, yield to maturity, duration, convexity, yield curves, and relative-value analysis.

> Current status: The project is in an early stage of development. A basic `Bond` class and the first learning notebook are available; the remaining documents and notebooks are placeholders for future work.

## Repository structure

```text
.
├── docs/
│   ├── architecture.md
│   └── mathematical_notes.md
└── python/
    ├── notebooks/
    │   ├── README.md
    │   └── note0001_...ipynb ~ note0008_...ipynb
    └── src/
        ├── fixed_income_analytics/
        │   └── bond.py
        ├── tests/
        ├── pyproject.toml
        └── requirements.txt
```

## Topics

- Basic bond attributes and representation
- Coupon and principal cash-flow generation
- Bond pricing
- Yield-to-maturity (YTM) calculation
- Duration, modified duration, and DV01
- Convexity
- Yield curves
- Bond relative-value analysis

See the [notebooks README](python/notebooks/README.md) for the planned learning sequence.

## Quick start

Python 3.10 or later is recommended. The packaging configuration and dependency list are still in progress, so clone the repository and add the source directory to `PYTHONPATH` to use the current code.

```bash
git clone https://github.com/BrianLee11/fixed_income_analytics.git
cd fixed_income_analytics
python -m venv python/.venv
source python/.venv/bin/activate
export PYTHONPATH="$PWD/python/src"
```

Install Jupyter separately to open the first notebook.

```bash
python -m pip install jupyter
jupyter lab python/notebooks
```

See the [Python source README](python/src/README.md) for current usage instructions.

## Development status

This repository is a workspace for learning and incremental implementation. Public APIs, calculation methods, and the directory structure may change during development.

## License

This project is licensed under the [MIT License](LICENSE).
