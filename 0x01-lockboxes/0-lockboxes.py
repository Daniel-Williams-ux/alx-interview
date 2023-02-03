#!/usr/bin/python3
"""solve lockboxes"""


def join(T, R):
    res = []
    for i in R:
        res += T[i]
    return res


def canUnlockAll(boxes):
    """determines if all the boxes can be opened."""
    index = 0
    total = list(set(boxes[0]) | {0})
    added = True
    while added:
        added = False
        for j in join(boxes, total[index:]):
            if j not in total:
                total.append(j)
                index += 1
                added = True

    return len(total) == len(boxes)
