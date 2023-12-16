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
        subprocess.run(['python', 'ten_primate/UI.py'])
        output_label.config(text="File 2 executed successfully!")
    except FileNotFoundError:
        output_label.config(text="Error: file2.py not found!")

def run_file3():
    try:
        subprocess.run(['python', 'fifteen_primate/UI.py'])
        output_label.config(text="File 3 executed successfully!")
    except FileNotFoundError:
        output_label.config(text="Error: file3.py not found!")

root = tk.Tk()
root.title("Phylogenetic Analysis on Endangered Primates")
root.configure(bg='#b5b5b5')
from PIL import Image, ImageTk 

background_image = Image.open("bg/bg2.png")  
background_photo = ImageTk.PhotoImage(background_image)


screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width - background_image.width) // 2
y = (screen_height - background_image.height) // 2
root.geometry(f"{background_image.width}x{background_image.height}+{x}+{y}")



background_label = tk.Label(root, image=background_photo)
background_label.place(relwidth=1, relheight=1)

# title_label = tk.Label(root, text="Phylogenetic Analysis on Endangered Primates", font=("Arial", 16, "bold"),bg= None)
# title_label.pack(pady=10)

# subtitle_label = tk.Label(root, text="William, Tiffany, Jocelin", font=("Arial", 12),bg= "#9A9A9A")
# subtitle_label.pack(pady=5)
button_frame = tk.Frame(root,bg = "black")
button_frame.pack(side=tk.TOP, pady=240)

# d1 = tk.Button(button_frame, text="Disease 1", command=lambda: search_button_click(sequence_dict[h], "Sickle Cell Anemia"), 
#                bg=button_colors[0], fg='white', font=button_font)
# d1.pack(side=tk.LEFT, padx=10, pady=10)

button1 = tk.Button(button_frame, text="5 Primate", command=run_file1, width=30, height=50,bg = "gray", fg= "white")
button1.pack(side=tk.LEFT,padx=10)

button2 = tk.Button(button_frame, text="10 Primate", command=run_file2, width=30, height=50, bg = "gray",fg = "white")
button2.pack(side=tk.LEFT,padx=10)

button3 = tk.Button(button_frame, text="15 Primate", command=run_file3, width=30, height=50, bg = "gray",fg = "white")
button3.pack(side=tk.LEFT, padx=10)

output_label = tk.Label(root, text="", fg="white", bg = "#9A9A9A")
output_label.pack()

root.mainloop()
