# ♠️♥️인디언 포커♦️♣️

🤖 **LLM 기반 힌트 생성 + 사용자 인터랙션이 있는 웹 인디언 포커 게임**입니다.  
카드를 보고 콜할지, 폴드할지 직접 선택해보세요!

---

## 🃏 게임 소개

- 상대의 카드를 보고 **힌트를 기반으로 승부 예측**
- 라운드마다 **배팅** 또는 **폴드**, **올인** 선택 가능
- **LLM (EEVE-Korean)** 모델이 상대 입장에서 힌트를 만들어냅니다.
- Streamlit 기반으로 **브라우저에서 직관적인 플레이** 가능

---

## 📌 프로젝트 개요

이 프로젝트는 대형 언어 모델(LLM)을 활용해 **상대 입장에서 생성한 힌트를 기반으로 한 카드 게임**입니다.  
Streamlit으로 웹 UI를 구성하고, 사용자가 직접 배팅/폴드/올인을 선택하며 자금을 관리해 나갑니다.

- 💬 자연어 힌트로 추론력 테스트
- 🎴 직관적이고 간단한 카드 게임
- 🤖 LLM 블러핑 기반의 심리전

---

## 🛠 기술 스택

| 기술명 | 역할 및 설명 | 뱃지 |
|--------|----------------|------|
| **Python** | 전체 애플리케이션 개발, 게임 로직 구현 | ![Python](https://img.shields.io/badge/Python-3.10+-blue?logo=python) |
| **Streamlit** | 웹 UI, 상태 관리, 인터랙티브 게임 구현 | ![Streamlit](https://img.shields.io/badge/Streamlit-Interactive-red?logo=streamlit) |
| **Ollama (LLM)** | 힌트 생성에 사용되는 LLM 실행 환경 | ![Ollama](https://img.shields.io/badge/Ollama-Model%20Runtime-black?logo=openai) |
| **EEVE-Korean-10.8B** | 내 카드 기반 블러핑 힌트를 생성하는 LLM | ![EEVE](https://img.shields.io/badge/EEVE-Korean--10.8B-yellow?style=flat-square) |

---


## ⚙️ 기능 구성

| 기능 | 설명 |
|------|------|
| 💬 힌트 생성 | 내 카드를 기반으로 상대가 힌트를 제공합니다 (LLM 활용) |
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
├── indian_poker_app.py     # Streamlit UI 코드 (별도 실행)
├── requirements.txt        # 의존성 명시
└── README.md               # 프로젝트 설명서

