#!/usr/bin/python3

import sys

file_to_read = "input"

def split_to_ints(levels):
    return [int(num) for num in levels]


def adj_check(x, y):
    return abs(x - y) <= 3 and abs(x - y) > 0
    

def is_increasing_safely(levels):
    increasing = True
    idx = 0
    while idx < len(levels):
        try:
            this = levels[idx]
            following = levels[idx+1]
        except IndexError:
            break 
        if this >= following or not adj_check(this, following):
            increasing = False
            break 
        idx += 1
    return increasing

def is_decreasing_safely(levels):
    decreasing = True
    idx = 0
    while idx < len(levels):
        try:
            this = levels[idx]
            following = levels[idx+1]
            if this <= following or not adj_check(this, following):
                decreasing = False
                break
        except IndexError:
            break 
        idx += 1
    return decreasing 


num_safe = 0


with open(file_to_read, "r") as f:
    content = f.readlines()
    for report in content:
        levels = report.split(" ")
        levels = split_to_ints(levels)
        if is_increasing_safely(levels) or is_decreasing_safely(levels):
            num_safe += 1

print(num_safe)

