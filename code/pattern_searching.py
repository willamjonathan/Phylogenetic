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
    if matched_sequences:
        result_text.insert(tk.END, "Files and headers of sequences containing the pattern:\n")
        for file_path, header in matched_sequences:
            result_text.insert(tk.END, f"{header}\n")
    else:
        result_text.insert(tk.END, "Pattern not found in any sequence.")

# FASTA file paths
fasta_files = [
    "code/seqs/sequence_dm.fasta",
    "code/seqs/sequence_ii.fasta",
    "code/seqs/sequence_agc.fasta",
    "code/seqs/sequence_ca.fasta",
    "code/seqs/sequence_pg.fasta"
]

root = tk.Tk()
root.title("Pattern Searching")
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

x = (screen_width - 800) // 2  
y = (screen_height - 600) // 2  

root.geometry(f"800x600+{x}+{y}")

title_label = tk.Label(root, text="Pattern Searching", font=("Arial", 24))
title_label.pack(pady=20)  

pattern_label = tk.Label(root, text="Enter Pattern:")
pattern_label.pack()
pattern_entry = tk.Entry(root)
pattern_entry.pack()

search_button = tk.Button(root, text="Search", command=search_button_click)
search_button.pack()

result_text = tk.Text(root, height=20, width=60)
result_text.pack(pady=10)
result_text.config(bg='#333333', fg='white', relief=tk.SUNKEN)

root.mainloop()
