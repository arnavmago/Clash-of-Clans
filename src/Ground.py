from colorama import Fore, Back, Style
from os import system
import math
from src.king import king
from src.barbarians import Barbarians
from src.barbarians1 import Barbarians1
from src.barbarians2 import Barbarians2
from src.hut import hut
from src.cannon import cannon
import os


class Village:
    def __init__(self):
        self.columns = 200
        self.rows = 45
        self.use=str(len(os.listdir("replays")) + 1)

        self.townhall_xcor = int(self.rows / 2)
        self.townhall_ycor = int(self.columns / 2)
        self.ongoing = 1

        # canons
        # self.cx1 = 30
        # self.cy1 = 50
        # self.cx2 = 30
        # self.cy2 = 180
        # self.cdamage = 1
        # self.crange = 3
        self.kingh = 20

        # spawning need to be done

        # self.huts_xcor1 = 4
        # self.huts_xcor2 = 8
        # self.huts_xcor3 = 12
        # self.huts_xcor4 = 16
        # self.huts_xcor5 = 20
        # self.huts_xcor6 = 24

        # self.huts_ycor = 120

        # self.hut_maxlife = 20
        # self.hut1_life = 20
        # self.hut2_life = 20
        # self.hut3_life = 20
        # self.hut4_life = 20
        # self.hut5_life = 20
        # self.hut6_life = 20

        self.background = Back.BLACK + " " + Style.RESET_ALL
        self.huts = Back.GREEN + " " + Style.RESET_ALL
        self.townhall = Back.GREEN + " " + Style.RESET_ALL
        self.cannon = Back.BLUE + " " + Style.RESET_ALL
        self.kingcolor = Back.MAGENTA + " " + Style.RESET_ALL
        self.spawning = Back.RED + " " + Style.RESET_ALL
        self.townwall = Back.WHITE + " " + Style.RESET_ALL

        # self.hut1_color = self.huts
        # self.hut2_color = self.huts
        # self.hut3_color = self.huts
        # self.hut4_color = self.huts
        # self.hut5_color = self.huts
        # self.hut6_color = self.huts

        #############################################################

        self.huts_arr = []

        for i in range(6):
            h = hut((i+1)*4,120,20,self.huts)
            self.huts_arr.append(h)
        
        self.cannons_arr = []
        cannon1 = cannon(30,50,1,3)
        cannon2 = cannon(30,180,1,3)

        self.cannons_arr.append(cannon1)
        self.cannons_arr.append(cannon2)
        
        #############################################################

        self.wall1_col = []
        self.wall2_col = []
        self.wall3_col = []
        self.wall4_col = []

        for i in range(9):
            self.wall1_col.append(self.townwall)
            self.wall2_col.append(self.townwall)

        for i in range(10):
            self.wall3_col.append(self.townwall)
            self.wall4_col.append(self.townwall)

        # connons need to be done

        self.king_xcor = 20
        self.king_ycor = 150
        self.king_life = 40
        self.king_damage = 4
        self.king = king(self.king_xcor, self.king_ycor)
        self.barbarians = Barbarians()
        self.barbarians1 = Barbarians1()
        self.barbarians2 = Barbarians2()

        self.win = 0

        self.render()

    def render(self):
        system("clear")

        self.ground = [
            [self.background for i in range(self.columns)] for j in range(self.rows)
        ]
        for i in range(0, 4):
            for j in range(0, 3):
                self.ground[self.townhall_xcor + i][
                    self.townhall_ycor + j
                ] = self.townhall


        # self.ground[self.cx1][self.cy1] = self.cannon
        # self.ground[self.cx2][self.cy2] = self.cannon


        #############################################################

        for c in self.cannons_arr:
            self.ground[c.xcor][c.ycor] = self.cannon

        #############################################################

        # for i in range(0, 1):
        #     for j in range(0, 1):
        #         if self.huts_xcor1 != -100:
        #             self.ground[self.huts_xcor1 + i]
        #                 self.huts_ycor + j
        #             ] = self.hut1_color
        #         if self.huts_xcor2 != -100:
        #             self.ground[self.huts_xcor2 + i][
        #                 self.huts_ycor + j
        #             ] = self.hut2_color
        #         if self.huts_xcor3 != -100:
        #             self.ground[self.huts_xcor3 + i][
        #                 self.huts_ycor + j
        #             ] = self.hut3_color
        #         if self.huts_xcor4 != -100:
        #             self.ground[self.huts_xcor4 + i][
        #                 self.huts_ycor + j
        #             ] = self.hut4_color
        #         if self.huts_xcor5 != -100:
        #             self.ground[self.huts_xcor5 + i][
        #                 self.huts_ycor + j
        #             ] = self.hut5_color
        #         if self.huts_xcor6 != -100:
        #             self.ground[self.huts_xcor6 + i][
        #                 self.huts_ycor + j
        #             ] = self.hut6_color
        
        #############################################################

        for h in self.huts_arr:
            if(h.xcor != -100):
                self.ground[h.xcor][h.ycor] = h.color
                print(h.xcor,end=" ")
                print(h.ycor)

        #############################################################

        for i in range(0, 9):
            # if(self.ground[self.townhall_xcor + 6][self.townhall_ycor -4 + i] ==self.wall1_col[i]):
            self.ground[self.townhall_xcor + 6][
                self.townhall_ycor - 4 + i
            ] = self.wall1_col[i]
            self.ground[self.townhall_xcor - 4][
                self.townhall_ycor - 4 + i
            ] = self.wall2_col[i]

        for i in range(0, 10):
            self.ground[self.townhall_xcor - 4 + i][
                self.townhall_ycor - 4
            ] = self.wall3_col[i]
            self.ground[self.townhall_xcor - 4 + i][
                self.townhall_ycor + 4
            ] = self.wall4_col[i]

        self.ground[self.king_xcor][self.king_ycor] = self.kingcolor
        if self.barbarians.start == 0:
            self.barbarians.barbarian_moment(self)
        if self.barbarians1.start == 0:
            self.barbarians1.barbarian_moment(self)
        if self.barbarians2.start == 0:
            self.barbarians2.barbarian_moment(self)

        if self.barbarians.count_bar >= 1:
            self.ground[self.barbarians.bar1_x][self.barbarians.bar1_y] = self.townhall
        if self.barbarians1.count_bar >= 1:
            self.ground[self.barbarians1.bar1_x][
                self.barbarians1.bar1_y
            ] = self.townhall
        if self.barbarians2.count_bar >= 1:
            self.ground[self.barbarians2.bar1_x][
                self.barbarians2.bar1_y
            ] = self.townhall

        # game endings
        count = 1
        # for i in range(0,4):
        #     for j in range(0,3):
        #         if(self.ground[self.townhall_xcor + i][self.townhall_ycor + j] !=self.background):
        #             count=0

        # if self.huts_xcor1 != -100:
        #     count = 0
        # if self.huts_xcor1 != -100:
        #     count = 0
        # if self.huts_xcor3 != -100:
        #     count = 0
        # if self.huts_xcor4 != -100:
        #     count = 0
        # if self.huts_xcor5 != -100:
        #     count = 0
        # if self.huts_xcor6 != -100:
        #     count = 0

        #############################################################

        for h in self.huts_arr:
            if(h.xcor != -100):
                count = 0

        #############################################################

        # if (self.king_xcor - self.cx1) ** 2 + (
        #     self.king_ycor - self.cy1
        # ) ** 2 < self.crange**2:
        #     self.kingh -= self.cdamage

        # if (self.king_xcor - self.cx2) ** 2 + (
        #     self.king_ycor - self.cy2
        # ) ** 2 < self.crange**2:
        #     self.kingh -= self.cdamage
        
        #############################################################

        for c in self.cannons_arr:
            if (self.king_xcor - c.xcor) ** 2 + (self.king_ycor - c.ycor) ** 2 < c.range**2:
                self.kingh -= c.damage

        #############################################################

        title = "Health Bar"
        for j in range(0, len(title)):
            self.ground[40][20+ j] = (
                Back.LIGHTBLUE_EX + Fore.WHITE + title[j] + Style.RESET_ALL)
        
        for i in range(self.kingh):
            self.ground[41][14 + i] = self.spawning

        if count == 1 and self.townhall_xcor == -100:
            self.ongoing = 0
            self.win = 1

        if self.kingh <= 0:
            self.win = 0
            self.ongoing = 0

        self.output="\n".join(["".join(row) for row in self.ground])
        print(self.output)
     

       
        repfile = "replays/replay" + self.use + ".txt"
        with open(repfile, "a+") as file:
            for i in self.output:
                for j in i:
                    file.write(j)
            file.write("\n")
            file.write("format\n")


        