from Bio import SeqIO

input_file = "seqs/sequence_pg.fasta"
output_file = "seqs/seqs(rna)/rna_pg.fasta"

def transcribe_dna_to_rna(dna_sequence):
    transcription_dict = {'A': 'U', 'T': 'A', 'C': 'G', 'G': 'C'}
    rna_sequence = ''.join(transcription_dict.get(base, base) for base in dna_sequence)
    return rna_sequence

with open(output_file, "w") as output_handle:
    for record in SeqIO.parse(input_file, "fasta"):
        dna_sequence = str(record.seq)  
        rna_sequence = transcribe_dna_to_rna(dna_sequence)
        rna_record = SeqIO.SeqRecord(rna_sequence, id=record.id, description=record.description)
        SeqIO.write(rna_record, output_handle, "fasta")

print(f"RNA sequences converted and saved in '{output_file}'.")
