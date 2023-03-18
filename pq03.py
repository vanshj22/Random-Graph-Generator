"""Q3) Generate at random 10 different simple graphs each with 20 vertices so that each such graph is equally likely to be generated."""

import networkx as nx                           #library to import graph related functions(to install enter "pip install networkx[default]" )
import matplotlib.pyplot as plt                  
from string import ascii_lowercase

labelsdict = {} 

#gnp_random_graph(n,p), where 'n' refers to number of nodes 
#and 'p' corresponds to the case(p=0.5) where all (2^(nC2)) graphs on n vertices are chosen with equal probability.

for i in range (10):
    G = nx.gnp_random_graph(20,0.5)             

    for j, node in enumerate(G.nodes()):        #assigns node labels to each node
        labelsdict[node] = ascii_lowercase[j] 

    print("GRAPH ",i+1,"------------------------------------------------------->")

    print("\nEdge Pairs:-") 
    print("G = ",nx.edges(G),)                  #prints edge pairs of each node
    
    print("Degree Sequence:-")                  #prints Degree Sequence of each node
    for k in range(len(labelsdict)):
        deg = G.degree[k]
        print(labelsdict[k],": ",deg)
    print("\n")

    nx.draw(G, pos= nx.circular_layout(G), labels=labelsdict, with_labels=True, font_size=14)    #draws and displays the graph 
    plt.show()
