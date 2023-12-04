import sys

def tsp(graph, start):
    num_cities = len(graph)
    visited = [False] * num_cities
    tour = [start]
    total_distance = 0

    for _ in range(num_cities - 1):
        current_city = tour[-1]
        nearest_city = None
        min_distance = sys.maxsize

        for next_city in range(num_cities):
            if not visited[next_city] and graph[current_city][next_city] < min_distance:
                nearest_city = next_city
                min_distance = graph[current_city][next_city]

        tour.append(nearest_city)
        visited[nearest_city] = True
        total_distance += min_distance


    tour.append(start)
    total_distance += graph[tour[-2]][start]

    return tour, total_distance

# Example usage
if __name__ == "__main__":
    graph = [
        [0, 10, 15, 20],
        [10, 0, 35, 25],
        [15, 35, 0, 30],
        [20, 25, 30, 0]
    ]

    start_city = 0
    tour, distance = tsp(graph, start_city)

    print(f"Optimal Tour: {tour}")
    print(f"Total Distance: {distance}")
