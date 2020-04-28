
### Null Model ###
# This code generates a graph by adding edges between grid cells.
# Each cell is considered as a node. 
# Each cell is connected to its adjacent cells i.e., (top, bottom, left & right)

import networkx as nx
import pandas as pd
import numpy as np



df = pd.read_csv('cells.csv')

cell_names = df['cell_names']
cell_ids = df['cell_id']


graph = nx.Graph()


for i in range(len(cell_ids)):

    # adding cell ids as graph nodes. 
    graph.add_node(cell_ids[i])


# # Getting range of rows and columns from last node
# size = len(list_of_names)

max_row = 0
max_col = 0

# getting max row and column to use it for assigning edges between grid cells.

for i in range(len(cell_names)):

    val = cell_names[i].split(":")
    row = int(val[0].replace("C", ""))
    col = int(val[1])

    if(max_row < row):
        max_row = row
    if(max_col < col):
        max_col = col


# reshaping 1D list into 2D array. 
# This helps in using it inside for loop and makes it easier 
# to generate edges. 
arr = np.array(cell_ids).reshape(max_row+1, max_col+1)

for i in range(max_row + 1):

    for j in range(max_col + 1):

        row_pos = i
        col_pos = j

        # getting indexes to move from the current position.

        left = max(0, col_pos - 1)
        right = min(max_col, col_pos + 1)

        top = max(0, row_pos - 1)
        bottom = min(max_row, row_pos + 1)

        # Adding edges between grid cells.
        # checking if there is a left column from current position
        if (col_pos != left):
            graph.add_edge(arr[row_pos][col_pos], arr[row_pos][left])

        # checking if there is a right column from current position
        if (col_pos != right):
            graph.add_edge(arr[row_pos][col_pos], arr[row_pos][right])

        # checking if there is a top column from the current position
        if (row_pos != top):
            graph.add_edge(arr[row_pos][col_pos], arr[top][col_pos])

        # checking if there is a bottom column from the current position
        if (row_pos != bottom):
            graph.add_edge(arr[row_pos][col_pos], arr[bottom][col_pos])

list_of_edges = list(graph.edges)

nodes = []
for i in range(len(list_of_edges)):
    nodes.append(str(list_of_edges[i]).replace("(", "").replace(")", "").replace(", ", " "))

f = open("nodes.edgelist", "w")

for i in range(len(nodes)):
    f.write(nodes[i] + "\n")

f.close()