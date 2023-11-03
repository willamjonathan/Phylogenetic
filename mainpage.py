import tkinter as tk
import subprocess

def run_file1():
    try:
        subprocess.run(['python', 'five_primate/UI.py'])
        output_label.config(text="File 1 executed successfully!")
    except FileNotFoundError:
        output_label.config(text="Error: file1.py not found!")

def run_file2():
    try:
        subprocess.run(['python', 'nine_primate/UI.py'])
        output_label.config(text="File 2 executed successfully!")
    except FileNotFoundError:
        output_label.config(text="Error: file2.py not found!")


root = tk.Tk()
root.title("Phylogenetic Analysis on Endangered Primates")
root.configure(bg='#b5b5b5')

# Get the screen width and height
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

x = (screen_width - 600) // 2  
y = (screen_height - 300) // 2  

# Set the window position
root.geometry(f"600x300+{x}+{y}")

title_label = tk.Label(root, text="Phylogenetic Analysis on Endangered Primates", font=("Arial", 16, "bold"),bg= "#9A9A9A")
title_label.pack(pady=10)

subtitle_label = tk.Label(root, text="William, Tiffany, Jocelin", font=("Arial", 12),bg= "#9A9A9A")
subtitle_label.pack(pady=5)

button1 = tk.Button(root, text="5 Primate", command=run_file1, width=15, height=2,bg = "green", fg= "white")
button1.pack(pady=10)

button2 = tk.Button(root, text="9 Primate", command=run_file2, width=15, height=2, bg = "blue",fg = "white")
button2.pack(pady=10)

output_label = tk.Label(root, text="", fg="white", bg = "#9A9A9A")
output_label.pack()

root.mainloop()
