import pygame
class Snake:
    def __init__(self,game):
        self.game = game
        self.x = 200
        self.y = 200
        self.direction = (1, 0)  # Initial direction
        self.cell_size = 10
        self.speed = 10
        self.body = [(self.x,self.y)]


    
    def draw(self):
        for body_part in self.body:
            rect = pygame.Rect(body_part[0],body_part[1],self.cell_size,self.cell_size)
            pygame.draw.rect(self.game.screen,'blue',rect)

    def update(self,food_eaten):
        self.movement()
        self.add_body(food_eaten)


    def check_for_game_over(self,head):
                # Assuming head is a tuple (x, y) representing the position of the snake's head
            x, y = head
            if (
                x < 0 or x > self.game.width or
                y < 0 or y >self.game.height or
                head in self.body[1:]
            ):
                self.game.game_is_running = False  # Stop the game if the snake collides with boundaries or itself
                return True
            else:
                return False  # No collision


    def add_body(self,food_eaten):
        if food_eaten:
            if self.direction == (-1, 0): # Left
                self.body.append([self.body[-1][0]+self.cell_size, self.body[-1][1]])

            elif self.direction == (1, 0):# Right
                self.body.append([self.body[-1][0]-self.cell_size, self.body[-1][1]])

            elif self.direction == (0, 1) : # Down
                self.body.append([self.body[-1][0], self.body[-1][1] - self.cell_size])

            elif self.direction == (0, -1) : # Up
                 self.body.append([self.body[-1][0], self.body[-1][1] + self.cell_size])
    

        
    def get_head(self):
        return self.body[0]

    def change_direction(self, direction):
        if direction == (-1, 0) and self.direction != (1, 0):  # Prevent reversing direction
            self.direction = (-1, 0)  # Left
        elif direction == (1, 0) and self.direction != (-1, 0):
            self.direction = (1, 0)  # Right
        elif direction == (0, 1) and self.direction != (0, -1):
            self.direction = (0, 1)  # Down
        elif direction == (0, -1) and self.direction != (0, 1):
            self.direction = (0, -1)  # Up

    def movement(self):
         # Extract the head position
        head = self.body[0]

        self.check_for_game_over(head)
        # Calculate the new head position based on the current direction and speed
        new_head = (
            head[0] + self.direction[0] * self.speed,
            head[1] + self.direction[1] * self.speed
        )
        # Insert the new head position at the beginning of the body list
        self.body = [new_head] + self.body[:-1]
