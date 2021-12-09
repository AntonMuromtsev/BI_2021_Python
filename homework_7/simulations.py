import numpy as np
import random
import time
import matplotlib.pyplot as plt
import statistics as st


def sorted_or_not_sorted(lst, reverse=False):
    """
    Checks whether list sorted or not
    :param lst: list with int or float elements
    :param reverse:  set True if you want to check decreasing sort
    :return: bool
    """
    if reverse is False:
        for pos in range(1, len(lst)):
            if lst[pos - 1] > lst[pos]:
                return False
        return True
    elif reverse is True:
        for pos in range(1, len(lst)):
            if lst[pos - 1] < lst[pos]:
                return False
        return True


def monkey_sort(lst, reverse=False):
    """
    Realises monkey sort based on random shuffling of given list
    :param lst: ljst of int or float elements
    :param reverse: parameter for orted_or_not_sorted fucntion
    :return: sorted list
    """
    while not sorted_or_not_sorted(lst, reverse):
        np.random.shuffle(lst)
    return lst


def text_shufler(text):
    """
    Suffles the words in text
    :param text: the text given
    :return: text with shuffled words. The first and the last word are kept on their places
    """
    text = text.split()
    for word in range(len(text)):
        if len(text[word]) == 1:
            continue
        mid = list(text[word][1:-1])
        np.random.shuffle(mid)
        mid = "".join(mid)
        text[word] = text[word][0] + mid + text[word][-1]
    return " ".join(text)


# Measuring the working time of random.uniform()
count = 0
number = np.zeros(1000)
timing = np.zeros(1000)
for k in range(1000):
    count += 1
    number[k] += count
    for i in range(100):
        start = time.time()
        for j in range(k):
            random.uniform(0, 1)
        end = time.time()
        dif = end - start
        timing[k] += dif
number = number
timing = timing / 100

# Measuring the working time of np.random.uniform()
count_np = 0
number_np = np.zeros(1000)
timing_np = np.zeros(1000)
for k in range(1000):
    count_np += 1
    number_np[k] += count_np
    for i in range(100):
        start = time.time()
        np.random.uniform(0, 1, size=k)
        end = time.time()
        dif = end - start
        timing_np[k] += dif
number_np = number_np
timing_np = timing_np / 100

# Comparing random.uniform() and np.random.uniform()
plt.plot(number, timing, color="red", label="random")
plt.plot(number_np, timing_np, color="blue", label="numpy")
plt.legend()
plt.savefig("random_vs_nprandom.png")
plt.clf()

# Measuring the working time of monkey_sort()
number = []
monkey_timing = []
monkey_error = []
count = 0
for i in range(11):
    count += 1
    number.append(count)
    av_timing = []
    for j in range(1, 11):
        Lst = np.random.randint(1, 10, size=i)
        start = time.time()
        monkey_sort(Lst)
        end = time.time()
        av_timing.append(end - start)
    error = st.stdev(av_timing)
    av_timing = st.mean(av_timing)
    monkey_timing.append(av_timing)
    monkey_error.append(error)

# Visualizing the  working time of monkey_sort()
plt.errorbar(number, monkey_timing, yerr=monkey_error)
plt.savefig("monkey_sort_timing.png")
plt.clf()

# Calculating random walking
dots_x = [0]
dots_y = [0]
for i in range(1000):
    step = np.random.uniform(size=2)
    dots_x.append(step[0])
    dots_y.append(step[1])

# Visualizing random walking
plt.scatter(dots_x, dots_y)
plt.savefig("random_walking.png")
plt.clf()

# Calculating sierpiński triangle

x = [np.random.uniform(), np.random.uniform(), np.random.uniform()]
y = [np.random.uniform(), np.random.uniform(), np.random.uniform()]

dot_x = np.random.uniform()
dot_y = np.random.uniform()
x.append(dot_x)
y.append(dot_y)

cases = 5000
for i in range(cases):
    case = np.random.randint(0, 3)
    dot_x = (dot_x + x[case]) / 2
    dot_y = (dot_y + y[case]) / 2
    x.append(dot_x)
    y.append(dot_y)

# Visualizing sierpiński triangle

plt.scatter(x, y)
plt.savefig("sierpiński_triangle.png")
