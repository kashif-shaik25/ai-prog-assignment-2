from collections import deque

class WaterJugAgent:
    def __init__(self, c1, c2, target):
        self.c1, self.c2, self.target = c1, c2, target

    def get_successors(self, state):
        j1, j2 = state
        return {
            (self.c1, j2), (j1, self.c2),
            (0, j2), (j1, 0),
            (j1 - min(j1, self.c2 - j2), j2 + min(j1, self.c2 - j2)),
            (j1 + min(j2, self.c1 - j1), j2 - min(j2, self.c1 - j1))
        }

    def solve_bfs(self):
        queue = deque([(0, 0, [])])
        visited = set()
        while queue:
            j1, j2, path = queue.popleft()
            if (j1, j2) in visited: continue
            visited.add((j1, j2))
            new_path = path + [(j1, j2)]
            if j1 == self.target or j2 == self.target: return new_path
            for s in self.get_successors((j1, j2)):
                queue.append((*s, new_path))
        return None

    def solve_dfs(self):
        stack = [(0, 0, [])]
        visited = set()
        while stack:
            j1, j2, path = stack.pop()
            if (j1, j2) in visited: continue
            visited.add((j1, j2))
            new_path = path + [(j1, j2)]
            if j1 == self.target or j2 == self.target: return new_path
            for s in self.get_successors((j1, j2)):
                stack.append((*s, new_path))
        return None

    def solve_iddfs(self, max_depth=20):
        for depth_limit in range(max_depth):
            stack = [(0, 0, [], 0)]
            while stack:
                j1, j2, path, current_depth = stack.pop()
                new_path = path + [(j1, j2)]
                if j1 == self.target or j2 == self.target: return new_path
                if current_depth < depth_limit:
                    for s in self.get_successors((j1, j2)):
                        stack.append((*s, new_path, current_depth + 1))
        return None

if __name__ == "__main__":
    agent = WaterJugAgent(4, 3, 2)
    print("BFS:", agent.solve_bfs())
    print("DFS:", agent.solve_dfs())
    print("IDDFS:", agent.solve_iddfs())
