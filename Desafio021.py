# Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3.

import pygame

pygame.init()
pygame.mixer.music.load('Desafio021.mp3')
pygame.mixer.music.player()
pygame.event.wait()
