# pylint: disable=no-member
import pygame
import xml.etree.ElementTree as ET
import tkinter as tk
import os
from tkinter import simpledialog
# Initialize Pygame
pygame.init()

saved = False
# Set the width and height of the screen (width, height)
size = (1000, 1000)  # draw on large grid which will later be scaled to 100x100
screen = pygame.display.set_mode(size)

# Set the title of the window
pygame.display.set_caption("Mouse Movement Tracker")

# Loop until the user clicks the close button
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# Variable to track whether the mouse button is down
mouse_down = False

# Create the root element for the XML document
xml_root = ET.Element("root")

while not done:
    #  Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # User clicked close
            done = True
        elif event.type == pygame.MOUSEBUTTONDOWN:  # Mouse button pressed
            mouse_down = True
        elif event.type == pygame.MOUSEBUTTONUP:  # Mouse button released
            mouse_down = False
        elif event.type == pygame.MOUSEMOTION:  # Mouse moved
            if mouse_down:
                # Draw a red dot at the mouse position
                pygame.draw.circle(screen, (255, 0, 0), event.pos, 10)

                # Add the mouse position to the XML document
                pos = ET.SubElement(xml_root, "partstitch")
                # divide by 10 to scale down to 100x100
                pos.set("x", str(round(event.pos[0]/10)))
                pos.set("y", str(round(event.pos[1]/10)))
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s:
                # The 's' key was pressed! Show the save dialog.
                root = tk.Tk()
                root.withdraw()  # Hide the main window
                filename = simpledialog.askstring("Filename", "Enter a name for the XML file:")
                if filename:
                    tree = ET.ElementTree(xml_root)
                    current_file_path = os.path.dirname(os.path.realpath(__file__))
                    file_path = os.path.join(current_file_path, 'patterns', f"{filename}.xml")
                    tree.write(file_path)
                    saved = True
#  Go ahead and update the screen with what we've drawn
    pygame.display.flip()

    #  Limit to 120 frames per second
    clock.tick(120)

# Create a Tkinter window to get the filename
root = tk.Tk()
root.withdraw()  # Hide the main window

# Show a simple dialog asking for the filename
if not saved:
    filename = simpledialog.askstring("Filename", "Enter a name for the XML file:")

    # Write the XML document to a file
    if filename!=None or "":
        tree = ET.ElementTree(xml_root)
        current_file_path = os.path.dirname(os.path.realpath(__file__))
        file_path = os.path.join(current_file_path, 'patterns', f"{filename}.xml")
        tree.write(file_path)
        saved = True

# Close the window and quit
pygame.quit()