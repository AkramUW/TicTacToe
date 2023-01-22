## Tuq Junior Developer Application
## Akram Elsaidy (2B Mathematics) - TicTacToe in Python 
#import modules
import pygame
from pygame.locals import *

## Initialize PyGame
pygame.init()

#Screen Constants
screen_width = 300
screen_height = 300
line_width = 6

green = (0, 255, 0)
red = (255, 0, 0)
yellow = (255,255,0)
bg = (28,60,59)
orange = (222,183,65)

peace_img = pygame.image.load('peace.png')
muscle_img = pygame.image.load('Muscle.png')
peace = pygame.transform.scale(peace_img, (50,50))
muscle = pygame.transform.scale(muscle_img, (50,50))

font = pygame.font.SysFont(None,40)

# Restart rectangle
again_rect = Rect(screen_width // 2 - 80, screen_height // 2 + 10, 160, 40)

# Variables
markers = []
CLICKED = False
pos = []
player = 1
winner = 0
game_over = False

screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption('Akram\'s TicTacToe')

## draw_grid: draws a 3x3 grid on the screen displayed
## draw_grid: None -> None
## Effects: Draws lines on the screen representing the game board
def draw_grid():
	# Specifying RGB colors to match resume
	bg =  (28,60,59)
	grid = (222,183,65)
	
	screen.fill(bg)
	
	# Drawing lines
	for x in range(1,3):
		pygame.draw.line(screen, grid, (0 , x * 100), 
				 (screen_width, x * 100), line_width)
		pygame.draw.line(screen, grid, (x * 100,0), 
				 (x * 100, screen_height), line_width)
		

## init_markers: initializes all the entries in the 3x3 grid markers to 0
## init_markers: listof[list] -> None
## Effects: Mutates markers
def init_markers(list):
	for x in range(3):
		row = [0] * 3
		markers.append(row)
		
init_markers(markers)
	
## draw_markers: Draws an Peace or Muscle emoji on the game board, depending on player
## Effects: Outputs images onto the screen
def draw_markers():
	x_pos = 0
	for x in markers:
		y_pos = 0
		for y in x:
			if y == 1:
				screen.blit(peace, (x_pos * 100 + 25, y_pos * 100 + 25 ))
			if y == -1:
				screen.blit(muscle, (x_pos * 100 + 25 , y_pos * 100 + 25 ))
			y_pos += 1
		x_pos += 1
	
## check_winner: Checks if there's a winner on the game board after each move
## Effects: Mutates variables winner & game_over
def check_winner():
	global winner
	global game_over
	
	y_pos = 0 
	for x in markers:
		#Checking columns
		if sum(x) == 3:
			winner = 1
			game_over = True
		elif sum(x) == -3:
			winner = 2
			game_over = True
		#Checking rows	
		if markers[0][y_pos] + markers[1][y_pos] + markers[2][y_pos] == 3:
			winner = 1
			game_over = True
		elif markers[0][y_pos] + markers[1][y_pos] + markers[2][y_pos] == -3:
			winner = 2 
			game_over = True
		y_pos += 1
		
	# Checking diagonals 
	if markers[0][0] + markers[1][1] + markers[2][2] == 3 \
	   or markers[2][0] + markers[1][1] + markers[0][2] == 3:
		winner = 1
		game_over = True
	if markers[0][0] + markers[1][1] + markers[2][2] == -3 \
	   or markers[2][0] + markers[1][1] + markers[0][2] == -3:
		winner = 2
		game_over = True
	# Checking tie 
	full_board = False
	for row in markers:
		if 0 in row:
			full_board = False
			break
		else:
			full_board = True
	if full_board == True:
		game_over = True
			
		
		

## draw_winner: Displays winner of the game on the screen and asks the user 
##		if they'd like to restart
## draw_winner: Int -> None
## Effects: Outputs image on screen
def draw_winner(winner):
	win_text = f" Player{winner} wins! "
	win_img = font.render(win_text, True, orange)
	pygame.draw.rect(screen, bg, (screen_width // 2 - 100, 
					 screen_height // 2 - 60, 200,50))
	
	screen.blit(win_img, (screen_width // 2 - 100, screen_height // 2 - 50))
	again_text = 'Restart?'
	again_img = font.render(again_text, True, orange)
	pygame.draw.rect(screen, bg, again_rect)
	screen.blit(again_img, (screen_width // 2 - 50, screen_height // 2 + 15))

## draw_tie: Check if the game is a tie, and asks user if they'd like to restart
## draw_tie: Int -> None
## Effects: Outputs text onto screen
def draw_tie(winner):
	tie_text = " Nobody won! "
	tie_img = font.render(tie_text, True, orange)
	pygame.draw.rect(screen, bg, (screen_width // 2 - 100, 
							 screen_height // 2 - 60, 200,50))
			
	screen.blit(tie_img, (screen_width // 2 - 100, screen_height // 2 - 50))
	again_text = 'Restart?'
	again_img = font.render(again_text, True, orange)
	pygame.draw.rect(screen, bg, again_rect)
	screen.blit(again_img, (screen_width // 2 - 50, screen_height // 2 + 15))

	
run = True

while run:
	
	draw_grid()
	draw_markers()
	
	# Event Handlers
	for event in pygame.event.get():
		# Exit
		if event.type == pygame.QUIT:
			run = False
		# Mouse Clicks
		if game_over == 0:
			if event.type == pygame.MOUSEBUTTONDOWN and CLICKED == False:
				CLICKED = True
			if event.type == pygame.MOUSEBUTTONUP and CLICKED == True :
				CLICKED = False
				pos = pygame.mouse.get_pos()
				cell_x = pos[0]
				cell_y = pos[1]
				if markers[cell_x // 100][cell_y // 100] == 0:
					markers[cell_x // 100][cell_y // 100] = player
					player *= -1
					check_winner()
		
	if game_over == True:
		if winner == 0:
			draw_tie(winner)
		else:
			draw_winner(winner)
		# check for mouseclick to check if user has restarted
		if event.type == pygame.MOUSEBUTTONDOWN and CLICKED == False:
			CLICKED = True
		if event.type == pygame.MOUSEBUTTONUP and CLICKED == True :
			CLICKED= False
			pos = pygame.mouse.get_pos()
			if again_rect.collidepoint(pos):
				#reset variables
				markers = []
				init_markers(markers)
				pos = []
				player = 1
				winner = 0
				game_over = False				
		
	

	pygame.display.update()

pygame.quit()

