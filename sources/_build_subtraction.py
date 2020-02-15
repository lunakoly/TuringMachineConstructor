# Copyright (C) 2020 luna_koly
#
# Instantiates the SubtractionMachine and
# compiles it to files inside 'out/'


from subtraction import SubtractionMachine

import compiler


machine = SubtractionMachine()
machine.TAPE = '. . . . * 1 1 1 1 1 . 1 1 1 X . .'


result = compiler.compile_dtm(machine, 'out/subtraction.dtm', blank='.')
result = compiler.compile_turing(machine, 'out/subtraction.utm')
