import random
import ollama

# 힌트 생성
def generate_hint(player_card):
    prompt = f"""
    나(사용자)는 인디언 포커를 참가하려고 합니다.
    너는는 나의 인디언 포커 상대입니다.
    나의 카드 숫자는 {player_card}입니다.

    아래 조건을 만족하는 힌트를 한 문장으로 만들어주세요:
    - 숫자는 직접 말하지 마세요
    - 너무 노골적인 표현은 피하고, 자연스럽게 유도하세요
    - 카드가 높으면 자신감을, 낮으면 경고를 주는 느낌이면 좋아요
    - 나의 카드 숫자가 11이상이거나 1이면 가끔 블러핑을 하세요

    힌트:
    """
    response = ollama.chat(
        model="EEVE-Korean-10.8B",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )
    return response['message']['content'].strip()

# 카드 배정
def assign_cards():
    return random.randint(1, 13), random.randint(1, 13)

# 결과 계산
def evaluate_result(player_card, opponent_card, bet, action, base_bet):
    if action == "폴드":
        return -base_bet, base_bet, "🙅‍♂️ 폴드!\n"
    else:
        print(f"👀 내 카드: {player_card} | 상대 카드: {opponent_card}")
        if player_card >= opponent_card:
            return bet, -bet, " 🤗승리!\n"
        else:
            return -bet, bet, " 🤮패배!\n"

# 게임 루프
def game_loop():
    try:
        print("☠️☠️☠️ 인디언 포커 ☠️☠️☠️")
        player_money = int(input("💰 시작 자금 입력 (최소 1000): "))
        if player_money < 1000:
            print(f"❌ {player_money}은 너무 적습니다. 최소 1000 이상 이어야 합니다.")
            return
    except:
        print("❌ 숫자를 입력하세요.")
        return

    opponent_money = player_money
    round_num = 1

    while player_money > 0 and opponent_money > 0:
        print(f"\n🎲 [라운드 {round_num}]")
        print(f"🧑 당신 자금: {player_money} | 🤖 상대 자금: {opponent_money}")

        base_bet = 100  # 고정된 기본 배팅금
        player_card, opponent_card = assign_cards()

        # 상대 카드 확인
        print(f"♠️♥️♣️ 카드 오픈 ♠️♥️♣️")
        print(f"👁️ 상대 카드 : {opponent_card}")
        hint = generate_hint(player_card)
        print(f"🤖 상대 힌트: \"{hint}\"")

        # 배팅금 입력 받기
        try:
            bet = int(input("💸 배팅할 금액 입력(최소 100): "))
            if bet < 100 or bet > player_money or bet > opponent_money:
                print("❌ 잘못된 배팅 금액입니다.")
                continue
        except:
            print("❌ 숫자를 입력하세요.")
            continue

        # 행동 입력
        action = input("👉 콜 / 폴드 / 올인 👈").strip()
        if action not in ["콜", "폴드", "올인"]:
            print("🚫 잘못된 입력. 게임 종료.")
            break

        # 행동 처리
        if action == "올인":
            bet = min(player_money, opponent_money)
            print(f"🔥🔥🔥 인생 한방이지!! 🔥🔥🔥 배팅금: {bet}")
        elif action == "폴드":
            print("🙅‍♂️ 폴드 선택! ")
        else:
            print(f"🪙 콜 선택! 배팅금: {bet}")

        # 결과 계산
        result_player, result_opponent, message = evaluate_result(player_card, opponent_card, bet, action, base_bet)
        player_money += result_player
        opponent_money += result_opponent

        print(f"📣 결과: {message}")
        print(f"💰 현재 자금 - 당신: {player_money}, 상대: {opponent_money}")

        if player_money <= 0:
            print("🤖🤖🤖파산하셨네요. 하.하.하. 인간시대의 끝이 도래했다.🤖🤖🤖")
            break
        elif opponent_money <= 0:
            print("🎉🎉🎉파산했습니다. 살아남으셨습니다🎉🎉🎉")
            break

        round_num += 1

# 실행
if __name__ == "__main__":
    game_loop()
