import sys



def find_min_edge(graph, VT, V):
    min_weight = sys.maxsize
    min_edge = None

    for v in VT:
        for u in range(len(graph)):
            if u not in VT and graph[v][u] < min_weight:
                min_weight = graph[v][u]
                min_edge = (v, u)

    return min_edge



def prim(graph):
    num_vertices = len(graph)
    VT = {0}
    ET = []

    for _ in range(num_vertices - 1):
        v, u = find_min_edge(graph, VT, range(num_vertices))
        VT.add(u)
        ET.append((v, u))

    return ET


# Example usage
if __name__ == '__main__':

    graph = [
        [0, 2, 0, 6, 0],
        [2, 0, 3, 8, 5],
        [0, 3, 0, 0, 7],
        [6, 8, 0, 0, 9],
        [0, 5, 7, 9, 0]
    ]

    minimum_spanning_tree = prim(graph)
    print("Minimum Cost Spanning Tree Edges:")
    for edge in minimum_spanning_tree:
        print(f"Edge {edge[0]} - {edge[1]}")

