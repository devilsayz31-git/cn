# Distance Vector Routing Algorithm (Bellman-Ford)
# Finds the routing table for each node

import sys

MAX = 10
INF = 999


def print_tables(dist, next_hop, n):
    for i in range(n):
        print(f"\nRouting Table for Node {i + 1}")
        print("------------------------------------")
        print(f"{'Destination':<14}{'Next Hop':<12}Distance")
        for j in range(n):
            hop = "-" if next_hop[i][j] == -1 else str(next_hop[i][j] + 1)
            distance = "INF" if dist[i][j] >= INF else str(dist[i][j])
            print(f"{j + 1:<14}{hop:<12}{distance}")


def distance_vector(cost, n):
    # Step 1: Each node knows only the cost to its direct neighbours
    dist = [row[:] for row in cost]
    next_hop = [[-1] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i == j:
                next_hop[i][j] = i
            elif cost[i][j] != INF:
                next_hop[i][j] = j

    # Step 2: Nodes exchange distance vectors with neighbours in rounds
    round_no = 0
    while True:
        updated = False
        round_no += 1

        # Vectors sent by every node at the start of this round
        old = [row[:] for row in dist]

        print(f"\n--- Round {round_no} ---")
        for i in range(n):
            for k in range(n):
                # k must be a direct neighbour of i
                if k == i or cost[i][k] == INF:
                    continue
                for j in range(n):
                    # Bellman-Ford equation: D(i,j) = min{ c(i,k) + D(k,j) }
                    if old[k][j] != INF and cost[i][k] + old[k][j] < dist[i][j]:
                        dist[i][j] = cost[i][k] + old[k][j]
                        next_hop[i][j] = k
                        updated = True
                        print(f"Node {i + 1}: route to {j + 1} updated via {k + 1} "
                              f"(cost {dist[i][j]})")

        if not updated:
            print("No changes. Routing tables have converged.")
            break

    print(f"\nConverged after {round_no} round(s)")
    print_tables(dist, next_hop, n)


def read_ints(count):
    # Reads numbers across any number of lines, like cin in C++
    values = []
    while len(values) < count:
        values.extend(int(x) for x in input().split())
    return values[:count]


def main():
    n = int(input("Enter the number of nodes: "))
    if n < 1 or n > MAX:
        print(f"Number of nodes must be between 1 and {MAX}")
        sys.exit(1)

    print("\nEnter the cost matrix:")
    print("(Enter 999 for no direct connection)\n")
    values = read_ints(n * n)
    cost = [values[i * n:(i + 1) * n] for i in range(n)]

    distance_vector(cost, n)


if __name__ == "__main__":
    main()
