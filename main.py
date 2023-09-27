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

class Triangle:
    def __init__(self, point1, point2, point3, position):
        self.point1 = point1
        self.point2 = point2
        self.point3 = point3
        self.position = position

triangle_color = (255, 0, 0)  # Červená (R, G, B)

# # Body trojúhelníku (x, y)
# point1 = (0, 0)
# point2 = (300, 300)
# point3 = (500, 300)

# Funkce, která se spustí po kliknutí na trojúhelník
def on_triangle_click():
    print("Trojúhelník byl kliknut!")

# Funkce pro ověření, zda bylo kliknuto na obrázek
def is_clicked_on_image(image_rect):
    mouse_pos = pygame.mouse.get_pos()
    if image_rect.collidepoint(mouse_pos):
        return True
    return False

def draw_window():
    WIN.fill((255, 255, 255)) #Výplň bílou
    # WIN.blit(BOARD, (0, 0)) #Pozadí - obrázek
    WIN.blit(BLACK_STONE, (1050, 50))
    WIN.blit(WHITE_STONE, (1050, 750))
    # draw_stones()
    draw_board()
    pygame.display.update()

def draw_board():
    # Vytvoření dvourozměrného pole 2x12
    triangle_array = [[None] * 12 for _ in range(2)]

    # Generování trojúhelníků a jejich umístění do pole
    for i in range(2):
        for j in range(12):
            # Generování bodů pro trojúhelník
            point1 = (j * WIDTH/12, i * WIDTH/12)
            point2 = (j * WIDTH/12 + 30, i * WIDTH/12)
            point3 = (j * HEIGHT/2 + 15, i * HEIGHT/2 + 30)
            points = [point1, point2, point3]

            # Vytvoření trojúhelníku a uložení do pole
            triangle = Triangle(point1, point2, point3, [i, j])
            triangle_array[i][j] = triangle

            pygame.draw.polygon(WIN, triangle_color, points)

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
            # elif event.type == pygame.MOUSEBUTTONDOWN:
            #     if pygame.mouse.get_pressed()[0]:  # Zkontrolujte, zda bylo kliknuto levým tlačítkem myši
            #         x, y = pygame.mouse.get_pos()
            #         # Kontrola, zda bylo kliknuto uvnitř trojúhelníka
            #         if (point1[0] <= x <= point3[0] and
            #             point1[1] <= y <= point2[1]):
            #             on_triangle_click()
            # elif event.type == pygame.MOUSEBUTTONDOWN:
            #     if pygame.mouse.get_pressed()[0]:
            #         if is_clicked_on_image(BLACK_STONE):
            #             print("Kliknuto na obrázek!")
    
        draw_window()

    pygame.quit()

if __name__ == "__main__":
    main()

