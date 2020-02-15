# Copyright (C) 2020 luna_koly
#
# Helper functions for turning a TM
# description into a particular text representation.


from turing import *
import math


def save(filename, data, task):
    '''
    Writes the `data` to the `filename` and
    logs messages with `task` prefix.
    '''
    with open(filename, 'w') as file:
        print(f'[{task}] Writing...')
        file.write(data)
        print(f'[{task}] Written.')


def compile_dtm(machine, file=None, blank='_'):
    '''
    Compiles a machine into the representation
    that can be used by Danya's turing machine
    implementation.
    '''
    print('[DTM] Compiling...')

    result = '[:] q' + str(machine.BEGIN.index) + '\n'
    result += '[.] q0\n\n'

    for it in machine.states:
        for that in it.paths:
            action = it.paths[that]

            start = it.index
            end = action.state.index

            was = that
            now = action.symbol

            step = action.step

            result += 'q{} {} -> q{} {} {}\n'.format(start, was, end, now, step)

    result += '\n=-=-=\n'
    result += 'inf~-1: ' + blank + '\n'
    result +=  '0~inf: ' + blank + '\n'

    parts  = machine.TAPE.split('*')
    before_text = parts[0].strip()
    after_text  = parts[1].strip()
    before = before_text.split(' ')
    after  = after_text.split(' ')

    if len(before_text) > 0:
        result += str(0 - len(before)) + '~-1: ' + ' '.join(before) + '\n'

    if len(after_text) > 0:
        result += '0: ' + ' '.join(after) + '\n'

    print('[DTM] Compiled.')

    if file != None:
        save(file, result, 'DTM')

    return result


def compile_turing(machine, file=None):
    '''
    Compiles a machine into the representation
    that the universal turing machine (`universal.py`)
    can handle. Don't forget about putting enough symbols
    on the tape before compiling!
    '''
    print('[Turing] Compiling...')

    result = 'M'

    def to_index(number, count):
        return ' 1' * number + ' 0' * (count - number - 1)

    states_count  = len(machine.states)
    symbols_count = len(machine.alphabet)

    for it in machine.states:
        for that in it.paths:
            action = it.paths[that]

            start = to_index(it.index, states_count)
            end = to_index(action.state.index, states_count)

            was = to_index(machine.alphabet.index(that), symbols_count)
            now = to_index(machine.alphabet.index(action.symbol), symbols_count)

            step = action.step

            result += ' I Qin{} Sin{} Sout{} Qout{} {}'.format(start, was, now, end, step)

    result += ' Q{} T '.format(to_index(machine.BEGIN.index, states_count))

    parts  = machine.TAPE.split('*')
    before_text = parts[0].strip()
    after_text  = parts[1].strip()
    before = before_text.split(' ')
    after  = after_text.split(' ')

    if len(before_text) > 0:
        for each in before:
            symbol = to_index(machine.alphabet.index(each), symbols_count)
            result += 'S{} '.format(symbol)

    result += '^'

    if len(after_text) > 0:
        for each in after:
            symbol = to_index(machine.alphabet.index(each), symbols_count)
            result += ' S{}'.format(symbol)

    print('[Turing] Compiled.')

    if file != None:
        save(file, result, 'Turing')

    return result
