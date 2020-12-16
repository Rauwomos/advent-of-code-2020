import math
import re

from day_12.ship import Ship

cmd_pattern = re.compile(r"(?P<letter>[A-Z])(?P<num>\d+)")


class Ship2(Ship):
    def __init__(self):
        super().__init__()
        self.w_x = 10
        self.w_y = 1

    def _rotate_waypoint_around_ship(self, angle: int):
        """Assumes angle is in degrees and divisible by 90. Rotates anti-clockwise"""
        rad = math.radians(angle)
        new_w_x = int(math.cos(rad)) * (self.w_x - self.x) - int(math.sin(rad)) * (self.w_y - self.y) + self.x
        new_w_y = int(math.sin(rad)) * (self.w_x - self.x) - int(math.cos(rad)) * (self.w_y - self.y) + self.y
        self.w_x = new_w_x
        self.w_y = new_w_y

    def move(self, cmd: str):
        cmd_match = cmd_pattern.match(cmd)
        if not cmd_match:
            raise Exception(f"Unrecognised cmd: {cmd}")
        num = int(cmd_match.group("num"))
        if cmd_match.group("letter") == 'N':
            self.w_y += num
        elif cmd_match.group("letter") == 'S':
            self.w_y -= num
        elif cmd_match.group("letter") == 'E':
            self.w_x += num
        elif cmd_match.group("letter") == 'W':
            self.w_x -= num
        elif cmd_match.group("letter") == 'L':
            self._rotate_waypoint_around_ship(num)
        elif cmd_match.group("letter") == 'R':
            self._rotate_waypoint_around_ship(-num)
        elif cmd_match.group("letter") == 'F':
            x_offset = (self.w_x - self.x) * num
            y_offset = (self.w_y - self.y) * num
            self.x += x_offset
            self.y += y_offset
            self.w_x += x_offset
            self.w_y += y_offset
        else:
            raise Exception("Unknown cmd letter")
        print(f"Ship: {self.x}, {self.y}")
        print(f"Wayp: {self.w_x}, {self.w_y}")
