import networkx  as nx
import matplotlib.pyplot as plt

# initialize graph
G = nx.Graph()

#Dictionaries to contain population values
SIR = { 'S' : 0, 'I' : 0, 'R' : 0}

#Dictionary to contain constants
ABC = { 'A' : 0, 'B' : 0, 'C' : 0}
p = [123,123]
G = nx.Graph()
G.add_nodes_from([('MA',SIR),('FL',SIR), ('CT', SIR)])

G.add_edges_from([('MA','FL',ABC),('MA','CT',ABC)])

G.add_path([1,2,3,4])
print G.neighbors('MA')
print [i for i in G.neighbors_iter('MA')]
#update node values
#G.node['MA'] = 400

#print G.node['MA']
#print (G.nodes())

nx.draw(G)
plt.show()

