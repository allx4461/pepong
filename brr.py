from pygame import *
speed=10
y1,y2=150,150
x1,x2=50,600
FPS=60
speedx=5
speedy=5
xm=150
ym=350
l=0
r=0

window=display.set_mode((700,500))
display.set_caption('Ппнг')
background=transform.scale(image.load('lain.jpg'), (700,500))
window_width=700

font.init()
font1=font.Font(None,40)
winl=font1.render('крайне левый мир победил',True,(255,215,0))
winr=font1.render('крайне правый доотбивался',True,(150,0,0))
#x=(len(l),':',len(r))
#sch=font1.render(x,True,(150,0,0))



game=True

clock = time.Clock()
class GameSprite(sprite.Sprite):
    def __init__(self, player_image,player_x,player_y,player_speed):
        super().__init__()
        self.image=transform.scale(image.load(player_image),(65,65))
        self.speed_x=player_speed
        self.speed_y=player_speed
        self.rect=self.image.get_rect()
        self.rect.x=player_x
        self.rect.y=player_y
    def reset(self):
        window.blit(self.image,(self.rect.x,self.rect.y))
class baal(GameSprite):
    def update(self,lk,rk):
        if not(self.rect.x<=0) and (not(self.rect.x>=700)):
            self.rect.x+=self.speed_x
        else:
           self.speed_x*=-1
           self.rect.x+=2*self.speed_x
        if not(self.rect.y<=0) and (not(self.rect.y>=500)):
            self.rect.y+=self.speed_y
        else:
           self.speed_y*=-1 
           self.rect.y+=2*self.speed_y
        if sprite.collide_rect(self,lk) or sprite.collide_rect(self,rk):
            #self.speed_y*=-1
            self.speed_x*=-1
        self.reset()
        
class rk(GameSprite):
    def update(self):
        keys_pressed=key.get_pressed()
        if keys_pressed[K_UP] and self.rect.y>5:
            self.rect.y-=self.speed_y
            self.reset()
        if keys_pressed[K_DOWN] and self.rect.y<395:
            self.rect.y+=self.speed_y
            self.reset()
        self.reset()
class lk(GameSprite):
    def update(self):
        keys_pressed=key.get_pressed()
        if keys_pressed[K_w] and self.rect.y>5:
            self.rect.y-=self.speed_y
            self.reset()
        if keys_pressed[K_s] and self.rect.y<395:
            self.rect.y+=self.speed_y
            self.reset()
        self.reset()    

left=lk('palka.png',x1,y1,10)
right=rk('palka.png',x2,y2,10)
ball=baal('eye.png',xm,ym,10)
finish=False

while game == True:
    for e in event.get():
        if e.type == QUIT:
            game=False
   
    if finish != True:
        window.blit(background,(0,0))
        ball.update(left,right)
        left.update()
        right.update()
        
        if ball.rect.x<=1:
            finish=True
            window.blit(winr,(200,200))
            '''r+=1
            window.blit(sch,(200,200))
            x=(len(l),':',len(r))'''
            display.update()
            time.wait(1000)
            ball.rect.x=150
            ball.rect.x=350
            finish=False
        if ball.rect.x>=699:
            finish=True
            window.blit(winl,(200,200))
            '''l+=1
            x=(len(l),':',len(r))
            window.blit(sch,(200,200))'''
            display.update()
            time.wait(1000)     
            ball.rect.x=150
            ball.rect.x=350
            finish=False
    display.update()
    clock.tick(FPS)
