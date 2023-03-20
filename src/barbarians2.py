from colorama import Back, Style
from src.input_ import get_input
from os import system
import src.Ground

class Barbarians2():
    def __init__(self):
        self.gree = Back.GREEN + ' ' + Style.RESET_ALL
        self.yell = Back.YELLOW + ' ' + Style.RESET_ALL
        self.blak = Back.BLACK + ' ' + Style.RESET_ALL
        self.rd = Back.RED + ' ' + Style.RESET_ALL

        self.bar1_x = 3
        self.bar1_y = 120

        self.count_bar = 0
        self.start=-1
        self.wait1=0
        self.wait2=0
        self.check = 0
    def inc(self):
        inp = get_input()
        if(inp == 'c'):
            self.count_bar = self.count_bar + 1
            self.start=0


    def barbarian_moment(self,ground):
        for i in range(0, self.count_bar):
            if(i == 0):
              if(self.wait1==0):
                self.bar1_x = self.bar1_x + 1
                #############################################################

                    for h in ground.huts_arr:
                        if(h.xcor != -100 and self.bar1_x == h.xcor):
                            if(h.color == self.gree):
                                self.bar1_x -= 1
                                h.color = self.yell
                            elif(h.color == self.yell):
                                self.bar1_x -= 1
                                h.color = self.rd
                            elif(h.color == self.rd):
                                self.bar1_x -= 1
                                h.color = self.blak
                                h.xcor = -100
                            break
                    
                #############################################################
                
                if(ground.huts_xcor1 != -100 and self.bar1_x == ground.huts_xcor1):
                    if(ground.hut1_color == self.gree):
                        self.bar1_x -= 1
                        ground.hut1_color = self.yell
                        continue
                    elif(ground.hut1_color == self.yell):
                        self.bar1_x -= 1
                        ground.hut1_color = self.rd
                        continue
                    elif(ground.hut1_color == self.rd):
                        self.bar1_x -= 1
                        ground.hut1_color = self.blak
                        ground.huts_xcor1 = -100
                elif(ground.huts_xcor2 != -100 and self.bar1_x == ground.huts_xcor2):
                    if(ground.hut2_color == self.gree):
                        self.bar1_x -= 1
                        ground.hut2_color = self.yell
                        continue
                    elif(ground.hut2_color == self.yell):
                        self.bar1_x -= 1
                        ground.hut2_color = self.rd
                        continue
                    elif(ground.hut2_color == self.rd):
                        self.bar1_x -= 1
                        ground.hut2_color = self.blak
                        ground.huts_xcor2 = -100
                elif(ground.huts_xcor3 != -100 and self.bar1_x == ground.huts_xcor3):
                    if(ground.hut3_color == self.gree):
                        self.bar1_x -= 1
                        ground.hut3_color = self.yell
                        continue
                    elif(ground.hut3_color == self.yell):
                        self.bar1_x -= 1
                        ground.hut3_color = self.rd
                        continue
                    elif(ground.hut3_color == self.rd):
                        self.bar1_x -= 1
                        ground.hut3_color = self.blak
                        ground.huts_xcor3 = -100
                elif(ground.huts_xcor4 != -100 and self.bar1_x == ground.huts_xcor4):
                    if(ground.hut4_color == self.gree):
                        self.bar1_x -= 1
                        ground.hut4_color = self.yell
                        continue
                    elif(ground.hut4_color == self.yell):
                        self.bar1_x -= 1
                        ground.hut4_color = self.rd
                        continue
                    elif(ground.hut4_color == self.rd):
                        self.bar1_x -= 1
                        ground.hut4_color = self.blak
                        ground.huts_xcor4 = -100
                elif(ground.huts_xcor5 != -100 and self.bar1_x == ground.huts_xcor5):
                    if(ground.hut5_color == self.gree):
                        self.bar1_x -= 1
                        ground.hut5_color = self.yell
                        continue
                    elif(ground.hut5_color == self.yell):
                        self.bar1_x -= 1
                        ground.hut5_color = self.rd
                        continue
                    elif(ground.hut5_color == self.rd):
                        self.bar1_x -= 1
                        ground.hut5_color = self.blak
                        ground.huts_xcor5 = -100
                elif(ground.huts_xcor6 != -100 and self.bar1_x == ground.huts_xcor6):
                    if(ground.hut6_color == self.gree):
                        self.bar1_x -= 1
                        ground.hut6_color = self.yell
                        continue
                    elif(ground.hut6_color == self.yell):
                        self.bar1_x -= 1
                        ground.hut6_color = self.rd
                        continue
                    elif(ground.hut6_color == self.rd):
                        self.bar1_x -= 1
                        ground.hut6_color = self.blak
                        ground.huts_xcor6 = -100
                if(self.bar1_x >= 24):
                    self.check = 1
                if(self.check == 1):
                    self.bar1_y = self.bar1_y - 2
                    if(self.bar1_y == 100): # 18,100
                        self.bar1_y = self.bar1_y + 2
                        self.bar1_x = self.bar1_x - 2
                        if(self.bar1_x ==ground.townhall_xcor+5 or self.bar1_x == ground.townhall_xcor+7):
                            if self.bar1_y in range(ground.townhall_ycor-4,ground.townhall_ycor+5):
                                ground.wall1_col[-ground.townhall_ycor+4+self.bar1_y]=self.blak
                                self.bar1_x = self.bar1_x - 1
                        if(self.bar1_x==ground.townhall_xcor+4):
                          if(self.bar1_y in range(ground.townhall_ycor,ground.townhall_ycor+3)):
                            if(ground.townhall==self.gree):
                              ground.townhall=self.yell
                              self.bar1_x = self.bar1_x + 1
                              continue
                              
                            elif(ground.townhall==self.yell):
                              ground.townhall=self.rd
                              self.bar1_x = self.bar1_x + 1
                              
                              continue

                            elif(ground.townhall==self.rd):
                              ground.townhall=self.blak 
                              self.bar1_x = self.bar1_x + 1
                              continue 
                            elif(ground.townhall==self.blak):
                              self.bar1_x = self.bar1_x + 1
                              ground.townhall_xcor = -100
                              continue 