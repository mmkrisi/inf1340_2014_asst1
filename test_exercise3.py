#!/usr/bin/env python3

import pytest
from exercise3 import decide_rps


def test_decide_rps():
    """
    Inputs that are the correct format and length
    """
    #assert decide_rps("Rock", "Paper") == 2
    #assert decide_rps("Scissors", "Scissors") == 0
    #assert decide_rps("Rock", "Scissors") == 1
    # other tests

    # Tie:
    assert decide_rps("Scissors", "Scissors") == 0
    assert decide_rps("Rock", "Rock") == 0
    assert decide_rps("Paper", "Paper") == 0

    # Win:
    assert decide_rps("Rock", "Scissors") == 1
    assert decide_rps("Scissors", "Paper") == 1
    assert decide_rps("Paper", "Rock") == 1

    # Loss:
    assert decide_rps("Rock", "Paper") == 2
    assert decide_rps("Paper", "Scissors") == 2
    assert decide_rps("Scissors", "Rock") == 2

def test_input():
    """
    Incorrect inputs
    """
    with pytest.raises(ValueError):
        #something here
        decide_rps("Apple", "Ball")
        decide_rps("Roc", "Papr")
        decide_rps("Scissors", "Papper")
        decide_rps("Ppr", "Scissors")
        decide_rps("", "Scissors")
        decide_rps("Rock", "")
    with pytest.raises(TypeError):
        decide_rps(2, 5)
        decide_rps("Rock", 12)
        decide_rps("Paper", 6.0)
        decide_rps(8.4, 12.2)
        decide_rps(9.5, "Paper")
        decide_rps("", "")
        decide_rps()
        decide_rps("", 12)