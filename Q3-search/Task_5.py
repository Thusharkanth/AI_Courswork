import random
import heapq
import time
from Task_3_Heuristic_Fun import chebyshev_distance  # Import your heuristic function

# Function to generate a random maze
def generate_maze(grid_size, barrier_count):
    maze = [[0 for _ in range(grid_size)] for _ in range(grid_size)]
    for _ in range(barrier_count):
        x = random.randint(0, grid_size - 1)
        y = random.randint(0, grid_size - 1)
        maze[x][y] = 1  # Barrier
    return maze

# Function to perform A* search (same as in Task 4)
def a_star_search(start, goal, maze):
    open_list = []
    heapq.heappush(open_list, (0 + chebyshev_distance(start, goal), 0, start))
    
    came_from = {}
    g_score = {start: 0}
    visited = set()
    
    while open_list:
        _, g, current_node = heapq.heappop(open_list)
        
        if current_node == goal:
            total_time = g * 1  # Time = g(n) since each move takes 1 minute
            path = reconstruct_path(came_from, current_node)
            return path, visited, total_time
        
        visited.add(current_node)
        
        neighbors = get_neighbors(current_node)
        
        for neighbor in neighbors:
            if maze[neighbor[0]][neighbor[1]] == 1 or neighbor in visited:  # Barrier or already visited
                continue
            
            tentative_g_score = g + 1
            if neighbor not in g_score or tentative_g_score < g_score[neighbor]:
                came_from[neighbor] = current_node
                g_score[neighbor] = tentative_g_score
                f_score = tentative_g_score + chebyshev_distance(neighbor, goal)
                heapq.heappush(open_list, (f_score, tentative_g_score, neighbor))
    
    return [], visited, -1

# Function to get valid neighbors of a node
def get_neighbors(node):
    x, y = node
    neighbors = [
        (x-1, y-1), (x-1, y), (x-1, y+1),  # Top row (diagonal, left, right)
        (x, y-1),             (x, y+1),      # Left, Right
        (x+1, y-1), (x+1, y), (x+1, y+1)   # Bottom row (diagonal, left, right)
    ]
    return [(nx, ny) for nx, ny in neighbors if 0 <= nx < 6 and 0 <= ny < 6]

# Function to reconstruct the path from start to goal
def reconstruct_path(came_from, current_node):
    path = [current_node]
    while current_node in came_from:
        current_node = came_from[current_node]
        path.append(current_node)
    return path[::-1]  # Reverse the path to get start to goal order

# Running the experiment for 3 different mazes
def run_experiment():
    grid_size = 6  # Size of the grid
    barrier_count = 6  # Number of barriers in each maze
    start = (0, 0)  # Example start position
    goal = (5, 5)   # Example goal position
    
    results = []
    
    for _ in range(3):  # Repeat 3 times
        maze = generate_maze(grid_size, barrier_count)
        
        # Track start time
        start_time = time.time()
        
        # Perform A* search
        path, visited_nodes, total_time = a_star_search(start, goal, maze)
        
        # Track end time
        end_time = time.time()
        search_time = end_time - start_time
        
        # Collect results
        path_length = len(path)
        results.append({
            "path_length": path_length,
            "time": total_time,
            "search_time": search_time,
            "visited_nodes": visited_nodes
        })
        
        # Print out results for each run
        print(f"Path found: {path}")
        print(f"Total Time: {total_time} minutes")
        print(f"Visited Nodes: {visited_nodes}")
        print(f"Search Time: {search_time} seconds")
    
    # Calculate the mean and variance for time and path length
    times = [result["search_time"] for result in results]
    path_lengths = [result["path_length"] for result in results]
    
    mean_time = sum(times) / len(times)
    mean_path_length = sum(path_lengths) / len(path_lengths)
    
    variance_time = sum((t - mean_time)**2 for t in times) / len(times)
    variance_path_length = sum((l - mean_path_length)**2 for l in path_lengths) / len(path_lengths)
    
    # Print out the analysis
    print("\n--- Analysis ---")
    print(f"Mean Time: {mean_time} seconds")
    print(f"Variance in Time: {variance_time}")
    print(f"Mean Path Length: {mean_path_length}")
    print(f"Variance in Path Length: {variance_path_length}")

# Run the experiment
run_experiment()
