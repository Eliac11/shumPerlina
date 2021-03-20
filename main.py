import pygame
import random 
import math
import noise


pygame.init()

screen = pygame.display.set_mode((1000,1000))

clock = pygame.time.Clock()



#seed = 111
k = 0
while 1:
    
    clock.tick(1)
    
    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                k += 0.01
    
    screen.fill((0,0,0))
    #random.seed(seed)
    index = 0

    areaseed = random.randint(0,99999)
    print(areaseed)
    for x in range(0,1000,1):
        for y in range(0,1000,1):
            

            s = abs(noise.pnoise3(float(x)*0.003, float(y)*0.003, areaseed,1)) * 100

            if s > 35:
                r,g,b = 0,0,255
                n = random.randint(0,50)
                biome = "water"
            elif s > 9:
                r,g,b = 0,255,0
                n = random.randint(0,150)
                biome = "green"
            elif s > 5:
                r,g,b = 200,200,0
                n = random.randint(0,100)
                biome = "sand"
            else:
                r,g,b = 20,20,20
                n = random.randint(0,50)
                biome = "road"

            

            r = (r + n) // 2
            g = (g + n) // 2
            b = (b + n) // 2

            pygame.draw.rect(screen,(r,g,b),(x,y,10,10))


            t = noise.pnoise3(float(x)*0.005, float(y)*0.005, areaseed,1) * 100
            if t > 10 and biome == "green":
                pygame.draw.circle(screen,(0,20,0),(x,y),4)

            #else:
            #    h = abs(noise.pnoise3(float(x)/2.1, float(y)/2.1, areaseed,1)) * 100
            #    if h > 65 and biome == "green":
            #        
            #        
            #        pygame.draw.circle(screen,(0,0,0),(x,y),20)

            
            #pygame.draw.rect(screen,(s,s,s),(x,y,1,1))

            #index += 100

         
    #seed += 0.005

    pygame.display.update()

pygame.quit()
