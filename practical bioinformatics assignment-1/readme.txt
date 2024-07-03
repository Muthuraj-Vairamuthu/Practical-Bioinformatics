To run:
Kindly open pb2.py and select Run python File in terminal by right clicking on the code


Outline of this project:
I have first downloaded the sequence_report.tsv from this website https://www.ncbi.nlm.nih.gov/datasets/genome/GCF_000146045.2/
for Saccharomyces cerevisiae and have extracted the RefSeq accession number from it using panda module of python
Later I ran the accession numbers in a loop to create all the files as a variable inside the standard procedure to download the fasta files
Now for the Origin of Replication I have referred the following Websites:
https://www.pnas.org/doi/10.1073/pnas.94.20.10786#:~:text=Autonomously%20replicating%20sequence%20(ARS)%20elements,sequence%20(ACS)%20for%20activity.
https://www.frontiersin.org/journals/microbiology/articles/10.3389/fmicb.2019.02122/full
https://genomebiology.biomedcentral.com/articles/10.1186/gb-2004-5-4-r22



Especially these lines:
'''
The replication of yeast chromosomes is accomplished by the activation of multiple cis-acting replicators (for review, see ref. 1). These replicators were first identified by their ability to promote high-frequency transformation and stable extrachromosomal maintenance of plasmids in yeast (2, 3).
 On the basis of these properties, they were named autonomously replicating sequence (ARS) elements.
 ARS elements are modular (Fig. 1). All contain an essential match or near match to the 11-bp ARS consensus sequence (ACS) WTTTAYRTTTW (where W is A or T, Y is T or C, and R is A or G; refs. 17 and 18). 
 Mutations in this sequence abolish ARS function (for review, see ref. 1). 
'''



Where I have learnt about Consensus Sequences and the method named ad Method A in these websites to obtain the Ori ,that is the ori would be of 
a 11bp sequence as WTTTAYRTTTW; where W can be A or T
where Y can be T or C
where R can be A or G 
Hence, I read through the array skip the header lines and run each line in which I check if the above mentioned conditions for an ORI is satisfied
the array mainting this ori_sequence maintains this properly and resets itself correctly before entering a new Fasta file
If it is satisfied I am adding the length of the array and the starting point of the ORI as a tuple in this format
for example (1,81) where 1 is the number of ORI found in the fasta as of now and 81 is the starting index/position of the ORI
I obtain all these values in an array 
and later print the tuples of the array 
I also have a counter to track the sum the Total number of ORI sequences found including 16 chromosomes and mitochondria and keep incrementing it with every ORI
found and its final value turns out to 462 



Name :Muthuraj Vairamuthu
