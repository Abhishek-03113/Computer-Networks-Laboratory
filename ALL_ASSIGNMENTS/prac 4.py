import sys

INFINITY = float('inf')

network_topology = {
    'A': {'B': 1, 'C': 3},
    'B': {'A': 1, 'C': 1, 'D': 4},
    'C': {'A': 3, 'B': 1, 'D': 1},
    'D': {'B': 4, 'C': 1},
}

distance_vector = {
    'A': {'A': 0, 'B': 1, 'C': 3, 'D': INFINITY},
    'B': {'A': 1, 'B': 0, 'C': 1, 'D': 4},
    'C': {'A': 3, 'B': 1, 'C': 0, 'D': 1},
    'D': {'A': INFINITY, 'B': 4, 'C': 1, 'D': 0},
}

def bellman_ford():
    for router in network_topology:
        for destination in network_topology[router]:
            min_cost = INFINITY
            for neighbor in network_topology[router]:
                if neighbor != destination:
                    cost = network_topology[router][neighbor] + distance_vector[neighbor][destination]
                    min_cost = min(min_cost, cost)
            distance_vector[router][destination] = min_cost

def print_distance_vector():
    print("Distance Vector Table:")
    for router, table in distance_vector.items():
        print(f"Router {router}: {table}")

for i in range(len(network_topology)):
    bellman_ford()
    print_distance_vector()

source_router = 'A'
destination_router = 'B'
cost = distance_vector[source_router][destination_router]

if cost == INFINITY:
    print(f"No path from {source_router} to {destination_router}")
else:
    print(f"Shortest path from {source_router} to {destination_router} with cost {cost}")

