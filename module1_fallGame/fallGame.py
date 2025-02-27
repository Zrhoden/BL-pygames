import pygame
import random

# initialize game - tells computer that the following code should be interpreted into the game 
pygame.init()

height = 600
width = 800
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption*("Avoid The Falling Objects!")

# Set frame rate
clock = pygame.time.Clock() # game runs on frames
FPS = 60 # Game updates 60 times per second

# Create player object
# Object - a data type that allows us to pass in unique data includind functions and other objects. 

class Player:
    def __init__(self):
        self.x = width // 2 #Start in the middle
        self.y = height - 60 #near the bottom
        self.playerWidth = 50
        self.playerHeight = 50
        self.playerSpeed = 5 # How fast the player moves

        def move(self, keys):
            if keys[pygame.K_LEFT] and self.x > 0:
                self.x -= self.playerSpeed
            if keys[pygame.K_RIGHT] and self.x < width - self.playerWidth:
                self.x += self.playerSpeed

    def draw(self):
        pygame.draw.rect(screen, (0,0,255), (self.x, self.y, self.playerWidth, self.playerHeight))