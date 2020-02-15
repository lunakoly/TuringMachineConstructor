# About
This code is an API for defining turing machines.

Special thanks to _Undumendil_ for providing a turing machine implementation: https://github.com/Undumendil/tm. A Compiled version of `tm` is available under `out/tm` (compiled via Ubuntu on Windows).


# Example
## Running *subtraction.dtm*:
`$ tm subtraction.dtm --fast`

for tape:
```
. . . . * 1 1 1 1 1 . 1 1 1 X . .
```
results in:
```
. . . . . . . . . . . . . . . . 1 1 . . . . . . . X . . . . . .
```

## Running *universal.dtm*:
`$ tm universal.dtm --fast`

for tape stored in `subtraction.utm`
results in:
```
. . . . . . . . . . . . . . . . M I Qin 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 Sin 0 0 Sout 0 0 Qout 1 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 r I Qin 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 Sin 1 0 Sout 1 0 Qout 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 r I Qin 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 Sin 1 1 Sout 1 1 Qout 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 r I Qin 1 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 Sin 0 0 Sout 0 0 Qout 1 1 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 l I Qin 1 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 Sin 1 0 Sout 1 0 Qout 1 1 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 l I Qin 1 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 Sin 1 1 Sout 1 1 Qout 1 1 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 l I Qin 1 1 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 Sin 0 0 Sout 0 0 Qout 1 1 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 r I Qin 1 1 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 Sin 1 0 Sout 1 0 Qout 1 1 1 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 r I Qin 1 1 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 Sin 1 1 Sout 1 1 Qout 1 1 1 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 r I Qin 1 1 1 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 Sin 0 0 Sout 0 0 Qout 1 1 1 1 1 0 0 0 0 0 0 0 0 0 0 0 0 0 l I Qin 1 1 1 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 Sin 1 0 Sout 1 0 Qout 1 1 1 1 1 0 0 0 0 0 0 0 0 0 0 0 0 0 l I Qin 1 1 1 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 Sin 1 1 Sout 1 1 Qout 1 1 1 1 1 0 0 0 0 0 0 0 0 0 0 0 0 0 l I Qin 1 1 1 1 1 0 0 0 0 0 0 0 0 0 0 0 0 0 Sin 1 1 Sout 1 1 Qout 1 1 1 1 1 1 0 0 0 0 0 0 0 0 0 0 0 0 l I Qin 1 1 1 1 1 0 0 0 0 0 0 0 0 0 0 0 0 0 Sin 1 0 Sout 1 0 Qout 1 1 1 1 1 1 1 1 1 1 0 0 0 0 0 0 0 0 r I Qin 1 1 1 1 1 1 0 0 0 0 0 0 0 0 0 0 0 0 Sin 0 0 Sout 0 0 Qout 1 1 1 1 1 1 0 0 0 0 0 0 0 0 0 0 0 0 l I Qin 1 1 1 1 1 1 0 0 0 0 0 0 0 0 0 0 0 0 Sin 1 0 Sout 1 0 Qout 1 1 1 1 1 1 1 0 0 0 0 0 0 0 0 0 0 0 r I Qin 1 1 1 1 1 1 0 0 0 0 0 0 0 0 0 0 0 0 Sin 1 1 Sout 1 1 Qout 1 1 1 1 1 1 0 0 0 0 0 0 0 0 0 0 0 0 l I Qin 1 1 1 1 1 1 1 0 0 0 0 0 0 0 0 0 0 0 Sin 0 0 Sout 0 0 Qout 1 1 1 1 1 1 1 1 0 0 0 0 0 0 0 0 0 0 l I Qin 1 1 1 1 1 1 1 0 0 0 0 0 0 0 0 0 0 0 Sin 1 0 Sout 1 0 Qout 1 1 1 1 1 1 1 1 0 0 0 0 0 0 0 0 0 0 l I Qin 1 1 1 1 1 1 1 0 0 0 0 0 0 0 0 0 0 0 Sin 1 1 Sout 1 1 Qout 1 1 1 1 1 1 1 1 0 0 0 0 0 0 0 0 0 0 l I Qin 1 1 1 1 1 1 1 1 0 0 0 0 0 0 0 0 0 0 Sin 1 0 Sout 1 0 Qout 1 1 1 1 1 1 1 1 0 0 0 0 0 0 0 0 0 0 l I Qin 1 1 1 1 1 1 1 1 0 0 0 0 0 0 0 0 0 0 Sin 0 0 Sout 0 0 Qout 1 1 1 1 1 1 1 1 1 0 0 0 0 0 0 0 0 0 r I Qin 1 1 1 1 1 1 1 1 0 0 0 0 0 0 0 0 0 0 Sin 1 1 Sout 1 1 Qout 1 1 1 1 1 1 1 1 1 0 0 0 0 0 0 0 0 0 r I Qin 1 1 1 1 1 1 1 1 1 0 0 0 0 0 0 0 0 0 Sin 0 0 Sout 0 0 Qout 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 l I Qin 1 1 1 1 1 1 1 1 1 0 0 0 0 0 0 0 0 0 Sin 1 0 Sout 1 0 Qout 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 l I Qin 1 1 1 1 1 1 1 1 1 0 0 0 0 0 0 0 0 0 Sin 1 1 Sout 1 1 Qout 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 l I Qin 1 1 1 1 1 1 1 1 1 1 0 0 0 0 0 0 0 0 Sin 1 0 Sout 1 0 Qout 1 1 1 1 1 1 1 1 1 1 0 0 0 0 0 0 0 0 r I Qin 1 1 1 1 1 1 1 1 1 1 0 0 0 0 0 0 0 0 Sin 0 0 Sout 0 0 Qout 1 1 1 1 1 1 1 1 1 1 1 0 0 0 0 0 0 0 l I Qin 1 1 1 1 1 1 1 1 1 1 0 0 0 0 0 0 0 0 Sin 1 1 Sout 1 1 Qout 1 1 1 1 1 1 1 1 1 1 1 0 0 0 0 0 0 0 l I Qin 1 1 1 1 1 1 1 1 1 1 1 0 0 0 0 0 0 0 Sin 0 0 Sout 0 0 Qout 1 1 1 1 1 1 1 1 1 1 1 1 0 0 0 0 0 0 l I Qin 1 1 1 1 1 1 1 1 1 1 1 0 0 0 0 0 0 0 Sin 1 0 Sout 0 0 Qout 1 1 1 1 1 1 1 1 1 1 1 1 0 0 0 0 0 0 l I Qin 1 1 1 1 1 1 1 1 1 1 1 0 0 0 0 0 0 0 Sin 1 1 Sout 0 0 Qout 1 1 1 1 1 1 1 1 1 1 1 1 0 0 0 0 0 0 l I Qin 1 1 1 1 1 1 1 1 1 1 1 1 0 0 0 0 0 0 Sin 1 0 Sout 1 0 Qout 1 1 1 1 1 1 1 1 1 1 1 1 0 0 0 0 0 0 l I Qin 1 1 1 1 1 1 1 1 1 1 1 1 0 0 0 0 0 0 Sin 0 0 Sout 0 0 Qout 1 1 1 1 1 1 1 1 1 1 1 1 1 0 0 0 0 0 r I Qin 1 1 1 1 1 1 1 1 1 1 1 1 0 0 0 0 0 0 Sin 1 1 Sout 1 1 Qout 1 1 1 1 1 1 1 1 1 1 1 1 1 0 0 0 0 0 r I Qin 1 1 1 1 1 1 1 1 1 1 1 1 1 0 0 0 0 0 Sin 0 0 Sout 0 0 Qout 1 1 1 1 1 1 1 1 1 1 1 1 1 1 0 0 0 0 l I Qin 1 1 1 1 1 1 1 1 1 1 1 1 1 0 0 0 0 0 Sin 1 0 Sout 1 0 Qout 1 1 1 1 1 1 1 1 1 1 1 1 1 1 0 0 0 0 l I Qin 1 1 1 1 1 1 1 1 1 1 1 1 1 0 0 0 0 0 Sin 1 1 Sout 1 1 Qout 1 1 1 1 1 1 1 1 1 1 1 1 1 1 0 0 0 0 l I Qin 1 1 1 1 1 1 1 1 1 1 1 1 1 1 0 0 0 0 Sin 0 0 Sout 0 0 Qout 1 1 1 1 1 1 1 1 1 1 1 1 1 1 0 0 0 0 l I Qin 1 1 1 1 1 1 1 1 1 1 1 1 1 1 0 0 0 0 Sin 1 0 Sout 1 0 Qout 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 0 0 0 r I Qin 1 1 1 1 1 1 1 1 1 1 1 1 1 1 0 0 0 0 Sin 1 1 Sout 1 1 Qout 1 1 1 1 1 1 1 1 1 1 1 1 1 1 0 0 0 0 l I Qin 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 0 0 0 Sin 0 0 Sout 0 0 Qout 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 0 0 l I Qin 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 0 0 0 Sin 1 0 Sout 1 0 Qout 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 0 0 l I Qin 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 0 0 0 Sin 1 1 Sout 1 1 Qout 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 0 0 l I Qin 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 0 0 Sin 0 0 Sout 0 0 Qout 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 0 l I Qin 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 0 0 Sin 1 0 Sout 0 0 Qout 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 0 l I Qin 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 0 0 Sin 1 1 Sout 0 0 Qout 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 0 l I Qin 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 0 Sin 0 0 Sout 0 0 Qout 1 1 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 r I Qin 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 0 Sin 1 0 Sout 1 0 Qout 1 1 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 r I Qin 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 0 Sin 1 1 Sout 1 1 Qout 1 1 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 r I Qin 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 Sin 0 0 Sout 0 0 Qout 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 r I Qin 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 Sin 1 0 Sout 1 0 Qout 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 r I Qin 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 Sin 1 1 Sout 1 1 Qout 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 r Q 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 T S 0 0 S 0 0 S 0 0 S 0 0 ^ S 1 0 S 1 0 S 0 0 S 0 0 S 0 0 S 0 0 S 0 0 S 0 0 S 0 0 S 1 1 S 0 0 S 0 0 . . . .
```
Where `S 0 0` is `.`, `S 1 0` is `1` and `S 1 1` is `X`.
Notice that takes *79455398* steps to finish.


