Steps to run the program:

1.select the file PDC1/PDC5/PDC6 and click on the run python file option
2.Once the gene sequence have finished writing you will get this message in the terminal : COMPLETED WRITING GENE SEQUENCE PDC{1/5/6}.fasta.
3.Then wait for few minutes and you will get the following output:
4.SNP sequences: {the total number of snp sequences}
5.Translated query amino acid sequence:
6.Translated subject amino acid sequences:
7.For part 4 the answer will be present in the screenshots folder for PDC1/PDC5/PDC6.

'''
Kindly note we have used reverse complement for strains PDC1,PDC6 and not for PDC5 due to several reasons including the factor it may contain ORF on the reverse strand but not for PDC5 since it is already in 5'-3'.
source taken from:https://www.yeastgenome.org/locus/S000004034 - PDC 1 , https://www.yeastgenome.org/locus/S000004124 -PDC5 , https://www.yeastgenome.org/locus/S000003319  - PDC6 
source taken from: https://www.bioinformatics.org/sms/rev_comp.html
Positions taken from the above mentioned website for the respective locations.
'''
Explanation of the code:
1.Firstly the code will download the gene sequence using the the respective accession number,start position,end position ,and a flag checking whether to do reverse complement or not for the downloaded sequence.
2.The written gene sequence is then read and using NCBIIWW a qblast takes place and the result of the qblast is return to a file named blast_result.
3.Now the blast_results.xml is read and iterated through the query and subject sequence to find the SNP Sequences.
4.It is identified as follows each particular character is checked it the character at the same position in query and subject is different and if the preceeding and succeeding characters are same in both query and subject subsequence then it is added to the list and the length of the list is printed along with evalue ,the corresponding SNP and hit description is printed. 
5.Now using the .translate() function a single query and all the subject sequences are translated into amino acids.
6.The part 4 is done as follows"
* converted the format of the query seqeuence  using this link https://www.hiv.lanl.gov/cgi-bin/FORMAT_CONVERSION/convert.cgi
* and compared the converted query amino acid sequence and one subject amino acid sequence using link https://text-compare.com/  and the results were used for indexed based  diferences in the poly phen-2 website http://genetics.bwh.harvard.edu/pph2/ ;where ther jobs were submitted and the results have been given as screenshots in the screenshots folder  
uses one  based indexing.


Explanation of the screenshots:
1.the query section gives details about the protein from query submission,Protein Acc,Position of variant ,original,variant,and description of protein.
2.HumDiv is best used to evaluate rare variants involved
in complex disease, whereas HumVar is best used for diagnostics of Mendelian diseases
3.HumDiv and HumVar produce prediction score between 0 and 1 ,High scores mean more  probability that variant will affecrt protein function,low score means low probability that the variant will affect protein function.
4.Prediction scores have threee categories :benign,
possibly damaging, and probably damaging.
A result of benign indicates that the variant is not likely to affect protein function.
A result of possibly damaging indicates that the variant may affect protein function.
A result of probably damaging indicates that the variant is likely to affect protein function.
5.The Multiple sequence alignment 
shows alignment of 75 amino acids near the variant protein in our protein of interest with similar proteins from other species,top sequence is labeled Query ;the variant amino acid is highlighted with black box.

Source and explanation taken from : 
https://www.jax.org/-/media/jaxweb/files/education-and-learning/tutorials/polyphen2_tutorials_clickable.pdf


Three excerpts explanation from PDC1,PDC5,PDC6

PDC1:
1. A-S index 106:
* HumDiv -BENIGN SCORE 0.000 SENSITIVITY 1.00 AND SPECIFICITY 0.00
* HumVAR -BENIGN SCORE 0.013 SENSITIVITY 0.96 AND SPECIFICITY 0.52

PDC5:
1. C-V index 19:
* HumDiv -BENIGN SCORE 0.000 SENSITIVITY 1.00 AND SPECIFICITY 0.00
* HumVAR -BENIGN SCORE 0.013 SENSITIVITY 0.99 AND SPECIFICITY 0.09

PDC6:
1. D-E index 41:
* HumDiv -BENIGN SCORE 0.000 SENSITIVITY 1.00 AND SPECIFICITY 0.00
* HumVAR -BENIGN SCORE 0.013 SENSITIVITY 1.00 AND SPECIFICITY 0.00