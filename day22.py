#Djikstra's algorithm

#graph for our djikstra example, including all nodes, sorted.
graph = {
    "1":{"2":2, "4":5},
    "2":{"1":2, "3":2, "4":2, "5":3},
    "3":{"2":2, "5":2},
    "4":{"1":5, "2":2, "5":2},
    "5":{"2":3, "3":2, "4":2}
}

START = "1"
DESTINATION = "5"

def djikstra(graph, start, dest):
    
    shortest_path = ""