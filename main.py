import pygame
import sys
import traceback
from pygame.locals import*
import myplane
import enemy
#初始化pygame以及混音器
pygame.init()
pygame.mixer.init()

bg_size = width,height = 480,650
#设置窗口大小
screen = pygame.display.set_mode(bg_size)
pygame.display.set_caption('飞机大战李小池')
#加载背景图片
background = pygame.image.load('images/background.png').convert()#background是不透明的所以用convert就可以了


#加载游戏音乐
pygame.mixer.music.load('sound/EscapeFromTarkov.mp3')
pygame.mixer.music.set_volume(0.2)
bullet_sound = pygame.mixer.Sound("sound/bullet.wav")
bullet_sound.set_volume(0.2)
bomb_sound = pygame.mixer.Sound("sound/use_bomb.wav")
bomb_sound.set_volume(0.2)
supply_sound = pygame.mixer.Sound("sound/supply.wav")
supply_sound.set_volume(0.2)
get_bomb_sound = pygame.mixer.Sound("sound/get_bomb.wav")
get_bomb_sound.set_volume(0.2)
get_bullet_sound = pygame.mixer.Sound("sound/get_bullet.wav")
get_bullet_sound.set_volume(0.2)
upgrade_sound = pygame.mixer.Sound("sound/upgrade.wav")
upgrade_sound.set_volume(0.2)
enemy3_fly_sound = pygame.mixer.Sound("sound/enemy3_flying.wav")
enemy3_fly_sound.set_volume(0.2)
enemy1_down_sound = pygame.mixer.Sound("sound/enemy1_down.wav")
enemy1_down_sound.set_volume(0.2)
enemy2_down_sound = pygame.mixer.Sound("sound/enemy2_down.wav")
enemy2_down_sound.set_volume(0.2)
enemy3_down_sound = pygame.mixer.Sound("sound/enemy3_down.wav")
enemy3_down_sound.set_volume(0.5)
me_down_sound = pygame.mixer.Sound("sound/me_down.wav")
me_down_sound.set_volume(0.2)

#分别初始化大中小三个飞机
def add_small_enemies(group1,group2,num):
    for i in range(num):
        e1 = enemy.SmallEnemy(bg_size)
        group1.add(e1)
        group2.add(e1)

        
def add_mid_enemies(group1,group2,num):
    for i in range(num):
        e2 = enemy.MidEnemy(bg_size)
        group1.add(e2)
        group2.add(e2)

        
def add_big_enemies(group1,group2,num):
    for i in range(num):
        e3 = enemy.BigEnemy(bg_size)
        group1.add(e3)
        group2.add(e3)



def main():
    
    pygame.mixer.music.play(-1)
    #生成我方飞机
    me = myplane.MyPlane(bg_size)
    #敌方飞机
    enemies = pygame.sprite.Group()
    #生成敌方小型飞机
    small_enemies = pygame.sprite.Group()
    add_small_enemies(small_enemies,enemies,15)
    #生成敌方中型飞机
    mid_enemies = pygame.sprite.Group()
    add_mid_enemies(mid_enemies,enemies,4)
    #生成敌方大型飞机
    big_enemies = pygame.sprite.Group()
    add_big_enemies(big_enemies,enemies,4)
    
    #中弹图片索引
    e1_destroy_index = 0
    e2_destroy_index = 0
    e3_destroy_index = 0
    me_destroy_index = 0
    



    #用于切换图片
    switch_image = True
    #用于延时
    delay = 0

    clock = pygame.time.Clock()

    while True:
        #退出游戏机制（先退出模块，后退出系统）
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        #检测用户的键盘操作（控制我方飞机）
        key_pressed = pygame.key.get_pressed()

        if key_pressed[K_w] or key_pressed[K_UP]:
            me.moveUp()
        if key_pressed[K_s] or key_pressed[K_DOWN]:
            me.moveDown()
        if key_pressed[K_a] or key_pressed[K_LEFT]:
            me.moveLeft()
        if key_pressed[K_d] or key_pressed[K_RIGHT]:
            me.moveRight()



        #绘制背景
        screen.blit(background,(0,0))
        #绘制大型敌机
        for each in big_enemies:
            if each.active:
                each.move()
                if switch_image:
                    screen.blit(each.image1,each.rect)
                else:
                    screen.blit(each.image2,each.rect)
                 #播放大型敌机出场音效
                #if each.rect.bottom > -50:
                    #enemy3_fly_sound.play()

            else:
                #毁灭飞机
                enemy3_down_sound.play()
                if not(delay % 3):
                    screen.blit(each.destroy_images[e3_destroy_index],each.rect)
                    e3_destroy_index = (e3_destroy_index + 1) % 6
                    if e3_destroy_index == 0:
                        each.reset()
                

                
       

        #绘制中型、小型飞机
        for each in mid_enemies:
            each.move()
            screen.blit(each.image,each.rect)

        for each in small_enemies:
            each.move()
            screen.blit(each.image,each.rect)

        #绘制我方飞机
        #通过switch方法来进行图片切换
        if switch_image:   
            screen.blit(me.image1,me.rect)
        else:
            screen.blit(me.image2,me.rect)
        #计算延时（用于我方飞机切换图片）
        delay += 1
        #当delay能被8整除的时候，就切换一下switch
        if not(delay % 8):
            switch_image = not switch_image
        
            
        
        pygame.display.flip()
        
        clock.tick(60)





if __name__ == '__main__':
    try:
        main()
    except SystemExit:
        pass
    except:
        traceback.print_exc()
        pygame.quit()
        input()

        


        


