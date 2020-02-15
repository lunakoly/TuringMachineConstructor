# Copyright (C) 2020 luna_koly
#
# Instantiates the UniversalMachine and
# compiles it to files inside 'out/'.
#
# Uses files of other machines from 'out/'
# to construct the tape.


from universal import UniversalMachine

import compiler


TARGET = 'out/subtraction.utm'
# TARGET = 'out/flipper.utm'

machine = UniversalMachine()

with open(TARGET) as file:
	machine.TAPE = '* ' + file.readline().strip()


result = compiler.compile_dtm(machine, 'out/universal.dtm', blank='.')
