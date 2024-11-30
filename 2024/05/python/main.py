#!/usr/bin/python3

file_to_read = "input.txt"

rules = []
updates = []
left_list = []
right_list = []
pages_that_follow = {}

def organize_input():
    top_done = False
    with open(file_to_read, "r") as f:
        for line in f:
            line = line.strip("\n")
            if line == "":
                top_done = True
                continue
            
            if top_done:
                updates.append(line)
            else:
                rules.append(line)


def check_ordering(items):
    for idx, x in enumerate(items):
        try:
            sub = items[idx+1:]
        except:
            break
        for y in sub:
            try:
                if y not in pages_that_follow[x]:
                    # print(f"{y} does not follow {x} | {pages_that_follow[x]}") debug
                    return False
            # if we get here, x has no pages that follow it. That means it should never come first
            except KeyError:
                return False 
    return True

def main():
    organize_input()

    for rule in rules:
        left_list.append(rule.split("|")[0])

    unique = set(left_list)

    for u in unique:
        pages_that_follow[u] = []

    for u in unique:
        for rule in rules:
            if u == rule.split("|")[0]:
                pages_that_follow[u].append(rule.split("|")[1])

    sum = 0

    for update in updates:
        items = update.split(",")
        if len(items)%2 != 1:
            print("can't check the middle of an even number")
            return
        if check_ordering(items):
            tmp = int(items[int(len(items)/2)])
            sum += tmp
    
    print(sum)


main()
