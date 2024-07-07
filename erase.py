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
        print(elements.get('x') , (round(event.pos[0]//10)*10) - 200)
        print(elements.get('y'), round(event.pos[1]//10)*10)
        x_loc=int(elements.get('x'))
        y_loc=int(elements.get('y'))
        if x_loc == (round(event.pos[0]//10)*10) - 200 and y_loc ==round(event.pos[1]//10)*10:
            xml.remove(elements)
            print('element removed')
def erase_at_pos_in_list():
    pass

