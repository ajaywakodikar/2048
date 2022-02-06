import random as rnd
import pygame as pg
import numpy as np

BG_COLORS = {
    0: (250, 250, 250),
    2: (238, 228, 218), 
    4: (238, 225, 201),
    8: (243, 178, 122),
    16: (246, 150, 100),
    32: (247, 124, 95),
    64: (247, 95, 59),
    128: (237, 208, 115),
    256: (237, 204, 98),
    512: (237, 201, 80),
    1024: (237, 197, 63),
    2048: (237, 194, 46)
}

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
        self.myFont = pg.font.SysFont("Overpass", 30)
        pg.display.set_caption("2048")

        #init board status
        self.boardStatus = np.zeros((self.N, self.N))
        self.addNewNumber() #add new number to board

    def addNewNumber(self):
        freePos = zip(*np.where(self.boardStatus == 0))
        freePos = list(freePos)

        for pos in rnd.sample(freePos, k = 1):
            self.boardStatus[pos] = 2

    def Board(self):
        self.win.fill(self.winBgColor)
        for r in range(self.N):
            rectY = self.blockSize * r + self.gap
            for c in range(self.N):
                rectX = self.blockSize * c + self.gap
                cellValue = int(self.boardStatus[r][c])
                pg.draw.rect(self.win, BG_COLORS[cellValue], pg.Rect(rectX, rectY, self.cellSize, self.cellSize))
                if cellValue != 0: 
                    textSurface = self.myFont.render(f"{cellValue}", True, (0, 0, 0))
                    textRect = textSurface.get_rect(center = (rectX + self.blockSize / 2, rectY + self.blockSize / 2))
                    self.win.blit(textSurface, textRect)

    def compressNumber(self, data):
        result = [0]
        data = [x for x in data if x != 0]
        for element in data:
            if element == result[len(result) - 1]:
                result[len(result) - 1] *= 2
                result.append(0)
            else:
                result.append(element)

        result = [x for x in result if x != 0]
        return result

    def move(self, dir):
        for i in range(self.N):
            if dir in "UD":
                data = self.boardStatus[:, i]
            else: 
                data = self.boardStatus[i, :]

            flip = False
            if dir in "RD":
                flip = True
                data = data[::-1]

            data = self.compressNumber(data)
            data = data + (self.N - len(data)) * [0]

            if flip: 
                data = data[::-1]

            if dir in "UD":
                self.boardStatus[:, i] = data
            else:
                self.boardStatus[i, :] = data

    def isGameOver(self):
        boardStatusBackup = self.boardStatus.copy()
        for dir in "UDLR":
            self.move(dir)
            if(self.boardStatus == boardStatusBackup).all() == False:
                self.boardStatus = boardStatusBackup
                return False
        return True

    def play(self):
        run = True
        while run:
            self.Board()
            pg.display.update()

            for event in pg.event.get(): 
                oldBoardStatus = self.boardStatus.copy()
                if event.type == pg.QUIT:
                    run = False
                elif event.type == pg.KEYDOWN:
                    if event.key == pg.K_UP: 
                        self.move("U")
                    elif event.key == pg.K_DOWN: 
                        self.move("D")
                    elif event.key == pg.K_LEFT: 
                        self.move("L")
                    elif event.key == pg.K_RIGHT: 
                        self.move("R")
                    elif event.key == pg.K_ESCAPE:
                        run = False
                
                if self.isGameOver():
                    print("Game Over !!")
                    return

                if(self.boardStatus == oldBoardStatus).all() == False:
                    self.addNewNumber()

if __name__ == "__main__":
    game = Game2048()
    game.play()
