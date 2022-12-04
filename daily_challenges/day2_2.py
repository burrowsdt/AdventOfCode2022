# AOC2022, Day 2 Challenge 2 - Rock Paper Scissors pt 2
# success -- Total game score is now 11258

# Get game list

with open("data/rockPaperScissors.txt") as f:
    rps = f.read()

rps = rps.splitlines()

# Set game-related values in dicts

rps_values = {
    "A": ["rock", 1],
    "B": ["paper", 2],
    "C": ["scissors", 3],
    "X": ["lose"],
    "Y": ["draw"],
    "Z": ["win"],
}

game_points = {
    "win": 6,
    "lose": 0,
    "draw": 3,
    "rock": 1,
    "paper": 2,
    "scissors": 3
}

play_chart = {
    "rock": {
        "win": "paper",
        "lose": "scissors",
        "draw": "rock"
    },
    "scissors": {
        "win": "rock",
        "lose": "paper",
        "draw": "scissors"
    },
    "paper": {
        "win": "scissors",
        "lose": "rock",
        "draw": "paper"
    }
}

# A single round

def rps_round(p1, p2, game_score):
    p1_shape, p1_value = rps_values[p1]
    p2_goal = rps_values[p2][0]
    game_status = p2_goal

    # Use play_chart to determine p2_shape and p2_value
    p2_shape = play_chart[p1_shape][p2_goal]
    p2_value = game_points[p2_shape]
    game_message = "Requested a {}. P1 = {}. P2 chose {}.".format(p2_goal, p1_shape, p2_shape)

    round_score = p2_value + game_points[game_status]
    game_score += round_score

    final_score_message = "P2 earned {} for the round. Total game score is now {}.".format(round_score, game_score)
    print(game_message)
    print(final_score_message)

    return game_score
    
def play_rps():
    game_score = 0
    for game in rps:
        p1, p2 = game.split()
        game_score = rps_round(p1, p2, game_score)

play_rps()




