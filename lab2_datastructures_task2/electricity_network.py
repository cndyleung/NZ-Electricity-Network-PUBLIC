from module_lab2_task2 import *

network = NetworkElectricNZ()
network.read_network("nz_network")
network.plot_network(save="electricity_network.png")

biggest_arc = network.arcs[0]
for arcs in network.arcs:
    if biggest_arc.weight < arcs.weight:
        biggest_arc = arcs

with open("network_answers.txt", 'w') as fp:
    fp.write(f"How many nodes are there in the network?\n")
    fp.write(f"There are {len(network.nodes)} nodes in the network.\n\n")

    fp.write("How many arcs are there in the network?\n")
    fp.write(f"There are {len(network.arcs)} arcs in the network.\n\n")

    fp.write(f"What is the largest arc weight in the network? Which nodes does it join, noting the source and "
             f"destination node name.\n")
    fp.write(f"The largest arc in the network is {biggest_arc}. This arc joins the source {biggest_arc.from_node}"
             f" to the\ndestination {biggest_arc.to_node}.\n")
