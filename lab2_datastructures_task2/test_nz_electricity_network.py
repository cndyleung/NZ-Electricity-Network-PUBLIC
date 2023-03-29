import pytest
from module_lab2_task2 import *


# MODULE 1 UNIT TESTT
def test_add_node():
    test = Network()

    test.add_node('CINDY', 19)
    assert test.nodes[0].name == 'CINDY'
    assert test.nodes[0].value == 19
    assert len(test.nodes) == 1

    test.add_node('node_no_value')
    assert test.nodes[1].name == 'node_no_value'
    assert test.nodes[1].value is None
    assert len(test.nodes) == 2


# MODULE 2 UNIT TEST
def test_add_arc():
    test = Network()

    node_a = Node('A')
    node_b = Node('B')

    test.add_node(node_a)
    test.add_node(node_b)

    test.add_arc(node_a, node_b, 56)

    assert test.arcs[0].from_node == node_a
    assert test.arcs[0].to_node == node_b
    assert test.arcs[0].weight == 56

    assert len(test.arcs) == 1

    assert len(node_a.arcs_out) == 1
    assert node_a.arcs_out[0] == test.arcs[0]

    assert len(node_b.arcs_in) == 1
    assert node_b.arcs_in[0] == test.arcs[0]


# MODULE 3 UNIT TEST
def test_read_network():
    test = Network()

    test.read_network('network.txt')

    assert(len(test.nodes) == 6)
    assert(len(test.arcs) == 9)

    assert test.nodes[2].name == 'C'
    assert test.arcs[7].weight == 2.0
