from random import *
from math import *
from kandinsky import *
from ion import *
L=[(255,0,0),(0,255,0),(0,0,255),
(255,255,0),(255,0,255),(0,255,255),]
16*11
20*20
cote=20
x,y=0,0
c1,c2=(255,230,150),(255,170,170)
fill_rect(0,0,320,222,c1)
for x in range(320//cote):
  fill_rect(x*20-1,0,2,222,c2)
for y in range(222//cote):
  fill_rect(0,y*20-1,320,2,c2)
x,y=0,0
fill_rect(0,0,cote,cote,(0,0,255))
fill_rect(2,2,cote-4,cote-4,(0,255,255))
while True:
  x0,y0=x,y
  if keydown(KEY_LEFT):
    while keydown(KEY_LEFT):True
    if x>0:
      x-=1
  if keydown(KEY_RIGHT):
    while keydown(KEY_RIGHT):True
    if x*cote<320-cote:
      x+=1
  if keydown(KEY_UP):
    while keydown(KEY_UP):True
    if y*cote>0:
      y-=1
  if keydown(KEY_DOWN):
    while keydown(KEY_DOWN):True
    if y*cote<220-cote:
      y+=1
            
  if x0!=x or y0!=y:
    fill_rect(x*cote,y*cote,cote,cote,(255,255,255))
    fill_rect(x*cote+2,y*cote+2,cote-4,cote-4,(0,0,0))
    #if not(keydown(KEY_OK)):
    #fill_rect(x0*cote,y0*cote,cote,cote,c2)
    #fill_rect(x0*cote+1,y0*cote+1,cote-2,cote-2,c1)
    c=L[randint(0,len(L)-1)]
    fill_rect(x0*cote,y0*cote,cote,cote,c)
    c=(255-c[0],255-c[1],255-c[2])
    fill_rect(x0*cote+2,y0*cote+2,cote-4,cote-4,c)
