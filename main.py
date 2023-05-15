import pygame
import os

WIDTH, HEIGHT = 1200, 900
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Vrhcáby!!")

FPS = 30

BOARD_IMAGE = pygame.image.load(os.path.join('Obrazky', 'board.jpg'))
BOARD = pygame.transform.scale(BOARD_IMAGE, (WIDTH, HEIGHT))
BLACK_STONE_IMAGE = pygame.image.load(os.path.join('Obrazky', 'black_stone.png'))
BLACK_STONE = pygame.transform.scale(BLACK_STONE_IMAGE, (50, 50))
WHITE_STONE_IMAGE = pygame.image.load(os.path.join('Obrazky', 'white_stone.png'))
WHITE_STONE = pygame.transform.scale(WHITE_STONE_IMAGE, (50, 50))

def draw_window():
    WIN.fill((255, 255, 255)) #Výplň bílou
    WIN.blit(BOARD, (0, 0))
    # WIN.blit(BLACK_STONE, (1050, 50))
    # WIN.blit(WHITE_STONE, (1050, 750))
    draw_stones()
    pygame.display.update()

def draw_stones():
    for i in range(0, 2):
        WIN.blit(BLACK_STONE, (1075, 50+i*(BLACK_STONE.get_width()+5)))
        WIN.blit(WHITE_STONE, (1075, 800-i*(WHITE_STONE.get_width()+5)))
    
    for i in range(0, 5):
        WIN.blit(BLACK_STONE, (625, 800-i*(BLACK_STONE.get_width()+5)))
        WIN.blit(WHITE_STONE, (625, 50+i*(WHITE_STONE.get_width()+5)))
        WIN.blit(BLACK_STONE, (75, 50+i*(BLACK_STONE.get_width()+5)))
        WIN.blit(WHITE_STONE, (75, 800-i*(WHITE_STONE.get_width()+5)))

    for i in range(0, 3):
        WIN.blit(BLACK_STONE, (525, 800-i*(BLACK_STONE.get_width()+5)))
        WIN.blit(WHITE_STONE, (525, 50+i*(WHITE_STONE.get_width()+5)))

def main():
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            #Zavírání okna
            if event.type == pygame.QUIT:
                run = False

        draw_window()

    pygame.quit()

if __name__ == "__main__":
    main()