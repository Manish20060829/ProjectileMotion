import pygame
import math
pygame.init()
def main():
    win = pygame.display.set_mode((1200,500))
    x = 15
    y = 485
    run = True
    g = 98
    maxheight = y
    clock = pygame.time.Clock()
    pressed = False
    enable = True
    vi1 = 0
    vx1 = 0
    vy1 = 0
    startime = 0
    time = 0
    launched = False
    font = pygame.font.SysFont('freesansbold.ttf', 15)
    while run:
        mouse = pygame.mouse.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a and pressed == False:
                    print("yo")
                    x = 15
                    y = 485
                    maxheight = y
                    pressed = False
                    enable = True
                    vi1 = 0
                    vx1 = 0
                    vy1 = 0
                    launched = False
                    startime = 0
                    time = 0
        if mouse[0] == True:
            pressed = True  
        mousecord = pygame.mouse.get_pos()
        if pressed == False:
            vx = mousecord[0] - x
            vy = y - mousecord[1]
        dt = clock.tick(200)/1000
        vi = math.sqrt((vx*vx) + (vy*vy))
        if pressed == True and enable == True and vi <= 300:
            vi1 = vi
            vx1 = vx
            vy1 = vy
            enable = False
            startime = pygame.time.get_ticks()
        if pressed == True and vi <= 300 and y <= 485 and launched == False:
            x += vx*dt
            y -= vy*dt
            vy -= g*dt
            time = pygame.time.get_ticks() - startime

        else:
            pressed = False
            y = 485
            if enable == False:
                launched = True
        if y < maxheight:
            maxheight = y
        win.fill((0,0,0))
        draw(win,x,y,vx,vi,vi1,vy1,vx1,vy,mousecord,pressed,font,enable,launched,maxheight,startime,time)
        pygame.display.update()
    pygame.quit()





def draw(win,x,y,vx,vi,vi1,vy1,vx1,vy,mousecord,pressed,font,enable,launched,maxheight,startime,time):
    circlecolour = (255,255,255)
    pygame.draw.circle(win,circlecolour,(x,y),15)
    if vi <= 300 and vx >= 0 and vy >= 0 and pressed == False:
        pygame.draw.line(win,(255,255,255),(x,y),(mousecord[0],mousecord[1]),3)
    if pressed == False and enable == True:
        vel = font.render("V intial: " + str(round(vi/10,1)), True, circlecolour)
        win.blit(vel,(5,10))
        if vx != 0:
            angle = font.render("Angle: " + str(round((math.atan(vy/vx)*180/math.pi),1)), True, circlecolour)
            win.blit(angle,(85,10))
        else:
            angle = font.render("Angle: 90", True, circlecolour)
            win.blit(angle,(85,10))
    else:
        vel = font.render("V intial: " + str(round(vi1/10,1)), True, circlecolour)
        win.blit(vel,(5,10))
        if vx1 != 0:
            angle = font.render("Angle: " + str(round((math.atan(vy1/vx1)*180/math.pi),1)), True, circlecolour)
            win.blit(angle,(85,10))
        else:
            angle = font.render("Angle: 90", True, circlecolour)
            win.blit(angle,(85,10))
    if launched == True:
        maxh = font.render("Max Height: " + str(round((y-maxheight)/10,1)), True, circlecolour)
        win.blit(maxh,(5,30))
        range = font.render("Range: " + str(round((x-15)/10,1)), True, circlecolour)
        win.blit(range,(120,30))
    time = font.render("Time: " + str(round((time/1000),2)), True, circlecolour)
    win.blit(time,(245,30))




main()   
    
    

