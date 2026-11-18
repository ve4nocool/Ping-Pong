from pygame import *

WHITE = (255,255,255)
RED = (255,0,0)
TURQUOISE = (172, 230, 224)

font.init()
mixer.init()

mixer.music.load('Transcendence-chosic.com_.mp3')
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
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y >= 0:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y <= win_height - 136:
            self.rect.y += self.speed

    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y >= 0: 
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y <= win_height - 136:
            self.rect.y += self.speed

win_width = 700
win_height = 500
window = display.set_mode((win_width, win_height))
display.set_caption('Пинг-Понг')
bg = transform.scale(image.load('tennisCourt.png'),(win_width, win_height))
clock = time.Clock()
ball = GameSprite('tenis_ball.png', 225, 325, 50, 50, 4)
padel_left = Player('racket.webp', 40, 190, 37, 136, 3)
padel_right = Player('racket.webp', 620, 190, 37, 136, 3)
d_y = 3
d_x = 3
score = 0
finish = False
run = True
fps = 60

while run:
    for e in event.get():
        if e.type == QUIT:
            run = False
    
    if not finish:
        window.blit(bg,(0,0))
        ball.draw()
        padel_left.draw()
        padel_right.draw()
        padel_left.update_l()
        padel_right.update_r()
        ball.rect.x += d_x
        ball.rect.y += d_y
        # text_score = font.SysFont(None, 33).render('Счет: '+str(score), 1, WHITE)
        
    display.update()
    clock.tick(fps)