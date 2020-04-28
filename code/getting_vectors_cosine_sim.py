import numpy as np
import time
#from pprint import pprint


def cos_sim(a, b):
    """Takes 2 vectors a, b and returns the cosine similarity according
    to the definition of the dot product
    """
    dot_product = np.dot(a, b)
    norm_a = np.linalg.norm(a)
    norm_b = np.linalg.norm(b)
    return dot_product / (norm_a * norm_b)


def getting_vector_cosine_sim(vector_file_01, vector_file_02): # null_nodes, real_nodes

    #Return the vectors and labels for the first n_words in vector file.
    
    # null nodes
    numpy_array_01 = []
    labels_array_01 = [] 


    # real nodes
    numpy_array_02 = []
    labels_array_02 = []

    # first embedding file
    with open(vector_file_01, 'r') as f:
        for c, r in enumerate(f):
            sr = r.split()

            # storing all the labels
            labels_array_01.append(int(sr[0]))

            # storing all the vectors
            numpy_array_01.append(np.array([float(i) for i in sr[1:]]))

 
    labels_array_01.pop(0)
    numpy_array_01.pop(0)



    with open(vector_file_02, 'r') as f:
        for c, r in enumerate(f):
            sr = r.split()

            # storing all the labels
            labels_array_02.append(int(sr[0]))

            # storing all the vectors
            numpy_array_02.append(np.array([float(i) for i in sr[1:]]))

    labels_array_02.pop(0)
    numpy_array_02.pop(0)



    # storing cell_ids and their embedded vectors in dict.
    # dict gives nearly constant time searching.
    
    null_dict = {}

    for i in range(len(labels_array_01)):
        null_dict.update({labels_array_01[i]: numpy_array_01[i]})



    real_dict = {}

    for i in range(len(labels_array_02)):
        real_dict.update({labels_array_02[i]: numpy_array_02[i]})



    i = min(labels_array_01)

    if i > int(min(labels_array_02)):
        i = int(min(labels_array_02))

    m = max(labels_array_01)

    if m < int(max(labels_array_02)):
        m = int(max(labels_array_02))

    print(i)
    print(m)

    f_cos_sim = open("cos_sim.csv", "w")
    f_cos_sim.write("node1,node2,null_cos_sim,real_cos_sim,diff\n")


    start = time.time()


    # two while loops only get n*(n-1) / 2 pairs out of cell nodes. (Avoid comparing similar nodes)

    while i < m:

        j = i + 1

        while j <= m:

            # storing node combinations and cosine similarity of null model values.
            f_cos_sim.write(str(i) + "," + str(j) + ",")

            if (i in null_dict) and (j in null_dict):

                if(cos_sim(null_dict[i], null_dict[j]) > 0):
                    f_cos_sim.write(str(cos_sim(null_dict[i], null_dict[j])) + ",")
                else:
                    f_cos_sim.write("less,")

            else:

                f_cos_sim.write("infinite,")

            # writing cosine similarity and it's difference if the nodes exist in real model.
            if (i in real_dict) and (j in real_dict):

                if(cos_sim(real_dict[i], real_dict[j]) > 0):

                    f_cos_sim.write(str(cos_sim(real_dict[i], real_dict[j])) + ",")
                else:

                    f_cos_sim.write("less,")


            # writing infinite if the nodes doesn't exist.
            else:

                f_cos_sim.write("infinite,")

            if (i in null_dict) and (j in null_dict) and (i in real_dict) and (j in real_dict):

                if (cos_sim(null_dict[i], null_dict[j]) > 0) and (cos_sim(real_dict[i], real_dict[j]) > 0):

                    f_cos_sim.write(str(abs(cos_sim(null_dict[i], null_dict[j]) - cos_sim(real_dict[i], real_dict[j]))) + "\n")

                else:

                    f_cos_sim.write("less\n")

            else:

                f_cos_sim.write("infinite\n")


            j = j + 1

        i = i + 1

    end = time.time()

    print(end - start)


getting_vector_cosine_sim('null_model.emb', 'real_model.emb')

