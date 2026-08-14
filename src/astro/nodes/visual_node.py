import pygame, random
from pygame import Vector2
from pathlib import Path
from config import SCRIPT_PATH

# Node imports
from .node import Node

class VisualNode(Node):
    def __init__(self, update_list: list, draw_list: list, positon: Vector2, scale: Vector2, rotation: float):
        super().__init__(update_list)
        draw_list.append(self)
        self.positon = positon
        self.scale = scale
        self.rotation = rotation
    def update(self, delta):
        super().update(self)
    def draw(self, screen):
        pass