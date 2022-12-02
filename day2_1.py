# AOC2022, Day 2 Challenge 1 - Rock Paper Scissors - success
# Your total score for the game so far is 14531
# This could be refactored a bit but not too shabby.

# Get game list

with open("data/rockPaperScissors.txt") as f:
    rps = f.read()

rps = rps.splitlines()

# Set game-related values in dicts

decryption_values = {
    "A": ["rock", 1],
    "B": ["paper", 2],
    "C": ["scissors", 3],
    "X": ["rock", 1],
    "Y": ["paper", 2],
    "Z": ["scissors", 3]
}

game_points = {
    "win": [6, "You won this round."],
    "lose": [0, "You lost this round."],
    "draw": [3, "This round was a draw."]
}

# Single round

def rps_round(p1, p2, game_score):
    p1_shape, p1_value = decryption_values[p1]
    p2_shape, p2_value = decryption_values[p2]

    if p2_shape == p1_shape:
        game_status = "draw"
    elif (p2_shape == "rock" and p1_shape == "scissors") or (p2_shape == "scissors" and p1_shape == "paper") or (p2_shape == "paper" and p1_shape == "rock"):
        game_status = "win"
    else:
        game_status = "lose"

    game_message = game_points[game_status][1]
    round_score = p2_value + game_points[game_status][0]
    game_score += round_score
    
    print("You played {} against {}.".format(p2_shape, p1_shape) + game_message)
    print("Your score for this round was {}".format(round_score))
    print("Your total score for the game so far is {}".format(game_score))

    return game_score

def play_rps():
    game_score = 0
    for game in rps:
        p1, p2 = game.split()
        game_score = rps_round(p1, p2, game_score)

play_rps()





