from typing import Callable, Dict, List


def is_valid_passport(passport: Dict[str, str]) -> bool:
    fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    for key in fields:
        if key not in passport:
            return False
    return True


def extract_valid_passports(raw_input: List[str],
                            is_valid: Callable[[Dict[str, str]], bool]) -> List[Dict[str, str]]:
    potential_passports = []
    passport = {}
    for line in raw_input:
        if len(line) == 0:
            potential_passports.append(passport)
            passport = {}
        else:
            for i in line.split(' '):
                if i.count(':') == 1:
                    key, value = i.split(':')
                    passport[key] = value
    potential_passports.append(passport)
    valid_passports = []
    for passport in potential_passports:
        if is_valid(passport):
            valid_passports.append(passport)
    return valid_passports


if __name__ == '__main__':
    with open("input.txt", "r") as f:
        input_lines = list(map(lambda x: x.strip(), f.readlines()))
    passports = extract_valid_passports(input_lines, is_valid_passport)
    print(len(passports))
