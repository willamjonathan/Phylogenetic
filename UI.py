import tkinter as tk
import subprocess

def button1_click():
    try:
        subprocess.run(["python", "code/show_alignment.py"])
        label.config(text="Multiple Sequence Alignment is run", fg="green")
    except Exception as e:
        label.config(text=f"Error: {str(e)}", fg="red")

def button2_click():
    try:
        subprocess.run(["python", "code/phylogenetic_tree.py"])
        label.config(text="Phylogenetic Draw is run", fg="green")
    except Exception as e:
        label.config(text=f"Error: {str(e)}", fg="red")

def button3_click():
    try:
        subprocess.run(["python", "code/pattern_searching.py"])
        label.config(text="Pattern Searching is run", fg="green")
    except Exception as e:
        label.config(text=f"Error: {str(e)}", fg="red")

def button4_click():
    label.config(text="On process", fg="green")

root = tk.Tk()
root.title("Phylogenetic Analysis on Primate")

# Get the screen width and height
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Calculate the x and y coordinates to center the window
x = (screen_width - 400) // 2  # You can adjust the width of the window as needed
y = (screen_height - 300) // 2  # You can adjust the height of the window as needed

# Set the window position
root.geometry(f"400x300+{x}+{y}")

label_title = tk.Label(
    root, text="Phylogenetic Analysis on Primate", font=("Arial", 16, "bold")
)
label_title.pack(pady=20)

button1 = tk.Button(
    root,
    text="Multiple Sequence Alignment",
    command=button1_click,
    bg="red",
    fg="white",
    width=25,
)
button2 = tk.Button(
    root,
    text="Phylogenetic Draw",
    command=button2_click,
    bg="green",
    fg="white",
    width=25,
)
button3 = tk.Button(
    root,
    text="Pattern Searching",
    command=button3_click,
    bg="blue",
    fg="white",
    width=25,
)
button4 = tk.Button(
    root, text="Disease", command=button4_click, bg="purple", fg="white", width=25
)

button1.pack()
button2.pack()
button3.pack()
button4.pack()

label = tk.Label(root, text="", font=("Arial", 12))
label.pack(pady=20)

root.mainloop()
