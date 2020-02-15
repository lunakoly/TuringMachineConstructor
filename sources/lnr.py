# Copyright (C) 2020 luna_koly
#
# This file defines an LNRMachine - the one
# that describes it's movement via 'l', 'n', and 'r'
# step symbols (in a particular TM simulator).
#
# LNRMachine contains several commonly used
# complex transition building methods within the
# LNRState.


from turing import State


ANY = None
KEEP = None

L = 'l'
R = 'r'
N = 'n'


class LNRState(State):
    '''
    A state of a machine that can describe
    its movement direction via 'l', 'n' and 'r'.
    '''
    def move_while(self, condition, direction, overstep=N):
        self.on(condition).cycle(direction)
        STOP = self.on(ANY).new(overstep)
        return STOP

    def move_left_while(self, condition, overstep=N):
        return self.move_while(condition, L, overstep)

    def move_right_while(self, condition, overstep=N):
        return self.move_while(condition, R, overstep)

    def move_until(self, condition, direction, overstep=N):
        self.on(ANY).cycle(direction)
        STOP = self.on(condition).new(overstep)
        return STOP

    def move_left_until(self, condition, overstep=N):
        return self.move_until(condition, L, overstep)

    def move_right_until(self, condition, overstep=N):
        return self.move_until(condition, R, overstep)

    def step(self, direction, symbol=KEEP):
        NEXT = self.on(ANY).new(direction, symbol)
        return NEXT

    def step_left(self, symbol=KEEP):
        return self.step(L, symbol)

    def step_right(self, symbol=KEEP):
        return self.step(R, symbol)

    def drop(self, symbol, direction=N):
        NEXT = self.on(ANY).new(direction, symbol)
        return NEXT

    def end(self):
        # self.on(ANY).go(N, self.machine.END)
        # dtm doesn't support N
        self.step_left().on(ANY).go(R, self.machine.END) # junk
