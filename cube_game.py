from math import *
from kandinsky import *
from ion import *
from random import *
boolsaut,compteur_saut,L_saut=False,0,[int(-0.4*(x/4)**2+70) for x in range(-52,52)]+[0]
#L_saut=[int(-1*(x/6)**2+70) for x in range(-50,50)]

#length side + 
side,y_floor=15,200
x,y=0,y_floor-side
c=0# just a counter for the rgb effect on the cube

#usually colors variable name begins with "c_" and then the object it relates to
c_sky,c_cloud=(169, 204, 227),(160,160,160)

fill_rect(0,0,320,222,c_sky)
#fill_rect(0,0,320,222,(0,0,0))



score=0
#variable for the square: length of each part
c_1=side//7
c_2=side//12
c_3=side-c_1*2-c_2*2
c_col_1=(255,255,255)
c_col_3=(255,255,255)
def display_square():
  c_1=side//7
  c_2=side//8
  c_3=side-c_1*2-c_2*2

  #fill_rect(x,y,cote,cote,c_col_1)
  fill_rect(x,y,side,c_1,c_col_1)
  fill_rect(x,y+side-c_1,side,c_1,c_col_1)
  fill_rect(x,y+c_1,c_1,c_3+c_2*2,c_col_1)
  fill_rect(x+side-c_1,y+c_1,c_1,c_3+c_2*2,c_col_1)
  
  fill_rect(x+c_1,y+c_1,side-2*c_1,c_2,c_carre)
  fill_rect(x+c_1,y+c_1+c_2+c_3,side-2*c_1,c_2,c_carre)
  fill_rect(x+c_1,y+c_1+c_2,c_2,c_3,c_carre)
  fill_rect(x+c_1+c_2+c_3,y+c_1+c_2,c_2,c_3,c_carre)
  
  fill_rect(x+c_1+c_2,y+c_1+c_2,side-(c_1+c_2)*2,side-(c_1+c_2)*2,c_col_3)
#carre  
def hsv_to_rgb(h, s=1.0, v=1.0):#rgb effect, feel free to use it in your own project
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
#  
def wipe_out_previous_square(b):
  fill_rect(x-b,y-b,2*b+side,b,c_sky)
  fill_rect(x-b,y,b,side,c_sky)
  fill_rect(x+side,y,b,side,c_sky)
  fill_rect(x-b,y+side,2*b+side,y_floor-y-side,c_sky)
#
###laser
L_projectiles=[]
w_projectile=8
h_projectile=6
v_projectile=4

##### SKY PART
offset=0#counter for clouds
L_clouds=[[0]*9+[2,1,1]+[0]*9,#here you can easily change the aspect of clouds (2 is meant to be directly placed at the left of 1)   {1 = a square of a cloud and 2 is the part to erase}
[0,0,2,1,1,0,0,0,0,2,1,1,0,0,0,2,1,1,0,0,0],
[0,2,1,1,1,1,0,0,2,1,1,1,1,0,2,1,1,1,1,0,0],
[2,1,1,1,1,1,0,2,1,1,1,1,1,0,2,1,1,1,1,1,0]]   
def display_clouds():
  global L_clouds,offset
  if offset ==16:
    offset=0
    L_clouds=[[i[-1]]+i[:-1]for i in L_clouds]
  else:offset+=1
  h,l=14,16
  for i,p in enumerate(L_clouds):
    for j,q in enumerate(p):
      if q==1:
        x_nuage,y_nuage=-1*l+offset+j*l,20+i*h
        fill_rect(x_nuage,y_nuage,l,h,c_cloud)
      if q==2:
        x_nuage,y_nuage=-1*l+offset+j*l+15,20+i*h
        fill_rect(x_nuage,y_nuage,2,h,c_sky)

