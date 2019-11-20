import pygame
import sys

audiopath=sys.argv[1]

pygame.mixer.init()
pygame.mixer.music.load(audiopath)
pygame.mixer.music.play()
while pygame.mixer.music.get_busy():
    pygame.time.Clock().tick(10)