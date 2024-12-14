import pygame
import random

# Initialize pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600

# Colors
BG_COLOR = (0, 125, 255)
FG_COLOR = (255, 255, 255)

# Initialize screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Coin Collector")

# Clock for controlling frame rate
clock = pygame.time.Clock()

# Player attributes
player_width, player_height = 50, 50
player_x, player_y = WIDTH // 2, HEIGHT // 2
player_speed = 5

# Coin attributes
coin_width, coin_height = 30, 30
coin_x = random.randint(0, WIDTH - coin_width)
coin_y = random.randint(0, HEIGHT - coin_height)

# Score
score = 0

font = pygame.font.Font("Ac437_Amstrad_PC.ttf", 36)

# Game loop
running = True
while running:
    screen.fill(BG_COLOR)

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Player movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and player_y > 0:
        player_y -= player_speed
    if keys[pygame.K_DOWN] and player_y < HEIGHT - player_height:
        player_y += player_speed
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < WIDTH - player_width:
        player_x += player_speed

    # Check collision with coin
    player_rect = pygame.Rect(player_x, player_y, player_width, player_height)
    coin_rect = pygame.Rect(coin_x, coin_y, coin_width, coin_height)
    if player_rect.colliderect(coin_rect):
        score += 1
        coin_x = random.randint(0, WIDTH - coin_width)
        coin_y = random.randint(0, HEIGHT - coin_height)

    # Draw player and coin
    pygame.draw.rect(screen, FG_COLOR, player_rect)
    pygame.draw.rect(screen, FG_COLOR, coin_rect)

    # Display score
    score_text = font.render(f"Score: {score}", True, FG_COLOR)
    screen.blit(score_text, (10, 10))

    # Update display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(30)

# Quit pygame
pygame.quit()
