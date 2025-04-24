#!/usr/bin/python3
"""
Module for solving the lockboxes puzzle.
"""


def canUnlockAll(boxes):
    """
    Determines if all boxes can be opened.

    Args:
        boxes (list of lists): A list where each index represents a box,
                               and the list at that index contains keys
                               (indices) to other boxes.

    Returns:
        bool: True if all boxes can be opened, False otherwise.
    """
    n = len(boxes)
    if n == 0:
        return True

    opened_boxes = [False] * n
    opened_boxes[0] = True  # The first box is initially unlocked
    queue = [0]  # Start with the first box (index 0)
    head = 0  # Use index to simulate queue dequeue efficiently

    while head < len(queue):
        current_box_index = queue[head]
        head += 1

        keys_in_box = boxes[current_box_index]
        for key in keys_in_box:
            # Check if the key is a valid box index and the box is not opened
            if 0 <= key < n and not opened_boxes[key]:
                opened_boxes[key] = True
                queue.append(key)  # Add the newly opened box to the queue

    # Check if all boxes have been marked as opened
    return all(opened_boxes)

