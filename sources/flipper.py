# Copyright (C) 2020 luna_koly
#
# A simple example of a machine that
# always goes right and prints either 'X'
# or 'Y' depending on which one of these
# it saw the last time.


from turing import TuringMachine
from lnr import LNRState


ANY = None
KEEP = None

L = 'l'
R = 'r'
N = 'n'

B = '.'
X = 'X'
Y = 'Y'


FLIPPER_ALPHABET = [
    B, X, Y
]


class FlipperState(LNRState):
    '''
    A state of a machine that
    always goes right and prints either 'X'
    or 'Y' depending on which one of these
    it saw the last time.
    '''
    def start_flips(self):
        PRINT_X = self
        PRINT_Y = self.state()

        PRINT_X.on(ANY).cycle(R, X)
        PRINT_X.on(Y).go(R, PRINT_Y)

        PRINT_Y.on(ANY).cycle(R, Y)
        PRINT_Y.on(X).go(R, PRINT_X)


class FlipperMachine(TuringMachine):
    '''
    A machine that
    always goes right and prints either 'X'
    or 'Y' depending on which one of these
    it saw the last time.
    '''
    def __init__(self):
        super().__init__(FLIPPER_ALPHABET, FlipperState)
        self.BEGIN.start_flips()
