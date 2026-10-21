#! /usr/bin/python3

# (C) 2026 by Folkert van Heusden <folkert@vanheusden.com>
# License: CC0

import json
import sys

from bus_test import bus_test
from cpu_6510 import cpu_6510

bus = bus_test(False)
bus.reset()
cpu = cpu_6510(bus)

errors = False

j = json.loads(open(sys.argv[1]).read())
for test in j:
    bus.reset()
    cpu.reset()

    initial = test['initial']
    cpu.pc = initial['pc']
    cpu.sp = initial['s']
    cpu.a = initial['a']
    cpu.x = initial['x']
    cpu.y = initial['y']
    cpu.p = initial['p']
    for entry in initial['ram']:
        bus.ram.write(entry[0], entry[1])

    if cpu.tick() == False:
        print(f'test {test["name"]}: opcode not implemented')
        sys.exit(1)

    def ma(a, b, name, test_name):
        if a != b:
            if type(a) == str:
                print(f'test {test_name}, mismatch for {name}: expected {b}, got {a}')
            else:
                print(f'test {test_name}, mismatch for {name}: expected {b:02x} ({b}), got {a:02x} ({a})')
            global errors
            errors = True

    test_name = test['name']

    final = test['final']
    ma(cpu.pc, final['pc'], 'pc', test_name)
    ma(cpu.sp, final['s'], 'sp', test_name)
    ma(cpu.a, final['a'], 'a', test_name)
    ma(cpu.x, final['x'], 'x', test_name)
    ma(cpu.y, final['y'], 'y', test_name)
    # ma(cpu.p, final['p'], 'p', test_name)
    for entry in final['ram']:
        ma(bus.ram.read(entry[0]), entry[1], f'RAM:{entry[0]:04x}', test_name)
    cycles = test['cycles']
    #n_cycles = len(cycles)
    #ma(len(bus.actions) - 2, n_cycles, 'cycles', test_name)
    #for c in range(n_cycles):
    #    cur_action = bus.actions[c + 2]
    #    cmp_cycle = cycles[c]
    #    ma(cur_action[0], cmp_cycle[0], 'cycles:addr', test_name)
    #    ma(cur_action[1], cmp_cycle[1], 'cycles:value', test_name)
    #    ma(cur_action[2], cmp_cycle[2], 'cycles:action', test_name)
    def verify_cycles_simplified(a, b, what, test_name):
        errors = False
        for action in a:  # skip cpu init
            if action[2] == 'read':
                continue
            assert action[2] == 'write'
            match = False
            for c in b:
                if c[2] == 'read':
                    continue
                if c[0] == action[0] and c[1] == action[1]:
                    match = True
                    break
            if match == False:
                print(f'test {test_name}, invalid RAM write to {action[0]}, value {action[1]}')
                errors = True
        return errors
    # simplified as pyc64 is not emulating each step of an instruction
    errors |= verify_cycles_simplified(bus.actions[2:], cycles, 'invalid RAM write', test_name)
    errors |= verify_cycles_simplified(cycles, bus.actions[2:], 'RAM write missing', test_name)

sys.exit(1 if errors else 0)
