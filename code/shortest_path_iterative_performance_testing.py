""" file to set the Recusion and Iterative files to be the same to perform performance testing"""
# Import the shortest path function
from shortest_path_iterative import floydWarshall

# set up the graph to use as a list
INF = 99999
graph = [[0, 5, INF, 10], [INF, 0, 3, INF], [INF, INF, 0, 1], [INF, INF, INF, 0]]
# calculate shorteat path
shortest_path = floydWarshall(graph)
print(shortest_path)
