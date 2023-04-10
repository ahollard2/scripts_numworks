from math import *
from math import *
from kandinsky import *
from ion import *
xmin=-5
xmax=5
ymin = -3.5
ymax = 3.5

#xmin=-4
#xmax=4
#ymin = -3
#ymax = 3

rangex = xmax - xmin
rangey = ymax - ymin
xscl = 320 / rangex
yscl = -222 / rangey

# fmatrix = [[0,0,0],[1,0,0],[1,2,0],[2,2,0],[2,3,0],[1,3,0],[1,4,0],
#          [3,4,0],[3,5,0],[0,5,0],
#     [0,0,1],[1,0,1],[1,2,1],[2,2,1],[2,3,1],[1,3,1],[1,4,1],
#          [3,4,1],[3,5,1],[0,5,1]]
# edges = [[0,1],[1,2],[2,3],[3,4],[4,5],[5,6],[6,7],
#         [7,8],[8,9],[9,0],
#         [10,11],[11,12],[12,13],[13,14],[14,15],[15,16],[16,17],
#         [17,18],[18,19],[19,10],
#         [0,10],[1,11],[2,12],[3,13],[4,14],[5,15],[6,16],[7,17],
#         [8,18],[9,19]]
Adepth = 0.5
Amatrix=[
    [-2,-2,Adepth],#z=0
    [-1,-2,Adepth],
    [-0.5,-0.5,Adepth],
    [0.5,-0.5,Adepth],
    [1,-2,Adepth],
    [2,-2,Adepth],
    [0.5,2,Adepth],
    [-0.5,2,Adepth],
    [-0.2,1,Adepth],
    [0.2,1,Adepth],
    [0.5,0,Adepth],
    [-0.5,0,Adepth],
    [-2,-2,-Adepth],#z =1
    [-1,-2,-Adepth],
    [-0.5,-0.5,-Adepth],
    [0.5,-0.5,-Adepth],
    [1,-2,-Adepth],
    [2,-2,-Adepth],
    [0.5,2,-Adepth],
    [-0.5,2,-Adepth],
    [-0.2,1,-Adepth],
    [0.2,1,-Adepth],
    [0.5,0,-Adepth],
    [-0.5,0,-Adepth],
]
Aedges= [
    [0,1],#traits de la face avant
    [1,2],
    [2,3],
    [3,4],
    [4,5],
    [5,6],
    [6,7],
    [7,0],
    [8,9],
    [11,10],
    [8,11],
    [9,10],
    
    [0,12],#entre les z0 et z1
    [1,13],
    [2,14],
    [3,15],
    [4,16],
    [5,17],
    [6,18],
    [7,19],
    [8,20],
    [9,21],
    [10,22],
    [11,23],
    
    #traits de la afce arriere
    [12, 13], [13, 14], [14, 15], [15, 16], [16, 17], [17, 18], [18, 19], [19, 12], [20, 21], [23, 22], [20, 23], [21, 22]
]
#
cote = 2

cube = [
    [-cote, cote,-cote],
    [-cote,-cote,-cote],
    [ cote, cote,-cote],
    [ cote,-cote,-cote],
    [-cote, cote,cote],
    [-cote,-cote,cote],
    [ cote, cote,cote],
    [ cote,-cote,cote]
]
edges = [
    [0,1],
    [1,3],
    [0,2],
    [2,3],
    [4,5],
    [4,6],
    [5,7],
    [7,6],
    [4,0],
    [6,2],
    [7,3],
    [1,5]
]

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

