"""Erase functions"""
import tkinter as tk
import pygame
import pygame_textinput

def erase_at_pos_on_canvas(screen, background_color, event, size):
   

    pygame.draw.rect(screen, background_color, (round(event.pos[0]//10)*10, round(event.pos[1]//10)*10, size, size))

    #call erase_at_pos_in_xml

    #call erase_at_pos_in_list


def erase_at_pos_in_xml():
   pass
    

def erase_at_pos_in_list():
    pass

