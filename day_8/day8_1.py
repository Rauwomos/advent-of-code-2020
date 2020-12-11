import re
from enum import Enum
from typing import List, Tuple


class Operation(Enum):
    nop = "nop"
    acc = "acc"
    jmp = "jmp"


loc_pattern = re.compile(r"^(?P<op>\S{3}) (?P<num>[+-]\d+)$")


def prettify_input(raw_input: List[str]) -> List[Tuple[Operation, int]]:
    code = []
    for line in raw_input:
        loc_match = loc_pattern.match(line)
        code.append((Operation(loc_match.group("op")), int(loc_match.group("num"))))
    return code


def get_acc(code: List[Tuple[Operation, int]]) -> int:
    """Returns acc when it finishes or restarts a loop"""
    executed_instructions = set()
    acc = 0
    op_ptr = 0
    while op_ptr not in executed_instructions and op_ptr < len(code):
        executed_instructions.add(op_ptr)
        if code[op_ptr][0] == Operation.acc:
            acc += code[op_ptr][1]
            op_ptr += 1
        elif code[op_ptr][0] == Operation.jmp:
            op_ptr += code[op_ptr][1]
        else:
            op_ptr += 1
    return acc


if __name__ == '__main__':
    with open("input.txt", 'r') as f:
        raw_input = list(map(lambda x: x.strip(), f.readlines()))
    code = prettify_input(raw_input)
    print(get_acc(code))
