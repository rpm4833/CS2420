from graph import Graph
from graph_matrix import Graph as MatrixGraph


def main():
    with open('data.txt', 'r') as file:
        num_vertices = int(file.readline())
        g = Graph(num_vertices)
        
        num_edges = int(file.readline())

        for e in range(num_edges):
            line = file.readline().split()
            g.add_edge(int(line[0]), int(line[1]))
        
        num_tests = int(file.readline())

        for t in range(num_tests):
            line = file.readline().split()
            print(g.find_path(int(line[0]), int(line[1])))
    print(g.visualize())

def main_m():
    with open('data.txt', 'r') as file:
        num_vertices = int(file.readline())
        g = MatrixGraph(num_vertices)
        
        num_edges = int(file.readline())

        for e in range(num_edges):
            line = file.readline().split()
            g.add_edge(int(line[0]), int(line[1]))
        
        num_tests = int(file.readline())

        for t in range(num_tests):
            line = file.readline().split()
            print(g.find_path(int(line[0]), int(line[1])))
        
    print(g.visualize())

if __name__ == "__main__":
    choice = input("Neigbor or Matrix? (N/M) ")
    match choice.lower():
        case 'n':
            main()
        case 'm':
            main_m()
        case _:
            print("Invalid option!")