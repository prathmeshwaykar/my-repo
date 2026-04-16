import random
import pygame
import sys

# Initialize Pygame
pygame.init()

# Window settings
WIDTH, HEIGHT = 640, 480
CELL_SIZE = 20
GRID_WIDTH = WIDTH // CELL_SIZE
GRID_HEIGHT = HEIGHT // CELL_SIZE
FPS = 12

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (34, 139, 34)
RED = (220, 20, 60)
BLUE = (66, 135, 245)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 36)


def draw_grid():
    for x in range(0, WIDTH, CELL_SIZE):
        pygame.draw.line(screen, (40, 40, 40), (x, 0), (x, HEIGHT))
    for y in range(0, HEIGHT, CELL_SIZE):
        pygame.draw.line(screen, (40, 40, 40), (0, y), (WIDTH, y))


def draw_rect(color, position):
    rect = pygame.Rect(position[0] * CELL_SIZE, position[1] * CELL_SIZE, CELL_SIZE, CELL_SIZE)
    pygame.draw.rect(screen, color, rect)


def random_food_position(snake):
    while True:
        position = (random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1))
        if position not in snake:
            return position


def show_text(text, color, x, y):
    surface = font.render(text, True, color)
    screen.blit(surface, (x, y))


def main():
    snake = [(GRID_WIDTH // 2, GRID_HEIGHT // 2)]
    direction = (1, 0)
    food = random_food_position(snake)
    score = 0
    game_over = False

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and direction != (0, 1):
                    direction = (0, -1)
                elif event.key == pygame.K_DOWN and direction != (0, -1):
                    direction = (0, 1)
                elif event.key == pygame.K_LEFT and direction != (1, 0):
                    direction = (-1, 0)
                elif event.key == pygame.K_RIGHT and direction != (-1, 0):
                    direction = (1, 0)
                elif event.key == pygame.K_r and game_over:
                    main()

        if not game_over:
            new_head = (snake[0][0] + direction[0], snake[0][1] + direction[1])

            if (
                new_head[0] < 0
                or new_head[0] >= GRID_WIDTH
                or new_head[1] < 0
                or new_head[1] >= GRID_HEIGHT
                or new_head in snake
            ):
                game_over = True
            else:
                snake.insert(0, new_head)
                if new_head == food:
                    score += 1
                    food = random_food_position(snake)
                else:
                    snake.pop()

        screen.fill(BLACK)
        draw_grid()

        for part in snake:
            draw_rect(GREEN, part)

        draw_rect(RED, food)

        show_text(f"Score: {score}", WHITE, 10, 10)

        if game_over:
            show_text("Game Over! Press R to restart.", BLUE, WIDTH // 2 - 180, HEIGHT // 2 - 15)

        pygame.display.update()
        clock.tick(FPS)


if __name__ == "__main__":
    main()
