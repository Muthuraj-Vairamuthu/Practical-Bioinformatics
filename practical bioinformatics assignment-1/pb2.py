import pandas as pd
from Bio import Entrez, SeqIO


def download_fasta_sequence(email, accession_number, output_file):
    Entrez.email = email
    handle = Entrez.efetch(
        db="nucleotide", id=accession_number, rettype="fasta", retmode="text")
    sequence = handle.read()
    with open(output_file, "w") as f:
        f.write(sequence)


email = "pallawik@iiitd.ac.in"
df = pd.read_csv("sequence_report.tsv", sep="\t")
RefSeq_accession = df["RefSeq seq accession"]


def ori_sequences(fasta_file):
    arr1 = []
    with open(fasta_file, "r") as f:
        ori_sequence = []
        for line in f:
            if line.startswith(">"):
                if ori_sequence:
                    o = ''.join(ori_sequence)
                    n = len(o)
                    for i in range(n - 11):
                        if (
                            o[i] in ["A", "T"]
                            and o[i + 1] == "T"
                            and o[i + 2] == "T"
                            and o[i + 3] == "T"
                            and o[i + 4] == "A"
                            and o[i + 5] in ["T", "C"]
                            and o[i + 6] in ["A", "G"]
                            and o[i + 7] == "T"
                            and o[i + 8] == "T"
                            and o[i + 9] == "T"
                            and o[i + 10] in ["A", "T"]
                        ):
                            arr1.append((len(arr1) + 1, i))
                ori_sequence = []
            else:
                ori_sequence.append(line.strip())
        if ori_sequence:
            o = ''.join(ori_sequence)
            n = len(o)
            for i in range(n - 11):
                if (
                    o[i] in ["A", "T"]
                    and o[i + 1] == "T"
                    and o[i + 2] == "T"
                    and o[i + 3] == "T"
                    and o[i + 4] == "A"
                    and o[i + 5] in ["T", "C"]
                    and o[i + 6] in ["A", "G"]
                    and o[i + 7] == "T"
                    and o[i + 8] == "T"
                    and o[i + 9] == "T"
                    and o[i + 10] in ["A", "T"]
                ):
                    arr1.append((len(arr1) + 1, i))

    return arr1


total_count = 0
each_file_count = 0
for i in RefSeq_accession:
    output_file = f"{i}.fasta"
    download_fasta_sequence(email, i, output_file)
    output_ori_sequences = ori_sequences(output_file)
    if output_ori_sequences:
        print(f"ORI positions present in {output_file}:")
        for j in output_ori_sequences:
            print(f" ORI Position  {j}")
            total_count += 1
            each_file_count += 1
    else:
        print(f"Not able to find any ORI sequence in {output_file}")

print("Total number of ORI sequences found including 16 chromosomes and mitochondria:", total_count)
