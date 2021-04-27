import pygame
import game_constants as constants

pygame.init()

screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((217, 211, 176))
    # Main game drawing goes here
    for i in range(64):
        filled_rect = pygame.Rect((((i//8) * constants.SPACE_DIMENSIONS) + constants.BOARD_X_OFFSET), (((i%8) * constants.SPACE_DIMENSIONS) + constants.BOARD_Y_OFFSET), constants.SPACE_DIMENSIONS, constants.SPACE_DIMENSIONS)
        color = constants.DARK_COLOR if ((i % 2 == 0 and (i//8) % 2 == 1) or (i % 2 == 1 and (i//8) % 2 == 0)) else constants.LIGHT_COLOR
        pygame.draw.rect(screen, color, filled_rect)

    pygame.display.update()