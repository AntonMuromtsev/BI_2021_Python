import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import re
import os
from sklearn.datasets import load_diabetes


def read_gff(path):
    pattern = re.compile("5S|16S|23S")
    with open(path) as rna, open(".corrected_annotation.gff", mode="w") as result:
        rna.readline()
        for line in rna:
            line = line.split("\t")
            global_addition = line[8]
            match = pattern.search(global_addition)
            target_addition = global_addition[match.start(): match.end()]
            line[8] = target_addition
            line = "\t".join(line)
            result.write(line + "\n")
    frame = pd.read_table(".corrected_annotation.gff", sep="\t", header=None, names=["seqname", "source",
                                                                                     "feature", "start", "end",
                                                                                     "score", "strand", "frame",
                                                                                     "RNA_type"])
    os.remove('.corrected_annotation.gff')
    return frame


def read_bed6(path):
    frame = pd.read_table(path, sep="\t", header=None, names=["chromosome", "start", "end", "name", "score",
                                                              "strand"])
    return frame


train = pd.read_csv("../data/train.csv")

# Build histograms for A,C,T,G¶

nucleotides = ["A", "C", "T", "G"]
fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(10, 8))
for i in range(2):
    for j in range(2):
        axes[i, j].hist(train[nucleotides[2 * i + j]])
        axes[i, j].set_title(nucleotides[2 * i + j])
        axes[i, j].set_xlabel("per position number")
        axes[i, j].set_ylabel("frequency")
fig.tight_layout()
plt.show()

# Subsetting train and writing to csv

train_part = train[train["matches"] > np.mean(train["matches"])]
train_part = train_part[["pos", "reads_all", "mismatches", "deletions", "insertions"]]
train_part.to_csv("train_part.csv")

# EDA of sklearn diabetes dataset

diabet = load_diabetes()
diabet = pd.DataFrame(data=diabet.data, columns=diabet.feature_names)

# Look at variables distribution

variables = diabet.columns

fig, axes = plt.subplots(nrows=5, ncols=2, figsize=(10, 14))
for i in range(len(variables) // 2):
    for j in range(2):
        axes[i, j].hist(diabet[variables[2 * i + j]])
        axes[i, j].set_title(variables[2 * i + j])
        axes[i, j].set_ylabel("frequency")
fig.tight_layout()
plt.show()

# Plotting correlations¶

corr_matr = diabet.corr()

plt.figure(figsize=(10, 8))
sns.heatmap(corr_matr, xticklabels=corr_matr.columns, yticklabels=corr_matr.columns, annot=True)
plt.title("Correlation heatmap of diabetes", fontsize=20)
plt.show()

# Reveal sex differencies

diabet.boxplot(column=['age', 'bmi', 'bp', 's1', 's2', 's3', 's4', 's5', 's6'], by='sex', figsize=(15, 15))
plt.tight_layout()
plt.show()

# Work with real data

gff_frame = read_gff("../data/rrna_annotation.gff")
bed = read_bed6("../data/alignment.bed")

# Counting number of different RNA types

rna_counts = gff_frame.groupby("RNA_type").apply(len)
plt.bar(rna_counts.index, rna_counts)
plt.title("RNA types frequencies")
plt.xlabel("RNA type")
plt.ylabel("frequency")
plt.show()

# Bedtools intersect in pandas

merged = gff_frame.merge(bed, left_on='seqname', right_on='chromosome')
intersected = merged[(merged["start_x"] > merged["start_y"]) & (merged["end_x"] < merged["end_y"])]
