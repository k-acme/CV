import math
def log2(v):
    return math.log(v)/math.log(2)
class Edge:
    def __init__(self, n1, n2):
        self.nodes = (n1, n2)
    
    def contains(self, n):
        return n in self.nodes
    
    def get_child(self, n):
        if n == self.nodes[0]:
            return self.nodes[1]
        elif n == self.nodes[1]:
            return self.nodes[0]
        else:
            return None
        
    def directed_equal(self, e):
        return self.nodes == e.nodes
    
    def undirected_equal(self, e):
        return self.nodes == e.nodes or (self.nodes[1] == e.nodes[0] and self.nodes[0] == e.nodes[1])


class Graph:
    def __init__(self):
        self.edges = []
        
    def create_graph(self, graph):
        for k, v in graph.items():
            for n in v:
                self.connect(k, n)
        
    def get_children(self, n):
        children = []
        for edge in self.edges:
            if edge.contains(n) and edge.get_child(n) not in children:
                children.append(edge.get_child(n))
        return children
    
    def connect(self, n1, n2):
        e = Edge(n1, n2)
        e_temp = Edge(n2, n1)
        if e not in self.edges and e_temp not in self.edges:
            self.edges.append(e)
            
    def iter_dfs(self, start, limit, goal = None):
        visited = []
        stack = [(start, 0)]
        level = 0
        while stack:
            node, level= stack.pop()
            visited.append(node)
            children = self.get_children(node)
            
            #for goal 
            if goal != None:
                if node == goal:
                    print("Goal reached")
                    return visited
                
            
            added = False
            if level < limit:
                children.reverse()
                for child in children:
                    if child not in visited:
                        added = True
                        stack.append((child, level + 1))
                if added:
                    level += 1
                else:
                    level -= 1
        if goal != None:            
            print("Goal not reached")
        return visited
            

g = Graph()

cityGraph = {
'Arad':['Zerind','Sibiu','Timisoara'],
'Bucharest':['Fagaras','Pitesti','Urziceni','Giurgiu'],
'Craivoa':['Rimnicu Vilcea','Pitesti','Dobreta'],
'Dobreta':['Mehadia','Craiova'],
'Eforie':[],
'Fagaras':['Sibiu','Bucharest'],
'Giurgiu':[],
'Hirsova':['Urziceni','Eforie'],
'Iasi':['Neamt','Vaslui'],
'Lugoj':['Timisoara','Mehadia'],
'Mehadia':['Lugoj','Dobreta'],
'Neamt':[],
'Oradea':['Zerind','Sibiu'],
'Pitesti':['Rimnicu Vilcea','Bucharest','Craiova'],
'Rimnicu Vilcea':['Sibiu','Pitesti','Craiova'],
'Sibiu':['Oradea','Arad','Fagaras','Rimnicu Vilcea'],
'Timisoara':['Arad','Lugoj'],
'Urziceni':['Vaslui','Hirsova','Bucharest'],
'Vaslui':['Iasi','Urziceni'],
'Zerind':['Oradea','Arad']
}
g.create_graph(cityGraph)

for i in range(14):
    print("limit: " + str(i))
    print(g.iter_dfs('Oradea', i, 'Rimnicu Vilcea'))

        
    


                
