import heapq
from Task_3_Heuristic_Fun import chebyshev_distance 

def a_star_search(start, goal, barriers):
    # Create a priority queue (min-heap) to store nodes
    open_list = []
    heapq.heappush(open_list, (0 + chebyshev_distance(start, goal), 0, start))  # (f(n), g(n), node)
    
    # Dictionary to store the parent of each node for path reconstruction
    came_from = {}
    
    # Dictionary to store the g(n) value for each node
    g_score = {start: 0}
    
    # Set to track visited nodes
    visited = set()
    
    while open_list:
        # Pop the node with the lowest f(n) from the priority queue
        _, g, current_node = heapq.heappop(open_list)
        
        # If we reach the goal, reconstruct the path
        if current_node == goal:
            total_time = g * 1  # Since it takes 1 minute to explore a node
            path = reconstruct_path(came_from, current_node)
            return path, visited, total_time
        
        # Add current node to visited nodes
        visited.add(current_node)
        
        # Get neighbors of the current node
        neighbors = get_neighbors(current_node)
        
        for neighbor in neighbors:
            # Skip if neighbor is a barrier or already visited
            if neighbor in barriers or neighbor in visited:
                continue
            
            # Calculate the tentative g(n) score for the neighbor
            tentative_g_score = g + 1  # Each move costs 1 minute (1 unit)
            
            # If this is the first time visiting the neighbor or a better g(n) is found
            if neighbor not in g_score or tentative_g_score < g_score[neighbor]:
                came_from[neighbor] = current_node
                g_score[neighbor] = tentative_g_score
                f_score = tentative_g_score + chebyshev_distance(neighbor, goal)
                
                # Push neighbor into the open list with updated f(n) and g(n)
                heapq.heappush(open_list, (f_score, tentative_g_score, neighbor))
    
    # Return empty if no path is found
    return [], visited, -1

# Function to reconstruct the path from start to goal
def reconstruct_path(came_from, current_node):
    path = [current_node]
    while current_node in came_from:
        current_node = came_from[current_node]
        path.append(current_node)
    return path[::-1]  # Reverse the path to get start to goal order

# Function to get valid neighbors of a node
def get_neighbors(node):
    x, y = node
    neighbors = [
        (x-1, y-1), (x-1, y), (x-1, y+1),  # Top row (diagonal, left, right)
        (x, y-1),             (x, y+1),      # Left, Right
        (x+1, y-1), (x+1, y), (x+1, y+1)   # Bottom row (diagonal, left, right)
    ]
    return [(nx, ny) for nx, ny in neighbors if 0 <= nx < 6 and 0 <= ny < 6]  # Ensure within grid

# Example setup:
start = (1, 2)  # Example start node
goal = (5, 1)   # Example goal node
barriers = [(3, 4), (2, 2), (0, 1), (1, 5)]  # Example barriers

# Perform A* search
path, visited_nodes, total_time = a_star_search(start, goal, barriers)

# Output the results
print(f"Path found: {path}")
print(f"Total Time: {total_time} minutes")
print(f"Visited Nodes: {visited_nodes}")
