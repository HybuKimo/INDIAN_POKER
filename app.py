import streamlit as st
import random
from game import generate_hint, assign_cards, evaluate_result

# Streamlit 기본 설정
st.set_page_config(page_title="죽음의 인디언 포커", layout="centered")
st.title("☠️ 인디언 포커 ☠️")
st.markdown("♣️♥️♠️게임에 참가하신 당신! 진심으로 환영합니다♠️♥️♣️")

# 세션 상태 초기화
if "player_money" not in st.session_state:
    st.session_state.player_money = 0
    st.session_state.opponent_money = 0
    st.session_state.round_num = 1
    st.session_state.message = ""
    st.session_state.game_over = False
    st.session_state.player_card = None
    st.session_state.opponent_card = None
    st.session_state.hint = ""

# 게임 시작 화면
if st.session_state.player_money == 0:
    money = st.number_input("💰 시작 자금 입력 (최소 1000)", min_value=1000, value=1000, step=100)
    if st.button("게임 시작"):
        st.session_state.player_money = money
        st.session_state.opponent_money = money
        st.rerun()

# 카드 및 힌트 고정 (버튼 클릭 전까지)
if st.session_state.player_card is None or st.session_state.opponent_card is None:
    player_card, opponent_card = assign_cards()
    st.session_state.player_card = player_card
    st.session_state.opponent_card = opponent_card
    st.session_state.hint = generate_hint(player_card)

# 게임 진행
if st.session_state.player_money > 0 and st.session_state.opponent_money > 0 and not st.session_state.game_over:
    st.subheader(f"🎲 Round {st.session_state.round_num}")
    base_bet = 100
    st.write(f"🧑 당신 자금: {st.session_state.player_money} | 🤖 상대 자금: {st.session_state.opponent_money}")

    st.markdown(f"👁️ 상대 카드: **{st.session_state.opponent_card}**")
    st.markdown(f"🤖 상대 힌트: *{st.session_state.hint}*")

    bet = st.number_input("💸 배팅할 금액 입력 (최소 100)", min_value=100,
                          max_value=min(st.session_state.player_money, st.session_state.opponent_money), step=50,
                          key="bet_input")

    action = st.radio("👉 행동을 선택하세요:", ["콜", "폴드", "올인"], key="action_input")

    if st.button("카드 오픈 및 결과 확인"):
        if action == "올인":
            bet = min(st.session_state.player_money, st.session_state.opponent_money)
            st.write(f"🔥 올인!! 인생은 한방이지!!! | 베팅금: {bet}")
        elif action == "폴드":
            st.write("🙅‍♂️ 폴드 선택! 기본 배팅금만 잃습니다.")
        else:
            st.write(f"🪙 콜 선택! | 베팅금: {bet}")

        result_player, result_opponent, message = evaluate_result(
            st.session_state.player_card,
            st.session_state.opponent_card,
            bet, action, base_bet
        )
        st.session_state.player_money += result_player
        st.session_state.opponent_money += result_opponent
        st.session_state.message = f"👀 당신 카드: {st.session_state.player_card} | 상대 카드: {st.session_state.opponent_card}\n" + message

        if st.session_state.player_money <= 0:
            st.session_state.message += "\n🤖🤖🤖파산하셨네요. 하.하.하. 인간시대의 끝이 도래했다.🤖🤖🤖"
            st.session_state.game_over = True
        elif st.session_state.opponent_money <= 0:
            st.session_state.message += "\n😛😛😛파산당했죠? 깡통자식 아무것도 못하쥬.😛😛😛"
            st.session_state.game_over = True
        else:
            st.session_state.round_num += 1

        # 다음 라운드 준비를 위해 카드 초기화
        st.session_state.player_card = None
        st.session_state.opponent_card = None

# 결과 출력
if st.session_state.message:
    st.markdown("---")
    st.markdown(f"**📣 결과:** {st.session_state.message}")

if st.session_state.game_over:
    if st.button("🔁 다시 시작"):
        for key in list(st.session_state.keys()):
            del st.session_state[key]
        st.rerun()
