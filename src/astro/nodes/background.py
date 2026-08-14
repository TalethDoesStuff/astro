import pygame

# Node import
from .node import Node

class Background(Node):
    def __init__(self, draw_list, color):
        super().__init__(draw_list)
        self.color = color
    
    def draw(self, screen):
        # Fill the screen with the provided color
        if self.color is not None:
            screen.fill(self.color)