#!/usr/bin/python3

file_to_read = "input.txt"

directions = [
    (-1, -1),
    (-1, 0),
    (-1, 1),
    (0, 1),
    (1, 1),
    (1, 0),
    (1, -1),
    (0, -1)
    ]

# for testing other ints
sum = 0
found = set()

with open(file_to_read, "r") as f:
    content = f.readlines()
    strippedContent = []
    for line in content:
        strippedContent.append(line.strip("\n"))
    for idy, line in enumerate(strippedContent):
        for idx, _ in enumerate(line):
            # check for forwards strings
            if strippedContent[idy][idx] == "X":
                for direction in directions:
                    matched_coords = []
                    matched_coords.append(tuple((idy, idx)))
                    ydir = direction[0]
                    xdir = direction[1]
                    # bounds checking
                    if idx + xdir < 0:
                        continue
                    if idy + ydir < 0:
                        continue
                    if idx + xdir == len(strippedContent[0]):
                        continue
                    if idy + ydir == len(strippedContent[0]):
                        continue
                    # check for letter
                    if strippedContent[idy + ydir][idx + xdir] == "M":
                        # print(f"found viable candidate at [{idy + ydir}][{idx + xdir}]")
                        matched_coords.append(tuple((idy + ydir, idx + xdir)))
                        # bounds checking
                        if idx + xdir * 2 < 0:
                            continue
                        if idy + ydir * 2 < 0:
                            continue
                        if idx + xdir * 2 == len(strippedContent[0]):
                            continue
                        if idy + ydir * 2 == len(strippedContent[0]):
                            continue
                        # check for letter
                        if strippedContent[idy + ydir * 2][idx + xdir * 2] == "A":
                            # print(f"found viable candidate at [{idy + ydir * 2}][{idx + xdir * 2}]")
                            matched_coords.append(tuple((idy + ydir * 2, idx + xdir * 2)))
                            # bounds checking
                            if idx + xdir * 3 < 0:
                                continue
                            if idy + ydir * 3 < 0:
                                continue
                            if idx + xdir * 3 == len(strippedContent[0]):
                                continue
                            if idy + ydir * 3 == len(strippedContent[0]):
                                continue
                            # check for letter
                            if strippedContent[idy + ydir * 3][idx + xdir * 3] == "S":
                                # print(f"found viable candidate at [{idy + ydir * 3}][{idx + xdir * 3}]")
                                matched_coords.append(tuple((idy + ydir * 3, idx + xdir * 3)))
                                matched_coords.sort()
                                coord_str = f"{matched_coords}"
                                # print(coord_str)
                                if coord_str not in found:
                                    found.add(f"{matched_coords}")
                                    sum += 1

            # check for backwards strings
            if strippedContent[idy][idx] == "S":
                for direction in directions:
                    matched_coords = []
                    matched_coords.append(tuple((idy, idx)))
                    ydir = direction[0]
                    xdir = direction[1]
                    # bounds checking
                    if idx + xdir < 0:
                        continue
                    if idy + ydir < 0:
                        continue
                    if idx + xdir == len(strippedContent[0]):
                        continue
                    if idy + ydir == len(strippedContent[0]):
                        continue
                    # check for letter
                    if strippedContent[idy + ydir][idx + xdir] == "A":
                        # print(f"found viable candidate at [{idy + ydir}][{idx + xdir}]")
                        matched_coords.append(tuple((idy + ydir, idx + xdir)))
                        # bounds checking
                        if idx + xdir * 2 < 0:
                            continue
                        if idy + ydir * 2 < 0:
                            continue
                        if idx + xdir * 2 == len(strippedContent[0]):
                            continue
                        if idy + ydir * 2 == len(strippedContent[0]):
                            continue
                        # check for letter
                        if strippedContent[idy + ydir * 2][idx + xdir * 2] == "M":
                            # print(f"found viable candidate at [{idy + ydir * 2}][{idx + xdir * 2}]")
                            matched_coords.append(tuple((idy + ydir * 2, idx + xdir * 2)))
                            # bounds checking
                            if idx + xdir * 3 < 0:
                                continue
                            if idy + ydir * 3 < 0:
                                continue
                            if idx + xdir * 3 == len(strippedContent[0]):
                                continue
                            if idy + ydir * 3 == len(strippedContent[0]):
                                continue
                            # check for letter
                            if strippedContent[idy + ydir * 3][idx + xdir * 3] == "X":
                                # print(f"found viable candidate at [{idy + ydir * 3}][{idx + xdir * 3}]")
                                matched_coords.append(tuple((idy + ydir * 3, idx + xdir * 3)))
                                matched_coords.sort()
                                coord_str = f"{matched_coords}"
                                # print(coord_str)
                                if coord_str not in found:
                                    found.add(f"{matched_coords}")
                                    sum += 1

print(sum)

exit(0)

