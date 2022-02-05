import pygame as pg

class Game2048:
    def __init__(self) -> None:
        self.Height = 540
        self.Width = 960

        pg.init()

        #window creation
        self.win = pg.display.set_mode((self.Width, self.Height))
        pg.display.set_caption("2048")

    def play(self):
        run = True
        while run:
            pg.display.update()

if __name__ == "__main__":
    game = Game2048()
    game.play()
