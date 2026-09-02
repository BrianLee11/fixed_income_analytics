# Fixed Income Analytics Notebooks

채권 분석 개념을 순서대로 학습하고 구현하기 위한 Jupyter Notebook 모음입니다. 각 노트북은 앞선 주제에서 만든 개념과 코드를 다음 주제로 확장하도록 구성할 예정입니다.

## Learning path

| 순서 | 노트북 | 주제 | 상태 |
| ---: | --- | --- | --- |
| 1 | `note0001_bond_object.ipynb` | 채권 객체 생성과 기본 속성 | 초안 작성 |
| 2 | `note0002_coupon_cash_flows.ipynb` | 쿠폰 및 원금 현금흐름 | 예정 |
| 3 | `note0003_bond_pricing.ipynb` | 현금흐름 할인과 채권 가격 | 예정 |
| 4 | `note0004_yield_to_maturity.ipynb` | 만기수익률(YTM) 계산 | 예정 |
| 5 | `note0005_duration_and_dv01.ipynb` | 듀레이션과 DV01 | 예정 |
| 6 | `note0006_convexity.ipynb` | 컨벡서티 | 예정 |
| 7 | `note0007_yield_curve.ipynb` | 수익률 곡선 구성과 해석 | 예정 |
| 8 | `note0008_relative_value.ipynb` | 상대가치 분석 | 예정 |

현재 `note0002`부터 `note0008`까지는 빈 자리표시자이며 실행 가능한 노트북이 아닙니다.

## Running the notebooks

저장소 루트에서 가상환경을 만들고 활성화합니다.

```bash
python -m venv python/.venv
source python/.venv/bin/activate
python -m pip install jupyter
export PYTHONPATH="$PWD/python/src"
jupyter lab python/notebooks
```

Windows PowerShell에서는 가상환경 활성화와 환경 변수 설정을 다음과 같이 바꿉니다.

```powershell
python -m venv python/.venv
python/.venv/Scripts/Activate.ps1
python -m pip install jupyter
$env:PYTHONPATH = "$PWD/python/src"
jupyter lab python/notebooks
```

## Conventions

- 노트북 파일명은 학습 순서를 나타내는 네 자리 번호를 사용합니다.
- 재사용할 계산 로직은 노트북에만 두지 않고 `python/src/fixed_income_analytics/`로 옮깁니다.
- 실행 결과는 재현 가능한 범위에서만 저장하고, 로컬 경로나 비공개 데이터는 포함하지 않습니다.
- 예제에서는 날짜, 이자율 단위 및 지급 빈도를 명시합니다.
