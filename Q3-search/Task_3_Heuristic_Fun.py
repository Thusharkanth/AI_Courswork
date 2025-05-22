def chebyshev_distance(node, goal):
    # Extract coordinates of the current node (Nx, Ny) and goal node (Gx, Gy)
    Nx, Ny = node
    Gx, Gy = goal
    
    # Calculate Chebyshev distance
    return max(abs(Nx - Gx), abs(Ny - Gy))

# Example usage:
current_node = (3, 4)
goal_node = (6, 7)
heuristic = chebyshev_distance(current_node, goal_node)
print(f"Heuristic cost from {current_node} to {goal_node} is: {heuristic}")
