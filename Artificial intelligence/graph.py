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
        
    def get_children(self, n):
        children = []
        for edge in self.edges:
            if edge.contains(n):
                children.append(edge.get_child(n))
        return children
    
    def connect(self, n1, n2):
        e = Edge(n1, n2)
        e_temp = Edge(n2, n1)
        if e not in self.edges and e_temp not in self.edges:
            self.edges.append(e)
            
    def iter_dfs(self, start, limit):
        visited = []
        stack = [(start, 0)]
        level = 0
        while stack:
            node, level= stack.pop()
            visited.append(node)
            children = self.get_children(node)
            
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
        return visited
            

g = Graph()
g.connect('a', 'b'); g.connect('a', 'c')
g.connect('b', 'd'); g.connect('b', 'e')
g.connect('c', 'f'); g.connect('c', 'g')
g.connect('d', 'h')
g.connect('f', 'i'); g.connect('f', 'j')
g.connect('h', 'k')
g.connect('i', 'l'); g.connect('i', 'm')
g.connect('j', 'n')



for i in range(5):
    print("limit: " + str(i))
    print(g.iter_dfs('a', i))

        
    


                