# Copyright (C) 2020 luna_koly
#
# An example of a machine that can subtract
# one unary number from another.


from turing import TuringMachine
from lnr import LNRState


ANY = None
KEEP = None

L = 'l'
R = 'r'
N = 'n'

B = '.'
l = '1'
X = 'X'


SUBTRACTION_ALPHABET = [
    B, l, X
]


class SubtractionState(LNRState):
    '''
    A state of a machine that can subtract
    one unary number from another. Expects '1..1 . 1..1 X'
    right after the caret position and the second sequence of ones
    must be less than the first one. Also the first sequence must be
    at leas 1 symbol long.
    '''
    def subtract(self):
        ITERATION = self.move_right_until(B, overstep=R).step_left() # junk

        X_CHECK = ITERATION.move_right_while(B, overstep=R).step_left() # junk

        END = (X_CHECK.on(X).new(L)
                .move_left_until(l, overstep=R).step_left() # junk
                .move_left_while(l, overstep=R)
        )

        (X_CHECK.on(l).new(R)
                .move_right_while(l, overstep=L)
                .drop(B, L)
                .move_left_while(l, overstep=R).step_left()
                .move_left_until(l, overstep=R).step_left()
                .drop(B, L)
                # .step_right()
                .on(ANY)
                .go(R, ITERATION) # junk
        )

        return END


class SubtractionMachine(TuringMachine):
    '''
    A machine that can subtract
    one unary number from another. Expects '1..1 . 1..1 X'
    right after the caret position and the second sequence of ones
    must be less than the first one. Also the first sequence must be
    at leas 1 symbol long.
    '''
    def __init__(self):
        super().__init__(SUBTRACTION_ALPHABET, SubtractionState)
        self.BEGIN.subtract().end()
