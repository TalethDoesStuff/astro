import pygame
from pygame import Vector2
from config import SCRIPT_PATH, VIRTUAL_WINDOW_SIZE, WINDOW_SIZE
from pathlib import Path

# Node imports
from .visual_node import VisualNode

ACCELERATION = 20.0
MAX_SPEED = 200.0
FRICTION = 12.0


def blitRotateCenter(surf, image, topleft, angle):

    rotated_image = pygame.transform.rotate(image, angle)
    new_rect = rotated_image.get_rect(center=image.get_rect(topleft=topleft).center)

    surf.blit(rotated_image, new_rect)


class Player(VisualNode):
    def __init__(
        self,
        update_list: list,
        draw_list: list,
        positon: Vector2,
        scale: Vector2,
        rotation: float,
        screen: pygame.Surface,
    ):
        super().__init__(update_list, draw_list, positon, scale, rotation)
        self.positon = positon
        self.scale = scale
        self.screen = screen
        self.rotation = rotation
        self.velocity = Vector2(0, 0)
        self.sprite = pygame.image.load(
            str(Path.joinpath(SCRIPT_PATH, "assets", "player.png"))
        )
        self.sprite = pygame.transform.scale(
            self.sprite,
            (self.sprite.get_width() * scale.x, self.sprite.get_height() * scale.y),
        )

    def update(self, delta):
        keys = pygame.key.get_pressed()

        input_vector = Vector2()
        input_vector.x = int(keys[pygame.K_d]) - int(keys[pygame.K_a])
        input_vector.y = int(keys[pygame.K_s]) - int(keys[pygame.K_w])
        self.velocity += input_vector * ACCELERATION * delta
        self.velocity.x = max(-MAX_SPEED, min(self.velocity.x, MAX_SPEED))
        self.velocity.y = max(-MAX_SPEED, min(self.velocity.y, MAX_SPEED))
        self.velocity.x = pygame.math.lerp(self.velocity.x, 0, FRICTION * delta)
        self.velocity.y = pygame.math.lerp(self.velocity.y, 0, FRICTION * delta)
        prev_position = self.positon.copy()
        self.positon += self.velocity
        if self.positon == prev_position:
            self.velocity = Vector2(0, 0)
        if input_vector.x == 0:
            self.positon.x = max(0, min(self.positon.x, self.screen.get_width()))
        if input_vector.y == 0:
            self.positon.y = max(0, min(self.positon.y, self.screen.get_height()))

        mouse = Vector2(pygame.mouse.get_pos())

        mouse.x *= VIRTUAL_WINDOW_SIZE[0] / WINDOW_SIZE[0]
        mouse.y *= VIRTUAL_WINDOW_SIZE[1] / WINDOW_SIZE[1]

        direction = pygame.Vector2(mouse) - self.positon
        self.rotation = direction.angle_to(pygame.Vector2(1, 0)) - 90

    def draw(self, screen):
        rotated_sprite = pygame.transform.rotate(self.sprite, self.rotation)

        rect = rotated_sprite.get_rect(center=self.positon)
        screen.blit(rotated_sprite, rect)
