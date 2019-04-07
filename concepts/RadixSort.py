#!/urs/bin/python

from math import log10
from random import randint


# 정렬할 데이터의 자리수 이용해서 정렬 ex) 1의 자리, 10의 자리로 정렬

def get_digit(number, base, pos):
    return (number // base ** pos) % base


def prefix_sum(array):
    for i in range(1, len(array)):
        array[i] = array[i] + array[i - 1]
    return array


def radixsort(l, base=10):
    passes = int(log10(max(l)) + 1)
    output = [0] * len(l)

    for pos in range(passes):
        count = [0] * base

        for i in l:
            digit = get_digit(i, base, pos)
            count[digit] += 1

        count = prefix_sum(count)

        for i in reversed(l):
            digit = get_digit(i, base, pos)
            count[digit] -= 1
            new_pos = count[digit]
            output[new_pos] = i

        l = list(output)

    return output


if __name__ == '__main__':
    l = []
    l = [randint(1, 20) for x in range(100)]

    print("<Before the arrangement>")
    print(l)

    sorted = radixsort(l)

    print("<After arrangement>")
    print(sorted)
