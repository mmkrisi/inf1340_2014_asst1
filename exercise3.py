#!/usr/bin/env python3


def decide_rps(player1, player2):
    return 1

decide_rps = [("rock", "scissors"), ("scissors", "paper"), ("paper", "rock")]

def decide_rps(player1, player2):
    if player1 == player2:
        return "0"
    if ((player1, player2)) in decide_rps:
        return "1"
    else:
        return player2 + "2"

