#!/usr/bin/python3
def canUnlockAll(boxes):
    n = len(boxes)
    opened = set([0])  # Start with the first box already opened
    stack = [0]  # Stack to manage the boxes to check

    while stack:
        box = stack.pop()
        for key in boxes[box]:
            if key not in opened and key < n:
                opened.add(key)
                stack.append(key)

    # Check if all boxes are opened
    return len(opened) == n

