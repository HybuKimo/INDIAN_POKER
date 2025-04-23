import streamlit as st
import random
from game import generate_hint, assign_cards, evaluate_result

# 세션 상태 초기화
if "player_money" not in st.session_state:
    st.session_state.player_money = 0
    st.session_state.opponent_money = 0
    st.session_state.round_num = 1
    st.session_state.message = ""
    st.session_state.game_over = False

# 게임 시작 화면
if st.session_state.player_money == 0:
    money = st.number_input("💰 시작 자금 입력 (최소 1000)", min_value=1000, value=1000, step=100)
    if st.button("게임 시작"):
        st.session_state.player_money = money
        st.session_state.opponent_money = money
        st.rerun()

# 게임 진행
if st.session_state.player_money > 0 and st.session_state.opponent_money > 0 and not st.session_state.game_over:
    st.subheader(f"🎲 Round {st.session_state.round_num}")
    base_bet = 100
    st.write(f"🧑 당신 자금: {st.session_state.player_money} | 🤖 상대 자금: {st.session_state.opponent_money}")

    player_card, opponent_card = assign_cards()
    st.markdown(f"👁️ 상대 카드: **{opponent_card}**")
    hint = generate_hint(player_card)
    st.markdown(f"🤖 상대 힌트: *{hint}*")

    bet = st.number_input("💸 배팅할 금액 입력 (최소 100)", min_value=100,
                          max_value=min(st.session_state.player_money, st.session_state.opponent_money), step=50)

    action = st.radio("👉 행동을 선택하세요:", ["콜", "폴드", "올인"])

    if st.button("카드 오픈 및 결과 확인"):
        if action == "올인":
            bet = min(st.session_state.player_money, st.session_state.opponent_money)
            st.write(f"🔥 올인! 베팅금: {bet}")
        elif action == "폴드":
            st.write("🙅‍♂️ 폴드 선택! 기본 배팅금만 손해입니다.")
        else:
            st.write(f"🪙 콜 선택! 베팅금: {bet}")

        result_player, result_opponent, message = evaluate_result(
            player_card, opponent_card, bet, action, base_bet
        )
        st.session_state.player_money += result_player
        st.session_state.opponent_money += result_opponent
        st.session_state.message = message

        if st.session_state.player_money <= 0:
            st.session_state.message += "\n💀 당신이 파산했습니다. 다음 생에 뵙겠습니다🌟🌟🌟🔫"
            st.session_state.game_over = True
        elif st.session_state.opponent_money <= 0:
            st.session_state.message += "\n🎉 상대가 파산했습니다. 살아남으셨습니다🎉🎉🎉"
            st.session_state.game_over = True
        else:
            st.session_state.round_num += 1

# 결과 출력
if st.session_state.message:
    st.markdown("---")
    st.markdown(f"**📣 결과:** {st.session_state.message}")

if st.session_state.game_over:
    if st.button("🔁 다시 시작"):
        for key in list(st.session_state.keys()):
            del st.session_state[key]
        st.rerun()