# Copyright (C) 2020 luna_koly
#
# This file defines the core elements of
# the turing machine constructor


class Action:
    '''
    Action is a way to describe the transition from one
    state to another.
    '''
    def __init__(self, step, state=None, symbol=None):
        self.symbol = symbol
        self.state = state
        self.step = step


class Slot:
    '''
    Slot as a helper object for constructing
    transitions. In fact, it's only purpose is
    to provide a simple `.on(SYMBOL).<do_something>()` API.
    '''
    def __init__(self, state, symbol):
        self.symbol = symbol
        self.state = state

    def apply(self, action):
        self.state[self.symbol] = action
        return action.state

    def cycle(self, step, symbol=None):
        '''
        Creates a cycling transition from a state
        into itself.
        '''
        return self.apply(Action(step, None, symbol))

    def new(self, step, symbol=None):
        '''
        Creates a transition to some new state.
        '''
        return self.apply(Action(step, self.state.state(), symbol))

    def go(self, step, state, symbol=None):
        '''
        Creates a transition to a particular state.
        '''
        return self.apply(Action(step, state, symbol))


class State:
    '''
    Describes a state)
    '''
    def __init__(self, machine, index, paths=None):
        self.machine = machine
        self.index = index
        self.paths = paths

        if paths == None:
            self.paths = {}

    def on(self, symbol):
        '''
        Returns a slot for constructing
        a transition from this state through
        the given symbol.
        '''
        return Slot(self, symbol)

    def __setitem__(self, symbol, action):
        '''
        Handles assignment of an action.
        If symbol is 'None', treats it as 'all'.
        If action's state is 'None', treats it as self.
        If action's symbol is 'None', treats it as 'keep current'.
        '''
        if action.state == None:
            action.state = self

        if symbol != None:
            self.paths[symbol] = action

            if action.symbol == None:
                action.symbol = symbol
        else:
            for each in self.machine.alphabet:
                if not each in self.paths:
                    # recursion
                    self[each] = Action(action.step, action.state, action.symbol)

    def state(self):
        '''
        Alias for machine.state().
        '''
        return self.machine.state()

    def apply(self, transform):
        '''
        Allows to chain functions that take
        a state as an argument with other state
        functions.

        E. g.: state.move_right_until('1')
                    .apply(<move_somewhere_particular>)
                    .drop('0')
        '''
        return transform(self)


class TuringMachine:
    '''
    Keeps track of allocated states.
    Encapsulates alphabet info.
    Knows where are the BEGIN, END states
    and has a TAPE representation.
    '''
    def __init__(self, alphabet, StateClass=State):
        '''
        StateClass is a prototype for all new States.
        Create your own with your machine logic (it's easier to
        describe it inside of State subclasses, not the machine ones).
        '''
        self.StateClass = StateClass
        self.alphabet = alphabet

        self.next_state_index = 0
        self.states = []

        # end is first to have index=0
        self.END = self.state()
        self.BEGIN = self.state()

        self.TAPE = '*'

    def state(self):
        '''
        Allocates a state within the machine.
        '''
        state = self.StateClass(self, self.next_state_index)
        self.next_state_index += 1
        self.states.append(state)
        return state
