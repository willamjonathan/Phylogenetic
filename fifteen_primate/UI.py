import tkinter as tk
import subprocess

def button1_click():
    try:
        subprocess.run(["python", "fifteen_primate/code/show_alignment.py"])
        label.config(text="Multiple Sequence Alignment is run", fg="green")
    except Exception as e:
        label.config(text=f"Error: {str(e)}", fg="red")

def button2_click():
    try:
        subprocess.run(["python", "fifteen_primate/code/phylogenetic_tree.py"])
        label.config(text="Phylogenetic Draw is run", fg="green")
    except Exception as e:
        label.config(text=f"Error: {str(e)}", fg="red")

def button3_click():
    try:
        subprocess.run(["python", "fifteen_primate/code/pattern_searching.py"])
        label.config(text="Pattern Searching is run", fg="green")
    except Exception as e:
        label.config(text=f"Error: {str(e)}", fg="red")

def button4_click():
    try:
        subprocess.run(["python", "fifteen_primate/code/disease.py"])
        label.config(text="Disease is run", fg="green")
    except Exception as e:
        label.config(text=f"Error: {str(e)}", fg="red")


root = tk.Tk()
root.title("Phylogenetic Analysis on Primate")
root.configure(bg='#b5b5b5')

from PIL import Image, ImageTk 

background_image = Image.open("bg/bg5.png") 
background_photo = ImageTk.PhotoImage(background_image)


screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width - background_image.width) // 2
y = (screen_height - background_image.height) // 2
root.geometry(f"{background_image.width}x{background_image.height}+{x}+{y}")


background_label = tk.Label(root, image=background_photo)
background_label.place(relwidth=1, relheight=1)

# label_title = tk.Label(
#     root, text="Phylogenetic Analysis on Primate (15)", font=("Arial", 16, "bold"),bg = "#9A9A9A"
# )
# label_title.pack(pady=20
button_frame = tk.Frame(root,bg = "black")
button_frame.pack(side=tk.BOTTOM, pady=120)

button_frame2 = tk.Frame(button_frame,bg = "black")
button_frame2.pack(side=tk.BOTTOM, pady=10)


button1 = tk.Button(
    button_frame,
    text="Multiple Sequence Alignment",
    command=button1_click,
    bg="gray",
    fg="white",
    width=30,
    height=4
)
button1.pack(side=tk.LEFT,padx=10)

button2 = tk.Button(
    button_frame,
    text="Phylogenetic Draw",
    command=button2_click,
    bg="gray",
    fg="white",
    width=30,
    height=4
)
button2.pack(side=tk.LEFT,padx=10)
button3 = tk.Button(
    button_frame2,
    text="Pattern Searching",
    command=button3_click,
    bg="gray",
    fg="white",
    width=30,
    height=4
)
button3.pack(side=tk.LEFT,padx=10)
button4 = tk.Button(
    button_frame2, text="Disease", command=button4_click, bg="gray", fg="white",  width=30,
    height=4
)
button4.pack(side=tk.LEFT,padx=10)


label = tk.Label(root, text="", font=("Arial", 12),bg = "#B5B5B5",fg="white")
label.pack(side = tk.TOP, pady=5)

root.mainloop()
