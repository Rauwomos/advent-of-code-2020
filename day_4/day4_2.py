import re
from typing import Dict

from day_4.day4_1 import extract_valid_passports

hcl_pattern = re.compile(r"^#[0-9a-f]{6}$")
pid_pattern = re.compile(r"^[0-9]{9}$")


def is_valid_byr(byr: str) -> bool:
    try:
        year = int(byr)
        return 1920 <= year <= 2002
    except ValueError:
        return False


def is_valid_iyr(iyr: str) -> bool:
    try:
        year = int(iyr)
        return 2010 <= year <= 2020
    except ValueError:
        return False


def is_valid_eyr(eyr: str) -> bool:
    try:
        year = int(eyr)
        return 2020 <= year <= 2030
    except ValueError:
        return False


def is_valid_hgt(hgt: str) -> bool:
    if hgt.endswith('cm'):
        min_hgt = 150
        max_hgt = 193
    elif hgt.endswith('in'):
        min_hgt = 59
        max_hgt = 76
    else:
        return False
    try:
        hgt_val = int(hgt[:-2])
        return min_hgt <= hgt_val <= max_hgt
    except ValueError:
        return False


def is_valid_hcl(hcl: str) -> bool:
    return bool(hcl_pattern.match(hcl))


def is_valid_ecl(ecl: str) -> bool:
    return ecl in {"amb", "blu", "brn", "gry", "grn", "hzl", "oth"}


def is_valid_pid(pid: str) -> bool:
    return bool(pid_pattern.match(pid))


def is_valid_passport(passport: Dict[str, str]) -> bool:
    fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    for key in fields:
        if key not in passport:
            return False
    return is_valid_byr(passport['byr']) \
        and is_valid_iyr(passport['iyr']) \
        and is_valid_eyr(passport['eyr']) \
        and is_valid_hgt(passport['hgt']) \
        and is_valid_hcl(passport['hcl']) \
        and is_valid_ecl(passport['ecl']) \
        and is_valid_pid(passport['pid'])


if __name__ == '__main__':
    with open("input.txt", "r") as f:
        input_lines = list(map(lambda x: x.strip(), f.readlines()))
    passports = extract_valid_passports(input_lines, is_valid_passport)
    print(len(passports))
