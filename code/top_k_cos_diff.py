import numpy as np
import pandas as pd
import time
import csv

# storing cosine similarity difference
# between real, intermediate and null model

def cos_sim_diff():

    df = pd.read_csv('cos_sim.csv')

    # fetching all the columns from file.
    diff = df['diff']

    f = open("diff_cos_sim.txt", "w")

    cleaned = []

    for i in range(len(diff)):

        if (diff[i] != "less") and (diff[i] != "infinite"):
            cleaned.append(float(diff[i]))

    # # reverse sorting to show the plot from highest to lowest.
    cleaned = sorted(cleaned, reverse=True)
    #
    for i in range(len(cleaned)):
        f.write(str(cleaned[i]) + "\n")

    f.close()

cos_sim_diff()

# sampling real nodes that are not infinite i.e., node pair doesn't exist
# and also not less i.e., cosine similarity less than zero.
def sample_nodes():

    df_real_null = pd.read_csv("cos_sim_porto_ten.csv")

    real_cos = df_real_null['real_cos_sim']
    node1_null = df_real_null['node1']
    node2_null = df_real_null['node2']

    # storing nodes that are part of real model
    file_nodes = open("sample_nodes.csv", "w")
    file_nodes.write("node1,node2\n")

    for i in range(len(real_cos)):

        if(real_cos[i] != "infinite") and (real_cos[i] != "less"):

            file_nodes.write(str(node1_null[i]) + "," + str(node2_null[i]) + "\n")


    file_nodes.close()

sample_nodes()

# This function creates a file
# to store only cosine similarities
# for real, intermediate and null model
# for the nodes existing in real model.
def sample_cos():

    df_nodes = pd.read_csv("sample_nodes.csv")

    # Taking nodes which are part of real model
    node1 = df_nodes['node1']
    node2 = df_nodes['node2']

    # reading through cosine similarity comparison between real, intermediate and null models.
    df_null = pd.read_csv("cos_sim_porto_ten.csv")
    df_inter = pd.read_csv("cos_sim_porto_ten_10.csv")

    # Taking columns from real_inter model
    # value
    real = df_inter['real_cos_sim']
    inter = df_inter['null_cos_sim']

    #key
    node1_inter = df_inter['node1']
    node2_inter = df_inter['node2']


    # making dictionary of real and intermediate cosine similarities
    dict_inter = pd.Series(list(zip(real,inter)), index=list(zip(node1_inter, node2_inter))).to_dict()

    # Taking columns from real_null model
    #value
    null = df_null['null_cos_sim']

    # key
    node1_null = df_null['node1']
    node2_null = df_null['node2']

    # making dictionary of null cosine similarities
    dict_null = pd.Series(null.values, index=list(zip(node1_null,node2_null))).to_dict()


    file_plot = open("plot_nodes.csv", "w")
    file_plot.write("node1,node2,real_cos,inter_cos,null_cos\n")

    for i in range(len(node1)):

        # storing the nodes from intermediate and null cosine similarities which are part of real model.
        # looking into dict_inter only because dict_null contains all the nodes.
        if tuple((node1[i],node2[i])) in dict_inter:

            file_plot.write(str(node1[i]) + "," + str(node2[i]) + "," + str(dict_inter[tuple((node1[i],node2[i]))]) + "," + str(dict_null[tuple((node1[i],node2[i]))])  +"\n")


    file_plot.close()
sample_cos()

# we remove the nodes that contains infinite or less values for nodes
def clean_plots():

    file_clean = open("clean_plots_porto.csv", 'w')

    with open("plot_nodes.csv","r") as csvFile:

        reader = csv.reader(csvFile)

        index = 0
        for row in reader:

            if index == 0:
                file_clean.write(str(row).replace("[","").replace("]","").replace("'","").replace(" ","") + "\n")
                index = index + 1

            elif str(row).__contains__("less") or str(row).__contains__("infinite"):
                print(row)

            else:
                file_clean.write(str(row).replace("[", "").replace("]", "").replace("'", "").replace(" ","").replace("\"", "").replace("(","").replace(")","") + "\n")

    file_clean.close()

clean_plots()

# finding how many pair of nodes has
# higher cosine similarity in real than null model
def higher_cos_sim():

    df_clean = pd.read_csv("clean_plots.csv")


    real_cos = df_clean['real_cos']
    null_cos = df_clean['null_cos']

    higher = 0

    for i in range(len(real_cos)):

        if real_cos[i] > null_cos[i]:
            higher = higher + 1


    print(len(real_cos))
    print(higher)
    print((higher / (len(real_cos))) * 100)


higher_cos_sim()






















