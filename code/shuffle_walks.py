import random
import pandas as pd
import numpy as np


def intermediate_model():
    # Reading entire grid cells.
    df = pd.read_csv('..\\cells.csv')

    # storing individual columns

    cell_ids = df['cell_id']
    cell_names = df['cell_names']

    max_row = 0
    max_col = 0

    # getting max row and column
    for i in range(len(cell_names)):

        val = cell_names[i].split(":")
        row = int(val[0].replace("C", ""))
        col = int(val[1])

        if (max_row < row):
            max_row = row
        if (max_col < col):
            max_col = col

    # reshaping 1D list into 2D array.
    # This helps in using it inside for loop
    arr = np.array(cell_ids).reshape(max_row + 1, max_col + 1)

    # Reading original walks.
    with open("..\\walks_ten.txt") as file:

        walks = file.readlines()

    # Creating walks for Intermediate Model which keeps
    # first node same as real model and rest of the nodes
    # are picked uniformly randomly from the current node.
    s_walk = open("..\\walks_inter_10.txt", "w")

    store_dict = {}

    # storing cell_id and cell_names as key/value pairs.
    for i in range(len(cell_ids)):
        store_dict.update({str(cell_ids[i]): cell_names[i]})

    walk = []

    # stores each walk created
    shuffle_all = []

    # Traversing through all the real walks.
    for i in range(len(walks)):

        walk = list(
            walks[i].replace("[", "").replace("]", "").replace(" ", "").replace("\n", "").split(","))

        # Getting first element of the array.
        first = walk.pop(0)

        shuffle_all.append(str(first).replace("'", ""))

        row = 0
        col = 0

        # finding first element and getting its location in the grid.
        if (str(first) in store_dict):
            val = str(store_dict[str(first)]).split(":")
            row = int(val[0].replace("C", ""))
            col = int(val[1])

        # range = avg - average of real walks
        for i in range(15):

            row_pos = row
            col_pos = col

            # getting indexes to move from the current position.

            left = max(0, col_pos - 1)
            right = min(max_col, col_pos + 1)

            top = max(0, row_pos - 1)
            bottom = min(max_row, row_pos + 1)

            # stores cell_ids from the current location
            current = []

            # checking if there is a left column from current position
            if (col_pos != left):
                current.append(arr[row_pos][left])

            # checking if there is a right column from current position
            if (col_pos != right):
                current.append(arr[row_pos][right])

            # checking if there is a top column from the current position
            if (row_pos != top):
                current.append(arr[top][col_pos])

            # checking if there is a bottom column from the current position
            if (row_pos != bottom):
                current.append(arr[bottom][col_pos])

            # Getting one cell id uniformly randomly.
            current_ele = random.choice(current)

            shuffle_all.append(str(current_ele))

            if (str(current_ele) in store_dict):
                val = str(store_dict[str(current_ele)]).split(":")
                row = int(val[0].replace("C", ""))
                col = int(val[1])

        s_walk.write(str(shuffle_all) + "\n")

        # creating k perturbations for every shuffled walk
        for k in range(9):
            
            random.shuffle(shuffle_all)
            s_walk.write(str(shuffle_all) + "\n")

        shuffle_all.clear()

    s_walk.close()


# This function returns average of real walks.
def average_of_cell_walks():
    with open("..\\walks_ten.txt") as file:
        walks = file.readlines()

    sum_of_walks_size = 0

    for i in range(len(walks)):
        walk = list(
            walks[i].replace("[", "").replace("]", "").replace(" ", "").replace("\n", "").replace("'", "").split(","))

        sum_of_walks_size = sum_of_walks_size + int((len(walk)))

    avg = sum_of_walks_size / int(len(walks))

    return avg


# We take real walks and add (k=9) perturbations for each walk.
def k_walk_perturbations():
    with open("..\\walks_ten.txt") as file:

        walks = file.readlines()

    s_walk = open("..\\walks_ten_10.txt", "w")

    walk = []

    for i in range(len(walks)):

        walk = list(walks[i].replace("[", "").replace("]", "").replace(" ", "").replace("\n", "").split(","))

        s_walk.write(str(walk) + "\n")

        for k in range(9):

            random.shuffle(walk)
            s_walk.write(str(walk) + "\n")

    s_walk.close()

k_walk_perturbations()
intermediate_model()
print(average_of_cell_walks())
