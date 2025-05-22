import heapq
from Task_1_maze_Setup import generate_maze

# Function to calculate Chebyshev distance (edge cost)
def chebyshev_distance(n, g):
    return max(abs(n[0] - g[0]), abs(n[1] - g[1]))

# Function to perform UCS
def uniform_cost_search(start, goal, barriers):
    # Directions: Up, Down, Left, Right, Diagonal (8 directions)
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]
    
    # Initialize the priority queue (min-heap)
    queue = [(0, start)]  # (cost, node)
    heapq.heapify(queue)
    
    # Dictionaries to track costs, parents, and visited nodes
    costs = {start: 0}  # Cost to reach each node
    parents = {start: None}  # To reconstruct the path
    visited = set()  # Set of visited nodes
    
    # Time counter (sum of nodes explored)
    total_explored = 0
    
    while queue:
        current_cost, current_node = heapq.heappop(queue)
        current_x, current_y = current_node
        
        # If we've reached the goal, reconstruct the path
        if current_node == goal:
            path = []
            while current_node:
                path.append(current_node)
                current_node = parents[current_node]
            path.reverse()
            print("Path found:", path)
            print("Total Time:", total_explored, "minutes")
            return path, visited, total_explored
        
        # Skip if already visited
        if current_node in visited:
            continue
        
        # Mark the node as visited
        visited.add(current_node)
        total_explored += 1
        
        # Explore all neighbors
        for dx, dy in directions:
            neighbor = (current_x + dx, current_y + dy)
            
            # Check if the neighbor is within bounds and not a barrier
            if 0 <= neighbor[0] < 6 and 0 <= neighbor[1] < 6 and neighbor not in barriers:
                new_cost = current_cost + chebyshev_distance(current_node, neighbor)
                
                # If this path to the neighbor is better, add it to the priority queue
                if neighbor not in costs or new_cost < costs[neighbor]:
                    costs[neighbor] = new_cost
                    heapq.heappush(queue, (new_cost, neighbor))
                    parents[neighbor] = current_node
    
    # If we exit the loop, no path was found
    print("No path found.")
    return None, visited, total_explored

# Generate the random maze (using the setup from Task 1)
start, goal, barriers = generate_maze()

# Perform UCS to find the shortest path
path, visited_nodes, total_time = uniform_cost_search(start, goal, barriers)

# Output the results
print("\nVisited Nodes:", visited_nodes)
print("Total Time:", total_time)