def main():
    global xscl, yscl, edges, cube
    #edges = Aedges
    #cube = Amatrix
    c=0
    col_fond = (0,0,0)
    col_cube = (0,0,255)
    fill_rect(0,0,320,222, col_fond)
    def graphPoints2(pointList,edges, _col):
        '''Graphs the points in a list using segments'''
        p_z=0.1
        if _col==col_fond:
          for pt1,pt2 in edges:
            x1,y1,z1=pointList[pt1]
            x2,y2,z2=pointList[pt2]
            #draw_line(
            #    int((x1+z1*0.2*x1)*xscl+160),int(111-(y1+z1*0.2*y1)*yscl),
            #    int((x2+z2*0.2*x2)*xscl+160),int(111-(y2+z2*0.2*y1)*yscl),col_fond)
            draw_line(
                int((x1-z1*p_z*x1)*xscl+160),int(111-(y1-z1*p_z*y1)*yscl),
                int((x2-z2*p_z*x2)*xscl+160),int(111-(y2-z2*p_z*y2)*yscl), _col)
            draw_line(
                int((x1-z1*p_z*x1)*xscl+160)+1,int(111-(y1-z1*p_z*y1)*yscl)+1,
                int((x2-z2*p_z*x2)*xscl+160)+1,int(111-(y2-z2*p_z*y2)*yscl)+1, _col)    
        
        else:
          #on cherche lindice du point le plus loin
          imax,max=0,pointList[0][2]
          for i in range(1,8):
            if pointList[i][2]>max:
              max,imax=pointList[i][2],i
          #ca sera sa col
          col2=int_to_rgb(c,1.0,0.4)
          #col2=(120,120,120)
          for pt1,pt2 in edges:
            if pt1==imax or pt2==imax:
              col=col2
            else:
              col=_col
            x1,y1,z1=pointList[pt1]
            x2,y2,z2=pointList[pt2]
            draw_line(
                int((x1-z1*p_z*x1)*xscl+160),int(111-(y1-z1*p_z*y1)*yscl),
                int((x2-z2*p_z*x2)*xscl+160),int(111-(y2-z2*p_z*y2)*yscl), col)
            draw_line(
                int((x1-z1*p_z*x1)*xscl+160)+1,int(111-(y1-z1*p_z*y1)*yscl)+1,
                int((x2-z2*p_z*x2)*xscl+160)+1,int(111-(y2-z2*p_z*y2)*yscl)+1, col)    
    def rottilt(rot,tilt):
        '''returns the matrix for rotating a number of degrees.'''
        rotmatrix_Y = [[cos(tilt),0.0,sin(tilt)],
                    [0.0,1.0,0.0],
                    [-sin(tilt),0.0,cos(tilt)]]
        rotmatrix_X = [[1.0,0.0,0.0],
                    [0.0,cos(rot),sin(rot)],
                    [0.0,-sin(rot),cos(rot)]]
        return multmatrix(rotmatrix_X,rotmatrix_Y)
    def multmatrix(a,b):
        n = len(a)
        m = len(b[0])
        newmatrix = [[0]*m for _ in range(n)]
        for i in range(n):
            #for every column in b
            for j in range(m):
                #for every element in the column
                for k in range(len(b)):
                    newmatrix[i][j] += a[i][k]*b[k][j]
        return newmatrix
    rot, tilt = pi, pi
    rot_matrix = rottilt(rot,tilt)
    newmatrix = multmatrix(cube,rot_matrix)
    graphPoints2(newmatrix,edges, col_cube)
    
    pas = 0.025
    has_changed = False
    

    while True:
        if keydown(KEY_DOWN):
            graphPoints2(newmatrix,edges, col_fond)
            tilt-=pas
            if tilt<=pas:
                tilt = 2*pi
            has_changed = True
        elif keydown(KEY_UP):
            graphPoints2(newmatrix,edges, col_fond)
            tilt+=pas%(2*pi)
            has_changed = True
        elif keydown(KEY_LEFT):
            graphPoints2(newmatrix,edges, col_fond)
            rot-=pas
            if rot<=pas:
                rot=2*pi
            has_changed = True
        elif keydown(KEY_RIGHT):
            graphPoints2(newmatrix,edges, col_fond)
            rot+=pas%(2*pi)
            has_changed = True
        pas_x=0.1    
        pas_z=0.1
        if keydown(KEY_SIX):
         graphPoints2(newmatrix,edges, col_fond)
         for i in range(len(cube)):
           cube[i][0]-=pas_x
            
          
        elif keydown(KEY_FOUR):
         graphPoints2(newmatrix,edges, col_fond)
         for i in range(len(cube)):
           cube[i][0]+=pas_x
        
        elif keydown(KEY_LEFTPARENTHESIS):
         graphPoints2(newmatrix,edges, col_fond)
         for i in range(len(cube)):
           cube[i][2]+=pas_z
        elif keydown(KEY_RIGHTPARENTHESIS):
         graphPoints2(newmatrix,edges, col_fond)
         for i in range(len(cube)):
           cube[i][2]-=pas_z
        
        if keydown(KEY_HOME):
        
         print(newmatrix)
           
        if has_changed:
           rot_matrix = rottilt(tilt,rot)
           newmatrix = multmatrix(cube,rot_matrix)
           graphPoints2(newmatrix,edges, col_cube)
           has_changed = False
        
        
        #couleur
        c+=1
        col_cube = int_to_rgb(c)
        rot_matrix = rottilt(tilt,rot)
        newmatrix = multmatrix(cube,rot_matrix)
        graphPoints2(newmatrix,edges, col_cube)


main()
