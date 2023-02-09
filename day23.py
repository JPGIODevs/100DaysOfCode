#Djikstra's algorithm

import sys
from heapq import heapify, heappush

def djikstra(graph, start, dest):
    inf = sys.maxsize
    node_data = {
    "A":{"cost":inf, "predecessor":[]},
    "B":{"cost":inf, "predecessor":[]},
    "C":{"cost":inf, "predecessor":[]},
    "D":{"cost":inf, "predecessor":[]},
    "E":{"cost":inf, "predecessor":[]},
    "F":{"cost":inf, "predecessor":[]}
    }

    node_data[start]["cost"] = 0
    visited = []
    temp = start

    for i in range(5):
        
        if temp not in visited:
            visited.append(temp)

            min_heap = []

            for j in graph[temp]:

                if j not in visited:

                    cost = node_data[temp]["cost"] + graph[temp][j]
                    if cost < node_data[j]["cost"]:
                        node_data[j]["cost"] = cost
                        node_data[j]["predecessor"] = node_data[temp]["predecessor"] + list(temp)
    
                    heappush(min_heap, (node_data[j]["cost"],j))
                    print(min_heap)

                heapify(min_heap)   
                temp = min_heap[0][1]

            print("shortest distance: "+ str(node_data[dest]["cost"]))
            print("shortest path: "+ str(node_data[dest]["predecessor"] + list(dest)))

#graph for our djikstra example, including all nodes, sorted.
if __name__ == "__main__":
    graph = {
        "A":{"B":2, "C":4},
        "B":{"A":2, "C":3, "D":8},
        "C":{"A":4, "B":3, "E":5, "D":2},
        "D":{"B":8, "C":2, "E":11, "F":22},
        "E":{"C":5, "D":11, "F":1},
        "F":{"D":22, "E":1}
    }

    START = "A"
    DESTINATION = "F"

    djikstra(graph, START, DESTINATION)
