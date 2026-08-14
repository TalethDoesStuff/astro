# Made by taleth, do not steal.

# Library imports
import pygame
import random
from pygame import Vector2, Vector3, rect
from config import WINDOW_SIZE, VIRTUAL_WINDOW_SIZE

# Node imports
from nodes.background import Background
from nodes.rock import Rock
from nodes.visual_node import VisualNode
from nodes.player import Player


def screen_center(screen: pygame.display) -> Vector2:
    return Vector2(screen.get_width() / 2, screen.get_height() / 2)


def main():
    # Window setup
    pygame.init()
    window = pygame.display.set_mode(WINDOW_SIZE)
    screen = pygame.Surface(VIRTUAL_WINDOW_SIZE)
    pygame.display.set_caption("Astro")
    clock = pygame.time.Clock()
    running = True
    delta = 0

    # Lists containing nodes to be updated
    draw_list = []
    update_list = []

    # rock
    background = Background(draw_list=draw_list, color=(0, 0, 0))
    player = Player(
        update_list=update_list,
        draw_list=draw_list,
        positon=screen_center(screen),
        scale=Vector2(1, 1),
        rotation=0,
        screen=screen,
    )

    for i in range(2):
        rock = Rock(
            update_list=update_list,
            draw_list=draw_list,
            positon=Vector2(0, 1),
            scale=Vector2(1, 1),
            velocity=Vector2(random.random() * 100, random.random() * 100),
            rotation=1,
            screen=screen,
        )

    # Main look
    while running:

        # Quit
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Update all the nodes
        for node in update_list:
            node.update(delta)

        # Clear the screen and draw all the nodes then apply changes
        screen.fill("purple")
        for node in draw_list:
            node.draw(screen)
        scaled_surface = pygame.transform.scale(screen, WINDOW_SIZE)
        window.blit(scaled_surface, (0, 0))
        pygame.display.flip()

        delta = clock.tick(60) / 1000

    pygame.quit()


if __name__ == "__main__":
    main()
