from ion import *;from random import *;from math import *;from kandinsky import *;from turtle import *
Lc3,Lc2,Lc,a=[],[],[],17
b=255//a
#Lc  
for i in range(a):
  Lc.append((255,i*b,0))
for i in range(a):
  Lc.append((255-i*b,255,0))
for i in range(a):
  Lc.append((0,255,i*b))
for i in range(a):
  Lc.append((0,255-i*b,255))
for i in range(a):
  Lc.append((i*b,0,255))
for i in range(a):
  Lc.append((255,0,255-i*b))

#Lc3 nuances de gris
for i in range(255):
  Lc3.append((i,i,i))
 
#


def angle_polaire(x,y):
  x,y=(x-160),(111-y)        
  alpha=atan(y/(x+0.0001))/(2*pi)*360
  if x>0 and y>0:angle=alpha
  elif x<0 and y>0:angle=180+alpha        
  elif x<0 and y<0:angle=180+alpha
  elif x>0 and y<0:angle=360+alpha   
  if x==0 and y==0:angle=0
  elif x==0:
    if y>0:angle=90
    elif y<0:angle=270
  elif y==0:
    if x>0:angle=0
    elif x<0:angle=180
  return angle    
def wooa0():
  while True:
    for i in Lc:
      fill_rect(0,0,320,222,i)
def wooa1():
  for i in range(222):
    for j in range(320):
      set_pixel(j,i,Lc[int(len(Lc)/542*(j+i))])
def wooa2():
  for x in range(320):
    for y in range(222):
      set_pixel(x,y,Lc[int(sqrt((x-160)**2+(111-y)**2)*len(Lc)/195)])
def wooa3():
  for x1 in range(320):
    for y1 in range(222):
      d=(x1-160)**2+(111-y1)**2
      if d<=100**2:
        angle=angle_polaire(x1,y1)
        set_pixel(x1,y1,Lc[int(angle*(len(Lc)/360))])  
  while True:
    if keydown(KEY_OK):
      penup();x,y=0,0
      while True:
        if keydown(KEY_LEFT):
          if x>-100: x-=3
        if keydown(KEY_RIGHT):
          if x<100: x+=3
        if keydown(KEY_UP):
          if y<111: y+=3
        if keydown(KEY_DOWN):
          if y>-111: y-=3
        goto(x,y)
        c=get_pixel(x+160+5,111-y+5)
        fill_rect(266,0,60,205,c)
        fill_rect(260,0,2,205,(0,0,0))
        fill_rect(262,0,2,205,(25,255,255))
        fill_rect(264,0,2,205,(0,0,0))
        draw_string(" R",125,205,(255,0,0),(0,0,0))
        draw_string("G",145,205,(0,255,0),(0,0,0))
        draw_string("B",155,205,(0,0,255),(0,0,0))
        draw_string(": "+str(c)+"       ",165,205,(25,255,255),(0,0,0))
        
def wooa4():
  while True:
    x=randint(0,320)
    y=randint(0,222)
    θ=angle_polaire(x,y)
    set_pixel(x,y,Lc[int(θ*(len(Lc)/360))])  
def wooa5():
  L1=[range(0,320,2),range(1,319,2),range(0,222,2),range(1,221,2)]
  for i in range(2):
    for j in range(2):
      for x in L1[i]:
        for y in L1[j+2]:
          θ=angle_polaire(x,y)
          set_pixel(x,y,Lc[int(θ*(len(Lc)/360))])  
def wooa6():
  for i in range(150):
    for j in range(320):
      c=int(j/320*255)
      set_pixel(j,i,(c,c,c))
      penup()
  x,y=0,0
  while True:
    if keydown(KEY_LEFT):
      if x>-160: x-=3
    if keydown(KEY_RIGHT):
      if x<160: x+=3
    if keydown(KEY_UP):
      if y<111: y+=3
    if keydown(KEY_DOWN):
      if y>-111: y-=3
    goto(x,y)
    c=get_pixel(x+160+5,111-y+5)
    fill_rect(0,150,320,72,c)
    draw_string("RGB="+str(c)+"    ",0,130,(255,255,255),(0,0,0))
def wooa7():
  for i in range(160):
    for j in range(320):
      c2=Lc[int(j/320*len(Lc))]
      r=c2[0]*i//160
      g=c2[1]*i//160
      b=c2[2]*i//160
      c=(r,g,b)
      set_pixel(j,i,c)
      penup()
      x,y=0,0
  while True:
    if keydown(KEY_LEFT):
      if x>-160: x-=3
    if keydown(KEY_RIGHT):
      if x<160: x+=3
    if keydown(KEY_UP):
      if y<111: y+=3
    if keydown(KEY_DOWN):
      if y>-111: y-=3
    goto(x,y)
    c=get_pixel(x+160+5,111-y+5)
    fill_rect(0,185,320,37,c)
    draw_string("RGB="+str(c)+" "*30+"\n"+" "*40,0,161,(255-c[0],255-c[1],255-c[2]),c)
    fill_rect(0,160,320,1,(0,0,0))
def wooa8():
  while True:
    x,y,c=randint(0,320),randint(0,222),randint(0,len(Lc)-1)
    #set_pixel(x,y,Lc[c])
    l,h=randint(0,20),randint(0,20)
    fill_rect(x,y,l,h,Lc[c])
def int_to_rgb(h, s=1.0, v=1.0):
    h = (h%360)/360
    if s == 0.0: v*=255; return (v, v, v)
    i = int(h*6.) # XXX assume int() truncates!
    f = (h*6.)-i; p,q,t = int(255*(v*(1.-s))), int(255*(v*(1.-s*f))), int(255*(v*(1.-s*(1.-f)))); v*=255; i%=6
    if i == 0: return (v, t, p)
    if i == 1: return (q, v, p)
    if i == 2: return (p, v, t)
    if i == 3: return (p, q, v)
    if i == 4: return (t, p, v)
    if i == 5: return (v, p, q)
def wooa9():
    a,c= 15,13
    
    x0,y0 = (320-a*c)//2,(222-a*c)//2
    fill_rect(0,0,320,222,(60,60,60))
    
    yo = 0
    while True:
      for i in range(a):
        for j in range(a):
            fill_rect(x0+i*c, y0+j*c, c,c,int_to_rgb(i*10+j*10+yo))
      yo-=10
def wooa10():
    c = 0
    while True:
        c+=1
        col = int_to_rgb(c%360)
        fill_rect(0,0,320,222,col)

#
wooa3()
