# Fixed Income Analytics

채권과 금리 상품의 핵심 개념을 Python으로 구현하며 학습하는 프로젝트입니다. 단순한 채권 객체에서 시작해 현금흐름, 가격, 만기수익률, 듀레이션, 컨벡서티, 수익률 곡선 및 상대가치 분석으로 범위를 확장하는 것을 목표로 합니다.

> 현재 상태: 초기 개발 단계입니다. 기본 `Bond` 클래스와 첫 번째 학습 노트북이 작성되어 있으며, 나머지 문서와 노트북은 향후 구현을 위한 자리표시자입니다.

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

- 채권의 기본 속성과 표현
- 쿠폰 및 원금 현금흐름 생성
- 채권 가격 계산
- 만기수익률(YTM) 산출
- 듀레이션, 수정 듀레이션 및 DV01
- 컨벡서티
- 수익률 곡선
- 채권 상대가치 분석

각 주제의 예정 학습 순서는 [notebooks README](python/notebooks/README.md)에서 확인할 수 있습니다.

## Quick start

Python 3.10 이상을 권장합니다. 현재 패키징 설정과 의존성 목록은 작성 중이므로, 저장소를 복제한 뒤 소스 디렉터리를 `PYTHONPATH`에 추가해 사용할 수 있습니다.

```bash
git clone https://github.com/BrianLee11/fixed_income_analytics.git
cd fixed_income_analytics
python -m venv python/.venv
source python/.venv/bin/activate
export PYTHONPATH="$PWD/python/src"
```

Jupyter를 별도로 설치한 뒤 첫 번째 노트북을 열 수 있습니다.

```bash
python -m pip install jupyter
jupyter lab python/notebooks
```

소스 코드의 현재 사용 방법은 [Python source README](python/src/README.md)를 참고하세요.

## Development status

이 저장소는 학습과 점진적 구현을 위한 작업 공간입니다. 공개 API, 계산 방식 및 디렉터리 구조는 개발 과정에서 변경될 수 있습니다.

## License

이 프로젝트는 [MIT License](LICENSE)를 따릅니다.
