from pymoo.algorithms.moo.moead import MOEAD
from pymoo.factory import get_problem, get_reference_directions
from time import sleep
from pythonosc import udp_client
import numpy as np
import matplotlib.pyplot as plt
from pymoo.visualization.scatter import Scatter

problem = get_problem("zdt1")

ref_dirs = get_reference_directions("das-dennis", 2, n_partitions=100)
algorithm = MOEAD(ref_dirs, n_neighbors=15, prob_neighbor_mating=0.7)

# prepare the algorithm to solve the specific problem
algorithm.setup(problem, ('n_gen', 250), seed=1)
iteration_number = 0
sleep(2)

# until the algorithm has no terminated
while algorithm.has_next():
    
    # do the next iteration
    algorithm.next()
    
    ######### format the approximation set and send it over to SonOpt via OSC #######
    approximation_set = algorithm.result().F
    obj_one = ['{:f}'.format(item) for item in approximation_set[:, 0]]
    obj_two = ['{:f}'.format(item) for item in approximation_set[:, 1]]
    objs_combined = [obj_one, obj_two]
    formatted_approximation_set = [' '.join(str(item) for item in column) for column in zip(*objs_combined)]
    client_a = udp_client.SimpleUDPClient("127.0.0.1", 5002)
    client_a.send_message("start", formatted_approximation_set)
    sleep(0.3)
    ################
    
plt.figure(figsize=(7, 5))
plt.scatter(approximation_set[:, 0], approximation_set[:, 1], s=35, facecolors='none', edgecolors='blue')
plt.title("Objective Space")
plt.show()
