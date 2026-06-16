# 🗺️ Shortest Path Finder (Dijkstra’s Algorithm)

A Python-based project that finds the shortest route between major cities
of Nepal using **Dijkstra's Algorithm** — one of the most famous graph
algorithms in computer science, developed by Dutch scientist Edsger W. Dijkstra.

## What it does
- Models major cities of Nepal as a weighted graph
- Roads between cities are edges, distances in km are weights
- Finds the shortest path between any two cities using Dijkstra's algorithm
- Visualises the graph and highlights the shortest route on screen

## Tech Stack
- **Python 3**
- **NetworkX** — graph data structure
- **Matplotlib** — visualization

## How to run
```bash
pip install networkx matplotlib
python src/main.py
```

## Project Structure
Shortest Distance /

├── src/

│   ├── main.py       # Entry point and visualization

│   ├── graph.py      # City nodes and road edges

│   └── dijkstra.py   # Shortest path algorithm

└── README.md

## Academic Context
Built as a university project for Data Structures & Algorithms course
