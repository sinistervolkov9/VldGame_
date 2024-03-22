import sys
from settings import *
import pygame as pg
# from scene_init import Scene
from card_class import CardClass
from player import Player
from card_loot import CardLoot
from deck import Deck
from screen import Screen
from button import Button


class Game:
    def __init__(self):
        pg.init()  # Инициализатор pygame
        self.screen = pg.display.set_mode(RES)
        self.clock = pg.time.Clock()
        self.new_game()

    def new_game(self):
        # self.scene = Scene(current_scene="scene_main_menu")

        self.screeeeennnn = Screen(self, None, None, None)
        self.button = Button(self, None, None, None, 'text', None, None)

        self.card_loot_1 = CardLoot(self,
                                    "resources/card_items/image/image.png",
                                    "resources/card_items/description_block/description_block.png",
                                    "resources/card_items/frame/frame.png",
                                    "resources/card_items/name_block/name_block.png",
                                    "меч", "Описание",
                                    'basic', 'strength', 2, 3,
                                    1, 3, 1,
                                    3, 0,
                                    [], [])
        self.card_loot_2 = CardLoot(self,
                                    "resources/card_items/image/image.png",
                                    "resources/card_items/description_block/description_block.png",
                                    "resources/card_items/frame/frame.png",
                                    "resources/card_items/name_block/name_block.png",
                                    "наручи", "Описание",
                                    'basic', 'strength', 2, 3,
                                    1, 3, 1,
                                    1, 1,
                                    [], [])
        self.deck = Deck(self, [self.card_loot_1, self.card_loot_2])
        self.card_class = CardClass(self,
                                    self.deck,
                                    "resources/card_items/image/image.png",
                                    "resources/card_items/description_block/description_block.png",
                                    "resources/card_items/frame/frame.png",
                                    "resources/card_items/name_block/name_block.png",
                                    "рыцарь", "Описание",
                                    2, 0, 0)
        self.player = Player(self, self.card_class, 1, 1, 1, 1, 5)

    def update(self):
        """
        Метод обновления экрана (flip)
        """
        # self.scene.button_update(self.screen)
        pg.display.flip()
        self.clock.tick(FPS)  # Чилсо итераций (обновлений основного цикла игры за одну секунду)
        pg.display.set_caption("Vld Game")

        self.button.check_hover(pg.mouse.get_pos())
        self.card_class.card_check_hover(pg.mouse.get_pos())

    def draw(self):
        """
        Метод нанасения на экран чего-либо
        (рисование, заливка).
        Видимо здесь должны подгружаться менюшки
        """
        self.screen.fill("black")
        # self.scene.screen_draw(self.screen)

        self.screeeeennnn.draw()
        self.button.draw()
        self.card_class.draw()

    def check_events(self):
        """
        Проверка на нажатие кнопок и т. п.
        """
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            # self.card_class.card_hover_event(event)
            self.button.handle_event(event)

        # self.scene.esc_event(event)
        # self.scene.button_click_event(event)
        # self.scene.button_handle_event(event)
        # self.scene.click_event(event)

    def run(self):
        """
        Работа программы, как процесс
        """
        # self.card_class.check_simbols()
        self.player.print_stats()
        while True:
            self.check_events()
            self.update()
            self.draw()


if __name__ == "__main__":
    game = Game()
    game.run()
