import pygame as pg

class Game2048:
    def __init__(self) -> None:
        self.N = 4
        self.cellSize = 100
        self.gap = 5
        self.blockSize = self.cellSize + self.gap * 2
        self.winBgColor = (100, 150, 200)
        self.winWidth = self.blockSize * 4
        self.winHeight = self.winWidth

        pg.init()

        #window creation
        self.win = pg.display.set_mode((self.winWidth, self.winHeight))
        pg.display.set_caption("2048")

    def Board(self):
        self.win.fill(self.winBgColor)
        for r in range(self.N):
            rectY = self.blockSize * r + self.gap
            for c in range(self.N):
                rectX = self.blockSize * c + self.gap
                pg.draw.rect(self.win, (0, 0, 0), pg.Rect(rectX, rectY, self.cellSize, self.cellSize))

    def play(self):
        run = True
        while run:
            self.Board()
            pg.display.update()

            for event in pg.event.get(): 
                if event.type == pg.QUIT:
                    run = False
                elif event.type == pg.KEYDOWN:
                    if event.key == pg.K_UP: 
                        print("U")
                    elif event.key == pg.K_DOWN: 
                        print("D")
                    elif event.key == pg.K_LEFT: 
                        print("L")
                    elif event.key == pg.K_RIGHT: 
                        print("R")
                    elif event.key == pg.K_ESCAPE:
                        run = False

if __name__ == "__main__":
    game = Game2048()
    game.play()
