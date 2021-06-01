import pygame
from random import*

'''*****************************小型敌机**********************************'''
'''*****************************小型敌机**********************************'''

class SmallEnemy(pygame.sprite.Sprite):
    def __init__(self,bg_size):
        pygame.sprite.Sprite.__init__(self)


        #加载图片，获得小飞机的矩形
        self.image = pygame.image.load('images/enemy1.png').convert_alpha()
        self.destroy_images[]
        self.destroy_images.extend([\
            pygame.image.load('images/enemy1_down1.png').convert_alpha(),\
            pygame.image.load('images/enemy1_down2.png').convert_alpha(),\
            pygame.image.load('images/enemy1_down3.png').convert_alpha(),\
            pygame.image.load('images/enemy1_down4.png').convert_alpha()\
            ])
        self.rect = self.image.get_rect()

        #定义背景，移动速度
        self.width,self.height = bg_size[0],bg_size[1]
        self.speed = 2
        
        #飞机是否存活
        self.active = True
        #飞机出生点位置
        self.rect.left , self.rect.top = \
                       randint(0 , self.width - self.rect.width),\
                       randint(-5 * self.height , 0)


    def move(self):
        if self.rect.top < self.height:
            self.rect.top += self.speed

        else:
            self.reset()

    def reset(self):
        self.active = True
        self.rect.left , self.rect.top = \
                   randint(0 , self.width - self.rect.width),\
                   randint(-5 * self.height , 0)



'''*****************************中型敌机**********************************'''
'''*****************************中型敌机**********************************'''

class MidEnemy(pygame.sprite.Sprite):
    def __init__(self,bg_size):
        pygame.sprite.Sprite.__init__(self)


        #加载图片，获得中飞机的矩形
        self.image = pygame.image.load('images/enemy2.png').convert_alpha()
        self.destroy_images[]
        self.destroy_images.extend([\
            pygame.image.load('images/enemy2_down1.png').convert_alpha(),\
            pygame.image.load('images/enemy2_down2.png').convert_alpha(),\
            pygame.image.load('images/enemy2_down3.png').convert_alpha(),\
            pygame.image.load('images/enemy2_down4.png').convert_alpha()\
            ])
        self.rect = self.image.get_rect()

        #定义背景，移动速度
        self.width,self.height = bg_size[0],bg_size[1]
        self.speed = 2
        self.active = True
        #飞机出生点位置
        self.rect.left , self.rect.top = \
                       randint(0 , self.width - self.rect.width),\
                       randint(-10 * self.height , - self.height)


    def move(self):
        if self.rect.top < self.height:
            self.rect.top += self.speed

        else:
            self.reset()

    def reset(self):
        self.active = True
        self.rect.left , self.rect.top = \
                   randint(0 , self.width - self.rect.width),\
                   randint(-10 * self.height , - self.height)


'''*****************************大型敌机**********************************'''
'''*****************************大型敌机**********************************'''

class BigEnemy(pygame.sprite.Sprite):
    def __init__(self,bg_size):
        pygame.sprite.Sprite.__init__(self)


        #加载图片，获得中飞机的矩形
        self.image1 = pygame.image.load('images/enemy3_n1.png').convert_alpha()
        self.image2 = pygame.image.load('images/enemy3_n2.png').convert_alpha()
        self.destroy_images[]
        self.destroy_images.extend([\
            pygame.image.load('images/enemy3_down1.png').convert_alpha(),\
            pygame.image.load('images/enemy3_down2.png').convert_alpha(),\
            pygame.image.load('images/enemy3_down3.png').convert_alpha(),\
            pygame.image.load('images/enemy3_down4.png').convert_alpha(),\
            pygame.image.load('images/enemy3_down5.png').convert_alpha(),\
            pygame.image.load('images/enemy3_down6.png').convert_alpha()\
            ])

        self.rect = self.image1.get_rect()

        #定义背景，移动速度
        self.width,self.height = bg_size[0],bg_size[1]
        self.speed = 2
        self.active = True

        #飞机出生点位置
        self.rect.left , self.rect.top = \
                       randint(0 , self.width - self.rect.width),\
                       randint(-15 * self.height , -5*self.height)


    def move(self):
        if self.rect.top < self.height:
            self.rect.top += self.speed

        else:
            self.reset()

    def reset(self):
        self.active = True
        self.rect.left , self.rect.top = \
                   randint(0 , self.width - self.rect.width),\
                   randint(-15 * self.height , -5*self.height)
            
