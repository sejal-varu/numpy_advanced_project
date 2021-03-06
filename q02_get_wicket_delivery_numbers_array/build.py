#Default Imports
import numpy as np

ipl_matches_array =np.genfromtxt("data/ipl_matches_small.csv", dtype="|S50", skip_header=1, delimiter=",")

#Your Solution
def get_wicket_delivery_numbers_array(player):
    played_out = ipl_matches_array[:,[11,20]]
    return played_out[played_out[:,1] == player][:,0]
