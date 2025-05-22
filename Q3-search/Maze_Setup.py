import random

# Step 1: Create a 6x6 grid (list of tuples representing coordinates)
maze_size = 6
nodes = [(x, y) for x in range(maze_size) for y in range(maze_size)]

# Step 2: Randomly select Start Node (from nodes 0 to 11)
start_node = random.choice(nodes[:12])  # Top-left corner (first 12 nodes)
print(f"Start Node: {start_node}")

# Step 3: Randomly select Goal Node (from nodes 24 to 35)
goal_node = random.choice(nodes[24:])  # Bottom-right corner (last 12 nodes)
print(f"Goal Node: {goal_node}")

# Step 4: Randomly select 4 Barrier Nodes (excluding start and goal)
remaining_nodes = [node for node in nodes if node != start_node and node != goal_node]
barrier_nodes = random.sample(remaining_nodes, 4)
print(f"Barrier Nodes: {barrier_nodes}")
