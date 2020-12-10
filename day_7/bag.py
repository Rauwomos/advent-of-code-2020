from __future__ import annotations

import math
import re
from typing import Dict, Set, List


parent_children_pattern = re.compile(r"^(?P<colour>.*) bags contain(?P<contents>.*)$")
child_pattern = re.compile(r"(?P<count>\d+) (?P<colour>[^,\.]+) bag[s]?[,\.]")


class Bag:
    def __init__(self, colour: str):
        self.colour = colour
        self.children = {}
        self.parents = set()

    def __hash__(self):
        return hash(self.colour)

    def __eq__(self, other):
        if isinstance(other, Bag):
            return self.colour == other.colour
        return False

    @staticmethod
    def create_bags(raw_input: List[str]) -> Dict[str, Bag]:
        bags = {}
        for line in raw_input:
            parent_match = parent_children_pattern.match(line)
            parent_colour = parent_match.group("colour")
            if parent_colour in bags:
                parent = bags[parent_colour]
            else:
                parent = Bag(parent_colour)
                bags[parent_colour] = parent
            for child_match in child_pattern.findall(parent_match.group("contents")):
                child_count = int(child_match[0])
                child_colour = child_match[1]
                if child_colour in bags:
                    child = bags[child_colour]
                else:
                    child = Bag(child_colour)
                    bags[child_colour] = child
                parent.add_child(child, child_count)
                child.add_parent(parent)
        return bags

    def add_child(self, child: Bag, count: int):
        if count > 0:
            self.children[child] = count

    def add_parent(self, parent: Bag):
        self.parents.add(parent)

    def get_children(self) -> Dict[Bag, int]:
        return self.children

    def get_parents(self) -> Set[Bag]:
        return self.parents

    def get_descendants(self, already_found=None) -> Set[Bag]:
        if already_found is None:
            already_found = set()
        descendants = set(self.children.keys()) | already_found
        for child in self.children.keys():
            if child not in already_found:
                descendants = descendants | child.get_descendants(descendants)
        return descendants

    def get_descendant_count(self) -> int:
        """Assumes there is no recursive loops, otherwise the result is inf"""
        child_bag_count = 0
        for child in self.children:
            child_bag_count += self.children[child]
            child_bag_count += self.children[child] * child.get_descendant_count()
        return child_bag_count

    def get_ancestors(self, already_found=None) -> Set[Bag]:
        if already_found is None:
            already_found = set()
        ancestors = self.parents | already_found
        for parent in self.parents:
            if parent not in already_found:
                ancestors = ancestors | parent.get_ancestors()
        return ancestors
