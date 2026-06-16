import heapq

def build_graph(cities, roads):
    # Each city starts with an empty neighbour list
    graph = {city: [] for city in cities}

    for (city_a, city_b, distance) in roads:
        # Roads go both ways (Kathmandu→Pokhara and Pokhara→Kathmandu)
        graph[city_a].append((city_b, distance))
        graph[city_b].append((city_a, distance))

    return graph


def dijkstra(graph, start, end):
    # All cities are unreachable at the beginning except the start
    distances = {city: float('inf') for city in graph}
    distances[start] = 0

    # We use this later to reconstruct the actual path, not just the distance
    previous = {city: None for city in graph}

    # (distance, city) — heapq always pops the smallest distance first
    priority_queue = [(0, start)]

    visited = set()

    while priority_queue:
        current_distance, current_city = heapq.heappop(priority_queue)

        # We may have added the same city multiple times with different distances
        # so skip it if we already finalized it
        if current_city in visited:
            continue

        visited.add(current_city)

        # No need to explore further once we've finalized the destination
        if current_city == end:
            break

        for (neighbour, weight) in graph[current_city]:
            if neighbour in visited:
                continue

            new_distance = current_distance + weight

            # Found a shorter route to this neighbour — update it
            if new_distance < distances[neighbour]:
                distances[neighbour] = new_distance
                previous[neighbour] = current_city
                heapq.heappush(priority_queue, (new_distance, neighbour))

    # Trace back from end to start using the previous[] chain
    path = []
    current = end
    while current is not None:
        path.append(current)
        current = previous[current]

    path.reverse()

    # If start isn't in the path, the destination was unreachable
    if path[0] != start:
        return float('inf'), []

    return distances[end], path