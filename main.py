from pygame import *

WHITE = (255,255,255)
RED = (255,0,0)
TURQUOISE = (172, 230, 224)

font.init()
mixer.init()

mixer.music.load('Transcendence-chosic.com_.mp3_')
mixer.music.play()
# hit_sound = mixer.Sound('')

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def draw(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x < win_width - 80:
            self.rect.x += self.speed

win_width = 700
win_height = 500
window = display.set_mode((win_width, win_height))
display.set_caption('Пинг-Понг')
# bg = transform.scale(image.load(''),(win_width, win_height))
clock = time.Clock()
score = 0
finish = False
run = True
fps = 60

while run:
    for e in event.get():
        if e.type == QUIT:
            run = False
    
    if not finish:
        pass
        # window.blit(bg,(0,0))
        # text_score = font.SysFont(None, 33).render('Счет: '+str(score), 1, WHITE)
        
    display.update()
    clock.tick(fps)