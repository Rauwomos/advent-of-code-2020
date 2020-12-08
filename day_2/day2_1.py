import re

parts = re.compile(r"^(?P<min>\d+)-(?P<max>\d+) (?P<letter>\S): (?P<pwd>\S+)$")

if __name__ == '__main__':
    with open("input.txt", "r") as f:
        passwords = f.readlines()
    valid_count = 0
    for pwd in passwords:
        if match := parts.match(pwd):
            if int(match.group('min')) <= match.group('pwd').count(match.group('letter')) <= int(match.group('max')):
                valid_count += 1
    print(valid_count)
