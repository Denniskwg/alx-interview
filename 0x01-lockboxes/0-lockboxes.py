#!/usr/bin/python3
"""0-lockboxes
"""


def canUnlockAll(boxes):
    """takes a list of lists and returns true if
    values inside a list has an index corresponding to
    another list inside the list of lists
    """
    open_boxes = boxes[0]
    if len(open_boxes) == 0:
        return False

    if len(boxes) == 1:
        return True

    flag = True
    for i in range(1, len(boxes)):
        if flag is False:
            break
        if i in open_boxes:
            flag = True
        else:
            flag = False
    if flag is True:
        return True

    lst = []
    for num in open_boxes:
        if num in range(len(boxes)):
            lst = lst + boxes[num]

    open_boxes = open_boxes + lst

    for i in range(1, len(boxes)):
        if i in open_boxes:
            lst = []
            for num in boxes[i]:
                if num in range(len(boxes)):
                    lst = lst + boxes[num]
            open_boxes = open_boxes + lst
        else:
            return False
    return True
