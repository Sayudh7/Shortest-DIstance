import matplotlib.pyplot as plt
import networkx as nx
from graph import cities, roads
from dijkstra import build_graph, dijkstra

def draw_graph(path=[]):
    G = nx.Graph()

    for city in cities:
        G.add_node(city)

    for (city_a, city_b, distance) in roads:
        G.add_edge(city_a, city_b, weight=distance)

    # Negate y so the map feels geographically natural (north = up)
    pos = {city: (cities[city][0], -cities[city][1]) for city in cities}

    # --- Categorize edges ---
    path_edges = []
    normal_edges = []

    for (city_a, city_b, _) in roads:
        if path and city_a in path and city_b in path:
            idx_a = path.index(city_a)
            idx_b = path.index(city_b)
            if abs(idx_a - idx_b) == 1:
                path_edges.append((city_a, city_b))
            else:
                normal_edges.append((city_a, city_b))
        else:
            normal_edges.append((city_a, city_b))

    # --- Categorize nodes ---
    if path:
        start_end_nodes = [path[0], path[-1]]
        middle_nodes    = path[1:-1]
        other_nodes     = [c for c in cities if c not in path]
    else:
        start_end_nodes = []
        middle_nodes    = []
        other_nodes     = list(cities.keys())

    # --- Draw ---
    nx.draw_networkx_edges(G, pos, edgelist=normal_edges,
        edge_color="#AAAAAA", width=1.2)

    nx.draw_networkx_edges(G, pos, edgelist=path_edges,
        edge_color="#1D9E75", width=3.5)

    nx.draw_networkx_nodes(G, pos, nodelist=other_nodes,
        node_color="#888780", node_size=350)

    nx.draw_networkx_nodes(G, pos, nodelist=middle_nodes,
        node_color="#378ADD", node_size=400)

    nx.draw_networkx_nodes(G, pos, nodelist=start_end_nodes,
        node_color="#E85D24", node_size=500)

    nx.draw_networkx_labels(G, pos,
        font_size=7, font_color="white", font_weight="bold")

    edge_labels = {(a, b): f"{d}km" for (a, b, d) in roads}
    nx.draw_networkx_edge_labels(G, pos,
        edge_labels=edge_labels, font_size=6, font_color="#555555")


def main():
    graph = build_graph(cities, roads)

    print("\n=== Nepal Shortest Path Finder ===")
    print("Available cities:")
    for i, city in enumerate(sorted(cities.keys()), 1):
        print(f"  {i:2}. {city}")

    print()
    start = input("Enter source city      : ").strip()
    end   = input("Enter destination city : ").strip()

    if start not in cities:
        print(f"❌ '{start}' not found.")
        return
    if end not in cities:
        print(f"❌ '{end}' not found.")
        return
    if start == end:
        print("❌ Source and destination cannot be the same.")
        return

    distance, path = dijkstra(graph, start, end)

    if not path:
        print(f"\n❌ No path found between {start} and {end}.")
        return

    print(f"\n✅ Shortest distance : {distance} km")
    print(f"📍 Path              : {' → '.join(path)}")

    plt.figure(figsize=(14, 8))
    plt.title(f"Shortest Path: {start} → {end}  ({distance} km)", fontsize=13)
    plt.axis("off")
    plt.tight_layout()

    draw_graph(path)
    plt.show()


if __name__ == "__main__":
    main()