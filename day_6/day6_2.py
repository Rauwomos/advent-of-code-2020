from typing import List, Set

from day_6.day6_1 import split_into_groups


def get_duplicate_yes_answers_in_group(group: List[Set[str]]) -> Set[str]:
    if not group:
        return set()
    yeses = group[0]
    for person in group:
        yeses &= person
    return yeses


if __name__ == '__main__':
    with open("input.txt", 'r') as f:
        raw_input = list(map(lambda x: x.strip(), f.readlines()))
    groups = split_into_groups(raw_input)
    groups = list(map(get_duplicate_yes_answers_in_group, groups))
    result = 0
    for g in groups:
        result += len(g)
    print(result)
