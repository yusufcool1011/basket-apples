import pygame
import random
screen_width = 1000
screen_height = 1000
pygame.init()
screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("Basket Apples")
clock = pygame.time.Clock()
bg = (144, 252, 196)
apple = pygame.image.load("images/apple.png").convert_alpha()
apple = pygame.transform.scale(apple, (50, 50))
apple_speed = 6
golden_apple = pygame.image.load("images/golden-apple.png").convert_alpha()
golden_apple = pygame.transform.scale(golden_apple, (50, 50))
golden_apple_speed = 6
score = 0
pygame.freetype.Font
pygame.font.init()
font = pygame.font.Font("RobotoSlab-Regular.ttf", 26)
apple_rect = apple.get_rect()
apple_rect.center = (random.randint(50, 950), 0)
colliding_enemies = pygame.sprite.spritecollide
basket = pygame.image.load("images/basket.png").convert_alpha()
basket = pygame.transform.scale(basket, (100, 100))
basket_rect = basket.get_rect()
basket_rect.y = 900
basket_rect.x = 500
basket_x = basket_rect.x
apple_x = 0
apple_y = 0
golden_apple_x = 0
golden_apple_y = 0
golden_apple_rect = golden_apple.get_rect()
golden_apple_active = False
fireball = pygame.image.load("images/fireball.png").convert_alpha()
fireball = pygame.transform.scale(fireball, (50, 50))
fireball_rect = fireball.get_rect()
fireball_rect.center = (random.randint(50, 950), 0)
fireball_x = 0
fireball_y = 0
fireball_speed = 8
lives = 3
heart = pygame.image.load("images/heart.png").convert_alpha()
heart = pygame.transform.scale(heart, (30, 30))
def draw_heart(surface, lives):
    for i in range(lives):
        surface.blit(heart, (10 + i*35, 10))
golden_apple_event = pygame.USEREVENT + 1
pygame.time.set_timer(golden_apple_event, 10000)


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

class Golden_Apple:
    def __init__(self, x, y):

        self.apple_rect = golden_apple.get_rect()
        self.apple_rect.x = x
        self.apple_rect.y = y

    def update_apple(self):
        self.apple_rect.y += apple_speed

        if self.apple_rect.y >= 1100:
            self.apple_rect.y = random.randint(0, 300)
            self.apple_rect.x = random.randint(50, 950)
        
            
apples = [Golden_Apple(random.randint(50, 950), random.randint(0, 300)), Golden_Apple(random.randint(50, 950), random.randint(0, 300))]


class Fireball:
    def __init__(self, x, y):

        self.fireball_rect = fireball.get_rect()
        self.fireball_rect.x = x
        self.fireball_rect.y = y

    def update_fireball(self):
        self.fireball_rect.y += fireball_speed

        if self.fireball_rect.y >= 1100:
            self.fireball_rect.y = random.randint(0, 300)
            self.fireball_rect.x = random.randint(50, 950)
        
            
fireballs = [Fireball(random.randint(50, 950), random.randint(0, 300)), Fireball(random.randint(50, 950), random.randint(0, 300))]

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
        
        if event.type == golden_apple_event:
            golden_apple_rect.x = random.randint(50, 950)
            golden_apple_rect.y = 0
            golden_apple_active = True
        
    # print("Cube Coordinates", cube_x, cube_y)
    keys = pygame.key.get_pressed()

    if basket_rect.x > 1000:
        basket_rect.x = 999

    if basket_rect.x < 0:
        basket_rect.x = 1


    if keys[pygame.K_LEFT]:
        #cube_x -= cube_speed
        basket_rect.x -= cube_speed

    if keys[pygame.K_RIGHT]:
            #cube_x += cube_speed
        basket_rect.x += cube_speed

    for event in pygame.event.get():
        if  event.type == golden_apple_event:
            golden_apple.x = random.randint(50, 950)
            golden_apple.y = 0
        
    #cube_rect = pygame.Rect(cube_x, cube_y, cube_width, cube_height)
    
    
    #pygame.draw.rect(screen, )
    #screen.blit(basket, (500, 900))

    # if apple.
    # apple_rect.y += apple_speed
    # if apple_rect.y >= 1100:
    #     apple_rect.y = 0
    #     apple_rect.x = random.randint(50, 950)

    screen.fill(bg)
    #pygame.draw.rect(screen, cube_color, (cube_x, cube_y, cube_width, cube_height))
    #pygame.draw.rect(screen, cube_color, cube_rect)
    screen.blit(basket, (basket_rect.x, 900))
    score_text = font.render(f"Score: {score}", True, (0, 0, 0))    
    for applec in apples:
        applec.update_apple()
        screen.blit(apple, (applec.apple_rect.x, applec.apple_rect.y))
        
        if applec.apple_rect.colliderect(basket_rect):
            time_lasthit = pygame.time.get_ticks()
            score += 1
            print(score)
            applec.apple_rect.y = random.randint(0, 300)
            applec.apple_rect.x = random.randint(50, 950)
        screen.blit(score_text, (850, 50))



    for fireballc in fireballs:
        fireballc.update_fireball()
        screen.blit(fireball, (fireballc.fireball_rect.x, fireballc.fireball_rect.y))

        
        if fireballc.fireball_rect.colliderect(basket_rect):
            time_lasthit = pygame.time.get_ticks()
            fireballc.fireball_rect.y = random.randint(0, 300)
            fireballc.fireball_rect.x = random.randint(50, 950)
            lives -= 1
            if lives == -1:
                pygame.quit()



    if golden_apple_active:
        golden_apple_rect.y += golden_apple_speed
        screen.blit(golden_apple, golden_apple_rect)

        if golden_apple_rect.colliderect(basket_rect):
            score += 10
            golden_apple_active = False

        if golden_apple_rect.y > 1100:
            golden_apple_active = False

    current_time = pygame.time.get_ticks()
    draw_heart(screen, lives)

    # screen.blit(apple, apple_rect)
    # Fill screen with blue
    pygame.display.flip()
    clock.tick(60)
    framecounter += 1

pygame.quit()
