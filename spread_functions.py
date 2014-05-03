from scipy.integrate import odeint
import numpy as np
import networkx as nx

def spread (graph, start, t_interval, end):
    neighbors = G.neighbors