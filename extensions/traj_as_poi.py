### Traj as POI ###

# This code generates POI walks
# for Model(s). Converts Random
# walks on cells into walks on POIS.


import pandas as pd
import numpy as np
from collections import defaultdict

# cell_poi contains cell ids and poi ids
# for the pois that are inside those cells.
df = pd.read_csv('cell_poi.csv')


cell_id = df['cell_id']
poi_id = df['poi_enum']

output = []


data_dict = defaultdict(list)

for i in range(len(cell_id)):

    data_dict[int(cell_id[i])].append(int(poi_id[i]))

# print(data_dict)
# stroing walks as pois
f_walk = open("walks_poi.txt", "w")

# # real walks
with open("walks.txt") as file:

    walks = file.readlines()

for i in range(len(walks)):

    walk = str(walks[i]).replace("[", "").replace("]", "").replace(" ", "").replace("\n","").replace("\'","").split(",")

    # for maintaining proper spacing in write file.
    x = 0

    for w in walk:
 
        if(int(w) in data_dict):

            x = x + 1
            # print(w, data_dict[int(w)])
            f_walk.write(str(data_dict[int(w)]))

    if x > 0:
        f_walk.write("\n")

f_walk.close()