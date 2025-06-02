# importing required library
import pygame
import random
import math

# constants
screen_width = 1200
screen_height = 300
background_color = (255, 255, 255)

# activate pygame
pygame.init()

# create screen
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('cats')

# load the image
original_img = pygame.image.load("cat.png").convert_alpha()

# helper function to tint image
def tint_image(img, color):
    img_copy = img.copy()
    img_copy.fill(color + (0,), special_flags=pygame.BLEND_RGBA_ADD)
    return img_copy

# define animated cat class
class AnimatedCat:
    def __init__(self):
        # random scale
        scale = random.uniform(0.5, 1.0)
        self.image = pygame.transform.scale(original_img, (int(100 * scale), int(100 * scale)))

        # random position
        self.x = random.randint(0, screen_width)
        self.y = random.randint(0, screen_height - 100)

        # random speed
        self.speed = random.randint(2, 10)

        # optional circular movement
        self.circular = random.choice([True, False])
        self.center_x = self.x
        self.center_y = self.y
        self.angle = 0
        self.radius = random.randint(20, 60)
        self.rotation_speed = random.uniform(0.02, 0.1)

    def move(self):
        if self.circular:
            self.angle += self.rotation_speed
            self.x = self.center_x + math.cos(self.angle) * self.radius
            self.y = self.center_y + math.sin(self.angle) * self.radius
        else:
            self.x += self.speed
            if self.x > screen_width:
                self.x = -100  # reset to left side

    def draw(self, surface):
        surface.blit(self.image, (int(self.x), int(self.y)))

# create list of cat objects
cats = [AnimatedCat() for _ in range(5)]

# init the clock
clock = pygame.time.Clock()

# main loop
running = True
while running:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill background
    screen.fill(background_color)

    # move and draw each cat
    for cat in cats:
        cat.move()
        cat.draw(screen)

    # update display
    pygame.display.flip()

pygame.quit()
