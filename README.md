# floyd_algorithm

# Description
A program implementing the Floyd-Warshall algorithm for computing the quickest route between any two given vertices
This project uses the Floyd-Warshall algorithm to find the shortest path between two vertices in a weighted graph using Python. 
# Prerequisites
requirements.txt file for required imports
# Getting Started
The main function in the program is:
find_shortest_path(
    source_node: int,
    destination_node: int,
    interim_node: int,
    path_length: list,
    number_of_nodes: int,
) -> list:


The function takes several parameters. 
path_length = [[0, 10, 15, 3], [99999, 0, 5, 12], [99999, 99999, 0, 7], [99999, 99999, 99999, 0]]
print(shortestPath(nodes, weights, 1, 2)) #print quickest path between from 1 to 2 for graph 1


# Outputs:

##Graphs The following graphs are included and used in the unit test.





# Authors
•	Rachael Duppa-Miller
________________________________________
# License
This project is licensed under the MIT License.
Copyright 2023 Rachael Duppa-Miller
######Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
######The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
######THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
