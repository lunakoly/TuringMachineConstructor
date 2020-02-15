# Copyright (C) 2020 luna_koly
#
# Instantiates the FlipperMachine and
# compiles it to files inside 'out/'


from flipper import FlipperMachine

import compiler


machine = FlipperMachine()
machine.TAPE = '. . * . . X . X . Y . Y . X . Y . Y Y . X . . X X'


result = compiler.compile_dtm(machine, 'out/flipper.dtm', blank='.')
result = compiler.compile_turing(machine, 'out/flipper.utm')
