import pygame
from collections import deque

class TreasureHunt:
    def __init__(self, state):
        self.state = state
        self.starting_position = (0, 0)
        self.goal_position = (6,4)

    def bfs_pathfinding(self):
        queue = deque([(self.starting_position, [])])
        visited = set()

        while queue:
            (x, y), path = queue.popleft()

            if (x, y) == self.goal_position:
                return path

            if 0 <= x < len(self.state[0]) and 0 <= y < len(self.state):
                if self.state[y][x] == 0 and (x, y) not in visited:
                    visited.add((x, y))
                    for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                        new_x, new_y = x + dx, y + dy
                        if 0 <= new_x < len(self.state[0]) and 0 <= new_y < len(self.state):
                            queue.append(((new_x, new_y), path + [(x, y)]))

        return []

if __name__ == "__main__":
    pygame.init()
    WIDTH, HEIGHT = 420, 300
    GRID_SIZE = 60
    WHITE = (255, 255, 255)
    BLUE = (0, 0, 255)
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Treasure Hunt")
    
    # 1 means wall and 0 means i can walk xd
    state = [
        [0, 0, 1, 0, 0, 1, 0],
        [0, 1, 0, 1, 0 ,0, 1],
        [0, 0, 1, 0, 0, 1, 1],
        [0, 1, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 1, 0]
    ]

    treasureHunt = TreasureHunt(state)

    path = treasureHunt.bfs_pathfinding()

    running = True
    step = 0

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill((0, 0, 0))

        for y in range(len(state)):
            for x in range(len(state[0])):
                if state[y][x] == 1:
                    pygame.draw.rect(screen, WHITE, (x * GRID_SIZE, y * GRID_SIZE, GRID_SIZE, GRID_SIZE))
                else:
                    pygame.draw.rect(screen, BLUE, (x * GRID_SIZE, y * GRID_SIZE, GRID_SIZE, GRID_SIZE))

        if step < len(path):
            x, y = path[step]
            pygame.draw.rect(screen, RED, (x * GRID_SIZE, y * GRID_SIZE, GRID_SIZE, GRID_SIZE))
            step += 1
        
        goal_x, goal_y = treasureHunt.goal_position
        pygame.draw.rect(screen, GREEN, (goal_x * GRID_SIZE, goal_y * GRID_SIZE, GRID_SIZE, GRID_SIZE))

        pygame.display.flip()
        pygame.time.wait(500)

    pygame.quit()
