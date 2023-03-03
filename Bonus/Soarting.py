import pygame
import random
import numpy as np


pygame.init()

WINDOW_SIZE = (800, 600)
WINDOW_TITLE = "Sorting Algorithm Visualizer"
window = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption(WINDOW_TITLE)


BACKGROUND_COLOR = (255, 255, 255)
BAR_COLOR = (0, 0, 255)
SWAP_COLOR = (255, 0, 0)
MAX_FREQUENCY = 2000

ARRAY_SIZE = 100


array = [random.randint(1, WINDOW_SIZE[1]) for i in range(ARRAY_SIZE)]


def bubble_sort(array):
    n = len(array)
    for i in range(n):
        for j in range(0, n-i-1):
            frequency = int(MAX_FREQUENCY * (j+1) / ARRAY_SIZE)
            duration = 50
            sample_rate = 44100
            t = np.linspace(0, duration / 1000, int(duration * sample_rate / 1000), False)
            wave = np.sin(2 * np.pi * frequency * t)
            sound_data = np.array(np.round(32767 * wave), dtype=np.int16)
            sound = pygame.mixer.Sound(sound_data)
            sound.set_volume(0.5)
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

    pygame.display.update()


bubble_sort(array)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
