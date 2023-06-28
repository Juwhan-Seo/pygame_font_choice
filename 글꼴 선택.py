import pygame
from pygame.locals import QUIT, K_SPACE, KEYDOWN
import sys


pygame.init()
fonts = pygame.font.get_fonts()
SUR = pygame.display.set_mode((300, 300))
FPS = pygame.time.Clock()


print(fonts)
f = [None] * len(fonts)
for i in range(len(fonts)):
    f[i] = pygame.font.SysFont(fonts[i], 30)
print(f)
fav = []
cnt = 0
idx = 88


while True:
    SUR.fill((0, 0, 0))
    for i in pygame.event.get():
        if i.type == QUIT:
            pygame.quit()
            sys.exit()
        elif i.type == KEYDOWN:
            if i.key == K_SPACE:
                fav.append(fonts[idx])
                print(fav)


    if cnt % 15 == 0:
        idx += 1
    cnt += 1
    mess = f[idx].render(
        f"Hello 안녕 {idx+1}/{len(fonts)}", True, (255, 255, 255))
    SUR.blit(mess, (0, 0))
    pygame.display.flip()


    FPS.tick(15)
