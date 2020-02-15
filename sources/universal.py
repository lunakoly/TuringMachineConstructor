# Copyright (C) 2020 luna_koly
#
# An example of a possible universal
# turing machine implementation.
#
# The structure of the machine is: '... M <instruction>+ <current state> T <symbol>* ^ <symbol>* ...'
# with caret initial position:          ^
#
# <id> = 1..1 0..0
#     Must contain at leas one digit.
#
# <instruction> = I Qin <id> Sin <id> Sout <id> Qout <id> <direction>
#     <direction> = l, n or r
#
# <current state> = Q <id>
#
# <symbol> = S <id>
#
# It's required that a simulated program could finish without
# any errors like an attempt to running an instruction that hasn't been
# defined. It's also important that the caret must not attempt to go
# left over T or right over the last symbol because I was too tired to implement
# tape shifting.


from turing import TuringMachine
from lnr import LNRState


ANY = None
KEEP = None

L = 'l'
R = 'r'
N = 'n'

l = '1'
lx = '1x'

O = '0'

I = 'I'
Ix = 'Ix'

Q = 'Q'
Qi = 'Qin'
Qo = 'Qout'

S = 'S'
Si = 'Sin'
So = 'Sout'

T = 'T'
M = 'M'
B = '.'
C = '^'


UNIVERSAL_ALPHABET = [
	L, R, N,
	l, lx,
	O,
	I, Ix,
	Q, Qi, Qo,
	S, Si, So,
	M,
	T,
	B,
	C
]


