#!/usr/bin/python
# -*- coding: utf-8 -*-

import pygame

from CODE.Const import WIN_WIDTH, WIN_HEIGTH
from CODE.menu import Menu


# uma vez o pygame instalado, aqui devo importá-lo

class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size=(WIN_WIDTH, WIN_HEIGTH))

    def run(self):


        while True:
            menu = Menu(self.window)
            menu.run()
            pass






