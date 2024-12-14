#!/usr/bin/python3

import re

file_to_read = "input.txt"

matches = []

with open(file_to_read, "r") as f:
    content = f.read()
    splitcontent = content.split("do()")
    for line in splitcontent:
        valid = line
        dont = re.search(r"don't\(\)", line)
        if dont:
            disregard = line[dont.span()[1]:]
            valid = line[:dont.span()[0]]
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
