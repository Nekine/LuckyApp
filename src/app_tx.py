import pygame
from unidecode import unidecode
from random import randint
from datetime import datetime

class Box_money:
	def __init__(self, text, position):
		self.text = text
		self.position = position
		
	def is_mouse_on_text(self):
		mouse_x, mouse_y = pygame.mouse.get_pos()
		if (mouse_x > self.position[0] and mouse_x < self.position[0]+self.text_box[2]) and (mouse_y > self.position[1] and mouse_y < self.position[1]+self.text_box[3]):
			return True
		else:
			return False
		
	def draw(self):
		font = pygame.font.SysFont('sans', 20)
		text = font.render(self.text, True, (255, 187, 51))
		self.text_box = text.get_rect()
		pygame.draw.rect(screen,(26, 0, 0),(self.position[0],self.position[1],self.text_box[2],self.text_box[3]))
		screen.blit(text, self.position)
		
def list_box():
	font = pygame.font.SysFont('sans', 20)
	list_box = []
	list_money = ["10.000", "20.000", "50.000", "100.000", "500.000", "1.000.000", "All in"]
	sum = 0
	for i in range(len(list_money)):
		text = font.render(list_money[i-1], True, (255, 187, 51))
		text_box = text.get_rect()
		if i == 0:
			sum += 85
		else: sum += text_box[2]+10
		money = Box_money(list_money[i], (sum, 350))
		list_box.append(money)
	return list_box

def list_xuc_xac(x, y, diem):
	list_link = ["Image\\1.jpg", "Image\\2.jpg", "Image\\3.jpg", "Image\\4.jpg", "Image\\5.jpg", "Image\\6.jpg"]
	img = pygame.image.load(list_link[diem-1])
	img = pygame.transform.scale(img, (40, 40))	
	screen.blit(img, (x, y))

def list_audio(x):
	list_link = ["Audio\\pew_pew.mp3", "Audio\\money.mp3", "Audio\\uwu.mp3", "Audio\\thua_2.mp3", "Audio\\xuc_xac.mp3", "Audio\\thua_1.mp3"]
	audio = pygame.mixer.Sound(list_link[x])
	audio.play()

def is_mouse_on_img(x, y, width, height):
	mouse_x, mouse_y = pygame.mouse.get_pos()
	if (mouse_x > x and mouse_x < x+width) and (mouse_y > y and mouse_y < y+height):
		return True
	else:
		return False
	
def di_chyen_chuot(x, y, mouse_x, mouse_y):
	position = []
	height = mouse_y - y - 65
	width = mouse_x - x - 60
	x += width
	y += height
	position.append(x)
	position.append(y)
	return position

def draw_2():
	x = [260, 315, 290]
	y = [95, 95, 145]
	for i in range(3):
		list_xuc_xac(x[i], y[i], diem[i])

def sum_money_select(input, money, money_player):
	if input == 1 and money_player >= 10000:
		money = 10000
	elif input == 2 and money_player >= 20000:
		money = 20000
	elif input == 3 and money_player >= 50000:
		money = 50000
	elif input == 4 and money_player >= 100000:
		money = 100000
	elif input == 5 and money_player >= 500000:
		money = 500000
	elif input == 6 and money_player >= 1000000:
		money = 1000000
	elif input == 7:
		money = money_player
	return money

def dat_cuoc(select, money):
	font = pygame.font.SysFont('sans', 20)
	text = font.render(str("{:.0f}".format(money)), True, (255, 187, 51))
	text_box = text.get_rect()
	if select == 1:
		pygame.draw.rect(screen, (26, 0, 0), (126-text_box[2]/2, 260, text_box[2], text_box[3]))
		screen.blit(text, (126-text_box[2]/2, 260))
	elif select == 2:
		pygame.draw.rect(screen, (26, 0, 0), (482-text_box[2]/2, 260, text_box[2], text_box[3]))
		screen.blit(text, (482-text_box[2]/2, 260))
	if select == 3:
		pygame.draw.rect(screen, (26, 0, 0), (126-text_box[2]/2, 260, text_box[2], text_box[3]))
		screen.blit(text, (126-text_box[2]/2, 260))
	elif select == 4:
		pygame.draw.rect(screen, (26, 0, 0), (482-text_box[2]/2, 260, text_box[2], text_box[3]))
		screen.blit(text, (482-text_box[2]/2, 260))

