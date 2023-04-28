# floyd_algorithm

# Description
A program implementing the Floyd-Warshall algorithm for computing the quickest route between any two given vertices. 
The algorithm is written in Python.
# Prerequisites
requirements.txt file for required imports
# Getting Started
The Shortest_path.py file contains all the code to assess the shortest path for any given route in a graph.  
The following .py files are used to performance test the algoritm
    1) shortest_path__ptest - set up to make the recursive and iterative files the same such that only the path function is different.
    2) shortest_parth_performance-testing - details the time tests performed 
    3) shortest_parth_iterative_performance-testing - details the time tests performed for iterative version
    4 shortest_path_iterative - iterative version provided by Mythri J L to use in performance testing. 
The Test area contains unittests for the shortest_parth funtions. 
The Graph area supplies some Graph examples   
# Usage
The main function in the program is:
find_shortest_path(
    source_node: int,
    destination_node: int,
    interim_node: int,
    path_length: list,
    number_of_nodes: int,
) -> list:

The graph_inputs area gives example graphs in a [source, destination, length] format which can be read into the shortest_path.py file.
The following functions are used to manipulate the code from raw file input to a usable form for the shortest_path function.
    - read_in_graph()
    - create_list(node: int)
    - set_self_edge(node_count: int, input_graphs: list)
    - num_of_nodes(listlength: list)
    - add_in_lengths(listlength: list, input_graphs: list) 

# Output Example
For example an input of
Graph - [[0, 2, 1, 3],[99999, 0, 2, 99999],[99999, 99999, 0, 1],[99999, 99999, 99999, 0]

![image](https://user-images.githubusercontent.com/129500210/233634850-0216aba5-287b-4bac-9a62-7891408de435.png)


Outputs
path_length = [[0, 2, 1, 2],[99999, 0, 2, 3],[99999, 99999, 0, 1],[99999, 99999, 99999, 0]]





# Authors
Rachael Duppa-Miller                            
The Iterative version used for performance testing is contributed by Mythri J L
________________________________________
# MIT License

Copyright 2023 Rachael Duppa-Miller

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
