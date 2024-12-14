#!/usr/bin/python3

import re

file_to_read = "input.txt"

matches = []

with open(file_to_read, "r") as f:
    content = f.readlines()
    for line in content:
        doline = re.split(r"do\(\)", line)
        for l in doline:
            valid = l
            dont = re.search(r"don't\(\)", l)
            if dont:
                disregard = l[dont.span()[1]:]
                valid = l[:dont.span()[0]]
            more = re.findall(r"mul\(\d+\,\d+\)", valid)
            matches += more

sum = 0

for match in matches:
    operands = re.search(r"\d+,\d+", match).group(0)
    operands = operands.split(",")
    x = operands[0]
    y = operands[1]
    sum += int(x) * int(y)

print(sum)
