
import pygame
import random
from pygame.locals import *

# Initialize Pygame
pygame.init()

# Constants
width, height = 640, 480
cell_size = 10
screen = pygame.display.set_mode((width, height))
BLACK, WHITE, GREEN, RED = (0, 0, 0), (255, 255, 255), (0, 255, 0), (255, 0, 0)

# Snake class
class Snake:
    def __init__(self, color, length):
        self.color = color
        self.length = length
        self.body = [(width // 2, height // 2)]
        self.direction = "right"

    def move(self):
        x, y = self.body[-1]
        if self.direction == "right":
            x += cell_size
        elif self.direction == "left":
            x -= cell_size
        elif self.direction == "up":
            y -= cell_size
        elif self.direction == "down":
            y += cell_size
        self.body.append((x, y))
        if len(self.body) > self.length:
            self.body.pop(0)

    def draw(self, screen):
        for segment in self.body:
            pygame.draw.rect(screen, self.color, (segment[0], segment[1], cell_size, cell_size))

# Food class
class Food:
    def __init__(self, color):
        self.color = color
        self.x, self.y = 0, 0
        self.generate()

    def generate(self):
        self.x = random.randint(0, (width // cell_size) - 1) * cell_size
        self.y = random.randint(0, (height // cell_size) - 1) * cell_size

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.x, self.y, cell_size, cell_size))

# Initialize snake and food
snake = Snake(GREEN, 1)
food = Food(RED)

# Main game loop
clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        elif event.type == KEYDOWN:
            if event.key == K_LEFT:
                snake.direction = "left"
            elif event.key == K_RIGHT:
                snake.direction = "right"
            elif event.key == K_UP:
                snake.direction = "up"
            elif event.key == K_DOWN:
                snake.direction = "down"

    # Move the snake
    snake.move()

    # Check for collision with walls or own body
    x, y = snake.body[-1]
    if x < 0 or x >= width or y < 0 or y >= height or (x, y) in snake.body[:-1]:
        print("Game Over!")
        running = False

    # Check for collision with food
    if snake.body[-1] == (food.x, food.y):
        food.generate()
        snake.length += 1

    # Clear the screen
    screen.fill(BLACK)

    # Draw the snake and food
    snake.draw(screen)
    food.draw(screen)

    # Update the screen
    pygame.display.flip()

    # Control the speed of the game
    clock.tick(10)

pygame.quit()
