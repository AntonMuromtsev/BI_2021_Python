import webbrowser
import matplotlib.pyplot as plt
from Bio.Seq import Seq
from Bio.SeqUtils import GC


class RomaToday:
    """
    Parameters: 
    
    mood: good / bad / angry
    lecturer: No / Yes
    Location: any
    
    """

    def __init__(self, mood="good", lecturer="No", location="DAS"):

        self.mood = mood
        self.lecturer = lecturer
        self.location = location

    def play_xbox(self):

        if self.location == "DAS":
            return "Game pass is my LOVE!"
        return "I don't have Xbox here, cannot play directly :("

    def help_students(self):

        if self.mood == "good":
            webbrowser.open('https://www.youtube.com/watch?v=NMbNwMKarcA')
        elif self.mood == "bad":
            webbrowser.open('https://www.youtube.com/playlist?list=PLjKdf6AHvR-EVtt5ocCAfU2WfJFobZzsD')
        elif self.mood == "angry":
            webbrowser.open('https://www.google.ru')

    def drink_beer(self):
        if self.lecturer == "No":
            return True
        elif self.lecturer == "Yes":
            return False


class RNA:

    def __init__(self, sequence):
        self.sequence = Seq(sequence)

    def translation(self):
        return self.sequence.translate()

    def reverse_transcription(self):
        return self.sequence.back_transcribe()


class PlusSet(set):

    def __init__(self, *args):
        self.elements = [arg for arg in args if arg > 0]
        super().__init__(self.elements)

    def add(self, element):
        if element > 0:
            super().add(element)

    def update(self, *addings):
        for element in addings:
            self.add(element)


class FastaStat:

    def __init__(self, path):
        self.path = path

    def __str__(self):
        return self.path

    def count_seq(self):
        count = 0
        with open(self.path) as fa:
            for line in fa:
                count += 1
        return count / 4

    def len_hist(self):
        count = 0
        lengths = []
        with open(self.path) as fa:
            for line in fa:
                count += 1
                if count % 4 == 2:
                    lengths.append(len(line))
        plt.hist(lengths)
        plt.title("Histogram of reads' length")
        plt.xlabel("length")
        plt.ylabel("frequency")
        plt.show()

    def gc_part(self):
        count = 0
        overall_len = 0
        gc_len = 0
        with open(self.path) as fa:
            for line in fa:
                count += 1
                if count % 4 == 2:
                    overall_len += len(line)
                    gc_len += GC(line) / 50 * len(line)
        return gc_len / overall_len * 100

    def four_meer_hist(self):
        count = 0
        four_meers = {}
        with open(self.path) as fa:
            for line in fa:
                count += 1
                if count % 4 == 2:
                    for base in range(len(line) - 3):
                        four_mer = line[base: base + 4]
                        if four_mer in four_meers:
                            four_meers[four_mer] += 1
                        else:
                            four_meers[four_mer] = 1
        plt.style.use('classic')
        plt.figure(figsize=(12, 8))
        plt.bar(four_meers.keys(), four_meers.values(), width=1)
        plt.tick_params(axis='x', which='major', labelsize=10)
        plt.xticks(fontsize=3, rotation=90)
        plt.title("Histogram of 4-meers")
        plt.xlabel("name of 4-meer")
        plt.ylabel("frequency")
        plt.show()
        return

    def stats(self):
        print("number of reads:", self.count_seq())
        print("gc percentage:", self.gc_part())
        print("reads length distribution:")
        self.len_hist()
        print("4-meers frequencies:")
        self.four_meer_hist()
        return
