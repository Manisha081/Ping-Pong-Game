import sys,pygame

mainClock=pygame.time.Clock()
from pygame.locals import *
pygame.init()
pygame.display.set_caption("ping pong")
width,height=750,500
display=pygame.display.set_mode((width,height),0,32)
font=pygame.font.SysFont(None,70)
font_1=pygame.font.SysFont(None,30)

winner_font = pygame.font.SysFont('cambria', 30)

#red = (255, 0, 0)
#black = (0, 0, 0)
#blue = (0, 0, 255)
#white = (255, 255, 255)
#green = (0, 255, 0)




def draw_text(text,font,color,surface,x,y):
	textobj=font.render(text,1,color)
	textrect=textobj.get_rect()
	textrect.topleft=(x,y)
	surface.blit(textobj,textrect)

click =False
def main_menu():
	while True:
		display.fill((0,0,0))
		draw_text('MAIN MENU',font,(255,255,255),display,250,25)
		draw_text('1.Play     2.How to play    3.Quit', font_1, (255, 255, 255), display, 230, 120)

		mx,my=pygame.mouse.get_pos()

		button1=pygame.Rect(300,180,200,50)
		button2 = pygame.Rect(300, 260, 200, 50)
		button3 = pygame.Rect(300, 340, 200, 50)


		if button1.collidepoint((mx,my)):
			if click:
				game()
		if button2.collidepoint((mx,my)):
			if click:
				options()
		if button3.collidepoint((mx,my)):
			if click:
				exit()

		pygame.draw.rect(display,(255,0,0),button1)
		pygame.draw.rect(display, (255, 0, 0), button2)
		pygame.draw.rect(display, (255, 0, 0), button3)

		click=False
		for event in pygame.event.get():
			if event.type==QUIT:
				pygame.quit()
				sys.exit()
			if event.type==KEYDOWN:
				if event.key==K_ESCAPE:
					pygame.quit()
					sys.exit()
			if event.type==MOUSEBUTTONDOWN:
				if event.button==1:
					click=True
		pygame.display.update()
		mainClock.tick(60)

def game():
	running = True
	display.fill((0, 0, 0))
	#while running:

	class Paddle1(pygame.sprite.Sprite):
		def __init__(self):
			pygame.sprite.Sprite.__init__(self)
			self.image = pygame.Surface([5, 105])
			self.image.fill((255, 0, 0))
			self.rect = self.image.get_rect()
			self.points = 0

	class Paddle2(pygame.sprite.Sprite):
		def __init__(self):
			pygame.sprite.Sprite.__init__(self)

			self.image = pygame.Surface([5, 105])
			self.image.fill((255, 0, 0))
			self.rect = self.image.get_rect()
			self.points = 0

	class Ball(pygame.sprite.Sprite):
		def __init__(self):
			pygame.sprite.Sprite.__init__(self)
			self.image = pygame.Surface((16, 16))
			self.image.fill((0, 255, 0))
			self.rect = self.image.get_rect()
			self.speed = 20
			self.dx = 1
			self.dy = 1
	paddle1 = Paddle1()
	paddle1.rect.x = 45
	paddle1.rect.y = 225


	paddle2 = Paddle2()
	paddle2.rect.x = 700
	paddle2.rect.y = 225

	paddle_speed = 15

	pong = Ball()
	pong.rect.x = 375
	pong.rect.y = 250

	all_sprites = pygame.sprite.Group()
	all_sprites.add(paddle1, paddle2, pong)

	def redraw():
		# Draws black screen
		display.fill((0,0,0))

		# Title font
		font = pygame.font.SysFont('italic', 30)
		text = font.render('PING PONG', False, (255,255,255))
		text_rect = text.get_rect()
		text_rect.center = (width//2, 25)
		display.blit(text, text_rect)

		# Player 1 Score
		font = pygame.font.SysFont('italic', 30)
		p1_score = font.render('Left player:' + str(paddle1.points), False, (0, 0, 255))
		p1_rect = p1_score.get_rect()
		p1_rect.center = (130, 25)
		display.blit(p1_score, p1_rect)

		# Player 2 Score
		font = pygame.font.SysFont('italic', 30)
		p2_score = font.render('Right player:' + str(paddle2.points), False, (0, 0, 255))
		p2_rect = p2_score.get_rect()
		p2_rect.center = (630, 25)
		display.blit(p2_score, p2_rect)

		# Updates all Sprites
		all_sprites.draw(display)

		# Draws updates
		pygame.display.update()

	def draw_winner(text):
		draw_text = winner_font.render(text, False, (0, 0, 255))

		display.blit(draw_text, (width//2 - draw_text.get_width() / 2, height // 2 - draw_text.get_height() / 2))
		pygame.display.update()
		pygame.time.delay(5000)

	#run = True
	paddle1.points = 0
	paddle2.points = 0

	while running:

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
				running = False

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

	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()
		if event.type == KEYDOWN:
			if event.key == K_ESCAPE:
				running = False

	pygame.display.update()
	mainClock.tick(60)

def options():
	running = True
	display.fill((0, 0, 0))
	while running:
		draw_text('HOW TO PLAY?', font, (255, 0, 0), display, 20, 20)
		draw_text('->Use W Keyword for left-paddle to move upwards.',font_1,(0, 0, 255),display,50,130)
		draw_text('->Use S Keyword for left-paddle to move downwards.',font_1,(0, 0, 255),display,50,160)
		draw_text('->Use Up-arrow for right-paddle to move upwards.',font_1,(0, 0, 255),display,50,190)
		draw_text('->Use Down-arrow for right-paddle to move downwards.',font_1,(0, 0, 255),display,50,220)
		draw_text('WHO WINS?',font_1,(255, 0, 0),display,50,290)

		draw_text('Player who scores more than 10 points wins the game',font_1,(0, 0, 255),display,50,330)
		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				sys.exit()
			if event.type == KEYDOWN:
				if event.key == K_ESCAPE:
					running = False

		pygame.display.update()
		mainClock.tick(60)


main_menu()