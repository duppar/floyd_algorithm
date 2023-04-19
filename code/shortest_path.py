"""python Program for Floyd Warshall Algorithm to find the shortest paths in a graph"""
from pathlib import Path
import pandas as pd

# Define infinity as the large value
# so that a given path will never be chosen for route of the shortest path
INF = 99999


def read_in_graph():
    """function to read in graphs from an excel file in the form of routes in to a dataframe
    dataframe =
        Source  destination  length
    0       0            1       3
    1       0            3       5
    2       1            2       5
    3       2            3       9

    The dataframe is then converted to a list to be used to create
      the input graph for the shortest path function.
    listlengths =
        [[0, 1, 3], [0, 3, 5], [1, 2, 5], [2, 3, 9]]
    """
    # path is initialised as the repository for input graphs
    graph_test1 = Path(
        "C:\\Users\\610109025\\OneDrive - BT Plc\\Documents - RDM Admin\\General\\Post Grad\
                \\sw developement\\floyd_algorithm\\graph_inputs\\graph_test2.csv"
    )
    dataframe = pd.read_csv(graph_test1.resolve(), sep=",")
    listlength = dataframe.values.tolist()
    print(listlength)
    return listlength


def create_list(node):
    """
    Function to create a graph for an inputted number of nodes all with infinite length
    """
    node_list = [[INF for i in range(node)] for i in range(node)]
    return node_list


def set_self_edge(node_count, input_graphs):
    """
    Function to set to route for each node to itself as zero so it does not add to the shortest path
    """
    for source_node in range(node_count):
        for destination_node in range(node_count):
            if source_node == destination_node:
                input_graphs[source_node][destination_node] = 0
    return input_graphs


def num_of_nodes(listlength):
    """
    function to look at the list of routes defined in the input graph file
    to calcualte the number of nodes in the graph
    """
    node = 0
    routes_in_file = len(listlength)
    for i in range(routes_in_file):
        node = max(node, listlength[i][0], listlength[i][1])
    return node


def add_in_lengths(listlength, input_graphs):
    """ "
    Function to add the defined route lengths from the input graph file
    in to hte graph to be calculated in the shortest route function
    """
    routes_in_file = len(listlength)
    for i in range(routes_in_file):
        source = listlength[i][0]
        dest = listlength[i][1]
        length = listlength[i][2]
        input_graphs[source][dest] = length
    return input_graphs


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


# initialise input_graph as an empty list
input_graph = []
# read in the routes and lengths
listlengths = read_in_graph()
# pull back the number of nodes in teh graph
nodes = num_of_nodes(listlengths) + 1
# create a graph all with infinite lengths for the number
# of nodes retrieved in the num_of_nodes function
input_graph = create_list(nodes)
# set the routes between a node and itselve to zero
# so no distance is added in the shortest path function
input_graph = set_self_edge(nodes, input_graph)
# add in the possible routes and lengths from the listlengths added in
input_graph = add_in_lengths(listlengths, input_graph)
# calculate the shortest path between each pair of nodes
shortest_path = find_shortest_path(0, 0, 0, input_graph, nodes)
print(shortest_path)
