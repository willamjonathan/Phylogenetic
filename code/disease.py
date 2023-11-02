import re
import os
import tkinter as tk
from tkinter import messagebox

sequence_dict = {
    "ATC": "ATGCTCATCAATT", #ngetes doang 
    "AGC": "AGG",
    "ACC": "ABT",
    "AAC": "ATG",
    "AAA": "TTT"
}
# penyakit, normal
# yang disearch yang normal

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

def search_button_click(pattern,diseasename):
    matched_sequences = search_pattern_in_fastas(fasta_files, pattern)
    result_text.delete(1.0, tk.END)  # Clear previous results
    i = 1
    if matched_sequences:
        result_text.insert(tk.END, "Normal sequence, mutated sequence: \n\n" )
        result_text.insert(tk.END, pattern + "\n")
        for key,value in sequence_dict.items():
            if value == pattern:
                result_text.insert(tk.END, key)
        result_text.insert(tk.END, "\n")
        result_text.insert(tk.END, "============================================================\n")
        result_text.insert(tk.END, "\tThere is a chance that the disease: "+  diseasename +"\n \tis found in the following list: \n\n")
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
            i  = i + 1
    else:
        result_text.insert(tk.END, "Mutated sequence:" )
        for key,value in sequence_dict.items():
            if value == pattern:
                result_text.insert(tk.END, key)
        result_text.insert(tk.END, "\n\n")
        result_text.insert(tk.END, "Disease not found in any sequence.")

# FASTA file paths
fasta_files = [
    "code/seqs/sequence_dm.fasta",
    "code/seqs/sequence_ii.fasta",
    "code/seqs/sequence_agc.fasta",
    "code/seqs/sequence_ca.fasta",
    "code/seqs/sequence_pg.fasta"
]

root = tk.Tk()
root.title("Disease")
root.configure(bg='#b5b5b5')
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

x = (screen_width - 800) // 2
y = (screen_height - 600) // 2

root.geometry(f"800x600+{x}+{y}")

title_label = tk.Label(root, text="Disease", font=("Arial", 24),bg = "#9A9A9A")
title_label.pack(pady=20)

h = "ATC"
i = "AGC"
j = "ACC"
k = "AAC"
l = "AAA"

button_frame = tk.Frame(root,bg = "#9A9A9A")
button_frame.pack(side=tk.TOP, padx=20, pady=10)

button_colors = ['#4CAF50', '#FFC107', '#2196F3', '#E91E63', '#9C27B0']

button_font = ('Arial', 14)  

d1 = tk.Button(button_frame, text="Disease 1", command=lambda: search_button_click(sequence_dict[h], "disease1"), 
               bg=button_colors[0], fg='white', font=button_font)
d1.pack(side=tk.LEFT, padx=10, pady=10)

d2 = tk.Button(button_frame, text="Disease 2", command=lambda: search_button_click(sequence_dict[i], "disease2"), 
               bg=button_colors[1], fg='white', font=button_font)
d2.pack(side=tk.LEFT, padx=10, pady=10)

d3 = tk.Button(button_frame, text="Disease 3", command=lambda: search_button_click(sequence_dict[j], "disease3"), 
               bg=button_colors[2], fg='white', font=button_font)
d3.pack(side=tk.LEFT, padx=10, pady=10)

d4 = tk.Button(button_frame, text="Disease 4", command=lambda: search_button_click(sequence_dict[k], "disease4"), 
               bg=button_colors[3], fg='white', font=button_font)
d4.pack(side=tk.LEFT, padx=10, pady=10)

d5 = tk.Button(button_frame, text="Disease 5", command=lambda: search_button_click(sequence_dict[l], "disease5"), 
               bg=button_colors[4], fg='white', font=button_font)
d5.pack(side=tk.LEFT, padx=10, pady=10)

result_text = tk.Text(root, height=20, width=60)
result_text.pack(pady=10)
result_text.config(bg='#333333', fg='white', relief=tk.SUNKEN)

root.mainloop()
