import re

parts = re.compile(r"^(?P<min>\d+)-(?P<max>\d+) (?P<letter>\S): (?P<pwd>\S+)$")

if __name__ == '__main__':
    with open("input.txt", "r") as f:
        passwords = f.readlines()
    valid_count = 0
    for pwd in passwords:
        if match := parts.match(pwd):
            first_letter = match.group('pwd')[int(match.group('min')) - 1]
            second_letter = match.group('pwd')[int(match.group('max')) - 1]
            if (first_letter == match.group('letter')) ^ (second_letter == match.group('letter')):
                valid_count += 1
    print(valid_count)
