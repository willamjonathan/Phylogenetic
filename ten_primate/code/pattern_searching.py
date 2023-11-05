import re
import os
import tkinter as tk
from tkinter import messagebox

# pattern searching
def search_pattern_in_fastas(fasta_files, pattern):
    pattern_found = []
    for fasta_file in fasta_files:
        with open(fasta_file, 'r') as file:
            sequences = file.read().split('>')
            for sequence in sequences[1:]:
                lines = sequence.split('\n')
                header = lines[0]
                sequence_data = ''.join(lines[1:])
                if re.search(pattern, sequence_data):
                    pattern_found.append((fasta_file, header))
    return pattern_found

def search_button_click():
    pattern = pattern_entry.get()
    matched_sequences = search_pattern_in_fastas(fasta_files, pattern)
    result_text.delete(1.0, tk.END)  # Clear previous results
    i = 1
    if matched_sequences:
        result_text.insert(tk.END,"Pattern searched:"+pattern)
        result_text.insert(tk.END,"\n\n")
        result_text.insert(tk.END, "Files and headers of sequences containing the pattern:\n")
        for file_path, header in matched_sequences:
            if header == "NC_010299.1 Daubentonia madagascariensis mitochondrion, complete genome":
                result_text.insert(tk.END,  f"{i}. Daubentonia madagascariensis mitochondrion\n")
            if header == "NC_026095.1 Indri indri isolate TANDRA4.18 mitochondrion, complete genome":
                result_text.insert(tk.END,  f"{i}. Indri indri isolate TANDRA4.18 mitochondrion\n")
            if header == "KY202428.1 Alouatta guariba clamitans mitochondrion, complete genome":
                result_text.insert(tk.END,  f"{i}. Alouatta guariba clamitans mitochondrion\n")
            if header == "NC_050682.1 Callithrix aurita mitochondrion, complete genome":
                result_text.insert(tk.END,  f"{i}. Callithrix aurita mitochondrion\n")
            if header == "NC_064205.1 Plecturocebus grovesi isolate RVR22 voucher INPA:7275 mitochondrion, complete genome":
                result_text.insert(tk.END,  f"{i}. Plecturocebus grovesi isolate RVR22 voucher INPA:7275 mitochondrion\n")
            if header == "NC_019582.1 Trachypithecus vetulus mitochondrion, complete genome":
                result_text.insert(tk.END,  f"{i}. Trachypithecus vetulus mitochondrion\n")
            if header == "HQ171089.1 Lepilemur jamesorum isolate VEV7.7 mitochondrion, complete genome":
                result_text.insert(tk.END,  f"{i}. Lepilemur jamesorum isolate VEV7.7 mitochondrion\n")
            if header == "NC_020667.1 Simias concolor mitochondrion, complete genome":
                result_text.insert(tk.END,  f"{i}. Simias concolor mitochondrion\n")
            if header == "NC_033884.1 Hoolock tianxing isolate NA1 mitochondrion, complete genome":
                result_text.insert(tk.END,  f"{i}. Hoolock tianxing isolate NA1 mitochondrion\n")
            if header =="NC_015485.1 Rhinopithecus avunculus mitochondrion, complete genome":
                result_text.insert(tk.END,  f"{i}. Rhinopithecus avunculus mitochondrion\n")
            i  = i + 1
    else:
        result_text.insert(tk.END,"Pattern: "+pattern)
        result_text.insert(tk.END,"\n\n")
        result_text.insert(tk.END, "Pattern not found in any sequence.")

# FASTA file paths
fasta_files = [
    "ten_primate/code/seqs/sequence_dm.fasta",
    "ten_primate/code/seqs/sequence_ii.fasta",
    "ten_primate/code/seqs/sequence_agc.fasta",
    "ten_primate/code/seqs/sequence_ca.fasta",
    "ten_primate/code/seqs/sequence_pg.fasta",
    "ten_primate/code/seqs/sequence_ht.fasta",
    "ten_primate/code/seqs/sequence_sc.fasta",
    "ten_primate/code/seqs/sequence_tv.fasta",
    "ten_primate/code/seqs/sequence_lj.fasta",
    "ten_primate/code/seqs/sequence_ra.fasta"
]

root = tk.Tk()
root.title("Pattern Searching")
root.configure(bg='#b5b5b5')
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

x = (screen_width - 800) // 2  
y = (screen_height - 600) // 2  

root.geometry(f"800x600+{x}+{y}")

title_label = tk.Label(root, text="Pattern Searching", font=("Arial", 24), bg = "#9A9A9A")
title_label.pack(pady=20)  

pattern_label = tk.Label(root, text="Enter Pattern:",bg = "#9A9A9A")
pattern_label.pack(pady = 5)
pattern_entry = tk.Entry(root, bg = "#9A9A9A")
pattern_entry.pack(pady = 5)

search_button = tk.Button(root, text="Search", command=search_button_click, bg = "#9A9A9A")
search_button.pack()

result_text = tk.Text(root, height=20, width=60)
result_text.pack(pady=10)
result_text.config(bg='#333333', fg='white', relief=tk.SUNKEN)

root.mainloop()
