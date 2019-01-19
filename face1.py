class express:
 import pygame
 import sys
 import math
# Initialize pygame library
 
 a=-1
 def face(funcno):
    import math
    import time
    import pygame
    pygame.init()

    rect1 = pygame.Rect(40,40,25,50)
    rect2 = pygame.Rect(40,100,30,30)

#colors
    red = (255,0,0)
    blue = (60,224,220)
    green = (0,255,0)
    yellow = (25,255,40)
    white = (255,255,255)
    black = (0,10,25)
    purple = (136,71,188)
    brown = (72, 36, 0)

#sizes
    global screenSize 
    screenSize = (800,600)
#t

#clock
 
    global clock
    clock=pygame.time.Clock()
    clock.tick(30)

#PI
    global PI
    PI=math.pi
#vars
    global a

    screenTitle = "Graphics Shapes"
    #Creates a screen to draw upon
    screen = pygame.display.set_mode(screenSize)
    pygame.display.set_caption(screenTitle)
    def quitting():
        for event in pygame.event.get():
           if event.type ==pygame.QUIT:
               pygame.display.quit()
    def talk():
        x2=1
        y2=0.4
        for i in range(1,50):     
         smile(x2)
         pygame.display.update()
         screen.fill(black)
         x2+=1
         y2+=0.1
        s=x2
        s2=y2
        x2=1
        for i in range(1,50):     
         smile(-x2+s)#,-y2+s2)
         pygame.display.update()
         screen.fill(black)
         x2+=1
         y2+=0.1
    
    #Make a smiley face
    def thanku():
        
        y2=2
        for i in range(1,40):     
         smile(0.0,y2)
         pygame.display.update()
         screen.fill(black)
         
         y2+=2
        
        s2=y2
        y2=2
        time.sleep(0.2)
        for i in range(1,40):     
         smile(0,-y2+s2)
         pygame.display.update()
         screen.fill(black)
         
         y2+=2
    
        funcno=0
    def smile(point=0,point2=0,ss=0,sp=0):
      #pygame.draw.circle(screen, white,(397,338) , 14)
      #ss*=1
      #print(ss)
      pygame.draw.circle(screen, blue,(260,165) , 80)
      pygame.draw.circle(screen, blue,(530,165) , 80)
      pygame.draw.circle(screen, black,(260,165+((int)(point2))), 50)
      pygame.draw.circle(screen, black,(530,165+((int)(point2))), 50)
      pygame.draw.arc(screen, white, [310-ss,340+point/2 -ss,170+ss,100+ss], 8*PI/7,(13*PI/7),4)
      pygame.draw.arc(screen, white, [320-ss,346+point/2 -ss,150+ss,101+ss], 6*PI/5,1.787*PI,6)
 #(4*PI-12*PI/7), 5)
    a=-1
    def laugh():
      
         #add=(40) 
        x2=0.3
        
        for i in range(1,200):     
         smile(x2)
         pygame.display.update()
         screen.fill(black)
         x2+=0.3
         
        s=x2 
        x2=0.3
        for i in range(1,200):     
         smile(-x2+s)
         pygame.display.update()
         screen.fill(black)
         x2+=0.3
         
    pygame.display.flip()

    
    a=-1
    
    while 1:
     functions=[smile,thanku,laugh ,talk]
     functions[funcno]()
     
     #thanku()
     quitting()
            
      
    


 face(2)           
 try:
    if __name__ == '__main__':
        face(2)
 except:
    print (sys.exc_info())
    pygame.display.quit()
