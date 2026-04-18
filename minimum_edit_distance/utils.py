from typing import List

DELETION_COST = 1
INSERTION_COST = 1
REPLACE_COST = 1


def create_2d_list(n: int, m: int) -> List[List[int]]:
    lst: List[List[int]] = []

    for _ in range(n):
        temp = []

        for _ in range(m):
            temp.append(0)

        lst.append(temp)

    return lst


class Grid:
    def __init__(self, n, m) -> None:
        self.lst = create_2d_list(n, m)

    def __getitem__(self, key):
        row, col = key

        return self.lst[row][col]

    def __setitem__(self, key, value: int) -> None:
        row, col = key

        self.lst[row][col] = value

    def __iter__(self):
        return iter(self.lst)
