from Bio import Entrez, SeqIO
from Bio.Seq import Seq
import pandas as pd
from Bio.Blast import NCBIWWW
from Bio import SearchIO

#PDC1 GENE
#q1
'''Access the NCBI database (https://www.ncbi.nlm.nih.gov/) and download the DNA sequence of the Saccharomyces cerevisiae PDC gene. (5 marks)'''

def fasta(email,accession_number, start_position, end_position, flag=False):
    Entrez.email = email
    handle = Entrez.efetch(db="nucleotide", id=accession_number,
                           rettype="fasta", seq_start=start_position, seq_stop=end_position)
    downloaded_gene_sequence = SeqIO.read(handle, "fasta")
    handle.close()
    if flag:
        downloaded_gene_sequence.seq = downloaded_gene_sequence.seq.reverse_complement()

    return downloaded_gene_sequence


accession_number = "NC_001144.5"
email ="pallawik@iiitd.ac.in"

start_position = 410723
end_position = 412414
downloaded_gene_sequence_record = fasta(email,
    accession_number, start_position, end_position, flag=False)
output_file = "PDC5.fasta"

with open(output_file, "w") as f:
    SeqIO.write(downloaded_gene_sequence_record, f, "fasta")

print("COMPLETED WRITING GENE SEQUENCE", output_file)



#q2
'''Use BLAST (Basic Local Alignment Search Tool) to compare the PDC gene sequence across different Saccharomyces cerevisiae strains and identify SNPs. (5 marks)'''
sequence_file = "PDC5.fasta"
sequence = ""
with open(sequence_file, "r") as f:
    for record in SeqIO.parse(f, "fasta"):
        sequence = str(record.seq)

result = NCBIWWW.qblast(
    "blastn", "nr", sequence, entrez_query="Saccharomyces cerevisiae[Organism]")

with open("blast_results.xml", "w") as out_handle:
    out_handle.write(result.read())

result.close()

blast_results = SearchIO.read("blast_results.xml", "blast-xml")
snp_sequences = []
for hit in blast_results:
    hit_desc = hit.description
    for hsp in hit.hsps:
        query_sequence = hsp.query.seq
        subject_sequence = hsp.hit.seq
        e_value = hsp.evalue
        for i in range(1, len(query_sequence) - 1):
            q = query_sequence[i]
            s = subject_sequence[i]
            q_prev = query_sequence[i - 1]
            s_prev = subject_sequence[i - 1]
            q_next = query_sequence[i + 1]
            s_next = subject_sequence[i + 1]
            if q != s and q != '-' and s != '-' and q_prev == s_prev and q_next == s_next:
                position = i  
                snp_sequences.append((q, s, position, e_value, hit_desc))

print("SNP sequences:")
for snp in snp_sequences:
    e_main = "{:.10e}".format(snp[3]) 
    print(f" {snp[0]} -> {snp[1]} is SNP, at the position {snp[2]} ,corresponding e value of the alignment {e_main} with hit description {snp[4]}")

print("------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")

print("Total SNP sequences found:", len(snp_sequences))
print("------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")

#q3
'''Use an translation tool (e.g., ExPASy Translate tool) to translate the normal and SNP-containing PDC gene sequences into amino acid sequences. (5 marks)'''

#for query Sequence
blast_results = SearchIO.read("blast_results.xml", "blast-xml")

query_translated = False
for hit in blast_results:
    if not query_translated:
        for hsp in hit.hsps:
            query_sequence = hsp.query.seq
            translated_query_seq = Seq(str(query_sequence)).translate()
            print("Translated query amino acid sequence:")
            print(translated_query_seq)
            query_translated = True
            break

print("------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")


#for all subject sequences
translated_sequences = []
for hit in blast_results:
    for hsp in hit.hsps:
        subject_sequence = hsp.hit.seq
        subject_sequence = subject_sequence.replace('-', '')
        translated_seq = Seq(subject_sequence).translate()
        translated_sequences.append(str(translated_seq))
print("Translated query amino acid sequences:")
print(translated_sequences)

print("------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")


#q4
'''Select a SNP within the PDC gene. Utilize tools like SIFT (Sorting Intolerant From Tolerant) or PolyPhen (Polymorphism Phenotyping) to predict the impact of the SNP on the PDC protein function.'''
'''
converted the format of the query seqeuence  using this link https://www.hiv.lanl.gov/cgi-bin/FORMAT_CONVERSION/convert.cgi
and have the converted amino acid sequence use the comparator link https://text-compare.com/ to compare let it run and then showcase the results
use one  based indexing
'''