import pandas as pd
from pathlib import Path

# from floyd_recursion2 import find_shortest_path

INF = 99999


def read_in_graph():
    for test_case in range(1):
        graph_test1 = Path(
            "C:\\Users\\610109025\\OneDrive - BT Plc\\Documents - RDM Admin\\General\\Post Grad\\sw developement\\floyd_algorithm\\graph_inputs\\graph_test1.csv"
        )
        df = pd.read_csv(graph_test1.resolve(), sep=",")
        listlengths = df.values.tolist()
        print(listlengths)
    return listlengths


def create_list(nodes):
    node_list = [[INF for i in range(nodes)] for i in range(nodes)]
    return node_list


def set_self_edge(nodes, input_graph):
    for m in range(nodes):
        for n in range(nodes):
            if m == n:
                input_graph[m][n] = 0
    return input_graph


def num_of_nodes(listlengths):
    nodes = 0
    for i in range(len(listlengths)):
        nodes = max(nodes, listlengths[i][0], listlengths[i][1])
    return nodes


def add_in_lengths(listlengths, input_graph):
    for i in range(len(listlengths)):
        source = listlengths[i][0]
        dest = listlengths[i][1]
        length = listlengths[i][2]
        input_graph[source][dest] = length
    return input_graph


def find_shortest_path(
    source_node, destination_node, interim_node, path_length, number_of_nodes
):
    """function to take a graph and find the shortest path between each pair of nodes
        input_graph = [[0, 10, INF, 30],
                  [INF, 0, 5, INF],
                  [INF, INF, 0,   7],
                  [INF, INF, INF, 0]
                  ]
                  and returns
    [[0, 10, 15, 3], [99999, 0, 5, 12], [99999, 99999, 0, 7], [99999, 99999, 99999, 0]]
    """

    if interim_node == number_of_nodes:
        return path_length

    if destination_node == number_of_nodes - 1 and source_node == number_of_nodes - 1:
        path_length[source_node][destination_node] = min(
            path_length[source_node][destination_node],
            path_length[source_node][interim_node]
            + path_length[interim_node][destination_node],
        )
        find_shortest_path(0, 0, interim_node + 1, path_length, number_of_nodes)

    elif destination_node == number_of_nodes - 1:
        path_length[source_node][destination_node] = min(
            path_length[source_node][destination_node],
            path_length[source_node][interim_node]
            + path_length[interim_node][destination_node],
        )
        find_shortest_path(
            source_node + 1, 0, interim_node, path_length, number_of_nodes
        )
    else:
        path_length[source_node][destination_node] = min(
            path_length[source_node][destination_node],
            path_length[source_node][interim_node]
            + path_length[interim_node][destination_node],
        )
        find_shortest_path(
            source_node,
            destination_node + 1,
            interim_node,
            path_length,
            number_of_nodes,
        )
        return path_length


input_graph = []


listlengths = read_in_graph()
nodes = num_of_nodes(listlengths) + 1
print("nodes", nodes)


input_graph = create_list(nodes)

# check this doesnt need a variable...??
input_graph = set_self_edge(nodes, input_graph)

print("o for self edges", input_graph)
input_graph = add_in_lengths(listlengths, input_graph)
print("after len", input_graph)


print(input_graph)

print("nodes", nodes)
number_of_nodes = len(input_graph)

short_path = find_shortest_path(0, 0, 0, input_graph, number_of_nodes)

print("shortest path", short_path)
