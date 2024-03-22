import pygame as pg
from settings import RES, SCREEN_POS


class Screen:
    def __init__(self,
                 game,
                 image,
                 size=None, pos=None
                 ):
        self.game = game

        self.image = 'resources/backgrounds/background.png' if image is None else image
        self.size = RES if size is None else size
        self.pos = SCREEN_POS["topleft"] if pos is None else pos

        self.load_images()
        self.get_size_pos()
        self.update()  # ?

    def load_images(self):
        self.image = pg.image.load(self.image)

    def update(self):
        self.image = pg.transform.scale(self.image, self.size)
        self.image_rect = self.image.get_rect(topleft=self.pos)

    def get_size_pos(self):
        pass

    def draw(self):
        self.game.screen.blit(self.image, self.image_rect.topleft)
