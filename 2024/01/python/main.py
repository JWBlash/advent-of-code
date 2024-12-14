#!/usr/bin/python3

file_to_read = "input"

left_list = []
right_list = []

with open(file_to_read, "r") as f:
    content = f.readlines()
    for line in content:
        split_line = line.split("   ")
        left_list.append(int(split_line[0]))
        right_list.append(int(split_line[1].strip("\n")))

unique_left = set(left_list)
translation_map = {}

for item in unique_left:
    times_appeared = right_list.count(item)
    translation_map[item] = item * times_appeared

sum_of_distances = 0

for item in left_list:
    sum_of_distances += translation_map[item]

print(f"total distance: {sum_of_distances}")
