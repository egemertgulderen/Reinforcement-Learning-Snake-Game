import pygame
import random
class Food:
    def __init__(self,game,x = 500,y = 500):
        self.game = game

        self.x= x
        self.y = y
        self.cell_size = 10

        self.box = pygame.Rect(self.x,self.y,self.cell_size,self.cell_size)
        self.eaten = False

    def update(self,snake_head):
        self.eaten = False
        snake_rect = pygame.Rect(snake_head[0],snake_head[1],self.cell_size,self.cell_size)
        if self.box.colliderect(snake_rect):
            self.new_spawn_point()
            self.eaten = True

    def get_eaten(self):
         return self.eaten
    def new_spawn_point(self):
            self.x = random.randrange(10,790,10)
            self.y = random.randrange(10,590,10)
            self.box = pygame.Rect(self.x,self.y,self.cell_size,self.cell_size)

    def draw(self):
        pygame.draw.rect(self.game.screen,'red',self.box)
        