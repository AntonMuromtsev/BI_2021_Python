def gc_bounds_filter(read_sequence, minimum=0, maximum=100):
    """Require a read sequence (second line) of raw read from fasta file.
    Returns True if relative GC content is above min and below max"""
    if minimum == 0 and maximum == 100:
        return True
    gc_set = {"G", "C"}
    gc_total = 0
    atgc_total = 0
    for nucleotide in read_sequence:
        if nucleotide in gc_set:
            gc_total += 1
            atgc_total += 1
        else:
            atgc_total += 1
    gc_part = (gc_total / atgc_total) * 100
    return minimum <= gc_part <= maximum



def length_bound_filter(read_sequence_length, minimum=0, maximum=2 ** 32):
    """Require a length of raw read from fasta file.
    Returns True if sequence length is above min and below max"""
    if minimum <= read_sequence_length <= maximum:
        return True
    return False


def quality_treshold_filter(read_quality, threshold=0):
    """Require a quality sequence (third line) of raw read from fasta file.
    Calculates the average quality of the read using Phred33 scale.
     Returns True if quality is above threshold"""

    cumulative_quality = 0
    for symbol in read_quality:
        cumulative_quality += ord(symbol) - 33
    average_quality = cumulative_quality / len(read_quality)
    if average_quality >= threshold:
        return True
    return False


def file_length_counter(count_file):
    """Counts the number of line in file. Returns the number"""
    with open(count_file) as counting:
        count = 0
        for line in counting:
            count += 1
        return count


def bounds_master(func_parameter, bounds, func):
    """Designed for gc_bounds_filter and length_bounds_filter. Bounds master take any bounds
    and place them properly in receiving function"""

    if type(bounds) == int or type(bounds) == float:
        return func(func_parameter, maximum=bounds)
    elif type(bounds) == tuple:
        bounds = sorted(list(bounds))
        return func(func_parameter, *bounds)


def main(input_fastq, output_file_prefix, gc_bounds=(0, 100), length_bounds=(0, 2 ** 32),
         quality_threshold=0, save_filtered=False):
    """Takes fastq file, filter the reads in accordance with filter parameters. Returns output file with reads
    passed the filters and, if required, returns file with reads didn't pass the filters

    Parameters:

        input_fastq: input file

        output_file_prefix: name of output files

        gc_bounds: minimum and maximum of gc percentage in raw read. Requires a tuple form, for example: (20,60).
        If only one bound is defined, it will be interpreted as maximum. Defaults: (minimum = 0, maximum = 100)

        length_bounds: minimum and maximum of length of raw read. Requires a tuple form, for example: (95,110).
        If only one bound is defined, it will be interpreted as maximum. Defaults: (minimum = 0, maximum = 2 ** 32)

        quality_threshold: the minimum average quality of the read. Default: 0

        save_filtered: set True if you want to save reads that didn't pass the filters

    """

    file_length = file_length_counter(input_fastq)
    with open(input_fastq) as raw, \
            open(f"{output_file_prefix}_passed.fastq", mode="w") as passed, \
            open(f"{output_file_prefix}_failed.fastq", mode="w") as failed:
        for raw_read in range(file_length // 4):
            read_information = raw.readline()
            read_sequence = raw.readline()
            read_length = len(read_sequence)
            plus_line = raw.readline()
            read_quality = raw.readline()
            if bounds_master(read_sequence, gc_bounds, gc_bounds_filter) is True \
                    and bounds_master(read_length, length_bounds, length_bound_filter) is True \
                    and quality_treshold_filter(read_quality, quality_threshold) is True:
                passed.write("".join([read_information, read_sequence, plus_line, read_quality]))
            else:
                if save_filtered is True:
                    failed.write("".join([read_information, read_sequence, plus_line, read_quality]))


main("/Users/tugidon/Desktop/amp_res_1.fastqc", "/Users/tugidon/Desktop/result")
#main("/Users/tugidon/Desktop/amp_res_1.fastqc", "/Users/tugidon/Desktop/result",20, save_filtered = True)
