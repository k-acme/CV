class Node:
    def __init__(self, name):
        self.name = name;
        self.connected_to = []
    
    def connect_to(self, node):
        should_add = True
        for n in self.connected_to:
            if n.name == node.name:
                should_add = False
                break
        if should_add:
            self.connected_to.append(node)
        
class Graph:
    def __init__(self):
        self.nodes = []
    
    def add_node(self, node):
        should_add = True
        for n in self.nodes:
            if n.name == node.name:
                should_add = False
                break
        if should_add:
            self.nodes.append(node);
            
    def create_connection(self, node, connected_to):
        for n in connected_to:
            node.connect_to(n)
            n.connect_to(node)
            
    def find_node(self, name):
        for n in self.nodes:
            if name == n.name:
                return n
        return -1
    
    def display(self):
        for node in self.nodes:
            print(node.name)
            n = []
            for neighbor in node.connected_to:
                n.append(neighbor.name)
            print(n)
            
    def bfs_connection(self, start):
        bfs = []
        queue = []
        queue.append(start)
        visited = []
        while queue:
            display(queue)
            node = queue.pop(0)
            if node not in visited:
                visited.append(node)
                bfs.append(node)
                for neighbor in node.connected_to:
                    queue.append(neighbor)
                
                
        return bfs
    
    def dfs_connection(self, start):
        dfs = []
        stack = []
        stack.append(start)
        visited = []
        while stack:
            display(stack)
            node = stack.pop()
            if node not in visited:
                visited.append(node)
                dfs.append(node)
                for neighbor in node.connected_to:
                    stack.append(neighbor)
                
                
        return dfs
    
    def dfs_path(self, start, end):
        dfs = []
        visited = []
        dfs.append(start)
        while dfs:
            print("STACK: "); display(dfs);
            node = dfs.pop()
            dfs.append(node)
            
            visited.append(node)
            if node == end:
                break
            
            counter = 0
            print("neighbors of: " + node.name)
            display( node.connected_to)
            for neighbor in node.connected_to:
                if neighbor not in visited:
                    counter += 1
                    dfs.append(neighbor)
                    break
            if counter <= 0:
                dfs.pop()
                
        return dfs
    
    def all_paths(self, current, dest, paths = [], path = []):
        my_path = []
        for i in path:
            my_path.append(i)
        path = my_path
        path.append(current)
        if current == dest:
            paths.append(path)
        else:
            neighbors = current.connected_to
            for neighbor in neighbors:
                if neighbor not in path:
                    self.all_paths(neighbor, dest, paths, path)

def display(nodes_array):
    n = []
    for x in nodes_array:
        n.append(x.name);
    print(n);
            
graph = Graph()
graph.add_node(Node("oradea"))
graph.add_node(Node("zerind"))
graph.add_node(Node("arad"))
graph.add_node(Node("sibiu"))
graph.add_node(Node("timisoara"))
graph.add_node(Node("lugoj"))
graph.add_node(Node("rimmicu vilcea"))
graph.add_node(Node("fagaras"))
graph.add_node(Node("mehadia"))
graph.add_node(Node("pitesti"))
graph.add_node(Node("drobeta"))
graph.add_node(Node("craiova"))
graph.add_node(Node("bucharest"))
graph.add_node(Node("giurgiu"))
graph.add_node(Node("urziceni"))
graph.add_node(Node("hirsova"))
graph.add_node(Node("eforie"))
graph.add_node(Node("vaslui"))
graph.add_node(Node("lasi"))
graph.add_node(Node("neamt"))

graph.create_connection(graph.find_node("oradea"), [graph.find_node("zerind"), graph.find_node("sibiu")])
graph.create_connection(graph.find_node("zerind"), [graph.find_node("arad")])
graph.create_connection(graph.find_node("arad"), [graph.find_node("sibiu"), graph.find_node("timisoara")])
graph.create_connection(graph.find_node("sibiu"), [graph.find_node("fagaras"), graph.find_node("rimmicu vilcea")])
graph.create_connection(graph.find_node("rimmicu vilcea"), [graph.find_node("pitesti")])
graph.create_connection(graph.find_node("timisoara"), [graph.find_node("lugoj")])
graph.create_connection(graph.find_node("lugoj"), [graph.find_node("mehadia")])
graph.create_connection(graph.find_node("mehadia"), [graph.find_node("drobeta")])
graph.create_connection(graph.find_node("drobeta"), [graph.find_node("craiova")])
graph.create_connection(graph.find_node("craiova"), [graph.find_node("rimmicu vilcea"), graph.find_node("pitesti")])
graph.create_connection(graph.find_node("pitesti"), [graph.find_node("bucharest")])
graph.create_connection(graph.find_node("fagaras"), [graph.find_node("bucharest")])
graph.create_connection(graph.find_node("bucharest"), [graph.find_node("giurgiu"), graph.find_node("urziceni")])
graph.create_connection(graph.find_node("urziceni"), [graph.find_node("hirsova"), graph.find_node("vaslui")])
graph.create_connection(graph.find_node("hirsova"), [graph.find_node("eforie")])
graph.create_connection(graph.find_node("vaslui"), [graph.find_node("lasi")])
graph.create_connection(graph.find_node("lasi"), [graph.find_node("neamt")])


bfs = graph.bfs_connection(graph.find_node("oradea"))
display(bfs)
    
print("DFS")
dfs = graph.dfs_connection(graph.find_node("oradea"))
display(dfs)

start = graph.find_node(input("Enter starting city: "))
end = graph.find_node(input("Enter destination: "))
paths = []
graph.all_paths(start, end, paths)
for i in paths:
    display(i)




