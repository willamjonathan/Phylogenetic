from Bio import SeqIO
# read fastanya
Seq1 = SeqIO.read("nine_primate/code/seqs/sequence_pg.fasta", "fasta")
Seq2 = SeqIO.read("nine_primate/code/seqs/sequence_ca.fasta", "fasta")
Seq3 = SeqIO.read("nine_primate/code/seqs/sequence_agc.fasta", "fasta")
Seq4 = SeqIO.read("nine_primate/code/seqs/sequence_ii.fasta", "fasta")
Seq5 = SeqIO.read("nine_primate/code/seqs/sequence_dm.fasta", "fasta")
Seq6 = SeqIO.read("nine_primate/code/seqs/sequence_ht.fasta", "fasta")
Seq7 = SeqIO.read("nine_primate/code/seqs/sequence_sc.fasta", "fasta")
Seq8 = SeqIO.read("nine_primate/code/seqs/sequence_tp.fasta", "fasta")
Seq9 = SeqIO.read("nine_primate/code/seqs/sequence_tv.fasta", "fasta")

# giving ID
Seq1.id = "Plecturocebus grovesi"
Seq2.id = "Callithrix aurita"
Seq3.id = "Alouatta guariba clamitans"
Seq4.id = "Indri Indri"
Seq5.id = "Daubentonia madagascariensis"
Seq6.id = "Hoolock tianxing"
Seq7.id = "Simias concolor"
Seq8.id = "Lepilemur jamesorum"
Seq9.id = "Trachypithe cusvetulus"

# merging all fasta to one fasta
merge_seq = SeqIO.write([Seq1,Seq2,Seq3,Seq4,Seq5,Seq6,Seq7,Seq8,Seq9], "merge_seq9.fasta","fasta")

# go to :
# https://www.ebi.ac.uk/Tools/msa/muscle/
# then masukin fasta filenya

