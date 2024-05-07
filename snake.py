# Import the necessary libraries
# Used Llama 2 running through Jan.AI
import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the display
width = 640
height = 480
screen = pygame.display.set_mode((width, height))

# Set up the title of the window
pygame.display.set_caption("Snake Game")

# Define some colors for the game
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Define the snake's starting position and size
snake_x = 320
snake_y = 240
snake_size = 10
snake_speed = 10

# Define the food's position and size
food_x = random.randint(0, width - snake_size)
food_y = random.randint(0, height - snake_size)
food_size = snake_size

# Set up the game loop
running = True
while running:
    # Handle events (e.g. arrow keys for movement)
    # Move the snake based on the arrow keys
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                snake_y -= snake_speed
            elif event.key == pygame.K_DOWN:
                snake_y += snake_speed
            elif event.key == pygame.K_LEFT:
                snake_x -= snake_speed
            elif event.key == pygame.K_RIGHT:
                snake_x += snake_speed

    # Check for collision with the wall or itself
    if snake_x < 0 or snake_x >= width - snake_size or snake_y < 0 or snake_y >= height - snake_size:
        print("Game over!")
        running = False

    # Check for collision with the food
    if (snake_x <= food_x <= snake_x + snake_size) and (snake_y <= food_y <= snake_y + snake_size):
        print("You ate the food!")
        food_x = random.randint(0, width - snake_size)
        food_y = random.randint(0, height - snake_size)

    # Clear the screen
    screen.fill(BLACK)

    # Draw the snake
    pygame.draw.rect(screen, WHITE, (snake_x, snake_y, snake_size, snake_size))

    # Draw the food
    pygame.draw.rect(screen, WHITE, (food_x, food_y, food_size, food_size))

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
