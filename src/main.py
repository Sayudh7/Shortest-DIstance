import matplotlib.pyplot as plt
import networkx as nx
from graph import cities, roads
from dijkstra import build_graph, dijkstra

# --- Global state ---
graph    = build_graph(cities, roads)
G        = nx.Graph()
selected = []  # stores [source, destination] as user clicks

# Build networkx graph
for city in cities:
    G.add_node(city)
for (city_a, city_b, distance) in roads:
    G.add_edge(city_a, city_b, weight=distance)

# Negate y so north is up
pos = {city: (cities[city][0], -cities[city][1]) for city in cities}


def get_clicked_city(x, y):
    """Find which city node the user clicked on."""
    for city, (cx, cy) in pos.items():
        # If click is within 15 units of a node center — count it as a click
        if abs(cx - x) < 15 and abs(cy - y) < 15:
            return city
    return None


def draw(path=[], source=None, destination=None):
    """Redraw the entire map."""
    plt.clf()  # clear previous drawing
    ax = plt.gca()
    ax.set_facecolor("#F8F6F0")
    plt.gcf().set_facecolor("#F8F6F0")

    # --- Categorize edges ---
    path_edges   = []
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
    if source and destination and path:
        start_end_nodes = [source, destination]
        middle_nodes    = [c for c in path if c not in start_end_nodes]
        other_nodes     = [c for c in cities if c not in path]
    elif source:
        # Only source selected so far
        start_end_nodes = [source]
        middle_nodes    = []
        other_nodes     = [c for c in cities if c != source]
    else:
        start_end_nodes = []
        middle_nodes    = []
        other_nodes     = list(cities.keys())

    # --- Draw edges ---
    nx.draw_networkx_edges(G, pos, edgelist=normal_edges,
        edge_color="#CCCCCC", width=1.2, ax=ax)

    nx.draw_networkx_edges(G, pos, edgelist=path_edges,
        edge_color="#1D9E75", width=4.0, ax=ax)

    # --- Draw nodes ---
    nx.draw_networkx_nodes(G, pos, nodelist=other_nodes,
        node_color="#888780", node_size=600, ax=ax)

    nx.draw_networkx_nodes(G, pos, nodelist=middle_nodes,
        node_color="#378ADD", node_size=650, ax=ax)

    nx.draw_networkx_nodes(G, pos, nodelist=start_end_nodes,
        node_color="#E85D24", node_size=700, ax=ax)

    # --- Labels above nodes ---
    label_pos = {city: (x, y + 8) for city, (x, y) in pos.items()}
    nx.draw_networkx_labels(G, label_pos,
        font_size=7, font_color="black", font_weight="bold", ax=ax)

    # --- Edge distance labels ---
    edge_labels = {(a, b): f"{d}km" for (a, b, d) in roads}
    nx.draw_networkx_edge_labels(G, pos,
        edge_labels=edge_labels, font_size=6, font_color="#777777", ax=ax)

    # --- Title / instruction ---
    if not source:
        plt.title("🗺  Click a city to select SOURCE", fontsize=13, pad=15)

    elif source and not destination:
        plt.title(f"✅ Source: {source}  |  Now click DESTINATION city",
            fontsize=13, pad=15)

    elif source and destination and path:
        plt.title(
            f"Shortest Path: {source} → {destination}  |  {distance_result[0]} km  |  "
            f"Route: {' → '.join(path)}",
            fontsize=11, pad=15)

    # --- Legend ---
    legend_elements = [
        plt.Line2D([0],[0], color="#1D9E75", linewidth=3,   label="Shortest path"),
        plt.Line2D([0],[0], color="#CCCCCC", linewidth=1.5, label="Road"),
        plt.scatter([],[], color="#E85D24", s=80, label="Source / Destination"),
        plt.scatter([],[], color="#378ADD", s=80, label="City on path"),
        plt.scatter([],[], color="#888780", s=80, label="Other city"),
    ]
    ax.legend(handles=legend_elements, loc="lower left", fontsize=8,
        framealpha=0.8, facecolor="white")

    plt.axis("off")
    plt.tight_layout()
    plt.draw()


distance_result = [0]  # mutable container to share distance between functions


def on_click(event):
    """Handle mouse click on the map."""
    if event.xdata is None or event.ydata is None:
        return  # clicked outside the graph area

    city = get_clicked_city(event.xdata, event.ydata)
    if not city:
        return  # clicked on empty space

    if len(selected) == 0:
        # First click — select source
        selected.append(city)
        print(f"✅ Source selected: {city}")
        draw(source=city)

    elif len(selected) == 1:
        if city == selected[0]:
            print("⚠️  Please click a different city for destination.")
            return
        # Second click — select destination and run Dijkstra
        selected.append(city)
        source      = selected[0]
        destination = selected[1]
        print(f"✅ Destination selected: {destination}")
        print(f"🔍 Finding shortest path...")

        dist, path = dijkstra(graph, source, destination)
        distance_result[0] = dist

        if not path:
            print(f"❌ No path found between {source} and {destination}")
            return

        print(f"✅ Shortest distance : {dist} km")
        print(f"📍 Path              : {' → '.join(path)}")
        draw(path=path, source=source, destination=destination)

    elif len(selected) == 2:
        # Third click — reset and start over
        selected.clear()
        selected.append(city)
        print(f"\n🔄 Reset! New source: {city}")
        draw(source=city)


def main():
    fig = plt.figure(figsize=(15, 9))
    fig.canvas.mpl_connect('button_press_event', on_click)

    print("\n=== Nepal Shortest Path Finder ===")
    print("👆 Click any city on the map to select SOURCE")
    print("👆 Click another city to select DESTINATION")
    print("👆 Click again anywhere to reset\n")

    draw()
    plt.show()


if __name__ == "__main__":
    main()