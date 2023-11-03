from Bio import AlignIO
import matplotlib.pyplot as plt
import numpy as np

clw_file = "five_primate/code/align_ms5.clw"
alignment = AlignIO.read(clw_file, "clustal")

step_size = 200  

# Convert the alignment to a numpy array of characters
alignment_array = np.array([list(rec.seq) for rec in alignment], dtype=np.character)

# Convert characters to numeric values (ASCII codes)
alignment_numeric = np.array(
    [[ord(char) for char in seq] for seq in alignment_array], dtype=np.int64
)

tick_positions = np.arange(0, alignment.get_alignment_length(), step_size)
tick_labels = [str(pos) for pos in tick_positions]

# Plot the alignment with increased figure size, decreased font size, and adjusted tick positions
fig, ax = plt.subplots(figsize=(15, 10))
ax.set_title("Multiple Sequence Alignment", fontsize = 18)
ax.set_xticks(tick_positions)
ax.set_xticklabels(tick_labels, rotation=90, fontsize=8)  # Adjust fontsize as needed

# Draw the alignment
ax.imshow(alignment_numeric, aspect="auto", cmap="rainbow")

plt.show()
