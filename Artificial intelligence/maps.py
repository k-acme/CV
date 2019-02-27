class Edge:
    def __init(self, start, end, weight, edge_type):
        self.start = start
        self.end = end
        self.weight = weight
        self.edge_type = edge_type
class Graph:
    def __init__(self):
        self.edges = []
    
    def connect(start, end, weight, edge_type):
        edge = 