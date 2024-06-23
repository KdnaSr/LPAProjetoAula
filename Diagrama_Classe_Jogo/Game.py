#!/usr/bin/python
#-*- coding: utf-8 -*-

import pygame as pygame

from Menu import Menu


class Game:

    def __init__(self):
        pygame.int()
        self.window = pygame.display.setmode(size=(600, 480))

    def run(self):
        while True:
            menu = Menu(self.window)
            menu.run()
            
            pass