#ground
y_ground1,y_ground2,c_herbe,c_ground1,c_ground2=y_floor+(222-y_floor)//3,215,(25, 111, 61 ),(160, 64, 0 ),(96,48,0)
def display_ground():
  fill_rect(0,y_floor,320,222-y_floor,c_herbe)
  fill_rect(0,y_ground1,320,222-y_ground1,c_ground1)
  for i in range(80):#320
    random = randint(0,20)
    h =random*(y_ground2-y_ground1)//20
    fill_rect(i*4,y_ground1,4,h,c_herbe)
  for i in range(190):#190
    xground,yground=randint(0,320),randint(y_ground2-4,222)
    fill_rect(xground,yground,3,3,c_ground2)
  L_col=[(88,140,0),(0,88,24),(0,168,0)]
  for i in range(320):#320
    cground,xground,yground=L_col[randint(0,2)],randint(0,320),randint(y_floor,y_ground1)
    fill_rect(xground,yground,2,2,cground)
display_ground()
#ground

c_carre=(148, 49, 38)
fill_rect(x,y,side,side,c_carre)

Direction=1
bool_tir=True
while True:
  
  precedent_y=y
   # direction du carre = direct du laser
  if keydown(KEY_LEFT):
    Direction=-1
    if x>0:
      fill_rect(x+side-2,y,2,side,c_sky)
      x-=2
  
  elif keydown(KEY_RIGHT):
    Direction=1
    if x+side<=320:
      fill_rect(x,y,2,side,c_sky)
      x+=2
  
  if keydown(KEY_OK):
    if y==y_floor-side: 
      boolsaut=True
  if keydown(KEY_TOOLBOX):
    if side<230:
        side+=1
        y-=1
        x-=side%2
        #w_projectile=cote//3
        #h_projectile=cote//4

  elif keydown(KEY_BACKSPACE):
    if side>8:
        fill_rect(x,y-1,side,3,c_sky)
        fill_rect(x+side-1,y+1,1,side-1,c_sky)
        if boolsaut:
          fill_rect(x-1,y+side-1,side+3,1,c_sky)
        
          
          
        fill_rect(x,y,2,side,c_sky)
        x+=side%2
        side-=1
        y+=1
        #w_projectile=cote//3
        #h_projectile=cote//4
  
    
  if keydown(KEY_HOME):
      if bool_tir:
        bool_tir=False
    #while keydown(KEY_HOME):True
      if len(L_projectiles)<15:
        if Direction==1:
          L_projectiles.append([x+side+3, y+4, 1,side//3,side//4])
        else:
          L_projectiles.append([x-3-w_projectile, y+4, -1,side//3,side//4])
  elif not(keydown(KEY_HOME)):
      bool_tir=True  
    
  
  if len(L_projectiles)!=0:
      for i in L_projectiles:
          if i[0]>320 or i[0]<0-i[3]:
              L_projectiles.remove(i)
          else:
              if i[2]==1:
                x_eff_projectile=i[0]
              else:
                x_eff_projectile=i[0]+i[3]-v_projectile
  
              fill_rect(x_eff_projectile,i[1],v_projectile, i[4], c_sky)
              i[0]+=v_projectile*i[2]
              fill_rect(i[0],i[1],i[3], i[4], (0,0,0))
              fill_rect(i[0]+(i[3]//6)+1,i[1]+(i[4]//6)+1,i[3]-(i[3]//6)*2-2,i[4]-(i[4]//6)*2-2, c_carre)
        
      
      
      
  if boolsaut:
      y=y_floor-side-L_saut[compteur_saut]
      compteur_saut+=1
      
      if compteur_saut== len(L_saut):
        compteur_saut=0
        boolsaut=False
        #y=y_sol-cote
      if precedent_y<y:
        fill_rect(x-2,y-4,side+4,4,c_sky)
      else:
        fill_rect(x-2,y+side,side+4,precedent_y-y,c_sky)
        
  
  
  #nettoyage_de_printemps(5)
  
  wipe_out_previous_square(5)
  #actualisation du carre
  display_square()
  
  #affichage et actualisation des nuages
  display_clouds()
  
  #little alien
  fill_rect(300,150,20,50,(255,0,0))
  fill_rect(304,160,4,4,(255,255,0))
  fill_rect(312,160,4,4,(255,255,0))
  fill_rect(304,170,12,2,(255,255,0))
  
  #
  #aff_ground()
    
  
  #colorful
  c+=1
  c_carre=hsv_to_rgb(c)
  
  #score=""
  draw_string("score= ;)",230,2,c_carre,c_sky)
#200eme ligne YES boys we did it,YYEEEEESSSSSS
