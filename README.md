# ♠️♥️인디언 포커♦️♣️
---

<p align="center">
  <img src="https://github.com/user-attachments/assets/f36e9fa4-b970-4159-b7f6-6aae7c048a0b" width="500"/>
  <img src="https://github.com/user-attachments/assets/b74e0185-f303-45f7-9e15-56c00e40596e" width="500"/>
</p>


## 📆 프로젝트 기간

- 2025년 4월 18일 ~ 4월 24일

---

## 📌 프로젝트 개요

대형 언어 모델(LLM)인 EEVE를 활용해 **직관적이고 간단한 카드 게임**입니다.
AI가 주는 힌트를 보고 사용자가 직접 행동(배팅/폴드/올인)을 선택하여 AI와 승부를 봐야합니다. 
AI가 주는 고도의 심리전을 즐겨보시길 바랍니다.

---

## 🛠 기술 스택

| 기술명 | 역할 및 설명 | 뱃지 |
|--------|----------------|------|
| **Python** | 전체 애플리케이션 개발, 게임 로직 구현 | ![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) |
| **Streamlit** | 웹 UI 및 상태 관리, 인터랙티브 게임 구현 | ![Streamlit](https://img.shields.io/badge/Streamlit-%23FE4B4B.svg?style=for-the-badge&logo=streamlit&logoColor=white) |
| **Ollama** | LLM 호출 및 실행(로컬) | <img src="https://img.shields.io/badge/Ollama-000000?style=for-the-badge&logo=OpenAI&logoColor=white"/> |
| **EEVE-Korean-10.8B** | 한국어 특화 LLM, 힌트 생성 및 상대 역할 수행,  | ![EEVE](https://img.shields.io/badge/EEVE-Korean--10.8B-yellow?style=flat-square) |

---

## 🎮 게임 진행 방식

1. **카드 배정**: 플레이어와 상대방 각각 1~13의 숫자 카드 부여
2. **상대 카드 확인**: 내 눈에 상대 카드만 보이고, 내 카드는 상대가 보고 힌트를 줌
3. **힌트 생성**: LLM이 내 카드를 기반으로 블러핑 포함된 힌트를 생성
4. **행동 선택**: 플레이어가 배팅금 입력 후 `콜`, `폴드`, `올인` 중 선택
5. **결과 판단**:
   - `콜`: 카드 숫자 비교하여 승패 결정
   - `폴드`: 기본 배팅금만 손해
   - `올인`: 보유 금액 전부 걸고 승패 판단
6. **자금 반영 후 라운드 진행**: 파산 시 게임 종료

---

## ⚙️ 기능 구성

| 기능 | 설명 |
|------|------|
| 💬 힌트 생성 | 내 카드를 기반으로 AI가 힌트를 제공합니다 (LLM 활용) |
| 🎴 카드 배정 | 1~13 범위의 숫자 카드 랜덤 할당 |
| 💸 배팅 시스템 | 최소 100 단위로 콜/폴드/올인 선택 가능 |
| 🔁 라운드 진행 | 라운드마다 자금 변화 반영, 자동 진행 |
| 🧠 폴드 | 확정 손해 (`기본 배팅금`만 손해) |
| 💻 웹 UI | Streamlit으로 동작, 클릭 인터페이스 제공 |
| 🗃 상태 관리 | `session_state`를 통한 라운드 유지 및 카드 고정 |

---

## 📁 파일 구조

```bash
project/
├── game.py                 # 게임 로직: 카드 배정, 힌트 생성, 승패 계산
├── app.py                  # Streamlit UI 코드 (별도 실행)
└── README.md               # 프로젝트 설명서
```

---

## 🔧 개선 방안

| 항목 | 설명 |
|------|------|
| 🤖 상대 AI 액션 자동화 | 상대 AI가 상황에 따라 콜/폴드/올인을 선택하는 로직 추가 |
| 🧠 힌트 다양성 향상 | 프롬프트 구성 개선 및 LLM 출력을 더 자연스럽게 조정 |
| 💬 힌트 옵션 모드 | 랜덤/고정형 힌트 생성 방식 선택 가능하게 변경 |
| 💾 플레이 기록 저장 | 게임 결과를 CSV 파일 등으로 저장하는 기능 추가 |
| ⚙️ 배팅 시스템 강화 | raise/체크 등 포커 규칙 요소 추가로 전략성 향상 |
