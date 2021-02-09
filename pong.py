from uagame import Window
from time import sleep
import pygame
from pygame.locals import *


def main():
    #window attributes
    window_width = 500
    window_height = 400    
    window = Window('Pong', window_width, window_height)
    window.set_auto_update(False)
    
    
    game = Game(window)
    game.play()
    window.close()
    
#User defined Classes

class Game:
    # an obj in this class represents a complete game
    def __init__(self, window):
        #Initialize a game.
        self.window = window
        self.bg_color = pygame.Color('black') #Background color
        self.close_clicked = False
        self.ball = Ball(5, 'white', [10, 4], self.window)
        self.continue_game = True
        self.left_paddle = pygame.Rect(80, 180, 10, 45)
        self.right_paddle = pygame.Rect(420, 180, 10, 45)
        pygame.key.set_repeat(20, 20)
        
    
    def play(self): #CALLS THE NEXT THREE METHODS
        while not self.close_clicked:
            self.handle_events()
            self.draw_frame()
            if self.continue_game:
                self.ball.move()
                self.ball.bounce()
                self.paddle_bounce()
                self.decide_continue() 
            sleep(0.03)
    
    def handle_events(self):
        event = pygame.event.poll()
        if event.type == QUIT:
            self.close_clicked = True
        elif event.type == KEYDOWN:
            self.key_DOWN_press()
            
    def key_DOWN_press(self):
        #uses keys k and p for right paddle
        #uses keys q and a for left paddle 
        list_of_keys = pygame.key.get_pressed()
        if list_of_keys[K_q] == True:
            self.left_paddle.top = self.left_paddle.top-10
            self.left_paddle.bottom = self.left_paddle.bottom-10
            if self.left_paddle.top < 0:
                self.left_paddle.top = 0 
        elif list_of_keys[K_a] == True:
            self.left_paddle.top = self.left_paddle.top+10
            self.left_paddle.bottom = self.left_paddle.bottom+10
            if self.left_paddle.bottom > 400:
                self.left_paddle.bottom = 400           
        
        elif list_of_keys[K_p] == True:
            self.right_paddle.top = self.right_paddle.top-10
            self.right_paddle.bottom = self.right_paddle.bottom-10
            if self.right_paddle.top < 0:
                self.right_paddle.top = 0            
        elif list_of_keys[K_l] == True:
            self.right_paddle.top = self.right_paddle.top+10
            self.right_paddle.bottom = self.right_paddle.bottom+10
            if self.right_paddle.bottom > 400:
                self.right_paddle.bottom = 400            
    
    def draw_frame(self):
        self.window.clear()
        self.ball.draw()
        pygame.draw.rect(self.window.get_surface(),pygame.Color("white"),self.left_paddle)
        pygame.draw.rect(self.window.get_surface(),pygame.Color("white"),self.right_paddle)
        self.ball.draw_score_boards()
        self.window.update()
        
    def decide_continue(self):
       
        
        if self.ball.score_right == 11 or self.ball.score_left == 11:
            self.continue_game = False

    def paddle_bounce(self):
        if (self.left_paddle.collidepoint(self.ball.position[0], self.ball.position[1]) or self.right_paddle.collidepoint(self.ball.position[0], self.ball.position[1])):
            self.ball.velocity[0] = -self.ball.velocity[0]
                        
        if (self.ball.position[1] >= self.window.get_height() - self.ball.size or self.ball.position[1] <= self.ball.size):
            self.ball.velocity[1] = -self.ball.velocity[1]        
    
        
        
class Ball:
    
    def __init__(self, size, color, velocity, window):
        self.size = size
        self.color = color
        self.velocity = velocity
        self.position = [250, 200]
        self.window = window
        self.score_left = 0
        self.score_right = 0
        
    
    def move(self):
        
        self.position[0] = self.position[0] + self.velocity[0]
        self.position[1] = self.position[1] + self.velocity[1]       
       
        
    def bounce(self):
        #hits right window
        if (self.position[0] >= self.window.get_width() - self.size):
            self.velocity[0] = -self.velocity[0]
            self.score_left = self.score_left +1
        #hits left window
        if self.position[0] <= self.size:
            self.velocity[0] = -self.velocity[0]
            self.score_right = self.score_right +1
        #hits 
       
        
  
    def draw(self):
        pygame.draw.circle(self.window.get_surface(), pygame.Color(self.color), self.position, self.size)
       
    
    def draw_score_boards(self): 
        self.window.set_font_size(60)

        score_left = self.window.draw_string(
        str(int(self.score_left)),
        0, 0)
        score_right = self.window.draw_string(
        str(int(self.score_right)),450,0)
              
main()
