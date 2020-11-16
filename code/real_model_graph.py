### Real Model ###

# This code generates walks of trajectory paths based on cells ids. 
# It outputs trajectory paths as list of cell ids.

import numpy as np
import pandas as pd
from collections import defaultdict

df = pd.read_csv('traj_as_cells_sample_10000.csv')

traj_id = df['traj_id']
cell_id = df['cell_id']

# Keeping distinct traj id's.
# As one traj ids appears multiple times.
# This helps us in storing all the cell id's
# against a single traj id i.e., the cells through
# which trajectory has passed.


arr = np.array(traj_id)
output = np.unique(arr)
data_dict = defaultdict(list)

for i in range(len(traj_id)):

    data_dict[int(traj_id[i])].append(int(cell_id[i]))

#print(data_dict)


f_walk = open("walks.txt", "w")

for i in range(len(output)):

    if int(output[i]) in data_dict:

        f_walk.write(str(data_dict[int(output[i])]) + "\n")
        # print(output[i])

f_walk.close()




