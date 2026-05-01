from queue import Queue
class Graph:
    def __init__(self, num_vert):
        self.neighbors = []
        for i in range(num_vert):
            self.neighbors.append([])
    
    def add_edge(self, f, t):
        if self.is_edge(f, t):
            return False
        self.neighbors[f].append(t)
        return True
    
    def is_edge(self, f, t):
        if t in self.neighbors[f]:
            return True
        return False
    
    def get_neighbors(self, v):
        return self.neighbors[v]
    
    def find_path(self, f, t):
        q = Queue()
        fr = [-1] * len(self.neighbors)
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
            
            for n in self.neighbors[current]:
                if fr[n] == -1:
                    q.put(n)
                    fr[n] = current

        return None
    
    def visualize(self):
        return self.neighbors