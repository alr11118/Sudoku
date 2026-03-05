import pygame
pygame.font.init()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREY = (100, 100, 100)

screenWidth, screenHeight = 1000, 750
screen = pygame.display.set_mode((screenWidth, screenHeight))

headerFont = pygame.font.SysFont('Arial', 20, pygame.font.Font.bold)
headerText = headerFont.render("Welcome to my Sudoku Game!", 1, BLACK)


FPS = 60
def drawGameBoard():
    startX = 150
    startY = 150
    for row in range(0, 9):
        for column in range(0, 9):
            pygame.draw.rect(screen, GREY, (50*column + startX, 50*row + startY, 50, 50), 2)
    for row in range(1, 4):
        for column in range(1, 4):
            pygame.draw.rect(screen, BLACK, (150*column, 150*row, 150, 150), 3)
    pygame.draw.rect(screen, BLACK, (150, 150, 450, 450), 6)
    

def drawScreen():
    screen.fill(WHITE)
    screen.blit(headerText, (screenWidth//2 - headerText.get_width()//2, 10))
    drawGameBoard()
    pygame.display.update()

def main():
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

        drawScreen()
    pygame.quit()

if __name__ == "__main__":
    main()