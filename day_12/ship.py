import re

cmd_pattern = re.compile(r"(?P<letter>[A-Z])(?P<num>\d+)")


class Ship:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.facing = 90

    def move(self, cmd: str):
        cmd_match = cmd_pattern.match(cmd)
        if not cmd_match:
            raise Exception(f"Unrecognised cmd: {cmd}")
        num = int(cmd_match.group("num"))
        if cmd_match.group("letter") == 'N':
            self.y += num
        elif cmd_match.group("letter") == 'S':
            self.y -= num
        elif cmd_match.group("letter") == 'E':
            self.x += num
        elif cmd_match.group("letter") == 'W':
            self.x -= num
        elif cmd_match.group("letter") == 'L':
            self.facing -= num
        elif cmd_match.group("letter") == 'R':
            self.facing += num
        elif cmd_match.group("letter") == 'F':
            self.facing = self.facing % 360
            if self.facing == 0:
                self.y += num
            elif self.facing == 90:
                self.x += num
            elif self.facing == 180:
                self.y -= num
            elif self.facing == 270:
                self.x -= num
            else:
                raise Exception(f"Facing unknown direction: {self.facing}")
        else:
            raise Exception("Unknown cmd letter")

    def run(self, file_path: str):
        with open(file_path, 'r') as f:
            raw_input = f.readlines()
        for line in raw_input:
            self.move(line)

    def manhattan_dist(self) -> int:
        return abs(self.x) + abs(self.y)