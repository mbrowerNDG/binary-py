numberSet = [
    1,
    5,
    7,
    14,
    42,
    43,
    47,
    49,
    86,
    95,
    110,
    122,
    126,
    131,
    132,
    159,
    163,
    164,
    168,
    171,
    173,
    185,
    197,
    205,
    209,
    234,
    262,
    264,
    265,
    273,
    285,
    299,
    306,
    319,
    329,
    352,
    374,
    379,
    385,
    387,
    388,
    403,
    407,
    420,
    423,
    441,
    449,
    455,
    458,
    476,
    484,
    507,
    508,
    510,
    515,
    519,
    523,
    524,
    527,
]


def binary_searchByindex(array, value):
    lowest = 0
    highest = len(array) - 1
    median = 0
    while lowest <= highest:
        median = median + round((lowest + highest) / 2)
        if (array[median] < value):
            lowest = median + 1
        elif(array[median] > value):
            highest = median - 1
        else:
            print(median)
            return median
        if (value != array[median]):
            print('no such number')
            return 'No such number in set'


binary_searchByindex(numberSet, 319)
