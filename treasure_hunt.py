import pygame
from collections import deque

class TreasureHunt:
    def __init__(self, state):
        self.state = state
        self.starting_position = (0, 0)
        self.goal_position = (6,4)

    def bfs(self):
        queue = deque([(self.starting_position, [])])
        visited = set()
        while queue:
            (x, y), path = queue.popleft()
            if (x, y) == self.goal_position:
                return path
            for direction in ["left", "right", "up", "down"]:
                new_x, new_y = x, y
                if direction == "left":
                    new_x -= 1
                elif direction == "right":
                    new_x += 1
                elif direction == "up":
                    new_y -= 1
                elif direction == "down":
                    new_y += 1
                if 0 <= new_x < len(self.state[0]) and 0 <= new_y < len(self.state):
                    new_state = (new_x, new_y)
                    if self.state[new_y][new_x] == 0 and new_state not in visited:
                        visited.add(new_state)
                        queue.append((new_state, path + [(x, y)]))

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

    path = treasureHunt.bfs()

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
                    
        goal_x, goal_y = treasureHunt.goal_position
        pygame.draw.rect(screen, GREEN, (goal_x * GRID_SIZE, goal_y * GRID_SIZE, GRID_SIZE, GRID_SIZE))
        if step < len(path):
            x, y = path[step]
            pygame.draw.rect(screen, RED, (x * GRID_SIZE, y * GRID_SIZE, GRID_SIZE, GRID_SIZE))
            step += 1
        pygame.display.flip()
        pygame.time.wait(500)
    pygame.quit()
