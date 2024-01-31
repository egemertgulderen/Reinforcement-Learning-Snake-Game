import pygame
import sys

from food import Food
from snake import Snake


class Game:
    def __init__(self, width=800, height=600):
        pygame.init()
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Reinforcement learning Snake Game")
        self.clock = pygame.time.Clock()

        self.font =  pygame.font.Font(None,36)

        self.score_point = 0
        self.game_is_running = True
        self.new_game()

    def new_game(self):
        self.score_point = 0
        self.game_is_running = True
        self.snake = Snake(self)
        self.food = Food(self)
        self.run()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.snake.change_direction((-1, 0))
                elif event.key == pygame.K_RIGHT:
                    self.snake.change_direction((1, 0))
                elif event.key == pygame.K_UP:
                    self.snake.change_direction((0, -1))
                elif event.key == pygame.K_DOWN:
                    self.snake.change_direction((0, 1))
                
            

    def score(self):
        if self.food.get_eaten():
            self.score_point +=10

    def draw_score(self):
        # Render the score text
        score_text = self.font.render("Score: " + str(self.score_point), True, (255, 255, 255))
        self.screen.blit(score_text, (10, 10))  # Position the text on the screen


    def update(self):
        self.food.update(self.snake.get_head())
        self.score()
        self.snake.update(self.food.get_eaten())


    def render(self):
        self.screen.fill((0, 0, 0))  # Fill screen with black color
        self.snake.draw()
        self.food.draw()
        self.draw_score()
        pygame.display.flip()  # Update the display

    def game_over(self):
        # Clear the screen
        self.screen.fill((0, 0, 0))

        # Render game over message
        game_over_text = self.font.render("Game Over", True, (255, 255, 255))
        self.screen.blit(game_over_text, ((self.width - game_over_text.get_width()) // 2, self.height // 2 - 50))

        # Render final score
        final_score_text = self.font.render("Final Score: " + str(self.score_point), True, (255, 255, 255))
        self.screen.blit(final_score_text, ((self.width - final_score_text.get_width()) // 2, self.height // 2))

        # Update the display
        pygame.display.flip()

        # Wait for a short time before quitting
        pygame.time.wait(2000)
    
        self.new_game()

    def run(self):
        while self.game_is_running:
            self.handle_events()
            self.update()
            self.render()
            self.clock.tick(20)

        self.game_over()

        




if __name__ == "__main__":
    game = Game()
    game.new_game()