class UniversalState(LNRState):
	'''
	A state of a universal turing machine that starts with
	the caret positioned at 'M' and
	'''
	def seek_unchecked_Qin(self):
		return (self
				.move_left_until(M, overstep=R)
				.move_right_until(I, overstep=R) # we're at Qin
				.step_right()
		)

	def seek_unchecked_Sin(self):
		return (self
				.move_left_until(M, overstep=R)
				.move_right_until(I, overstep=R) # we're at Qin
				.move_right_until(Si, overstep=R)
		)

	def seek_unchecked_Sout(self):
		return (self
				.move_left_until(M, overstep=R)
				.move_right_until(I, overstep=R) # we're at Qin
				.move_right_until(So, overstep=R)
		)

	def seek_unchecked_Qout(self):
		return (self
				.move_left_until(M, overstep=R)
				.move_right_until(I, overstep=R) # we're at Qin
				.move_right_until(Qo, overstep=R)
		)

	def mark_next_lx(self):
		SHOULD_MARK = (self
				.move_right_while(lx, overstep=R)
				.step_left()
		)

		STOP = SHOULD_MARK.on(l).new(R, lx).step_left()
		SHOULD_MARK.on(ANY).new(R).on(ANY).go(L, STOP)
		return STOP

	def clear_lx(self):
		BACKWARD = self.move_right_while(lx, overstep=L)
		BACKWARD.on(lx).cycle(L, l)
		STOP = BACKWARD.on(ANY).new(R)
		return STOP

	def compare(self, to_left, to_right):
		SUCCESS = self.state()
		FAILURE = self.state()

		RIGHT_FAILED = self.state()
		(RIGHT_FAILED
				.clear_lx()
				.apply(to_left)
				.clear_lx()
				.step_right()
				.on(ANY)
				.go(L, FAILURE)
		)

		CHECK_LEFT_END = self.mark_next_lx()

		CHECK_RIGHT_END = (CHECK_LEFT_END.on(lx).new(R)
				.apply(to_right)
				.mark_next_lx()
		)

		(CHECK_RIGHT_END.on(lx).new(L)
				.apply(to_left)
				.step_left()
				.on(ANY)
				.go(R, self)
		)

		CHECK_RIGHT_END.on(ANY).new(R).on(ANY).go(L, RIGHT_FAILED)

		CHECK_RIGHT_END_2 = (CHECK_LEFT_END.on(ANY).new(R)
				.apply(to_right)
				.mark_next_lx()
		)

		CHECK_RIGHT_END_2.on(lx).new(R).on(ANY).go(L, RIGHT_FAILED)

		(CHECK_RIGHT_END_2.on(ANY).new(L)
				.clear_lx()
				.apply(to_left)
				.clear_lx()
				.step_right()
				.on(ANY)
				.go(L, SUCCESS)
		)

		return (SUCCESS, FAILURE)

	def mark_instruction(self):
		return (self
				.move_left_until(I, overstep=R)
				.step_left()
				.drop(Ix, R)
		)

	def zero_out(self):
		self.on(l).cycle(R, O)
		self.on(lx).cycle(R, O)
		STOP = self.on(ANY).new(L)
		return STOP

	def append_l(self):
		return (self
				.move_right_while(l, overstep=L)
				.step_right()
				.drop(l, R)
		)

	def copy(self, to_left, to_right):
		REPEAT = self.apply(to_right).zero_out()

		CHECK = REPEAT.apply(to_left).mark_next_lx()

		(CHECK.on(lx).new(R)
				.apply(to_right)
				.append_l()
				.on(ANY)
				.go(L, REPEAT)
		)

		END = CHECK.on(ANY).new(R).apply(to_left)
		return END

	def move_to_direction_instruction(self):
		self.on(ANY).cycle(R)
		STOP = self.on(L).new(R).step_left()
		self.on(N).new(R).on(ANY).go(L, STOP)
		self.on(R).new(R).on(ANY).go(L, STOP)
		return STOP

	def apply_direction(self):
		DONE = self.state()
		CHECK_DIRECTION = self.move_to_direction_instruction()

		RIGHT_CHECK_S_ZERO = (CHECK_DIRECTION.on(R).new(R)
				.move_right_until(C, overstep=R)
				.step_left()
				.drop(S, R)
				.step_right()
		)

		(RIGHT_CHECK_S_ZERO.on(O).new(L)
				.drop(O, R)
				.move_right_until(S, overstep=L)
				.drop(C, L)
				.on(ANY)
				.go(R, DONE)
		)

		(RIGHT_CHECK_S_ZERO.on(l).new(L)
			   .drop(l, R)
			   .move_right_while(l, overstep=L)
			   .drop(O, L)
			   .move_right_until(S, overstep=L)
			   .drop(C, L)
			   .on(ANY)
			   .go(R, DONE)
		)

		LEFT_CHECK_S_ZERO = (CHECK_DIRECTION.on(L).new(R)
				.move_right_until(C, overstep=L)
				.move_left_until(S, overstep=R)
		)

		(LEFT_CHECK_S_ZERO.on(O).new(R)
				.step_left()
				.drop(S, L)
				.drop(C, R)
				.move_right_until(C, overstep=R)
				.step_left()
				.drop(O, L)
				.on(ANY)
				.go(R, DONE)
		)

		(LEFT_CHECK_S_ZERO.on(l).new(R)
				.move_right_until(C, overstep=R)
				.step_left()
				.drop(O, L)
				.move_left_until(S, overstep=R)
				.move_right_while(l, overstep=R)
				.step_left()
				.drop(l, L)
				.move_left_until(S, overstep=R)
				.drop(S, L)
				.drop(C, R)
				.on(ANY)
				.go(R, DONE)
		)

		(CHECK_DIRECTION.on(ANY).new(L)
						.move_right_until(T, overstep=R)
						.step_left()
						.on(ANY)
						.go(R, DONE)
		)

		return DONE

	def reset(self):
		self.on(ANY).cycle(L)
		self.on(lx).cycle(L, l)
		self.on(Ix).cycle(L, I)
		STOP = self.on(M).new(R)
		return STOP

	def work(self):
		GO_TO_CHECK = self.on(ANY).new(R)
		CHECK_END = GO_TO_CHECK.move_right_until(Q, overstep=R)

		to_left_Qi = lambda self: self.seek_unchecked_Qin()
		to_right_Q = lambda self: self.move_right_until(Q, overstep=R)

		SUCCESS_Q, FAILURE_Q = (CHECK_END.on(l).new(L)
				.seek_unchecked_Qin()
				.compare(to_left_Qi, to_right_Q)
		)

		(FAILURE_Q
				.mark_instruction()
				.on(ANY)
				.go(R, GO_TO_CHECK)
		)

		to_left_Si = lambda self: self.seek_unchecked_Sin()
		to_right_S = lambda self: self.move_right_until(C, overstep=R).step_right()

		SUCCESS_S, FAILURE_S = (SUCCESS_Q
				.seek_unchecked_Sin()
				.compare(to_left_Si, to_right_S)
		)

		(FAILURE_S
				.mark_instruction()
				.on(ANY)
				.go(R, GO_TO_CHECK)
		)

		to_left_So = lambda self: self.seek_unchecked_Sout()
		to_left_Qo = lambda self: self.seek_unchecked_Qout()

		(SUCCESS_S
				.move_right_until(So, overstep=R)
				.copy(to_left_So, to_right_S)
				.move_right_until(Qo, overstep=R)
				.copy(to_left_Qo, to_right_Q)
				.apply_direction()
				.reset()
				.on(ANY)
				.go(R, GO_TO_CHECK)
		)

		(CHECK_END.on(ANY).new(R)
				.move_left_until(M, overstep=R)
				.step_left()
				.end()
		)


class UniversalMachine(TuringMachine):
	'''
	A universal turing machine that starts with
	the caret positioned at 'M' and
	'''
	def __init__(self):
		super().__init__(UNIVERSAL_ALPHABET, UniversalState)
		self.BEGIN.work()
