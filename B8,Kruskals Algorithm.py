class DisjointSet:
    def __init__(self, size):
        self.parent = list(range(size))

    def find(self, element):
        if self.parent[element] == element:
            return element
        return self.find(self.parent[element])

    def union(self, a, b):
        root_a = self.find(a)
        root_b = self.find(b)
        self.parent[root_a] = root_b


def kruskal(graph):
    num_vertices = len(graph)
    ET = []
    ecounter = 0


    edges = []
    for v in range(num_vertices):
        for u in range(v + 1, num_vertices):
            if graph[v][u] > 0:
                edges.append((v, u, graph[v][u]))
    edges.sort(key=lambda edge: edge[2])


    ds = DisjointSet(num_vertices)

    k = 0
    while ecounter < num_vertices - 1:
        v, u, weight = edges[k]
        k += 1


        if ds.find(v) != ds.find(u):
            ET.append((v, u))
            ecounter += 1
            ds.union(v, u)

    return ET


if __name__ == '__main__':

    graph = [
        [0, 2, 0, 6, 0],
        [2, 0, 3, 8, 5],
        [0, 3, 0, 0, 7],
        [6, 8, 0, 0, 9],
        [0, 5, 7, 9, 0]
    ]

    minimum_spanning_tree = kruskal(graph)
    print("Minimum Cost Spanning Tree Edges:")
    for edge in minimum_spanning_tree:
        print(f"Edge {edge[0]} - {edge[1]}")

