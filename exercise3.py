#!/usr/bin/env python3

def decide_rps(player1, player2):
    """Returns the result of the rock, paper, scissors game

    :param:
        player1 (string): the choice of player1
        player2 (string): the choice of player2
        The strings accepted are only "Rock", "Paper" and "Scissor"

    :return:
        int: the result of the choices between player1 and player2's in one game:
        If player 1 wins: 1
        If player 2 wins: 2
        If tie: 0

    :raises:
        TypeError if input is not one of the three strings given as choices for the game.
    """
    return 1

decide_rps = [("rock", "scissors"), ("scissors", "paper"), ("paper", "rock")]

def decide_rps(player1, player2):
    if player1 == player2:
        return "0"
    if ((player1, player2)) in decide_rps:
        return "1"
    else:
        return player2 + "2"


#Krisi
result_game_dictionary = {"Rock": 0, "Paper": 1, "Scissors": 2} # I remember we need to use dictionaries for this exercise.



