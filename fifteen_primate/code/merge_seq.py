from Bio import SeqIO
# read fastanya
Seq1 = SeqIO.read("fifteen_primate/code/seqs/sequence_pg.fasta", "fasta")
Seq2 = SeqIO.read("fifteen_primate/code/seqs/sequence_ca.fasta", "fasta")
Seq3 = SeqIO.read("fifteen_primate/code/seqs/sequence_agc.fasta", "fasta")
Seq4 = SeqIO.read("fifteen_primate/code/seqs/sequence_ii.fasta", "fasta")
Seq5 = SeqIO.read("fifteen_primate/code/seqs/sequence_dm.fasta", "fasta")
Seq6 = SeqIO.read("fifteen_primate/code/seqs/sequence_ht.fasta", "fasta")
Seq7 = SeqIO.read("fifteen_primate/code/seqs/sequence_sc.fasta", "fasta")
Seq8 = SeqIO.read("fifteen_primate/code/seqs/sequence_lj.fasta", "fasta")
Seq9 = SeqIO.read("fifteen_primate/code/seqs/sequence_tv.fasta", "fasta")
Seq10 = SeqIO.read("fifteen_primate/code/seqs/sequence_ra.fasta", "fasta")
Seq11 = SeqIO.read("fifteen_primate/code/seqs/sequence_pb.fasta", "fasta")
Seq12 = SeqIO.read("fifteen_primate/code/seqs/sequence_mn.fasta", "fasta")
Seq13 = SeqIO.read("fifteen_primate/code/seqs/sequence_pp.fasta", "fasta")
Seq14 = SeqIO.read("fifteen_primate/code/seqs/sequence_am.fasta", "fasta")
Seq15 = SeqIO.read("fifteen_primate/code/seqs/sequence_lc.fasta", "fasta")

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
Seq10.id = "Rhinopithecus avunculus"
Seq11.id = "Piliocolobus badius"
Seq12.id = "Macaca nigra"
Seq13.id = "Pongo pygmameus"
Seq14.id = "Ateles marginatus"
Seq15.id = "Lemur catta"


# merging all fasta to one fasta
merge_seq = SeqIO.write([Seq1,Seq2,Seq3,Seq4,Seq5,Seq6,Seq7,Seq8,Seq9,Seq10,Seq11,Seq12,Seq13,Seq14,Seq15], "fifteen_primate/code/merge_seq15.fasta","fasta")

# go to :
# https://www.ebi.ac.uk/Tools/msa/muscle/
# then masukin fasta filenya

