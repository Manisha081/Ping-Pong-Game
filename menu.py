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
			if not click:
				continue
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
	while running:

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
