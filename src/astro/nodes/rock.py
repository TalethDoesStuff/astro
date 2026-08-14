import pygame
from pygame import Vector2, Vector3, rect
from pathlib import Path
from config import SCRIPT_PATH
from .visual_node import VisualNode


class Rock(VisualNode):
    def __init__(
        self,
        update_list: list,
        draw_list: list,
        position: Vector2,
        scale: Vector2,
        rotation: float,
        velocity: Vector2,
        screen: pygame.Surface,
    ):
        super().__init__(update_list, draw_list, position, scale, rotation)
        self.position = position
        self.scale = scale
        self.velocity = velocity
        self.screen = screen
        self.sprite = pygame.image.load(
            str(Path.joinpath(SCRIPT_PATH, "assets", "rock.png"))
        )

    def update(self, delta):
        self.position += self.velocity * delta
        if self.position.x > self.screen.get_width():
            self.position.x = 0
        if self.position.x < 0:
            self.position.x = self.screen.get_width()
        if self.position.y > self.screen.get_height():
            self.position.y = 0
        if self.position.y < 0:
            self.position.y = self.screen.get_height()

    def draw(self, screen: pygame.Surface):
        self.sprite = pygame.transform.scale(
            self.sprite,
            (
                self.sprite.get_width() * self.scale.x,
                self.sprite.get_height() * self.scale.y,
            ),
        )
        screen.blit(self.sprite, self.position)
