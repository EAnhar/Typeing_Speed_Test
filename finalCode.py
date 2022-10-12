import sys
import time
import random
import pygame 
from pygame.locals import *

# Fonts:
titleFont = 'fonts/simpfxo.ttf'
TjLight = 'fonts/Tajawal-Light.ttf'
TjReg = "fonts/Tajawal-Regular.ttf"
TjBold = 'fonts/Tajawal-Bold.ttf'
#  
class Test():
   
    def __init__(self):
        self.color_heading = (255,213,102)
        self.color_text = (255,0,0)
        self.color_results = (255,70,70)
        self.w=750
        self.h=500
        self.reset=True
        self.wpm = 0
        self.end = False
        self.active = False
        self.input_text=''
        self.word = ''
        self.results = ' '
        self.start_time = 0
        self.overall_time = 0
        self.accuracy = ' '
        
        
       
        pygame.init()
        self.image_open = pygame.image.load('imgs/startBG.jpg')
        self.image_open = pygame.transform.scale(self.image_open, (self.w,self.h))


        self.bg = pygame.image.load('imgs/mainBG.jpg')
        self.bg = pygame.transform.scale(self.bg, (750,500))

        self.screen = pygame.display.set_mode((self.w,self.h))
        pygame.display.set_caption('Typing Speed Test')
        
        programIcon = pygame.image.load('icons/logo.png')
        pygame.display.set_icon(programIcon)
       
        
    def draw_text(self, screen, message, x_val, y_val ,f_size, color, fontF):
        font = pygame.font.Font(fontF, f_size)
        text = font.render(message, 5, color)
        text_rect = text.get_rect(topleft=(x_val, y_val-20))
        # text_rect = text.get_rect(start = (self.w/4, y_val))
        screen.blit(text, text_rect)
        pygame.display.update()
        
    def get_challenge(self,level):
        return random.choice(open(f'Levels/{level}').read().split('\n'))

    def results_show(self, screen):
        if(not self.end):
            # Calculate time ellapsed 
            self.overall_time = time.time() - self.start_time                
            count = 0
            for i,c in enumerate(self.word):
                try:
                    if self.input_text[i] == c:
                        count = count + 1
                except:
                    pass
            # count is the number of correct typed characters 
            # Calculate accuracy using given formula
            self.accuracy = (count*100)/len(self.word)
           
            #Calculate Words per Minute
            self.wpm = (len(self.input_text)*60)/(5*self.overall_time)
            self.end = True
            print(self.overall_time)
            
            timeIcon = pygame.image.load('icons/time.png')
            timeIcon = pygame.transform.scale(timeIcon, (23, 26))
            screen.blit(timeIcon, (85, 358))
            
            accIcon = pygame.image.load('icons/Acc.png')
            accIcon = pygame.transform.scale(accIcon, (23, 26))
            screen.blit(accIcon, (85, 395))
            
            self.draw_text(screen,"Time: ", 115, 377, 18, "black", TjLight)
            self.draw_text(screen,str(round(self.overall_time))+" sec", 165, 377, 18, "black", TjBold)
            self.draw_text(screen,"Accuracy: ", 115, 412, 18, "black", TjLight)
            self.draw_text(screen,str(round(self.accuracy)) + " %", 195, 412, 18, "black", TjBold)
            self.draw_text(screen,"Word Per Minutes:", 85, 445, 18, "black", TjLight)
            self.draw_text(screen,str(round(self.wpm)), 230, 445, 18, "black", TjBold)
                
            # Draw Icon image
            self.time_img = pygame.image.load("icons/restart.png")
            self.time_img = pygame.transform.scale(self.time_img, (30, 30))
            screen.blit(self.time_img, (355.5, 15))
            
            print(self.results)
            pygame.display.update()

    def run(self,level):
        # everytime we run it should automatically reset the variables
        self.reset_game(level)
    
        # a variable which shows the state of game whether
        # it is running or not
        self.running=True
        
        # we will run an infinite loop till the running is True
        while(self.running):
            clock = pygame.time.Clock()
            self.screen.fill((0,0,0), (50,250,650,50))
            pygame.draw.rect(self.screen, "white", (50,250,650,50))
            r = Rect(75, 172, 601, 47)
            pygame.draw.rect(self.screen, (100, 160, 214), r, 5)
            r2 = Rect(75, 261, 601, 47)
            pygame.draw.rect(self.screen, (100, 160, 214), r2, 2)
            # Update the text of user input dynamically
            self.draw_text(self.screen, self.input_text, 85, 290, 18,(0,0,0), TjReg)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == QUIT:
                    self.running = False
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONUP:
                    # get the position of mouse pointer x,y
                    x,y = pygame.mouse.get_pos()
                    
                    # position of input box
                    # these x and y values should lie as 
                    # x = [50,650] and y = [250,300] because the timer 
                    # will start when user clicks the input box
                    
                    if(x>=50 and x<=650 and y>=250 and y<=300):
                        self.active = True
                        self.input_text = ''
                        self.start_time = time.time() 
                    
                    # position of reset box
                    if(x>=300 and x<=390 and y<=30 and self.end):
                        self.reset_game(level)
                        x,y = pygame.mouse.get_pos()
         
                        
                elif event.type == pygame.KEYDOWN:
                    if self.active and not self.end:
                        if event.key == pygame.K_RETURN:
                            print(self.input_text)
                            self.results_show(self.screen)
                            print(self.results)
                            self.draw_text(self.screen, self.results, 85, 350, 28, self.color_results, TjBold)  
                            self.end = True
                        
                        # event handler for backspace
                        # i.e simply take the string upto the second last character
                        elif event.key == pygame.K_BACKSPACE:
                            self.input_text = self.input_text[:-1]
                        else:
                            try:
                                self.input_text += event.unicode
                            except:
                                pass
            
            pygame.display.update()
        # clock timer
        clock.tick(60)

    def reset_game(self,level):
        self.screen.blit(self.image_open, (0,0))

        pygame.display.update()
        time.sleep(1)
        
        # reset all the project variables.
        self.reset=False
        self.end = False

        self.input_text=''
        self.word = ''
        self.start_time = 0
        self.overall_time = 0
        self.wpm = 0
 
        self.word = self.get_challenge(level)
        if (not self.word): self.reset_game(level)
                   
        self.screen.fill((0,0,0))
        self.screen.blit(self.bg,(0,0))
        message = "TYPING SPEED TEST"
        self.draw_text(self.screen, message,65, 80, 60,"black", titleFont)  
        self.draw_text(self.screen, self.word, 85, 210, 18,'Black', TjReg)
        
        pygame.display.update()