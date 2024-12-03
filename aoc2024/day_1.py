import re

from aoc2024.util import is_blank

_pair_pattern = "^(\d+)\s+(\d+)$"

def parse_pair(s: str) -> (str, str):
    match = re.search(_pair_pattern, s)
    return int(match.group(1)), int(match.group(2))

with open("../resources/day_1.txt") as f:
    pairs = (parse_pair(line) for line in f if not is_blank(line))
    left, right = [sorted(n) for n in zip(*pairs)]
    diff = (abs(a - b) for a, b in zip(left, right))
    print(sum(diff))
