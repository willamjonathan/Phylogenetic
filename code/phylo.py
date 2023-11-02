from Bio import Phylo
from Bio.Phylo.TreeConstruction import DistanceCalculator
from Bio.Phylo.TreeConstruction import DistanceTreeConstructor
from Bio import AlignIO

with open("code/align_ms5.clw", "r") as aln:
    alignment = AlignIO.read(aln, "clustal")
    print(type(alignment))

calculator = DistanceCalculator("identity")
distance_matrix = calculator.get_distance(alignment)
print(distance_matrix)

constructor = DistanceTreeConstructor(calculator)
rRNA_ps_tree = constructor.build_tree(alignment)
rRNA_ps_tree.rooted = True
print(rRNA_ps_tree)

Phylo.draw_ascii(rRNA_ps_tree)
