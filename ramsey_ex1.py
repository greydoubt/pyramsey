'''    Ramsey's Theorem

Ramsey's Theorem states that any graph with a large enough number of nodes must contain a complete subgraph of a certain size, or an independent set of a certain size. We can use Python to prove this theorem for a particular set of values. '''

import networkx as nx

G = nx.complete_graph(5)
print(nx.ramsey_R2(G))


#Output: (3, (0, 1, 2))

# This means that in a complete graph with 5 nodes, there must be either a complete subgraph of size 3 or an independent set of size 3.