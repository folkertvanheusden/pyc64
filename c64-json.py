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
            print(f'test {test_name}, mismatch for {name}: expected {b:02x}, got {a:02x}')
            global errors
            errors = True

    final = test['final']
    ma(cpu.pc, final['pc'], 'pc', test['name'])
    ma(cpu.sp, final['s'], 'sp', test['name'])
    ma(cpu.a, final['a'], 'a', test['name'])
    ma(cpu.x, final['x'], 'x', test['name'])
    ma(cpu.y, final['y'], 'y', test['name'])
    # ma(cpu.p, final['p'], 'p', test['name'])
    for entry in final['ram']:
        ma(bus.ram.read(entry[0]), entry[1], f'RAM:{entry[0]:04x}', test['name'])

sys.exit(1 if errors else 0)
