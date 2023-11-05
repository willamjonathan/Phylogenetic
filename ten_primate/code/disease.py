import re
import os
import tkinter as tk
from tkinter import messagebox
import time  # Import the time module
import psutil

sequence_dict = {
    # normal yang disearch
    "AGATGA": "AGCTGA", 
    "TGCGGA": "TGCAGA",
    "ATCGCA": "ATGGCA",
    "CCTGT": "CCAGT",
    "GACCAA": "GATCAA"

    # # (yang disearch penyakit)
    # "AGCTGA": "AGATGA", 
    # "TGCAGA": "TGCGGA",
    # "ATGGCA": "ATCGCA",
    # "CCAGT": "CCTGT",
    # "GATCAA": "GACCAA"
}

root = tk.Tk()
root.title("Disease")
root.configure(bg='#b5b5b5')
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

x = (screen_width - 800) // 2
y = (screen_height - 600) // 2

root.geometry(f"800x600+{x}+{y}")
# yang ke 1, key = normal, value = mutated

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

# # time and memory

# execution_time_label = tk.Label(root, text="", font=("Arial", 12), bg="#b5b5b5")
# execution_time_label.pack()

# memory_usage_label = tk.Label(root, text="", font=("Arial", 12), bg="#b5b5b5")
# memory_usage_label.pack()


def search_button_click(pattern,diseasename):
    # start_time = time.time()

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
        result_text.insert(tk.END, "Mutated sequence:" )
        for key,value in sequence_dict.items():
            if value == pattern:
                result_text.insert(tk.END, key)
        result_text.insert(tk.END, "\n\n")
        result_text.insert(tk.END, "Disease not found in any sequence.")
    
    # TIME and memory
    # end_time = time.time()  # Get the end time
    # execution_time = end_time - start_time  # Calculate execution time
    
    # # Get memory usage
    # process = psutil.Process(os.getpid())
    # memory_usage = process.memory_info().rss / (1024 ** 2)  # in MB
    
    # # Update labels with execution time and memory usage
    # execution_time_label.config(text=f"Execution Time: {execution_time:.2f} seconds")
    # memory_usage_label.config(text=f"Memory Usage: {memory_usage:.2f} MB")


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

# root = tk.Tk()
# root.title("Disease")
# root.configure(bg='#b5b5b5')
# screen_width = root.winfo_screenwidth()
# screen_height = root.winfo_screenheight()

# x = (screen_width - 800) // 2
# y = (screen_height - 600) // 2

# root.geometry(f"800x600+{x}+{y}")

title_label = tk.Label(root, text="Disease", font=("Arial", 24),bg = "#9A9A9A")
title_label.pack(pady=20)

# normal yang disearch
h = "AGATGA"
i = "TGCGGA"
j = "ATCGCA"
k = "CCTGT"
l = "GACCAA"

# # penyakit yang disearch
# h = "AGCTGA"
# i = "TGCAGA"
# j = "ATGGCA"
# k = "CCAGT"
# l = "GATCAA"


button_frame = tk.Frame(root,bg = "#9A9A9A")
button_frame.pack(side=tk.TOP, padx=20, pady=10)

button_colors = ['#4CAF50', '#FFC107', '#2196F3', '#E91E63', '#9C27B0']

button_font = ('Arial', 14)  

d1 = tk.Button(button_frame, text="Disease 1", command=lambda: search_button_click(sequence_dict[h], "Sickle Cell Anemia"), 
               bg=button_colors[0], fg='white', font=button_font)
d1.pack(side=tk.LEFT, padx=10, pady=10)

d2 = tk.Button(button_frame, text="Disease 2", command=lambda: search_button_click(sequence_dict[i], "Cystic Fibrosis"), 
               bg=button_colors[1], fg='white', font=button_font)
d2.pack(side=tk.LEFT, padx=10, pady=10)

d3 = tk.Button(button_frame, text="Disease 3", command=lambda: search_button_click(sequence_dict[j], " Phenylketonuria (PKU)"), 
               bg=button_colors[2], fg='white', font=button_font)
d3.pack(side=tk.LEFT, padx=10, pady=10)

d4 = tk.Button(button_frame, text="Disease 4", command=lambda: search_button_click(sequence_dict[k], "Hemophilia A"), 
               bg=button_colors[3], fg='white', font=button_font)
d4.pack(side=tk.LEFT, padx=10, pady=10)

d5 = tk.Button(button_frame, text="Disease 5", command=lambda: search_button_click(sequence_dict[l], "Beta-Thalassemia"), 
               bg=button_colors[4], fg='white', font=button_font)
d5.pack(side=tk.LEFT, padx=10, pady=10)

result_text = tk.Text(root, height=20, width=60)
result_text.pack(pady=10)
result_text.config(bg='#333333', fg='white', relief=tk.SUNKEN)

root.mainloop()
