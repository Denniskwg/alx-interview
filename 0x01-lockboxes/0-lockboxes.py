#!/usr/bin/python3
"""0-lockboxes defines a function canUnlockAll that
loops over a list of lists and checks if each list
has a value equivalent to an index of another list
inside the list of lists
"""


def canUnlockAll(boxes):
    """takes a list of lists and returns true if
    values inside a list has an index corresponding to
    another list inside the list of lists
    """
    index_list = []

    def get_values(lst):
        length = len(boxes) - 1
        indexes = []
        for val in lst:
            if val > length:
                continue
            for i in range(len(boxes[val])):
                indexes.append(boxes[val][i])
            indexes.append(val)
        indexes = list(set(indexes))
        return indexes

    index_list = get_values(boxes[0])
    print(index_list)

    def compare_list(lst):
        reference = []
        sorted_lst = lst.sort()
        for i in range(len(boxes)):
            reference.append(i)

        if reference == sorted_lst:
            return True
        else:
            return False

    if compare_list(index_list):
        return True

    for i in range(1, len(boxes)):
        if i in index_list:
            index_list.extend(get_values(boxes[i]))
            index_list = list(set(index_list))
        else:
            return False
    return True
