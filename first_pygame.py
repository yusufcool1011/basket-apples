import pygame
import random
screen_width = 1000
screen_height = 1000
pygame.init()
screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("Basket Apples")
clock = pygame.time.Clock()
blue = (0, 0, 255)
apple = pygame.image.load("apple.png").convert_alpha()
apple = pygame.transform.scale(apple, (50, 50))
apple_speed = 6
score = 0
pygame.freetype.Font
pygame.font.init()
my_font = pygame.font.Font("Roboto_Slab/static/RobotoSlab-Regular.ttf", 26)
apple_rect = apple.get_rect()
apple_rect.center = (random.randint(50, 950), 0)
colliding_enemies = pygame.sprite.spritecollide
basket = pygame.image.load("basket.png").convert_alpha()
basket = pygame.transform.scale(basket, (70, 70))
basket_rect = basket.get_rect()
basket_rect.y = 900
basket_rect.x = 500
basket_x = basket_rect.x
apple_x = 0
apple_y = 0
time_lasthit = 0



class Apple:
    def __init__(self, x, y):

        self.apple_rect = apple.get_rect()
        self.apple_rect.x = x
        self.apple_rect.y = y

    def update_apple(self):
        self.apple_rect.y += apple_speed

        if self.apple_rect.y >= 1100:
            self.apple_rect.y = random.randint(0, 300)
            self.apple_rect.x = random.randint(50, 950)
        
            
apples = [Apple(random.randint(50, 950), random.randint(0, 300)), Apple(random.randint(50, 950), random.randint(0, 300))]

cube_width = 50
cube_height = 50
cube_x = 500
cube_y = 900
cube_color = (255, 0, 0)
cube_speed = 5
cooldown = 1000
running = True
framecounter = 0
while running:
    
    # Only for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
 
    #for ap in apples:
        #print(ap.x, ap.y)
        
        
    # print("Cube Coordinates", cube_x, cube_y)
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        #cube_x -= cube_speed
        basket_rect.x -= cube_speed

    if keys[pygame.K_RIGHT]:
        #cube_x += cube_speed
        basket_rect.x += cube_speed
        
    #cube_rect = pygame.Rect(cube_x, cube_y, cube_width, cube_height)
    
    
    #pygame.draw.rect(screen, )
    #screen.blit(basket, (500, 900))

    # if apple.
    # apple_rect.y += apple_speed
    # if apple_rect.y >= 1100:
    #     apple_rect.y = 0
    #     apple_rect.x = random.randint(50, 950)

    screen.fill(blue)
    #pygame.draw.rect(screen, cube_color, (cube_x, cube_y, cube_width, cube_height))
    #pygame.draw.rect(screen, cube_color, cube_rect)
    screen.blit(basket, (basket_rect.x, 900))
    
    for applec in apples:
        applec.update_apple()
        screen.blit(apple, (applec.apple_rect.x, applec.apple_rect.y))
        
        current_time = pygame.time.get_ticks()

        if applec.apple_rect.colliderect(basket_rect):
            time_lasthit = pygame.time.get_ticks()
            score += 1
            print(score)
            applec.apple_rect.y = random.randint(0, 300)
            applec.apple_rect.x = random.randint(50, 950)


    # screen.blit(apple, apple_rect)
    # Fill screen with blue
    pygame.display.flip()
    clock.tick(60)
    framecounter += 1

pygame.quit()