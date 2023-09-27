from consts import *


def quick_sort(arr):
    if len(arr) <= 1:
        return []

    stack = [(0, len(arr) - 1)]  # Stack to store the left and right indices
    instructions = []
    instructions.append(["pointer", {"id": "p", "index": 0, "colour": RED}])

    while stack:
        left, right = stack.pop()
        if left < right:
            pivot_index, _instructions = partition(arr, left, right)
            instructions.extend(_instructions)
            if pivot_index - left > right - pivot_index:
                stack.append((left, pivot_index - 1))
                stack.append((pivot_index + 1, right))
            else:
                stack.append((pivot_index + 1, right))
                stack.append((left, pivot_index - 1))

    yield from instructions


def partition(arr, low, high):
    instructions = []

    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        instructions.append(["mp", ("p", pivot)])

        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
            instructions.append(["swap", (i, j)])

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    instructions.append(["swap", (i + 1, high)])

    return i + 1, instructions


def bubble_sort(lst):
    yield ["pointer", {"id": "c", "index": 0, "colour": RED}]
    yield ["pointer", {"id": "i", "index": 0, "colour": BLUE}]
    for c in range(len(lst) - 1, 0, -1):
        yield ["mp", ("c", c)]
        swap = False
        for i in range(0, c):
            yield ["mp", ("i", i)]
            if lst[i] > lst[i + 1]:
                lst[i], lst[i + 1] = lst[i + 1], lst[i]
                swap = True
                yield ["swap", (i, i + 1)]

        if not swap:
            return


def insertion_sort(lst):
    yield ["pointer", {"id": "i", "index": 0, "colour": RED}]
    yield ["pointer", {"id": "j", "index": 0, "colour": BLUE}]
    for i in range(len(lst)):
        yield ["mp", ("i", i)]
        j = i
        yield ["mp", ("j", j)]
        while j > 0 and lst[j - 1] > lst[j]:
            lst[j], lst[j - 1] = lst[j - 1], lst[j]
            yield ["swap", (j, j - 1)]
            yield ["mp", ("j", j)]
            j -= 1


def selection_sort(lst):
    yield ["pointer", {"id": "i", "index": 0, "colour": RED}]
    yield ["pointer", {"id": "j", "index": 0, "colour": BLUE}]
    for i in range(len(lst)):
        yield ["mp", ("i", i)]

        small_num = lst[i]
        for j in range(len(lst) - 1, i, -1):
            yield ["mp", ("j", j)]

            if lst[j] < small_num:
                small_num = lst[j]
                lst[i], lst[j] = lst[j], lst[i]
                yield ["swap", (i, j)]


def merge_sort(lst):
    if len(lst) <= 1:
        return lst
    yield ["pointer", {"id": "i", "index": 0, "colour": RED}]
    yield ["pointer", {"id": "j", "index": 0, "colour": BLUE}]

    groups = [
        [
            i,
        ]
        for i in lst
    ]
    group_size = 1
    while len(groups) >= 2:

        new_groups = []
        for index in range(0, len(groups), 2):
            if index < len(groups) - 1:
                lst = groups[index] + groups[index + 1]
            else:
                lst = groups[index]

            real_index = index * group_size

            # i, j = 0, group_size
            # yield ["mp", ("i", i + real_index)]
            # yield ["mp", ("j", j + real_index)]

            # using selection

            for i in range(len(lst)):
                yield ["mp", ("i", i + real_index)]

                small_num = lst[i]
                start = group_size if i < len(lst) // 2 else i

                for j in range(start, len(lst)):
                    yield ["mp", ("j", j + real_index)]

                    if lst[j] < small_num:
                        small_num = lst[j]
                        lst[i], lst[j] = lst[j], lst[i]
                        yield ["swap", (i + real_index, j + real_index)]

                    # when gets to a minimum stop
                    if j < len(lst) - 1 and lst[j + 1] > lst[j]:

                        break

            new_groups.append(lst)

        groups = new_groups
        group_size *= 2
