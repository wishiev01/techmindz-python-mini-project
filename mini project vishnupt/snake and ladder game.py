# snake and ladder game

import random

snakes = {
    99: 54,
    70: 55,
    52: 42,
    25: 2,
    95: 72
}

ladders = {
    6: 25,
    11: 40,
    60: 85,
    46: 90,
    17: 69
}

def roll_dice():
    return random.randint(1, 6)

def play_game():
    positions = {"Player 1": 0, "Player 2": 0}
    winner = None

    print("Welcome to Snake and Ladder!")
    print("First player to reach 100 wins.\n")

    while not winner:
        for player in positions:
            input(f"{player}, press Enter to roll the dice...")
            dice = roll_dice()
            print(f"{player} rolled a {dice}")

            pos = positions[player] + dice
            if pos > 100:
                print(f"{player} cannot move, needs exact number to reach 100.\n")
                continue

            if pos in snakes:
                print(f"Oh no! {player} got bitten by a snake! {pos} -> {snakes[pos]}")
                pos = snakes[pos]
            elif pos in ladders:
                print(f"Yay! {player} climbed a ladder! {positions[player] + dice} -> {ladders[pos]}")
                pos = ladders[pos]

            positions[player] = pos
            print(f"{player} is now at position {pos}\n")

            if pos == 100:
                winner = player
                break

    print(f"🎉 {winner} wins the game! Congratulations!")

if __name__ == "__main__":
    play_game()

