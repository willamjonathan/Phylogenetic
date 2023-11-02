import tkinter as tk
import subprocess


def button1_click():
    try:
        subprocess.run(["python", "code/alignment_show.py"])
        label.config(text="Multiple Sequence Alignment Script Executed", fg="green")
    except Exception as e:
        label.config(text=f"Error: {str(e)}", fg="red")


# print("ayam")
# "rjahfsdjk"


def button2_click():
    label.config(text="On process", fg="green")


def button3_click():
    label.config(text="On process", fg="green")


def button4_click():
    label.config(text="On process", fg="green")


root = tk.Tk()
root.title("Phylogenetic Analysis on Primate")

# Create a label for the title
label_title = tk.Label(
    root, text="Phylogenetic Analysis Toolkit", font=("Arial", 16, "bold")
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
