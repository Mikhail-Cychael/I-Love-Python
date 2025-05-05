import pygame
import sys
import random

# Initialize PyGame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Flappy Bird")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (135, 206, 250)
GREEN = (0, 200, 0)

# Game variables
gravity = 0.5
bird_movement = 0
bird_y = SCREEN_HEIGHT // 2
bird_x = 50
pipe_width = 60
pipe_gap = 150
pipe_speed = 3
score = 0

# Load assets
font = pygame.font.Font(None, 36)
clock = pygame.time.Clock()

# Pipe list
pipes = []

def create_pipe():
    height = random.randint(150, 450)
    top_pipe = pygame.Rect(SCREEN_WIDTH, 0, pipe_width, height - pipe_gap // 2)
    bottom_pipe = pygame.Rect(SCREEN_WIDTH, height + pipe_gap // 2, pipe_width, SCREEN_HEIGHT - height)
    return top_pipe, bottom_pipe

def move_pipes(pipes):
    for pipe in pipes:
        pipe.centerx -= pipe_speed
    return [pipe for pipe in pipes if pipe.right > 0]

def draw_pipes(pipes):
    for pipe in pipes:
        pygame.draw.rect(screen, GREEN, pipe)

def check_collision(pipes):
    for pipe in pipes:
        if bird.colliderect(pipe):
            return True
    if bird.top <= 0 or bird.bottom >= SCREEN_HEIGHT:
        return True
    return False

# Main game loop
running = True
while running:
    screen.fill(BLUE)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bird_movement = -10

    # Bird movement
    bird_movement += gravity
    bird_y += bird_movement
    bird = pygame.Rect(bird_x, bird_y, 30, 30)
    pygame.draw.ellipse(screen, BLACK, bird)

    # Pipe logic
    if not pipes or pipes[-1].centerx < SCREEN_WIDTH - 200:
        pipes.extend(create_pipe())
    pipes = move_pipes(pipes)
    draw_pipes(pipes)

    # Collision detection
    if check_collision(pipes):
        running = False

    # Score
    for pipe in pipes:
        if pipe.centerx == bird_x:
            score += 0.5
    score_text = font.render(f"Score: {int(score)}", True, WHITE)
    screen.blit(score_text, (10, 10))

    pygame.display.update()
    clock.tick(30)