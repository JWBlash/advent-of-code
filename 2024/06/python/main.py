#!/usr/bin/python3

file_to_read = "sample.txt"

with open(file_to_read, "r") as f:
    for line in f.readlines():
        print(line.strip("\n"))
