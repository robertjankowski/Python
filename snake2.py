import pygame,sys,random,time

check_error = pygame.init()
if check_error[1] > 0:
	print("(!) Had {0} initailizing errors,exiting".format(check_error))
	sys.exit(-1)
else:
	print("Yeah, it's working !")

# Screen
tab = [720,460]
playSurface = pygame.display.set_mode(tab)
pygame.display.set_caption('Snake game!')

# Colors pygame.Color(r,g,b)
red = pygame.Color(255,0,0) # gameover 
green = pygame.Color(0,255,0) #snake
black = pygame.Color(0,0,0) #score
white = pygame.Color(50,50,0) #backgound
brown = pygame.Color(0,0,0) #food

# FPS controller
fps = pygame.time.Clock()

# Variables
snakePos = [100,50] 
snakeBody = [[100,50],[90,50],[80,50]]

foodPos = [random.randrange(1,72)*10,random.randrange(1,46)*10]
foodSpawn = True

direction = 'RIGHT'
changeto = direction
score = 0
speed = 18
# Game over
def gameOver():
	myFont = pygame.font.SysFont('monaco',100)
	GOsurf = myFont.render('Game over!',True,red)
	GOrect = GOsurf.get_rect()
	GOrect.midtop = (360,15)
	playSurface.blit(GOsurf,GOrect)
	showScore(2)
	pygame.display.flip()
	time.sleep(4)
	pygame.quit()
	sys.exit()

def showScore(choice = 1):
	sFont = pygame.font.SysFont('monaco',25)
	Ssurf = sFont.render('Score: {0}'.format(score) ,True,black)
	Srect = Ssurf.get_rect()
	if choice == 1:
		Srect.midtop = (50,10)
	else:
		Srect.midtop = (360,120)
	playSurface.blit(Ssurf,Srect)
	# pygame.display.flip()

# Main Logic
while 1:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()
		elif event.type == pygame.KEYDOWN:
			if event.key == pygame.K_RIGHT or event.key == ord('d'):
				changeto = 'RIGHT'
			if event.key == pygame.K_LEFT or event.key == ord('a'):
				changeto = 'LEFT'
			if event.key == pygame.K_UP or event.key == ord('w'):
				changeto = 'UP'
			if event.key == pygame.K_DOWN or event.key == ord('s'):
				changeto = 'DOWN'
			if event.key == pygame.K_ESCAPE:
				pygame.event.post(pygame.event.Event(pygame.QUIT))

	if changeto == 'RIGHT' and not direction == 'LEFT':
		direction = 'RIGHT'
	if changeto == 'LEFT' and not direction == 'RIGHT':
		direction = 'LEFT'		
	if changeto == 'UP' and not direction == 'DOWN':
		direction = 'UP'
	if changeto == 'DOWN' and not direction == 'UP':
		direction = 'DOWN'

	if direction == 'RIGHT':
		snakePos[0] += 10
	if direction == 'LEFT':
		snakePos[0] -= 10
	if direction == 'UP':
		snakePos[1] -= 10
	if direction == 'DOWN':
		snakePos[1] += 10
	# Snake body
	snakeBody.insert(0,list(snakePos))
	if snakePos[0] == foodPos[0] and snakePos[1] == foodPos[1]:
		foodSpawn = False
		score += 10
		speed += 1
	else:
		snakeBody.pop()

	if foodSpawn == False:
		foodPos = [random.randrange(1,72)*10,random.randrange(1,46)*10]
	foodSpawn = True

	playSurface.fill(white)
	for pos in snakeBody:
		pygame.draw.rect(playSurface,green,pygame.Rect(pos[0],pos[1],10,10))

	pygame.draw.rect(playSurface,brown,pygame.Rect(foodPos[0],foodPos[1],10,10))

	if snakePos[0] > 710 or snakePos[0] < 0:
		gameOver()
	if snakePos[1] > 450 or snakePos[1] < 0:
		gameOver()

	for block in snakeBody[1:]:
		if snakePos[0] == block[0] and snakePos[1] == block[1]:
			gameOver()

	showScore()
	pygame.display.flip()
	fps.tick(speed)


