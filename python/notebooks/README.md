# Fixed Income Analytics Notebooks

A collection of Jupyter notebooks for learning and implementing fixed-income analytics concepts in sequence. Each notebook is intended to build on the concepts and code introduced in the preceding topics.

## Learning path

| Order | Notebook | Topic | Status |
| ---: | --- | --- | --- |
| 1 | `note0001_bond_object.ipynb` | Creating a bond object and defining its basic attributes | Draft |
| 2 | `note0002_coupon_cash_flows.ipynb` | Coupon and principal cash flows | Planned |
| 3 | `note0003_bond_pricing.ipynb` | Cash-flow discounting and bond pricing | Planned |
| 4 | `note0004_yield_to_maturity.ipynb` | Yield-to-maturity (YTM) calculation | Planned |
| 5 | `note0005_duration_and_dv01.ipynb` | Duration and DV01 | Planned |
| 6 | `note0006_convexity.ipynb` | Convexity | Planned |
| 7 | `note0007_yield_curve.ipynb` | Yield-curve construction and interpretation | Planned |
| 8 | `note0008_relative_value.ipynb` | Relative-value analysis | Planned |

The files from `note0002` through `note0008` are currently empty placeholders and are not executable notebooks.

## Running the notebooks

Create and activate a virtual environment from the repository root.

```bash
python -m venv python/.venv
source python/.venv/bin/activate
python -m pip install jupyter
export PYTHONPATH="$PWD/python/src"
jupyter lab python/notebooks
```

On Windows PowerShell, use the following commands to activate the environment and set `PYTHONPATH`.

```powershell
python -m venv python/.venv
python/.venv/Scripts/Activate.ps1
python -m pip install jupyter
$env:PYTHONPATH = "$PWD/python/src"
jupyter lab python/notebooks
```

## Conventions

- Notebook filenames use a four-digit prefix to indicate the learning sequence.
- Move reusable calculation logic into `python/src/fixed_income_analytics/` instead of keeping it only in notebooks.
- Save outputs only when they are reproducible, and do not include local paths or private data.
- State date conventions, interest-rate units, and payment frequencies explicitly in examples.
