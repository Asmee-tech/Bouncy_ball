import pgzrun
import random
TITLE="Bouncy balls!"
WIDTH=800
HEIGHT=800
grav=2000.0
#ball class
class bouncy():
    def __init__(self,x,y,radius):
        self.x=x
        self.y=y
        self.radius=radius
        self.vx=200
        self.vy=0
    #function for drawing
    def draw(self):
        #generating random colors
        r=random.randint(0,255)
        g=random.randint(0,255)
        b=random.randint(0,255)
        comc=r,g,b
        pos=(self.x,self.y)
        screen.draw.filled_circle(pos,self.radius,comc)
#object creation
circ1=bouncy(60,60,50)
circles=[circ1]
def draw():
    circ1.draw()
#defining update
def update(ti):
    global circles
    pass
    for i in circles:
        uy = i.vy
        i.vy += grav * ti
        i.y += (uy + i.vy) * 0.5 * ti
    #handeling bouncing
        if i.y>800:
            i.y=800
            i.vy=-i.vy*0.9
        i.x+=i.vx*ti
        if i.x>800 or i.x<0:
            i.vx=-i.vx
#key down event
def on_key_down(key):
    if key==keys.SPACE:
        circ1.y=-200
    
    
    
pgzrun.go()
    
    
    
pgzrun.go()
