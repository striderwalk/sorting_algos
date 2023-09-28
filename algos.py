from consts import *


def quick_sort(arr):
    if len(arr) <= 1:
        return []

    stack = [(0, len(arr) - 1)]  # Stack to store the left and right indices

    yield ["pointer", {"id": "p", "index": 0, "colour": GREEN}]
    yield ["pointer", {"id": "i", "index": 0, "colour": RED}]
    yield ["pointer", {"id": "j", "index": 0, "colour": BLUE}]

    while stack:
        left, right = stack.pop()
        if left < right:

            pivot = arr[right]
            yield ["mp", ("p", left + (right - left) // 2)]

            i = left - 1
            yield ["mp", ("i", i)]

            for j in range(left, right):
                yield ["mp", ("j", j)]

                if arr[j] < pivot:
                    i += 1
                    yield ["mp", ("i", i)]

                    arr[i], arr[j] = arr[j], arr[i]
                    yield ["swap", (i, j)]

            arr[i + 1], arr[right] = arr[right], arr[i + 1]
            yield ["swap", (i + 1, right)]

            pivot_index = i + 1
            yield ["mp", ("p", pivot_index)]

            if pivot_index - left > right - pivot_index:
                stack.append((left, pivot_index - 1))
                stack.append((pivot_index + 1, right))
            else:
                stack.append((pivot_index + 1, right))
                stack.append((left, pivot_index - 1))


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
                lst1 = groups[index]
                lst2 = groups[index + 1]

            else:
                lst = groups[index]
                new_groups.append(lst)
                continue

            real_index_1 = index * group_size
            real_index_2 = real_index_1 + len(lst1)

            for i in range(len(lst2) - 1, -1, -1):
                yield ["mp", ("i", i + real_index_2)]

                last = lst1[len(lst1) - 1]
                j = len(lst1) - 2
                yield ["mp", ("j", j + real_index_1)]

                while j >= 0 and lst1[j] > lst2[i]:
                    lst1[j + 1] = lst1[j]
                    yield ["swap", (j + real_index_1, j + real_index_1 + 1)]

                    j -= 1
                    yield ["mp", ("j", j + real_index_1)]

                if last > lst2[i]:
                    yield ["swap", (j + 1 + real_index_1, i + real_index_2)]

                    lst1[j + 1] = lst2[i]
                    lst2[i] = last

            new_groups.append(lst1 + lst2)

        groups = new_groups
        group_size *= 2
