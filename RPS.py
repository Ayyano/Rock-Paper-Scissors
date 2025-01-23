import random

def player(prev_play, opponent_history=[]):
    if prev_play:
        opponent_history.append(prev_play)

    # Default to random move if no history
    if not opponent_history:
        return random.choice(["R", "P", "S"])

    # Frequency analysis strategy
    move_counts = {"R": 0, "P": 0, "S": 0}
    for move in opponent_history:
        move_counts[move] += 1

    most_frequent_move = max(move_counts, key=move_counts.get)

    # Counter the opponent's most frequent move
    if most_frequent_move == "R":
        return "P"
    elif most_frequent_move == "P":
        return "S"
    else:
        return "R"