def check_time(time, img_2, x, y):
	font_time = pygame.font.SysFont('sans', 35)
	text_time = font_time.render(str(60-time), True, (255, 187, 51))
	time_box = text_time.get_rect()
	pygame.draw.rect(screen, (26, 0, 0), (280, 240, 60, 40))
	screen.blit(text_time, (308-time_box[2]/2, 240))

	pygame.draw.circle(screen, (0, 0, 0), (309, 135), 85)
	draw_2()
	screen.blit(img_2, (x, y))

def nhay_chu(time, event_mouse, sum, select, money, start):
	if event_mouse == 3 and 60-time > 52:
		if sum > 10 :
			font_3 = pygame.font.SysFont('sans', 100)
			tai = font_3.render("TAI", True, (255, 255, 26))
			xiu = font_3.render("XIU", True, (0, 0, 0))
			screen.blit(tai, (60, 140))
			screen.blit(xiu, (410, 140))
			if select == 3:
				if 60-time >= 55:
					list_audio(2)
				font = pygame.font.SysFont('sans', 30)
				text = font.render("+" + str("{:.0f}".format(money*1.9)), True, (255, 255, 26))
				if start >= 20:
					screen.blit(text, (80, start))
			if select == 4:
				if 60-time >= 55:
					list_audio(3)
				font = pygame.font.SysFont('sans', 30)
				text = font.render(str("{:.0f}".format(-money)), True, (0, 0, 0))
				if start >= 20:
					screen.blit(text, (430, start))
		elif sum <= 10:
			font_3 = pygame.font.SysFont('sans', 100)
			tai = font_3.render("TAI", True, (0, 0, 0))
			xiu = font_3.render("XIU", True, (255, 255, 26))
			screen.blit(tai, (60, 140))
			screen.blit(xiu, (410, 140))
			if select == 4:
				if 60-time >= 55:
					list_audio(2)
				font = pygame.font.SysFont('sans', 30)
				text = font.render("+" + str("{:.0f}".format(money*1.9)), True, (255, 255, 26))
				if start >= 20:
					screen.blit(text, (430, start))
			if select == 3:
				if 60-time >= 55:
					list_audio(3)
				font = pygame.font.SysFont('sans', 30)
				text = font.render(str("{:.0f}".format(-money)), True, (0, 0, 0))
				if start >= 20:
					screen.blit(text, (80, start))
	else:
		font_3 = pygame.font.SysFont('sans', 100)
		tai = font_3.render("TAI", True, (0,0,0))
		xiu = font_3.render("XIU", True, (0,0,0))
		screen.blit(tai, (60, 140))
		screen.blit(xiu, (410, 140))

pygame.init()
screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption('App lucky')
running = True
BLACK = (0,0,0)

clock = pygame.time.Clock()

font = pygame.font.SysFont('sans', 35)
text = font.render("CUOC", True, (255, 187, 51))
text_box = text.get_rect()
box_money = list_box()
img = pygame.image.load('Image\eyes.jpg')
img = pygame.transform.scale(img, (100, 100))
img_2 = pygame.image.load('Image\dia.png')
img_2 = pygame.transform.scale(img_2, (160, 160))

