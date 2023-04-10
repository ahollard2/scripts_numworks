from ion import *
from math import *
from kandinsky import *
from random import *

Lrect=[[0,0,320,222]]

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
def random_color():
  return hsv_to_rgb(randint(0,360))
def main():
  c=random_color()
  fill_rect(0,0,320,222,c)
  while True:
    if keydown(KEY_OK) or keydown(KEY_DOWN):
      while keydown(KEY_OK)or keydown(KEY_DOWN):True
      i=Lrect[randint(0,len(Lrect)-1)]
      while i[2]<20 or i[3]<20:
        Lrect.remove(i)
        i=Lrect[randint(0,len(Lrect)-1)]
      x,y,l,h=i[0],i[1],i[2],i[3]
      Lnewrect=[[[x,y,l,h//2],[x,y+h//2,l,h//2]],[[x,y,l//2,h],
      [x+l//2,y,l//2,h]]]
      d=Lnewrect[randint(0,1)]
      c=randint(0,1)
      a=d[c]
      b=d[abs(c-1)]  
      Lrect.remove(i)
      Lrect.append(a)
      Lrect.append(b)
      fill_rect(a[0],a[1],a[2],a[3],random_color())
main()
