#!/usr/bin/env python3


def decide_rps(player1, player2):
    return 1

#1 is Player 1, 2 is Player 2

decide_rps = [("rock", "scissors"), ("scissors", "paper"), ("paper", "rock")]

def decide_rps(player1, player2):
    if player1 == player2:
        return "Tie"
    if ((player1, player2)) in decide_rps:
        return player1 + "wins"
    else:
        return player2 + "wins"

