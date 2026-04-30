import numpy as np
import matplotlib.pyplot as plt
from queue import Queue
class Graph:
    def __init__(self, num_vert):
        self.graph = np.full((num_vert, num_vert), False)
    

    def add_edge(self, f, t):
        if self.is_edge(f, t):
            return False
        self.graph[f, t] = True
        return True
    
    def is_edge(self, f, t):
        if self.graph[f, t]:
            return True
        return False
    
    def find_path(self, f, t):
        q = Queue()
        num_verts = self.graph.shape[0]
        fr = [-1] * num_verts
        q.put(f)
        fr[f] = f

        while not q.empty():
            current = q.get()
            if current == t:
                path = [current]
                while current != f:
                    current = fr[current]
                    path.append(current)
                path.reverse()
                return path
            
            for i in range(num_verts):
                if self.graph[current, i] and fr[i] == -1:
                    q.put(i)
                    fr[i] = current

        return None

    def get_neighbors(self, v):
        return np.where(self.graph[v] == True)[0]
    
    def visualize(self):
        plt.imshow(self.graph, cmap='gray', interpolation='none')
        plt.title("Graph Bag Pathing Matrix")
        plt.xlabel("To Vertex")
        plt.ylabel("From Vertex")

        plt.show()