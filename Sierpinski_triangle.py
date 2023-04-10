from kandinsky import* ;from random import*
def triangle(N):
  x,y,n=0,0,0
  while n<N:
    b=randint(0,2)
    if b==2:
      mx,my=0.5,1
    if b==1:
      mx,my=1,0
    if b==0:
      mx,my=0,0
    x,y=(x+mx)/2,(y+my)/2
    set_pixel(int(x*320),222-int(y*222),(0,0,255))
    n+=1
    
def square(N_i):
  x,y,n,A,B=0,0,0,4,4
  while n<N_i:
    while B==A:
      A=randint(0,3)
    B=A
    if A==0:
      mx,my=0,0
    if A==1:
      mx,my=1,0
    if A==2:
      mx,my=0,1
    if A==3:
      mx,my=1,1
    x,y=(x+mx)/2,(y+my)/2
    set_pixel(int(x*320),222-int(y*222),(255,0,255))
    n+=1
triangle(50000)
square(50000)
