#!/usr/bin/python3
"""Method that determines if all the boxes can be opened."""


def unlocking_boxes(boxes, index_box, opened_boxes, keys):
    """Recursive function to open the boxes"""

    n_boxes = len(boxes)
    expected_boxes = list(range(0, n_boxes))

    # Number of the boxes opened
    if index_box not in opened_boxes:
        opened_boxes.append(index_box)
        opened_boxes.sort()

    # number of keys we belong
    for key in boxes[index_box]:
        if key not in keys:
            keys.append(key)

    # Verify if the keys can open all the boxes
    if expected_boxes == opened_boxes:
        return True

    for key in keys:
        if key not in opened_boxes:
            return unlocking_boxes(boxes, key, opened_boxes, keys)

    return False


def canUnlockAll(boxes):
    """Method that determines if all the boxes can be opened."""
    if type(boxes) is not list:
        return False

    if len(boxes) == 0:
        return False

    opened_boxes = [0]
    keys = []

    result = unlocking_boxes(boxes, 0, opened_boxes, keys)
    return result
