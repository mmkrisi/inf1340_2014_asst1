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

    # make a dictionary, giving an int value to the type of choice
    result_game_dictionary = {"Rock": 1, "Paper": 2, "Scissors": 3}
    #the logic is to apply mathematics when deciding who wins in each of the 9 possible outcomes
    #check whether the input is a string
    if type(player1) and type(player2) is not str:
        #return a TypeError when the input is not a string
        raise TypeError("Invalid type")
    else:
        #check that the input is one of the three possible choices
        if player1 in result_game_dictionary:
            #asign the value corresponding to the choice as per the dictionary
            player1_choice = result_game_dictionary[player1]
        else:
            #return a ValueError when invalid string input for Player1
            raise ValueError("The value for Player1 is incorrect")
        #check that the input is one of the three possible choices
        if player2 in result_game_dictionary:
            #asign the value corresponding to the choice as per the dictionary
            player2_choice = result_game_dictionary[player2]
            #check the combination through mathematical logic to find the winning Player
            game_result = player1_choice - player2_choice
            if game_result == 0:
                return 0
            elif game_result == -2 or game_result == 1:
                return 1
            elif game_result == -1 or game_result == 2:
                return 2
            else:
                #return a ValueError when invalid string input for Player2
                raise ValueError("The value for Player2 is incorrect")


