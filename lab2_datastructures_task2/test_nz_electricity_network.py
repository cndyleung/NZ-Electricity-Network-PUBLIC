import pytest
from module_lab2_task2 import *


def test_add_node():
    test = Network()
    test.add_node('C', 1)
    assert test.nodes[0].name == 'C'
    assert test.nodes[0].value == 1


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


def test_read_network():
    test = Network()
    test.read_network('network.txt')
    assert(len(test.nodes) == 6)
    assert(len(test.arcs) == 9)
