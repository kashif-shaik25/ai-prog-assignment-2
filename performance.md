
### Breadth-First Search (BFS)
- Logic: Uses a FIFO queue to explore level by level.
- Optimality: Guaranteed to find the shortest sequence
- Memory: High as it stores all nodes at the current depth

### Depth-First Search (DFS)
- Logic: Uses a LIFO stack to explore as deeply as possible first.
- Optimality: Low; often returns a long, non-optimal path.
- Memory: Low as it only stores the current path.

### Iterative Deepening DFS (IDDFS)
- Logic: Repeatedly runs DFS with an increasing depth limit.
- Optimality: High; finds the same shortest path as BFS.
- Memory: Low; maintains the space efficiency of DFS.

- BFS: Finds the shortest path and is complete, but uses high memory.
- DFS: Uses minimal memory but is not optimal and can fail to find the shortest path.
- IDDFS: Provides the optimal solution like BFS while keeping memory usage low like DFS.

IDDFS is the most efficient choice for this problem as it finds the optimal solution while using minimal memory.
