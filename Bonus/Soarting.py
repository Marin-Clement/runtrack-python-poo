import pygame
import random
import time

pygame.init()

WINDOW_SIZE = (800, 600)
WINDOW_TITLE = "Sorting Algorithm Visualizer"
window = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption(WINDOW_TITLE)


FONT_SIZE = 30
font = pygame.font.SysFont(None, FONT_SIZE)


BACKGROUND_COLOR = (255, 255, 255)
BAR_COLOR = (0, 0, 255)
SWAP_COLOR = (255, 0, 0)
SOUND_FREQUENCY = 44100


ARRAY_SIZE = 50


array = [random.randint(1, WINDOW_SIZE[1] - FONT_SIZE) for i in range(ARRAY_SIZE)]


def bubble_sort(array):
    n = len(array)
    for i in range(n):
        for j in range(0, n-i-1):
            sound = pygame.mixer.Sound("beep.wav")
            sound.play()
            draw_bars(array, j, j+1)

            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]

                draw_bars(array, j, j+1, SWAP_COLOR)


def draw_bars(array, index1=None, index2=None, color=BAR_COLOR):

    window.fill(BACKGROUND_COLOR)

    for i, value in enumerate(array):
        if i == index1 or i == index2:
            pygame.draw.rect(window, color, (i * (WINDOW_SIZE[0] / ARRAY_SIZE), WINDOW_SIZE[1] - value, WINDOW_SIZE[0] / ARRAY_SIZE, value))
        else:
            pygame.draw.rect(window, BAR_COLOR, (i * (WINDOW_SIZE[0] / ARRAY_SIZE), WINDOW_SIZE[1] - value, WINDOW_SIZE[0] / ARRAY_SIZE, value))

        text = font.render(str(value), True, (0, 0, 0))
        window.blit(text, (i * (WINDOW_SIZE[0] / ARRAY_SIZE) + 10, WINDOW_SIZE[1] - value - FONT_SIZE))

    pygame.display.update()


bubble_sort(array)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
