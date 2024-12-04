from typing import List, Iterator

from aoc2024.util import is_blank

def part_1():
    with open("../resources/day_2.txt") as f:
        reports = (parse_report(line) for line in f if not is_blank(line))
        sum = len(list(filter(is_safe, reports)))
        print(f"Part 1: {sum}")

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

def part_2():
    with open("../resources/day_2.txt") as f:
        reports = (parse_report(line) for line in f if not is_blank(line))
        sum = len(list(filter(is_safe_with_damper, reports)))
        print(f"Part 2: {sum}")

def is_safe_with_damper(l: List[int]) -> bool:
    negatives = sum(1 for n in diffs(l) if n < 0)
    positives = len(l) - negatives
    return has_small_gaps(l) if negatives == 0 or positives == 0 \
        else any((is_safe(remove_at_index(l, i)) for i in range(0, len(l))))

def remove_at_index[E](l: List[E], i: int) -> List[E]:
    copy = l.copy()
    copy.pop(i)
    return copy

part_1()
part_2()
