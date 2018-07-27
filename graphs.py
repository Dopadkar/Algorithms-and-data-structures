import networkx as nx
import matplotlib.pyplot as plt
import jupyter

%matplotlib inline

G = nx.Graph()
G.add_node(1)
G.add_nodes_from([2.3,4])

nx.draw_networkx(G,node_color='green',node_size=700)
