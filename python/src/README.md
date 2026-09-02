# Python Source

This directory contains the implementation and tests for the `fixed_income_analytics` package.

> Current status: The package is in an early stage of development. Only the basic attributes of the `Bond` class are implemented; pricing, cash-flow and risk calculations, and formal packaging configuration are not yet available.

## Layout

```text
python/src/
├── fixed_income_analytics/
│   ├── __init__.py
│   └── bond.py
├── tests/
│   └── test_bond.py
├── pyproject.toml
└── requirements.txt
```

## Current API

`Bond` accepts the following arguments:

- `face_value`: The bond's face value
- `coupon_rate`: The annual coupon rate expressed as a decimal
- `maturity`: The maturity date as a `datetime.date`
- `payment_frequency`: The number of coupon payments per year

In the current implementation, `payment_frequency` is fixed internally at `2`, representing semiannual payments, regardless of the supplied argument. This behavior is expected to change as the implementation develops.

## Usage

Because `pyproject.toml` is currently empty, the project is not yet configured as an installable package. Set `PYTHONPATH` from the repository root to import the current code.

```bash
export PYTHONPATH="$PWD/python/src"
python - <<'PY'
import datetime

from fixed_income_analytics.bond import Bond

bond = Bond(
    face_value=1_000,
    coupon_rate=0.05,
    maturity=datetime.date(2030, 12, 31),
    payment_frequency=2,
)

print(bond.face_value)
print(bond.coupon_rate)
print(bond.maturity)
print(bond.payment_frequency)
PY
```

## Tests

`tests/test_bond.py` is currently an empty placeholder. After tests have been added and `pytest` is installed, run them from the repository root with:

```bash
python -m pytest python/src/tests
```

## Planned work

- Validate inputs and handle payment frequencies
- Generate coupon schedules and cash flows
- Calculate prices and yield to maturity
- Calculate duration, DV01, and convexity
- Define packaging metadata and dependencies
- Add unit tests and numerical validation
