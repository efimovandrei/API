import os
import sys

import pygame
import requests

LON = '48.566888'
LAT = '55.856320'
zoom = 1
api_server = 'http://static-maps.yandex.ru/1.x/'
par = {
    "ll": ",".join([LON, LAT]),

    "l": "map",
    'z': str(zoom)
}

response = requests.get(api_server, params=par)

if not response:
    print("Ошибка выполнения запроса:")

    print("Http статус:", response.status_code, "(", response.reason, ")")
    sys.exit(1)

# Запишем полученное изображение в файл.
map_file = "map.png"
with open(map_file, "wb") as file:
    file.write(response.content)

# Инициализируем pygame
pygame.init()
screen = pygame.display.set_mode((600, 450))
# Рисуем картинку, загружаемую из только что созданного файла.
# Переключаем экран и ждем закрытия окна.
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_PAGEUP:
                if zoom + 1 <= 19:
                    zoom += 1
                    par = {
                        "ll": ",".join([LON, LAT]),

                        "l": "map",
                        'z': str(zoom)
                    }
                    response = requests.get(api_server, params=par)
                    map_file = "map.png"
                    with open(map_file, "wb") as file:
                        file.write(response.content)
            if event.key == pygame.K_PAGEDOWN:
                if zoom - 1 >= 1:
                    zoom -= 1
                    par = {
                        "ll": ",".join([LON, LAT]),

                        "l": "map",
                        'z': str(zoom)
                    }
                    response = requests.get(api_server, params=par)
                    map_file = "map.png"
                    with open(map_file, "wb") as file:
                        file.write(response.content)

    screen.blit(pygame.image.load(map_file), (0, 0))
    # Переключаем экран и ждем закрытия окна.
    pygame.display.flip()
pygame.quit()

# Удаляем за собой файл с изображением.
os.remove(map_file)

