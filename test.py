import pygame
pygame.init()

# Set up the screen
screen = pygame.display.set_mode((800, 600))

# Load player image
playerImg = pygame.image.load('player.png')

# Initial position of the player
x = 100
y = 200

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Clear the screen
    screen.fill((0, 0, 0))  # Fill with black to clear previous frame
    
    # Draw the player image at position (x, y)
    screen.blit(playerImg, (x, y))
    
    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
