from Bio import Phylo
from Bio.Phylo.TreeConstruction import DistanceCalculator
from Bio.Phylo.TreeConstruction import DistanceTreeConstructor
from Bio import AlignIO
import tkinter as tk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Read the multiple sequence alignment from file
with open("code/align_ms5.clw", "r") as aln:
    alignment = AlignIO.read(aln, "clustal")

calculator = DistanceCalculator("identity")
distance_matrix = calculator.get_distance(alignment)

constructor = DistanceTreeConstructor(calculator)
rRNA_ps_tree = constructor.build_tree(alignment)
rRNA_ps_tree.rooted = True

root = tk.Tk()
root.title("Phylogenetic Tree Viewer")
root.configure(bg='#b5b5b5')

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

x = (screen_width - 800) // 2  
y = (screen_height - 600) // 2  

root.geometry(f"800x600+{x}+{y}")

def draw_tree():
    for widget in frame.winfo_children():
        widget.destroy()

    fig = Figure(figsize=(8, 6))
    ax = fig.add_subplot(111)
    
    Phylo.draw(rRNA_ps_tree, axes=ax, do_show=False)
    # ax.set_title("Phylogenetic Tree of 5 primates")
    ax.set_ylabel("Primates")
    ax.set_xlabel("Distance")
    
    canvas = FigureCanvasTkAgg(fig, master=frame)
    canvas_widget = canvas.get_tk_widget()
    canvas_widget.pack(side=tk.TOP, fill=tk.BOTH, expand=1)
    canvas.draw()

title_label = tk.Label(root, text="Phylogenetic Tree", font=("Arial", 24),bg = "#9A9A9A")
title_label.pack(pady=20)  

draw_button = tk.Button(root, text="Draw Tree", command=draw_tree)
draw_button.pack(pady=20)

frame = tk.Frame(root)
frame.pack()

root.mainloop()
