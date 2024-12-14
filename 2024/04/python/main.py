#!/usr/bin/python3

file_to_read = "sample.txt"

with open(file_to_read, "r") as f:
    content = f.readlines()

    for xidx, x in enumerate(content):
        print(x)
        for yidx, y in enumerate(x):
            print(y)
        # try:
        #     print(f"")
        # except IndexError:
        #     break