# Docs


## class `Action`
Action is a way to describe the transition from one state to another.

Defined in `turing.py`


## class `Slot`
Slot as a helper object for constructing
transitions. In fact, it's only purpose is
to provide a simple `.on(SYMBOL).<do_something>()` API.

Defined in `turing.py`

### function `cycle(self, step, symbol=None)`
Creates a cycling transition from a state
into itself.

### function `new(self, step, symbol=None)`
Creates a transition to some new state.

### function `go(self, step, state, symbol=None)`
Creates a transition to a particular state.


## class `State`
Describes a state)

Defined in `turing.py`

### function `on(self, symbol)`
Returns a slot for constructing
a transition from this state through
the given symbol.

### function `state(self)`
Alias for machine.state().

### function `apply(self, transform)`
Allows to chain functions that take
a state as an argument with other state
functions.

E. g.: 
```python
state.move_right_until('1')
     .apply(<move_somewhere_particular>)
     .drop('0')
```


## class `TuringMachine`
Keeps track of allocated states.
Encapsulates alphabet info.
Knows where are the `BEGIN`, `END` states
and has a `TAPE` representation.

Defined in `turing.py`

### function `state(self)`
Allocates a state within the machine.


## class `LNRState`
A state of a machine that can describe
its movement direction via 'l', 'n' and 'r'.

Defined in `lnr.py`

### Helpers
```
move_while(self, condition, direction, overstep=N)

move_left_while(self, condition, overstep=N)

move_right_while(self, condition, overstep=N)

move_until(self, condition, direction, overstep=N)

move_left_until(self, condition, overstep=N)

move_right_until(self, condition, overstep=N)

step(self, direction, symbol=KEEP)

step_left(self, symbol=KEEP)

step_right(self, symbol=KEEP)

drop(self, symbol, direction=N)

end(self)
```


## module `Compiler`
Helper functions for turning a TM
description into a particular text representation.

Defined as `compiler.py`

### function `save(filename, data, task)`
Writes the `data` to the `filename` and
logs messages with `task` prefix.

### function `compile_dtm(machine, file=None, blank='_')`
Compiles a machine into the representation
that can be used by Danya's turing machine
implementation.

### function `compile_turing(machine, file=None)`
Compiles a machine into the representation
that the universal turing machine (`universal.py`)
can handle. Don't forget about putting enough symbols
on the tape before compiling!
