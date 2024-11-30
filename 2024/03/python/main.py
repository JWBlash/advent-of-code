#!/usr/bin/python3

import re

file_to_read = "input.txt"

matches = []

with open(file_to_read, "r") as f:
    content = f.readlines()
    for line in content:
        matches += re.findall(r"mul\(\d+\,\d+\)", line)

sum = 0

for match in matches:
    operands = re.search(r"\d+,\d+", match).group(0)
    operands = operands.split(",")
    x = operands[0]
    y = operands[1]
    sum += int(x) * int(y)

print(sum)
    

