from copy import deepcopy
from typing import List, Tuple

from day_8.day8_1 import Operation, prettify_input, get_acc


def halts_correctly(code: List[Tuple[Operation, int]]) -> bool:
    executed_instructions = set()
    op_ptr = 0
    while op_ptr not in executed_instructions and op_ptr < len(code) - 1:
        executed_instructions.add(op_ptr)
        if code[op_ptr][0] == Operation.jmp:
            op_ptr += code[op_ptr][1]
        else:
            op_ptr += 1
    return op_ptr == len(code) - 1


def fix_code(code: List[Tuple[Operation, int]]) -> List[Tuple[Operation, int]]:
    fixed_code = deepcopy(code)
    for i in range(7, len(code)):
        if code[i][0] == Operation.jmp:
            fixed_code[i] = (Operation.nop, code[i][1])
            if halts_correctly(fixed_code):
                return fixed_code
            fixed_code[i] = (Operation.jmp, code[i][1])
        elif code[i][0] == Operation.nop:
            fixed_code[i] = (Operation.jmp, code[i][1])
            if halts_correctly(fixed_code):
                return fixed_code
            fixed_code[i] = (Operation.nop, code[i][1])
    raise Exception("Could not find fix")


if __name__ == '__main__':
    with open("input.txt", 'r') as f:
        raw_input = list(map(lambda x: x.strip(), f.readlines()))
    code = prettify_input(raw_input)
    code = fix_code(code)
    print(get_acc(code))

