from typing import List, Iterator

from aoc2024.util import is_blank

def parse_report(s: str) -> List[int]:
    return [int(n) for n in s.split(" ")]

def is_safe(report: List[int]) -> bool:
    return is_unidirectional(report) and has_small_gaps(report)

def is_unidirectional(l: List[int]) -> bool:
    expected_diff = diffs(l).__next__()
    return all(n < 0 for n in diffs(l)) if (expected_diff < 0) else all(n > 0 for n in diffs(l))

def has_small_gaps(l) -> bool:
    return all(abs(n) <= 3 for n in diffs(l))

def diffs(l: List[int]) -> Iterator[int]:
    return (l[i + 1] - l[i] for i in range(0, len(l) - 1))

# Part 1
with open("../resources/day_2.txt") as f:
    reports = (parse_report(line) for line in f if not is_blank(line))
    sum = len(list(filter(is_safe, reports)))
    print(f"Part 1: {sum}")
