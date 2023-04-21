""" 
file to set the Recusion and Iterative files to be the same for performance testing

All tests are listed and commented out for completeness 

"""
# importing the required module
import timeit

# import cProfile  # test 9
# import datetime  # Test 1 normal Timer
# from shortest_path_ptest import find_shortest_path

# starting_time = timeit.default_timer()  # Test 2 Default Timer
# start_time = datetime.datetime.now()  # Test 1 normal Timer

# Import the shortest path function
mysetup = "from shortest_path_ptest import find_shortest_path"

# code snippet whose execution time is to be measured
mycode = """
# set up the graph to use as a list
INF = 99999
#graph = [[0, 5, INF, 10], [INF, 0, 3, INF], [INF, INF, 0, 1], [INF, INF, INF, 0]]
graph = [[0, 5, INF, 5], [INF, 0, 3, INF], [INF, INF, 0, 2], [INF, 3, INF, 0]]
# calculate shorteat path
shortest_path = find_shortest_path(0, 0, 0, graph, 4)
#print(shortest_path)

"""

# timeit & cProfile statement used to test the code

# end_time = datetime.datetime.now()  # Test 1 normal Timer
# print(end_time - start_time)  # Test 1 normal Timer
# print(
#    "Time difference :", timeit.default_timer() - starting_time
# )  # Test 2 Default Timer
# print(timeit.timeit(setup=mysetup, stmt=mycode, number=1))  # Test 3
# print(timeit.timeit(setup=mysetup, stmt=mycode, number=10000))  # Test 4
# print(timeit.timeit(setup=mysetup, stmt=mycode, number=10))  # Test 5
# print(min(timeit.repeat(setup=mysetup, stmt=mycode, number=10)))  # Test 6
# print(min(timeit.repeat(setup=mysetup, stmt=mycode,number=10000)))  # Test 7
print(
    min(timeit.repeat(setup=mysetup, stmt=mycode, repeat=1000, number=1000000))
)  # Test 8
# cProfile.run(mycode)  # Test 9
# print(min(timeit.repeat(setup=mysetup, stmt=mycode, number=10000))) #Test 10 - new graph
