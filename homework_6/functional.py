import numpy as np


def sequential_map(*args):
    container = args[-1]
    for arg in args[:-1]:
        container = arg(container)
    return container


def sequential_map_modified(*args):
    in_arg = args[-1]

    def inner(in_arg):
        for arg in args[:-1]:
            in_arg = arg(in_arg)
        return in_arg

    return inner(in_arg)


def consensus_filter(*args):
    container = args[-1]
    for arg in args[:-1]:
        temp = []
        for i in container:
            if arg(i):
                temp.append(i)
        container = temp
    return container


def conditional_reduce(func_1, func_2, container):
    container = container[::-1]
    while len(container) > 1:
        temp = []
        for i in container:
            if func_1(i):
                temp.append(i)
        if len(temp) == 0:
            return "All filtered"
        elif len(temp) == 1:
            return temp[0]
        a = temp.pop()
        b = temp.pop()
        res = func_2(a, b)
        temp.append(res)
        container = temp
    return container[0]


def func_chain(*args):
    def inner(in_arg):
        for arg in args:
            in_arg = arg(in_arg)
        return in_arg

    return inner


def multiple_partial(*args, axis):  # the example was proveded with axis, so I did it with axes. But now axis is
    # obligate to use
    funcs = []

    def outer(arg):
        def inner(in_arg):
            in_arg = arg(in_arg, axis=axis)
            return in_arg

        return inner

    for arg in args:
        funcs.append(outer(arg))
    return funcs


if __name__ == "__main__":
    print("base version of sequental_map:", sequential_map(np.square, np.sqrt, lambda x: x ** 3, [1, 2, 3, 4, 5]))
    print("modified varison on sequental_map:", sequential_map_modified(np.square,
                                                                        np.sqrt, lambda x: x ** 3, [1, 2, 3, 4, 5]))
    print(consensus_filter(lambda x: x > 0, lambda x: x > 5, lambda x: x < 10, [-2, 0, 4, 6, 11]))
    print(conditional_reduce(lambda x: x < 5, lambda x, y: x + y, [1, 3, 5, 10]))

    my_chain = func_chain(lambda x: x + 2, lambda x: (x / 4, x // 4))
    print("my_chain(37) is", my_chain(37))

    ax1_mean, ax1_max, ax1_sum = multiple_partial(np.mean, np.max, np.sum, axis=1)
    example = np.array([[1, 2, 3, ], [4, 5, 6, ]])
    print("mean | max | sum:", f"{ax1_mean(example)} |", f"{ax1_max(example)} |", f"{ax1_sum(example)}")
