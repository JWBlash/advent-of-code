#!/usr/bin/python3

import sys

file_to_read = "input"

left_list = []
right_list = []

with open(file_to_read, "r") as f:
    content = f.readlines()
    for line in content:
        split_line = line.split("   ")
        left_list.append(int(split_line[0]))
        right_list.append(int(split_line[1].strip("\n")))

left_list.sort()
right_list.sort()

# make sure these things are the same size before we loop over them
if len(left_list) != len(right_list):
    print("real problem here")
    sys.exit(1)

sum_of_distances = 0

idx = 0
while idx < len(left_list):
    distance = abs(left_list[idx] - right_list[idx])
    sum_of_distances += distance
    idx += 1

print(f"total distance: {sum_of_distances}")

