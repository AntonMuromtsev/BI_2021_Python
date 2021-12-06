import re
import matplotlib.pyplot as plt

# looking for ftp links
with open("references.txt") as ref, open("ftps.txt", mode="w") as result:
    pattern = re.compile(r'\W(ftp\.[^\s;]+)')
    for line in ref:
        a = pattern.finditer(line)
        for i in a:
            result.write(i.group(1) + '\n')
# looking for numbers
with open("2430AD.txt") as story:
    pattern = re.compile(r'[^\d]?(\d+)')
    for line in story:
        a = pattern.finditer(line)
        for i in a:
            print(i.group(1) + '\n')
# looking for words that contain "a or A"
with open("2430AD.txt") as story:
    pattern = re.compile(r'\b\w*[Aa]\w*\b')
    for line in story:
        a = pattern.finditer(line)
        for i in a:
            print(i.group(0) + '\n')
# looking for sentences with exclamation marks
with open("2430AD.txt") as story:
    pattern = re.compile(r'[A-Z][^\.!?]*[!]')
    for line in story:
        a = pattern.finditer(line)
        for i in a:
            print(i.group(0) + '\n')
# Calculating frequences of words (case differences are irrelevant)
with open("2430AD.txt") as story:
    pattern = re.compile(r'[A-z]+')
    words = set()
    for line in story:
        a = pattern.finditer(line)
        for i in a:
            words.add(i.group(0).lower())
    words_count = []
    for i in words:
        words_count.append(len(i))
# Plotting a histogram of word length distribution
plt.hist(words_count)
plt.show()
