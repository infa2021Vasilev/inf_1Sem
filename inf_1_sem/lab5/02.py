# -*- coding: utf-8 -*-
import pygame as pg
import numpy as np

def trig(f,x,y,l,a,cl):
	#Auxiliary function, called in the man drawing function
	#Draws a man's hair
	#f is a pygame object.Surface
	#x, y - coordinates of one of the vertices of the image hair
	#cl - color
	#bl - black color
	#l - hair sizes
	#a - angle of rotation
     pg.draw.polygon(f,cl,([x,y],[int(x+l*np.cos(a)),int(y-l*np.sin(a))],[int(x+l*np.cos(a+1.047)),int(y - np.sin(a+1.047)*l)]))
     pg.draw.polygon(f,bl,([x,y],[int(x+l*np.cos(a)),int(y-l*np.sin(a))],[int(x+l*np.cos(a+1.047)),int(y - np.sin(a+1.047)*l)]),1)
	 
def man(ck,cg,cm,cv,cn,cr,x,y,a,d):
	#Main function
	# Draws a man
	#ck - Color of hands and face
	#cg - Eye color
	#cm - Shirt color
	#cm - Hair color
	#cn - Nose color
	#cr - Mouth color
	#x,y - coordinates of the upper left corner of the man
	#a,d - vertical and horizontal dimensions
	
	
    #s - object of pygame.Surface
    s = pg.Surface((927, 769), pg.SRCALPHA) 
	
	
	#Body
    pg.draw.circle(s,cm,(447,769),246,0)

    pg.draw.polygon(s,ck,([669,558],[700,573],[854,124],[823,124]),0)
    pg.draw.polygon(s,ck,([202,574],[233,563],[103,116],[71,126]),0)

    pg.draw.ellipse(s,ck,(42,40,85,95),0)
    pg.draw.ellipse(s,ck,(790,36,87,110),0)
    pg.draw.ellipse(s,wh,(42,40,85,95),1)
    pg.draw.ellipse(s,wh,(790,36,87,110),1)

    pg.draw.polygon(s,cm,([174,578],[258,531],[316,600],[272,690],[185,676]),0)
    pg.draw.polygon(s,bl,([174,578],[258,531],[316,600],[272,690],[185,676]),1)

    pg.draw.polygon(s,cm,([585,607],[642,531],[724,568],[720,668],[636,692]),0)
    pg.draw.polygon(s,bl,([585,607],[642,531],[724,568],[720,668],[636,692]),1)

	
    #Head
    pg.draw.ellipse(s,ck,(222,168,455,463),0)
    pg.draw.ellipse(s,cg,(327,316,99,87),0)
    pg.draw.ellipse(s,bl,(327,316,99,87),1)
    pg.draw.ellipse(s,bl,(360,350,28,28),0)

    pg.draw.ellipse(s,cg,(474,316,99,87),0)
    pg.draw.ellipse(s,bl,(474,316,99,87),1)
    pg.draw.ellipse(s,bl,(509,350,28,28),0)


    pg.draw.polygon(s,cn,([433,416],[471,416],[452,450]),0)
    pg.draw.polygon(s,cr,([324,467],[568,467],[454,545]),0)
    pg.draw.polygon(s,bl,([433,416],[471,416],[452,450]),1)
    pg.draw.polygon(s,bl,([324,467],[568,467],[454,545]),1)

	
    #Hair
    L = 72

    trig(s,252,286,L,1.01,cv)
    trig(s,276,243,L,0.66,cv)
    trig(s,314,216,L,0.62,cv)
    trig(s,352,193,L,0.25,cv)
    trig(s,390,180,L,0.15,cv)
    trig(s,438,180,L,-0.125,cv)
    trig(s,489,185,L,0,cv)
    trig(s,538,183,L,-0.57,cv)
    trig(s,576,201,L,-0.74,cv)
    trig(s,611,230,L,-1,cv)
	
	
    s = pg.transform.smoothscale(s,(int(a), int(d)))
    screen.blit(s, (x,y))
	
def tablichka(x,y,a,d,sign):
	#Main function
	#Draws a sign with the inscription
	#x,y - coordinates of the upper left corner of the man
	#a,d - vertical and horizontal dimensions
	#sign - sign, string type
	
	#s - object of pygame.Surface
	s = pg.Surface((927, 90), pg.SRCALPHA)
	
	myfont = pg.font.SysFont('arial', 60)
	textsurface = myfont.render(sign, False, (0, 0, 0))
	
	pg.draw.rect(s,lg,(0,0,927,90),0)	# Draws an inscription (something obscene about python)
	pg.draw.rect(s,bl,(0,0,927,90),1)
	u = myfont.size(sign)
	s.blit(textsurface,(int((927 - u[0])/2),0))
	s = pg.transform.smoothscale(s,(int(a), int(d)))
	screen.blit(s, (x,y))
	
pg.init() 
 
#BEGIN OF DRAWING
 
FPS = 30 
screen = pg.display.set_mode((1500, 769)) 


#COLORS:
bl = (0,0,0,255)		#black
wh = (255,255,255,255)  #white
ye = (255,212,42,255)	#yellow
gr =(0,128,0,255)		#green
ar =(255,102,0,255)		#orrange
re = (255,42,42,255)	#red
pu = (212,42,255,255)	#purple
br = (120,68,33,255)	#brown
go = (128,179,255,255)	#blue
se = (190,200,183,255)	#gray
sc = (233,198,175,255)	#color of the skin
lg = (127,255,42,255)	#light green


screen.fill(wh)
man(sc,go,ar,pu,br,re,0,0,750,769)
man(br,gr,pu,lg,sc,re,750,0,750,769)
tablichka(0,0,1500,90,'Python sucks!!!')

#END OF DRAWING

pg.display.update() 
clock = pg.time.Clock() 
finished = False 
 
while not finished: 
    clock.tick(FPS) 
    for event in pg.event.get(): 
        if event.type == pg.QUIT: 
            finished = True 
 
pg.quit()