from typing import List, Set


def split_into_groups(raw_input: List[str]) -> List[List[Set[str]]]:
    groups = []
    group = []
    for line in raw_input:
        if line == "":
            groups.append(group)
            group = []
        else:
            person = set()
            for c in line:
                person.add(c)
            group.append(person)
    if group:
        groups.append(group)
    return groups


def get_all_yes_answers_in_group(group: List[Set[str]]) -> Set[str]:
    yeses = set()
    for person in group:
        yeses.update(person)
    return yeses


if __name__ == '__main__':
    with open("input.txt", 'r') as f:
        raw_input = list(map(lambda x: x.strip(), f.readlines()))
    groups = split_into_groups(raw_input)
    groups = list(map(get_all_yes_answers_in_group, groups))
    result = 0
    for g in groups:
        result += len(g)
    print(result)