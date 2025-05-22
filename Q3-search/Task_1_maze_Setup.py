import random

# Function to generate the maze and select start, goal, and barriers
def generate_maze():
    # Create the grid (6x6, 36 nodes numbered from 0 to 35)
    grid = [(x, y) for x in range(6) for y in range(6)]
    
    # Randomly select the start node (from nodes 0 to 11)
    start_node = random.choice(grid[:12])  # Nodes from (0,0) to (2,5)
    
    # Randomly select the goal node (from nodes 24 to 35)
    goal_node = random.choice(grid[24:])  # Nodes from (4,0) to (5,5)
    
    # Remove start and goal from the grid to avoid overlap with barriers
    grid.remove(start_node)
    grid.remove(goal_node)
    
    # Randomly select 4 barrier nodes from the remaining grid
    barrier_nodes = random.sample(grid, 4)
    
    # Print the generated maze configuration
    print("Start Node:", start_node)
    print("Goal Node:", goal_node)
    print("Barrier Nodes:", barrier_nodes)
    
    # Return the generated maze setup
    return start_node, goal_node, barrier_nodes

# Generate the random maze
start, goal, barriers = generate_maze()
