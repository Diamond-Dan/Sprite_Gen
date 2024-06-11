import pygame

# Initialize Pygame
pygame.init()

saved = False

# Set the width and height of the screen (width, height)
size = (1000, 1000)
screen = pygame.display.set_mode(size)

# Create a new surface for the section
section = pygame.Surface((100, 100))
section.fill((100, 255, 255))  # Fill the section with a color

# Set the title of the window
pygame.display.set_caption("Sectioned Area Example")

# Loop until the user clicks the close button
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

while not done:
    # Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # User clicked close
            done = True

    # Clear the screen
    screen.fill((255, 255, 255))

    # Draw the section onto the main screen at the desired position
    screen.blit(section, (50, 50))

    # Go ahead and update the screen with what we've drawn
    pygame.display.flip()

    # Limit to 60 frames per second
    clock.tick(60)

# Close the window and quit
pygame.quit()
