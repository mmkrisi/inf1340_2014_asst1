#!/usr/bin/env python3


def decide_rps(player1, player2):
    """Returns the result of the rock, paper, scissors game

    :param:
        player1 (string): the choice of player1
        player2 (string): the choice of player2
        The strings accepted are only "Rock", "Paper" and "Scissor"

    :return:
        int: the result of the choices between player1 and player2's in one game:
        If player 1 wins: return 1
        If player 2 wins: return 2
        If tie: return 0

    :raises:
        ValueError if input is not one of the three strings given as choices for the game.
        ValueError if input is not a string.
    """

    # decide_rps = [("rock", "scissors"), ("scissors", "paper"), ("paper", "rock")]
    # def decide_rps(player1, player2):
    #     if player1 == player2:
    #         return "0"
    #     if ((player1, player2)) in decide_rps:
    #         return "1"
    #     else:
    #         return "2"

    # #Krisi's version of the code:

    available_player_choices = ["Rock", "Paper", "Scissors"] #make a list of the three possible players' choices
    result_game_dictionary = {"Rock": 1, "Paper": 2, "Scissors": 3} #make a dictionary, giving an int value to the type of choice
    #the logic is to apply mathematics when deciding who wins in each of the 9 possible outcomes

    if type (player1) and type (player2) is not str: #check whether the input is a string
        raise TypeError("Invalid type") #return a TypeError when the input is not a string
    else:
        if player1 in available_player_choices: #check that the input is one of the three possible choices
            player1_choice = result_game_dictionary[player1] #asign the value corresponding to the choice as per the dictionary
        else:
            raise ValueError("The value for Player1 is incorrect") #return a ValueError when invalid string input for Player1
        if player2 in available_player_choices: #check that the input is one of the three possible choices
            player2_choice = result_game_dictionary[player2] #asign the value corresponding to the choice as per the dictionary
            game_result = player1_choice - player2_choice #check the combination through mathematical logic to find the winning Player
            if game_result == 0: #check tie
                return 0
            elif game_result == -2 or game_result == 1:
                return 1
            elif game_result == -1 or game_result == 2:
                return 2
            else:
                raise ValueError("The value for Player2 is incorrect") #return a ValueError when invalid string input for Player2


