import pygame
import sys

pygame.init()

# Настройки экрана
WIDTH, HEIGHT = 400, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Python Clicker")

# Цвета (RGB)
BG_COLOR = (25, 25, 30)
BTN_COLOR = (0, 200, 150)
WHITE = (255, 255, 255)

# Шрифт и переменные
font = pygame.font.Font(None, 48)
gold = 0

# Прямоугольник кнопки (x, y, width, height)
button_rect = pygame.Rect(100, 350, 200, 80)

clock = pygame.time.Clock()

while True:
    screen.fill(BG_COLOR)

    # Обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # Клик мыши или тап по экрану
        if event.type == pygame.MOUSEBUTTONDOWN:
            if button_rect.collidepoint(event.pos):
                gold += 1

    # Рисуем кнопку
    pygame.draw.rect(screen, BTN_COLOR, button_rect, border_radius=12)

    # Отрисовка текста счетчика
    text_gold = font.render(f"Голда: {gold}", True, WHITE)
    screen.blit(text_gold, (text_gold.get_rect(center=(WIDTH // 2, 180))))

    # Отрисовка текста на кнопке
    text_btn = font.render("ТЫК!", True, BG_COLOR)
    screen.blit(text_btn, (text_btn.get_rect(center=button_rect.center)))

    pygame.display.flip()
    clock.tick(60)
