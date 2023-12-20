#!/usr/bin/env python3

import math

TYPE, MEMORY, OUTPUT = 0, 1, 2
LOW, HIGH, NO_SIGNAL = 0, 1, 2

encode_type = {'b': 0, '%': 1, '&': 2}
decode_type = {0: 'broadcaster', 1: 'toggle', 2: 'conjunction'}

def pulse(id, signal, buttons, pulses, source, marker, main_conjunction, n):
    queue = [(id, signal, source)]

    while queue:
        id, signal, source = queue[0]
        pulses[signal] += 1
        queue = queue[1:]

        if id not in buttons:
            continue

        match decode_type[buttons[id][TYPE]]:
            case 'broadcaster':
                send = signal
            case 'toggle':
                if signal == LOW:
                    stored = buttons[id][MEMORY]['self']
                    buttons[id][MEMORY]['self'] = HIGH if stored == LOW else LOW
                    send = buttons[id][MEMORY]['self']
                else:
                    send = NO_SIGNAL
            case 'conjunction':
                buttons[id][MEMORY][source] = signal
                if id == main_conjunction and any(buttons[id][MEMORY].values()):
                    marker.append(n)
                if all(buttons[id][MEMORY].values()):
                    send = LOW
                else:
                    send = HIGH

        if send != NO_SIGNAL:
            for output in buttons[id][OUTPUT]:
                queue.append((output, send, id))

with open("input.txt") as file:
    buttons = {}
    pulses = {LOW: 0, HIGH: 0}

    for line in file.read().strip().split("\n"):
        type = line[0]
        name = line.split()[0] if type == 'b' else line.split()[0][1:]
        outputs = [output.strip() for output in line.split("->")[1].split(',')]
        match decode_type[encode_type[type]]:
            case 'broadcaster':
                buttons[name] = (encode_type[type], {}, tuple(outputs))
            case 'toggle':
                buttons[name] = (encode_type[type], {'self': LOW}, tuple(outputs))
            case 'conjunction':
                buttons[name] = (encode_type[type], {}, tuple(outputs))
    
    for name in buttons:
        for output in buttons[name][OUTPUT]:
            if output in buttons and decode_type[buttons[output][TYPE]] == 'conjunction':
                buttons[output][MEMORY][name] = LOW

    main_conjunction = [b for b in buttons if 'rx' in buttons[b][OUTPUT]][0]
    marker = []

    for i in range(1, 4096):
        pulse('broadcaster', LOW, buttons, pulses, 'button', marker, main_conjunction, i)

    print(math.lcm(*marker))