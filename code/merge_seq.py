from Bio import SeqIO
# read fastanya
Seq1 = SeqIO.read("code/seqs/sequence_pg.fasta", "fasta")
Seq2 = SeqIO.read("code/seqs/sequence_ca.fasta", "fasta")
Seq3 = SeqIO.read("code/seqs/sequence_agc.fasta", "fasta")
Seq4 = SeqIO.read("code/seqs/sequence_ii.fasta", "fasta")
Seq5 = SeqIO.read("code/seqs/sequence_dm.fasta", "fasta")

# giving ID
Seq1.id = "Plecturocebus grovesi"
Seq2.id = "Callithrix aurita"
Seq3.id = "Alouatta guariba clamitans"
Seq4.id = "Indri Indri"
Seq5.id = "Daubentonia madagascariensis"
# merging all fasta to one fasta
merge_seq = SeqIO.write([Seq1,Seq2,Seq3,Seq4,Seq5], "merge_seq.fasta","fasta")

# go to :
# https://www.ebi.ac.uk/Tools/msa/muscle/
# then masukin fasta filenya