down_mouse = 1
rec_x = 230
rec_y = 400
sum_money = 0
money_player = 500000
tmp = 0
font_2 = pygame.font.SysFont('sans', 45)
text_2 = font_2.render("$" + str(money_player), True, (0,0,0))
text_box_2 = text_2.get_rect()
center = 300 - text_box_2[2]/2
select = 0
input = None
diem = [0, 0, 0]
sum = 0
start = 130
while running:		
	clock.tick(60)
	screen.fill((204, 153, 102))
	time = datetime.now().second
	mouse = pygame.mouse.get_pos()
	mouse_x = mouse[0]
	mouse_y = mouse[1]

	if not select == 0:
		dat_cuoc(select, tmp)
	if 10 < 60-time <= 12:
		diem[0] = randint(1, 6)
		diem[1] = randint(1, 6)
		diem[2] = randint(1, 6)
		sum = diem[0]+diem[1]+diem[2]
	if 60-time == 12:
		list_audio(4)

	if select < 3:
		pygame.draw.rect(screen, (55, 39, 21), (83, 289, text_box[2], text_box[3]))
		screen.blit(text, (83, 289))
		pygame.draw.rect(screen, (55, 39, 21), (439, 289, text_box[2], text_box[3]))
		screen.blit(text, (439, 289))

	font_2 = pygame.font.SysFont('sans', 45)
	text_2 = font_2.render("$" + str("{:.0f}".format(money_player)), True, (0,0,0))
	screen.blit(text_2, (center, 0))
	pygame.draw.circle(screen, (0, 0, 0), (309, 135), 85)
	check_time(time, img_2, rec_x, rec_y)
	nhay_chu(time, down_mouse, sum, select, tmp, start)
	for i in range(len(box_money)):
		box_money[i].draw()

	if 60-time == 55:
		down_mouse = 3
	if down_mouse == 2:
		position = di_chyen_chuot(rec_x, rec_y, mouse_x, mouse_y)
		rec_x = position[0]
		rec_y = position[1]
		screen.blit(img_2, (rec_x, rec_y))
	elif down_mouse == 3 and 60-time > 10:
		rec_x = 230
		rec_y = 400
		screen.blit(img_2, (rec_x, rec_y))
	elif 60-time <= 10:
		down_mouse = 1
		rec_x = 228
		rec_y = 58
	if down_mouse == 3 and 60-time > 52:
		start -= 1
	if 60-time == 52:
		start = 130


	if down_mouse == 3 and select == 3 and 60-time == 52:
		if sum > 10:
			money_player += tmp*1.9
			select = 0
			tmp = 0
	elif down_mouse == 3 and select == 4 and 60-time == 52:
		if sum <= 10:
			money_player += tmp*1.9
			select = 0
			tmp = 0
	elif 60-time == 52:
		tmp = 0 
		select = 0

	if 60-time == 52 and money_player == 0:
		running = False

	screen.blit(img, (0, 0))
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
		if event.type == pygame.MOUSEBUTTONDOWN and is_mouse_on_img(rec_x, rec_y, 160, 160) and 60-time > 10:
			down_mouse = 2
		if event.type == pygame.MOUSEBUTTONUP:
			down_mouse = 3
		if select == 1 and event.type == pygame.MOUSEBUTTONDOWN and is_mouse_on_img(83, 289, text_box[2], text_box[3]) and 10 < 60-time < 52:
			select = 3
			money_player -= tmp
			sum_money = 0
			list_audio(1)
		elif select	== 2 and event.type == pygame.MOUSEBUTTONDOWN and is_mouse_on_img(439, 289, text_box[2], text_box[3]) and 10 < 60-time < 52: 
			select = 4
			money_player -= tmp
			sum_money = 0
			list_audio(1)
		elif event.type == pygame.MOUSEBUTTONDOWN and is_mouse_on_img(83, 289, text_box[2], text_box[3]) and 10 < 60-time < 52:
			select = 1
			list_audio(0)
		elif event.type == pygame.MOUSEBUTTONDOWN and is_mouse_on_img(439, 289, text_box[2], text_box[3]) and 10 < 60-time < 52: 
			select = 2
			list_audio(0)
		if not select == 0:
			for i in range(len(box_money)):
				if event.type == pygame.MOUSEBUTTONDOWN and box_money[i].is_mouse_on_text() and 10 < 60-time < 52:
					input = i+1
					if i == len(box_money)-1:
						sum_money = 0
						sum_money = money_player-tmp
						if not sum_money == 0:
							list_audio(0)
							tmp += sum_money
						else: list_audio(5)
					else:
						sum_money = 0
						sum_money = sum_money_select(input, sum_money, money_player-tmp)
						if not sum_money == 0:
							list_audio(0)
							tmp += sum_money
						else: list_audio(5)
	
	pygame.display.flip()

pygame.quit()