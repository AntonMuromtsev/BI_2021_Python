#!/usr/bin/env python3

import multiprocessing
import time

from Bio import SeqIO
import multiprocess
import argparse

parser = argparse.ArgumentParser(description='Contigs description')
parser.add_argument('path', type=str, help='Input file path')
parser.add_argument('cores', type=int, help='number of cores to use (not threads)')
args = parser.parse_args()


def parse_sequence(record_id, record_seq):
    parser = {}
    for word in record_seq:
        if word in parser:
            parser[word] += 1
        else:
            parser[word] = 1
    print(f"Contig {record_id}:    ", end="")
    parsered = []
    for key, value in zip(parser.keys(), parser.values()):
        parsered.append(f"{key}={value}")
    print(*parsered, sep=", ")
    return


class MyProcess(multiprocess.Process):
    def __init__(self, records):
        super().__init__()
        self.records = records

    def run(self):
        for record in self.records:
            parse_sequence(record.id, record.seq)


def parse_fasta_fast(filename, threads):
    print(f"started to process {filename}, number of cores is {threads}")
    records = SeqIO.parse(filename, "fasta")
    processes = []
    for i in range(threads):
        processes.append(MyProcess(records))
    for proc in processes:
        proc.start()
    for proc in processes:
        proc.join()


if __name__ == "__main__":
    parse_fasta_fast(args.path, args.cores)
