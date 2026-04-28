import pygame
import sys

pygame.init()

# Устанавливаем размеры окна
screen_width = 800
screen_height = 600
window_size = (screen_width, screen_height)

# ИСПРАВЛЕНИЕ: Присваиваем объект окна переменной screen
screen = pygame.display.set_mode(window_size) 

# Задаем цвет фона
bg_color = (255, 255, 255)
screen.fill(bg_color)

# Выводим текст на экран
font = pygame.font.SysFont(None, 75)
text = font.render("Hello appsec world*", True, (0, 255, 0))
text_rect = text.get_rect()
text_rect.center = (400, 300)
screen.blit(text, text_rect)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    # ИСПРАВЛЕНИЕ: Обновление экрана перенесено внутрь цикла
    pygame.display.flip() 
