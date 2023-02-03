#!/usr/bin/python3
"""solve lockboxes"""


def canUnlockAll(boxes):
    def dfs(i, visited):
        if i in visited:
            return False
        visited.add(i)
        for j in boxes[i]:
            if j not in visited:
                dfs(j, visited)
        return True

    visited = set()
    return dfs(0, visited) and len(visited) == len(boxes)
