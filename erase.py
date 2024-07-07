"""Erase functions"""
import xml.etree.ElementTree as ET
import tkinter as tk
import pygame
import pygame_textinput


def erase_at_pos_on_canvas(screen, background_color, event, size):
   

    pygame.draw.rect(screen, background_color, (round(event.pos[0]//10)*10, round(event.pos[1]//10)*10, size, size))

    #call erase_at_pos_in_xml

    #call erase_at_pos_in_list


def erase_at_pos_in_xml(xml,event):

    for elements in xml.findall('sprite'):
        x_loc=int(elements.get('x'))
        y_loc=int(elements.get('y'))
        if x_loc == (round(event.pos[0]//10)*10) - 200 and y_loc ==round(event.pos[1]//10)*10:
            xml.remove(elements)
            
def erase_at_pos_in_list(drawing_array, event):
    for coord in drawing_array:
        x_loc=coord.x
        y_loc=coord.y
        print(x_loc,(round(event.pos[0]//10)*10))
        print(y_loc,round(event.pos[1]//10)*10)
        if x_loc == (round(event.pos[0]//10)*10) and y_loc ==round(event.pos[1]//10)*10:
            print("removing coord")
            drawing_array.remove(coord)
    return drawing_array  

    

