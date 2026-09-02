# Python Source

`fixed_income_analytics` 패키지의 구현 코드와 테스트를 두는 디렉터리입니다.

> 현재 상태: 패키지는 초기 개발 단계입니다. `Bond` 클래스의 기본 속성만 구현되어 있으며 가격·현금흐름·위험지표 계산과 정식 패키징 설정은 아직 제공하지 않습니다.

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

`Bond`는 다음 입력값을 받습니다.

- `face_value`: 채권의 액면가
- `coupon_rate`: 연 쿠폰 금리(소수 표기)
- `maturity`: `datetime.date` 형식의 만기일
- `payment_frequency`: 연간 쿠폰 지급 횟수

현재 구현에서는 `payment_frequency` 인수가 전달되더라도 내부 값이 반기 지급을 의미하는 `2`로 고정됩니다. 이 동작은 구현이 확장되면서 변경될 예정입니다.

## Usage

아직 `pyproject.toml`이 비어 있어 설치 가능한 패키지로 구성되지 않았습니다. 저장소 루트에서 `PYTHONPATH`를 지정해 현재 코드를 불러올 수 있습니다.

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

`tests/test_bond.py`는 현재 빈 자리표시자입니다. 테스트가 추가되고 `pytest`가 설치된 환경에서는 저장소 루트에서 다음 명령을 사용할 예정입니다.

```bash
python -m pytest python/src/tests
```

## Planned work

- 입력값 검증과 지급 빈도 처리
- 쿠폰 일정 및 현금흐름 생성
- 가격과 만기수익률 계산
- 듀레이션, DV01 및 컨벡서티 계산
- 패키징 메타데이터와 의존성 정의
- 단위 테스트 및 수치 검증 추가
