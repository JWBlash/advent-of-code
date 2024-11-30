#!/usr/bin/python3

file_to_read = "input"
debug = False


def split_to_ints(levels):
    return [int(num) for num in levels]


def adj_check(x, y):
    return abs(x - y) <= 3 and abs(x - y) > 0
    

def is_increasing(x, y):
    return x >= y


def is_decreasing(x, y):
    return x <= y


def problem_dampener_increasing(levels_no_problem):
        return is_safe(levels_no_problem, increasing=True, dampen=False)


def problem_dampener_decreasing(levels_no_problem):
        return is_safe(levels_no_problem, increasing=False, dampen=False)


def is_safe(levels, increasing=True, dampen=True):
    if increasing:
        safety_check = is_increasing
        dampen_func = problem_dampener_increasing
    else:
        safety_check = is_decreasing 
        dampen_func = problem_dampener_decreasing
    safe = True
    idx = 0
    while idx < len(levels):
        try:
            this = levels[idx]
            next = levels[idx+1]
        except IndexError:
            break 
        if safety_check(this, next) or not adj_check(this, next):
            safe = False
        if not safe and dampen:
            without_this = levels.copy()
            del without_this[idx]
            without_next = levels.copy()
            del without_next[idx+1]
            if dampen_func(without_this) or dampen_func(without_next):
                safe = True
        idx += 1
    return safe


num_safe = 0


with open(file_to_read, "r") as f:
    content = f.readlines()
    for report in content:
        levels = report.split(" ")
        levels = split_to_ints(levels)
        if is_safe(levels) or is_safe(levels, increasing=False):
            num_safe += 1

print(num_safe)

