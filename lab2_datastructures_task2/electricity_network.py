from module_lab2_task2 import *

ntwk = NetworkElectricNZ()
ntwk.read_network("nz_network")
ntwk.plot_network(save="electricity_network.png")

biggest_arc = ntwk.arcs[0]
for arcs in ntwk.arcs:
    if biggest_arc.weight < arcs.weight:
        biggest_arc = arcs

with open("network_answers.txt", 'w') as fp:
    fp.write(f"There are {len(ntwk.nodes)} nodes in the network.\n\n")

    fp.write(f"There are {len(ntwk.arcs)} arcs in the network.\n\n")

    fp.write(f"The largest arc in the network is {biggest_arc}.\n\n")
    fp.write(f"The source node is {biggest_arc.from_node}.\n\n")
    fp.write(f"The destination node is {biggest_arc.to_node}.\n\n")
    fp.write(f"This arc joins {biggest_arc.from_node} to {biggest_arc.to_node}.\n\n")