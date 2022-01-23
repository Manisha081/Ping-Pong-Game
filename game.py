import pygame,sys
pygame.init()
#display
width,height=750,500
display = pygame.display.set_mode((width,height))
pygame.display.set_caption('ping pong')
winner_font = pygame.font.SysFont('cambria', 30)
# Colors
red = (255, 0, 0)
black = (0, 0, 0)
blue = (0, 0, 255)
white = (255, 255, 255)
green = (0, 255, 0)

# Classes
class Paddle1(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([5, 105])
        self.image.fill(red)
        self.rect = self.image.get_rect()
        self.points = 0


class Paddle2(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([5, 105])
        self.image.fill(red)
        self.rect = self.image.get_rect()
        self.points = 0


class Ball(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((16, 16))
        self.image.fill(green)
        self.rect = self.image.get_rect()
        self.speed = 15
        self.dx = 1
        self.dy = 1

# Creation

paddle1 = Paddle1()
paddle1.rect.x = 45
paddle1.rect.y = 225

paddle2 = Paddle2()
paddle2.rect.x = 700
paddle2.rect.y = 225

paddle_speed = 10

pong = Ball()
pong.rect.x = 375
pong.rect.y = 250

# Group of Sprites

all_sprites = pygame.sprite.Group()
all_sprites.add(paddle1, paddle2, pong)


def redraw():
    # Draws black screen
    display.fill(black)

    # Title font
    font = pygame.font.SysFont('italic',30)
    text = font.render('PING PONG', False, white)
    text_rect = text.get_rect()
    text_rect.center = (width // 2, 25)
    display.blit(text, text_rect)

    # Player 1 Score
    font = pygame.font.SysFont('italic',30)
    p1_score = font.render('Left player:'+str(paddle1.points), False, blue)
    p1_rect = p1_score.get_rect()
    p1_rect.center = (130,25)
    display.blit(p1_score, p1_rect)

    # Player 2 Score
    font = pygame.font.SysFont('italic', 30)
    p2_score = font.render('Right player:'+str(paddle2.points), False, blue)
    p2_rect = p2_score.get_rect()
    p2_rect.center = (630, 25)
    display.blit(p2_score, p2_rect)

    # Updates all Sprites
    all_sprites.draw(display)

    # Draws updates
    pygame.display.update()

def draw_winner(text):
    draw_text = winner_font.render(text, False, blue)
    display.blit(draw_text, (width//2 - draw_text.get_width()/2, height//2 - draw_text.get_height()/2))
    pygame.display.update()
    pygame.time.delay(5000)

run = True
paddle1.points = 0
paddle2.points = 0
# Main Loop
while run:

    pygame.time.delay(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    winner_text = ' '
    if paddle1.points >= 10:
        winner_text = 'LEFT PLAYER WINS!'

    if paddle2.points >= 10:
        winner_text = 'RIGHT PLAYER WINS!'

    if winner_text != ' ':
        draw_winner(winner_text)
        break

    # Quit Event
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # Paddle Movement
    key = pygame.key.get_pressed()
    if key[pygame.K_w]:
        paddle1.rect.y += -paddle_speed
    if key[pygame.K_s]:
        paddle1.rect.y += paddle_speed
    if key[pygame.K_UP]:
        paddle2.rect.y += -paddle_speed
    if key[pygame.K_DOWN]:
        paddle2.rect.y += paddle_speed

    # Moves pong ball
    pong.rect.x += pong.speed * pong.dx
    pong.rect.y += pong.speed * pong.dy

    # Wall and Paddle Bounces
    if pong.rect.y > 490:
        pong.dy = -1

    if pong.rect.y < 1:
        pong.dy = 1

    if pong.rect.x > 740:
        pong.rect.x, pong.rect.y = 375, 250
        pong.dx = -1
        paddle1.points += 1

    if pong.rect.x < 1:
        pong.rect.x, pong.rect.y = 375, 250
        pong.dx = 1
        paddle2.points += 1

    if paddle1.rect.colliderect(pong.rect):
        pong.dx = 1

    if paddle2.rect.colliderect(pong.rect):
        pong.dx = -1


    # Runs redraw function above
    redraw()

pygame.quit()