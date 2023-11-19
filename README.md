# CSC498_AKS
This is my project implementation for CSC498 at UTM. My project topic is showing that the AKS Primality Test is in P. So this repository contains my implementation of the AKS algorithm in Python, which is aks.py. If you want to see my report, check out aks_report.pdf.

Note: log base 2 is used is used in this implementation.

Usage: 

    python3 aks.py n
(n must be a positive integer greater than 1)

## Performance testing ##
To test the runtime of aks.py, there are 2 scripts: testPerformance and plotruntimes.

testPerformance runs the aks.py program from 1 to $INPUT_NUM, where $INPUT_NUM is how many numbers you want to test aks.py on, and records the runtime in a file called runtimes.tsv (see testPerformance file for more). The format of runtimes.tsv is as follows:

    Input [3 spaces]  Execution time (secs)

plotruntimes plots the results from runtimes.tsv onto a graph using gnuplot. The x-axis represents the input that we ran on aks.py, and the y-axis represents the execution time for that specific input on aks.py.
Currently, we plot execution time in seconds on the graph, since nanoseconds can output numbers that are very large and so it might throw an error for some computers. Hence, if you want to see the runtime in nanoseconds, it is best to run these tests on a DH Lab PC. See plotruntimes file for more.

Also, another way you can test the runtime of aks.py is by using the "time" command. 

Example (run this in the terminal):

    time python3 aks.py 107

