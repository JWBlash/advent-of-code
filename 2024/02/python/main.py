#!/usr/bin/python3

file_to_read = "input"
debug = False


def split_to_ints(levels):
    return [int(num) for num in levels]


def adj_check(x, y):
    return abs(x - y) <= 3 and abs(x - y) > 0
    

def problem_dampener_increasing(levels_no_problem):
        return is_increasing_safely(levels_no_problem, dampen=False)


def problem_dampener_decreasing(levels_no_problem):
        return is_decreasing_safely(levels_no_problem, dampen=False)


def is_increasing_safely(levels, dampen=True):
    safe = True
    idx = 0
    while idx < len(levels):
        try:
            this = levels[idx]
            next = levels[idx+1]
        except IndexError:
            break 
        if this >= next or not adj_check(this, next):
            if dampen:
                without_this = levels.copy()
                without_this.remove(this)
                without_next = levels.copy()
                without_next.remove(next)
                if problem_dampener_increasing(without_this) or problem_dampener_increasing(without_next):
                    return True
            safe = False
        idx += 1
    return safe 


def is_decreasing_safely(levels, dampen=True):
    safe = True
    idx = 0
    while idx < len(levels):
        try:
            this = levels[idx]
            next = levels[idx+1]
        except IndexError:
            break 
        if this <= next or not adj_check(this, next):
            if dampen:
                without_this = levels.copy()
                without_this.remove(this)
                without_next = levels.copy()
                without_next.remove(next)
                if problem_dampener_decreasing(without_this) or problem_dampener_decreasing(without_next):
                    return True
            safe = False
        idx += 1
    return safe


num_safe = 0


with open(file_to_read, "r") as f:
    content = f.readlines()
    for report in content:
        levels = report.split(" ")
        levels = split_to_ints(levels)
        if is_increasing_safely(levels) or is_decreasing_safely(levels):
            num_safe += 1

print(num_safe)

