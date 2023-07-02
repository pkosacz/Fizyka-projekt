import time
import numpy as np
import pygame

color_background = (0, 0, 0)
color_grid = (30, 30, 30)
color_cell = (255, 255, 255)
pygame.init()
pygame.display.set_caption("Game of life")
icon = pygame.image.load("icon.png")
pygame.display.set_icon(icon)


def update_cell(screen, cells, size, with_progress=False):
    updated_cells = np.zeros((cells.shape[0], cells.shape[1]))

    for row, column in np.ndindex(cells.shape):
        alive = np.sum(cells[row-1:row+2, column-1:column+2]) - cells[row, column]

        if cells[row, column] == 0:
            color = color_background
        else:
            color = color_cell

        if cells[row, column] == 1:
            if alive < 2 or alive > 3:
                if with_progress == True:
                    color = color_background
            elif 2 <= alive <= 3:
                updated_cells[row, column] = 1
                if with_progress == True:
                    color = color_cell
        else:
            if alive == 3:
                updated_cells[row, column] = 1
                if with_progress == True:
                    color = color_cell

        pygame.draw.rect(screen, color, (column * size, row * size, size - 1, size - 1))

    return updated_cells


def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))

    cells = np.zeros((30, 40))
    screen.fill(color_grid)
    update_cell(screen, cells, 20)

    pygame.display.flip()
    pygame.display.update()

    running = False

    while True:
        for Q in pygame.event.get():
            if Q.type == pygame.QUIT:
                pygame.quit()
                return
            elif Q.type == pygame.KEYDOWN:
                if Q.key == pygame.K_SPACE:
                    running = not running
                    update_cell(screen, cells, 20)
                    pygame.display.update()
            if pygame.mouse.get_pressed()[0]:
                pos = pygame.mouse.get_pos()
                cells[pos[1] // 20, pos[0] // 20] = 1
                update_cell(screen, cells, 20)
                pygame.display.update()

        screen.fill(color_grid)

        if running == True:
            cells = update_cell(screen, cells, 20, with_progress=True)
            pygame.display.update()
            time.sleep(0.1)


if __name__ == "__main__":
    main()
