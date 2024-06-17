# pylint: disable=no-member
import xml.etree.ElementTree as ET
import tkinter as tk
import os
from tkinter import simpledialog
import pygame
import pygame_textinput
import sprite_micro_gen


def main():
    # Initialize Pygame
    pygame.init()
    # DO NOT FORGET TO ADJUST FOR 1200x1000 frame in XML
    saved = False
    # Set the width and height of the screen (width, height)
    size = (1200, 1000)  # draw on large grid which will later be scaled to 100x100
    screen = pygame.display.set_mode(size)
    section = pygame.Surface((10, 1000))
    section.fill((100, 255, 255))
    section_background = pygame.Surface((190, 1000))
    section_background.fill((200, 200, 200))
    filename = None
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

    color = [255, 255, 255]
    # Set initial positions for the text inputs
    positions = [(10, 10), (10, 60), (10, 110)]
    font = pygame.font.Font(None, 32)
    color_fonts = [0, 0, 0]
    for i, color_font in enumerate(color_fonts):
        color_fonts[i] = font.render(str(color[i]), True, (255, 0, 0))
    

    preview_rect = pygame.Rect(10, 200, 50, 50)
    text_inputs = [pygame_textinput.TextInputVisualizer() for _ in range(3)]
    text_rects = [pygame.Rect(10, 10, 140, 32) for _ in range(3)]
    for i, pos in enumerate(positions):
        text_rects[i].topleft = pos
        text_rects[i].size = (140, 32)

    for i, text_input in enumerate(text_inputs):
        text_inputs[i].manager.input_string = color[i]
    pause_string = "Press Enter"
    pause_string_2 = "to change colors"
    paused_string = "DRAWING PAUSED"
    save_string = "Press 's' to save"
    click_number_string = "click numbers to"
    click_number_string_2 = "assign RGB value"
    pause_font = pygame.font.Font(None, 32)

    pause_text_location = (0, 360)
    paused_text_pos = (0, 160)
    paused_text_color = (255, 0, 0)
    paused_text_color_off = (255, 255, 255)
    pause_text = pause_font.render(pause_string, True, paused_text_color)
    pause_text_2 = pause_font.render(pause_string_2, True, paused_text_color)
    paused_text = pause_font.render(paused_string, True, paused_text_color)
    paused_text_off = pause_font.render(paused_string, True, paused_text_color_off)
    click_num = pause_font.render(click_number_string, True, paused_text_color)
    click_num_2 = pause_font.render(click_number_string_2, True, paused_text_color)
    saved_text = pause_font.render(save_string, True, paused_text_color)
    screen.fill((255, 255, 255))
    menu = False
    rect_selected = -1

    create_images_button = pygame.Rect(5, 800, 160, 50)
    button_string = "Create Images"
    button_text = pause_font.render(button_string, True, (0, 0, 0))
    while not done:

        events = pygame.event.get()
        #  Main event loop
        for event in events:
            # draw sections and text
            if not menu:
                screen.blit(paused_text_off, paused_text_pos)

            screen.blit(section, (190, 0))
            screen.blit(section_background, (0, 0))
            screen.blit(color_fonts[0], positions[0])
            screen.blit(color_fonts[1], positions[1])
            screen.blit(color_fonts[2], positions[2])
            screen.blit(pause_text, pause_text_location)
            screen.blit(pause_text_2, (0, 390))
            screen.blit(click_num, (0, 420))
            screen.blit(click_num_2, (0, 450))
            screen.blit(saved_text, (0, 620))

            #draw buttons
            pygame.draw.rect(screen, (0, 0, 0), create_images_button, 2)
            screen.blit(button_text, (10, 810))
            if event.type == pygame.QUIT:  # User clicked close
                done = True
            if not menu:
                if event.type == pygame.MOUSEBUTTONDOWN:  # Mouse button pressed
                    mouse_down = True
                elif event.type == pygame.MOUSEBUTTONUP:  # Mouse button released
                    mouse_down = False
                elif event.type == pygame.MOUSEMOTION:  # Mouse moved
                    if mouse_down:

                        if event.pos[0] > 200 and event.pos[0] < 1200:
                            if event.pos[1] > 0 and event.pos[1] < 1000:
                                print(event.pos)
                                # Draw a red dot at the mouse position
                                pygame.draw.circle(screen, color, event.pos, 10)

                                # Add the mouse position to the XML document
                                pos = ET.SubElement(xml_root, "partstitch")
                                # divide by 10 to scale down to 100x100
                                pos.set("x", str(round((event.pos[0] - 200))))
                                pos.set("y", str(round(event.pos[1])))
                                pos.set("color_1", str(color[0]))
                                pos.set("color_2", str(color[1]))
                                pos.set("color_3", str(color[2]))
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_s:
                        # The 's' key was pressed! Show the save dialog.
                        saved, filename = save_xml(xml_root)
            # Update text inputs
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN and not menu:
                    menu = True

                elif event.key == pygame.K_RETURN and menu:
                    menu = False
            if menu:
                pygame.draw.rect(screen, (0, 0, 0), text_rects[0], 2)
                pygame.draw.rect(screen, (0, 0, 0), text_rects[1], 2)
                pygame.draw.rect(screen, (0, 0, 0), text_rects[2], 2)
                pygame.draw.rect(screen, (255, 255, 30), create_images_button, 5)
                screen.blit(paused_text, paused_text_pos)
                if event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = pygame.mouse.get_pos()
                    for i, text_input in enumerate(text_rects):
                        # Check if the text input box was clicked

                        if text_rects[i].collidepoint(x, y):
                            rect_selected = i
                            # Set focus to the clicked text input box
                    if create_images_button.collidepoint(x, y):
                        if filename is None:
                            saved, filename = save_xml(xml_root)
                        if filename is not None:
                            sprite_micro_gen.main(50, 50, 25, 3, 1300, "2", 1, str(filename+".xml"), 15, str(filename+".xml"), False)
            if rect_selected == 0:

                pygame.draw.rect(screen, (255, 0, 0), text_rects[0], 2)
                new_color = color_select()
                if new_color is not None:
                    color[0] = int(new_color)
                    color_fonts[0] = font.render(str(color[0]), True, (255, 0, 0))
                    rect_selected = -1
            elif rect_selected == 1:
                pygame.draw.rect(screen, (255, 0, 0), text_rects[1], 2)
                new_color = color_select()
                if new_color is not None:
                    color[1] = int(new_color)
                    color_fonts[1] = font.render(str(color[1]), True, (255, 0, 0))
                    rect_selected = -1
            elif rect_selected == 2:
                pygame.draw.rect(screen, (255, 0, 0), text_rects[2], 2)
                new_color = color_select()
                if new_color is not None:
                    color[2] = int(new_color)
                    color_fonts[2] = font.render(str(color[2]), True, (255, 0, 0))
                    rect_selected = -1

        # Draw a preview of the pattern in the top left corner
        pygame.draw.rect(screen, (color[0], color[1], color[2]), preview_rect)
        # draw box around preview rect
        pygame.draw.rect(screen, (0, 0, 0), preview_rect, 2)
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
        if filename != None or "":
            tree = ET.ElementTree(xml_root)
            current_file_path = os.path.dirname(os.path.realpath(__file__))
            file_path = os.path.join(current_file_path, "patterns", f"{filename}.xml")
            tree.write(file_path)
            saved = True

    # Close the window and quit
    pygame.quit()

def save_xml(xml_root):
    root = tk.Tk()
    root.withdraw()  # Hide the main window
    filename = None
    while filename is None or filename == "":
        filename = simpledialog.askstring(
            "Filename", "Enter a name for the XML file:"
        )
        
        if filename is not None and filename != "":
            tree = ET.ElementTree(xml_root)
            current_file_path = os.path.dirname(
                os.path.realpath(__file__)
            )
            file_path = os.path.join(
                current_file_path, "patterns", f"{filename}.xml"
            )
            tree.write(file_path)
            saved = True
    return saved, filename
def color_select():
    root = tk.Tk()
    root.withdraw()  # Hide the main window
    new_color = simpledialog.askinteger("Color", "Enter a new color (0-255):")
    return new_color


if __name__ == "__main__":
    main()
