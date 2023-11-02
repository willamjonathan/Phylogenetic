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

# Create a tkinter window
root = tk.Tk()
root.title("Phylogenetic Tree Viewer")

# Function to draw the tree with custom design
def draw_tree():
    # Clear previous drawings
    for widget in frame.winfo_children():
        widget.destroy()

    # Draw the tree with custom design elements
    fig = Figure(figsize=(8, 6))
    ax = fig.add_subplot(111)
    
    # Customize tree visualization (add labels, colors, etc.)
    for clade in rRNA_ps_tree.find_clades():
        if clade.is_terminal():
            clade.branch_color = "#87CEFA"  # Light Sky Blue in hexadecimal
            clade.label = clade.name  # Use sequence names as labels
    
    Phylo.draw(rRNA_ps_tree, axes=ax, do_show=False)
    ax.set_title("Phylogenetic Tree")
    
    canvas = FigureCanvasTkAgg(fig, master=frame)
    canvas_widget = canvas.get_tk_widget()
    canvas_widget.pack(side=tk.TOP, fill=tk.BOTH, expand=1)
    canvas.draw()

# Button to draw the tree
draw_button = tk.Button(root, text="Draw Tree", command=draw_tree)
draw_button.pack()

# Frame to contain the tree visualization
frame = tk.Frame(root)
frame.pack()

# Run the tkinter main loop
root.mainloop()
