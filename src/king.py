from colorama import Back, Style
from src.input_ import get_input
from os import system

class king():
    def __init__(self, kx, ky):
        self.king_xcor = kx
        self.king_ycor = ky
        self.gree = Back.GREEN + ' ' + Style.RESET_ALL
        self.yell = Back.YELLOW + ' ' + Style.RESET_ALL
        self.blak = Back.BLACK + ' ' + Style.RESET_ALL
        self.rd = Back.RED + ' ' + Style.RESET_ALL

    def modify(self, kx, ky):
        self.king_xcor = kx
        self.king_ycor = ky

    def motion(self, ground):
        direction = get_input()
        if(direction == 'w' or direction == 'a' or direction == 's' or direction == 'd'):
            system("aplay -q ./src/strike.wav &")

        if(direction == 'w'):  
            ground.king_xcor = ground.king_xcor-1
            if(ground.king_ycor == ground.huts_ycor):
                # if(ground.king_xcor == ground.huts_xcor1):
                #     ground.king_xcor = ground.king_xcor + 1
                # elif(ground.king_xcor == ground.huts_xcor2):
                #     ground.king_xcor = ground.king_xcor + 1
                # elif(ground.king_xcor == ground.huts_xcor3):
                #     ground.king_xcor = ground.king_xcor + 1
                # elif(ground.king_xcor == ground.huts_xcor4):
                #     ground.king_xcor = ground.king_xcor + 1
                # elif(ground.king_xcor == ground.huts_xcor5):
                #     ground.king_xcor = ground.king_xcor + 1
                # elif(ground.king_xcor == ground.huts_xcor6):
                #     ground.king_xcor = ground.king_xcor + 1
                
                #############################################################

                for h in ground.huts_arr:
                    if(ground.king_xcor == h.xcor):
                        ground.king_xcor = ground.king_xcor + 1
                        break
                
                #############################################################

        elif(direction == 'a'):
            ground.king_ycor = ground.king_ycor - 1
            if(ground.king_ycor == ground.huts_ycor):
                # if(ground.king_xcor == ground.huts_xcor1):
                #     ground.king_ycor = ground.king_ycor + 1
                # elif(ground.king_xcor == ground.huts_xcor2):
                #     ground.king_ycor = ground.king_ycor + 1
                # elif(ground.king_xcor == ground.huts_xcor3):
                #     ground.king_ycor = ground.king_ycor + 1
                # elif(ground.king_xcor == ground.huts_xcor4):
                #     ground.king_ycor = ground.king_ycor + 1
                # elif(ground.king_xcor == ground.huts_xcor5):
                #     ground.king_ycor = ground.king_ycor + 1
                # elif(ground.king_xcor == ground.huts_xcor6):
                #     ground.king_ycor = ground.king_ycor + 1
                
                #############################################################

                for h in ground.huts_arr:
                    if(ground.king_xcor == h.xcor):
                        ground.king_ycor = ground.king_ycor + 1
                        break
                
                #############################################################

        elif(direction == 's'):
            ground.king_xcor = 1 + ground.king_xcor
            if(ground.king_ycor == ground.huts_ycor):
                # if(ground.king_xcor == ground.huts_xcor1):
                #     ground.king_xcor = ground.king_xcor - 1
                # elif(ground.king_xcor == ground.huts_xcor2):
                #     ground.king_xcor = ground.king_xcor - 1
                # elif(ground.king_xcor == ground.huts_xcor3):
                #     ground.king_xcor = ground.king_xcor - 1
                # elif(ground.king_xcor == ground.huts_xcor4):
                #     ground.king_xcor = ground.king_xcor - 1
                # elif(ground.king_xcor == ground.huts_xcor5):
                #     ground.king_xcor = ground.king_xcor - 1
                # elif(ground.king_xcor == ground.huts_xcor6):
                #     ground.king_xcor = ground.king_xcor - 1 
                
                #############################################################

                for h in ground.huts_arr:
                    if(ground.king_xcor == h.xcor):
                        ground.king_xcor = ground.king_xcor - 1
                        break
                
                #############################################################

        elif(direction == 'd'): 
            ground.king_ycor = 1 + ground.king_ycor
            if(ground.king_ycor == ground.huts_ycor):
                # if(ground.king_xcor == ground.huts_xcor1):
                #     ground.king_ycor = ground.king_ycor - 1
                # elif(ground.king_xcor == ground.huts_xcor2):
                #     ground.king_ycor = ground.king_ycor - 1
                # elif(ground.king_xcor == ground.huts_xcor3):
                #     ground.king_ycor = ground.king_ycor - 1
                # elif(ground.king_xcor == ground.huts_xcor4):
                #     ground.king_ycor = ground.king_ycor - 1
                # elif(ground.king_xcor == ground.huts_xcor5):
                #     ground.king_ycor = ground.king_ycor - 1
                # elif(ground.king_xcor == ground.huts_xcor6):
                #     ground.king_ycor = ground.king_ycor - 1   

                #############################################################

                for h in ground.huts_arr:
                    if(ground.king_xcor == h.xcor):
                        ground.king_ycor = ground.king_ycor - 1   
                        break
                
                #############################################################
            
        elif(direction == ' '):

            if(ground.king_xcor==ground.townhall_xcor+5 or ground.king_xcor==ground.townhall_xcor+7):
                if ground.king_ycor in range(ground.townhall_ycor-4,ground.townhall_ycor+5):
                        ground.wall1_col[-ground.townhall_ycor+4+ground.king_ycor]=self.blak

            if(ground.king_xcor==ground.townhall_xcor-5 or ground.king_xcor==ground.townhall_xcor-3):
                if ground.king_ycor in range(ground.townhall_ycor-4,ground.townhall_ycor+5):
                        ground.wall2_col[-ground.townhall_ycor+4+ground.king_ycor]=self.blak

            if(ground.king_ycor==ground.townhall_ycor-5 or ground.king_ycor==ground.townhall_ycor-3):
                if ground.king_xcor in range(ground.townhall_xcor-4,ground.townhall_xcor+6):
                        ground.wall3_col[-ground.townhall_xcor+4+ground.king_xcor]=self.blak

            if(ground.king_ycor==ground.townhall_ycor+3 or ground.king_ycor==ground.townhall_ycor+5):
                if ground.king_xcor in range(ground.townhall_xcor-4,ground.townhall_xcor+6):
                        ground.wall4_col[-ground.townhall_xcor+4+ground.king_xcor]=self.blak

            if(ground.king_xcor+1==ground.townhall_xcor or ground.king_xcor==ground.townhall_xcor+4):
                if(ground.king_ycor in range(ground.townhall_ycor,ground.townhall_ycor+3)):
                   
                          if(ground.townhall==self.gree):
                              ground.townhall=self.yell
                              
                          elif(ground.townhall==self.yell):
                              ground.townhall=self.rd
                          elif(ground.townhall==self.rd):
                              ground.townhall=self.blak
                              ground.townhall_xcor=-100

            elif(ground.king_ycor+1==ground.townhall_ycor or ground.king_ycor==ground.townhall_ycor+3):
                if(ground.king_xcor in range(ground.townhall_xcor,ground.townhall_xcor+4)):
                          if(ground.townhall==self.gree):
                              ground.townhall=self.yell
                          elif(ground.townhall==self.yell):
                              ground.townhall=self.rd
                          elif(ground.townhall==self.rd):
                              ground.townhall=self.blak
                              ground.townhall_xcor=-100

            if(ground.king_ycor == ground.huts_ycor):
                #############################################################

                for h in ground.huts_arr:
                    if(ground.king_xcor == h.xcor + 1 or ground.king_xcor == h.xcor - 1):
                        if(ground.king_life >= h.life):
                            h.life = h.life - ground.king_damage
                            if(h.life >= 10 and h.life <= 20):
                                h.color = self.gree
                            elif(h.life >= 4 and h.life <= 10):
                                h.color = self.yell
                            elif(h.life >= 0 and h.life <= 4):
                                h.color = self.rd
                            else: 
                                ground.king_xcor = h.xcor
                                h.color = self.blak
                                h.xcor = -100
                        break
                
                #############################################################
                # if(ground.king_xcor == ground.huts_xcor1 + 1 or ground.king_xcor == ground.huts_xcor1 - 1):
                #     if(ground.king_life >= ground.hut1_life):
                #         ground.hut1_life = ground.hut1_life - ground.king_damage
                #         if(ground.hut1_life >= 10 and ground.hut1_life <= 20):
                #             ground.hut1_color = self.gree
                #         elif(ground.hut1_life >= 4 and ground.hut1_life <= 10):
                #             ground.hut1_color = self.yell
                #         elif(ground.hut1_life >= 0 and ground.hut1_life <= 4):
                #             ground.hut1_color = self.rd
                #         else: 
                #             ground.king_xcor = ground.huts_xcor1
                #             ground.hut1_color = self.blak
                #             ground.huts_xcor1 = -100
                # elif(ground.king_xcor == ground.huts_xcor2 + 1 or ground.king_xcor == ground.huts_xcor2 - 1):
                #     if(ground.king_life >= ground.hut2_life):
                #         ground.hut2_life = ground.hut2_life - ground.king_damage
                #         if(ground.hut2_life >= 10 and ground.hut2_life <= 20):
                #             ground.hut2_color = self.gree
                #         elif(ground.hut2_life >= 4 and ground.hut2_life <= 10):
                #             ground.hut2_color = self.yell
                #         elif(ground.hut2_life >= 0 and ground.hut2_life <= 4):
                #             ground.hut2_color = self.rd
                #         else:
                #             ground.king_xcor = ground.huts_xcor2
                #             ground.hut2_color = self.blak
                #             ground.huts_xcor2 = -100
                # elif(ground.king_xcor == ground.huts_xcor3 + 1 or ground.king_xcor == ground.huts_xcor3 - 1):
                #     if(ground.king_life >= ground.hut3_life):
                #         ground.hut3_life = ground.hut3_life - ground.king_damage
                #         if(ground.hut3_life >= 10 and ground.hut3_life <= 20):
                #             ground.hut3_color = self.gree
                #         elif(ground.hut3_life >= 4 and ground.hut3_life <= 10):
                #             ground.hut3_color = self.yell
                #         elif(ground.hut3_life >= 0 and ground.hut3_life <= 4):
                #             ground.hut3_color = self.rd
                #         else:
                #             ground.king_xcor = ground.huts_xcor3
                #             ground.hut3_color = self.blak
                #             ground.huts_xcor3 = -100
                # elif(ground.king_xcor == ground.huts_xcor4 + 1 or ground.king_xcor == ground.huts_xcor4 - 1):
                #     if(ground.king_life >= ground.hut4_life):
                #         ground.hut4_life = ground.hut4_life - ground.king_damage
                #         if(ground.hut4_life >= 10 and ground.hut4_life <= 20):
                #             ground.hut4_color = self.gree
                #         elif(ground.hut4_life >= 4 and ground.hut4_life <= 10):
                #             ground.hut4_color = self.yell
                #         elif(ground.hut4_life >= 0 and ground.hut4_life <= 4):
                #             ground.hut4_color = self.rd
                #         else:
                #             ground.king_xcor = ground.huts_xcor4
                #             ground.hut4_color = self.blak
                #             ground.huts_xcor4 = -100
                # elif(ground.king_xcor == ground.huts_xcor5 + 1 or ground.king_xcor == ground.huts_xcor5 - 1):
                #     if(ground.king_life >= ground.hut5_life):
                #         ground.hut5_life = ground.hut5_life - ground.king_damage
                #         if(ground.hut5_life >= 10 and ground.hut5_life <= 20):
                #             ground.hut5_color = self.gree
                #         elif(ground.hut5_life >= 4 and ground.hut5_life <= 10):
                #             ground.hut5_color = self.yell
                #         elif(ground.hut5_life >= 0 and ground.hut5_life <= 4):
                #             ground.hut5_color = self.rd
                #         else:
                #             ground.king_xcor = ground.huts_xcor5
                #             ground.hut5_color = self.blak
                #             ground.huts_xcor5 = -100
                # elif(ground.king_xcor == ground.huts_xcor6 + 1 or ground.king_xcor == ground.huts_xcor6 - 1):
                #     if(ground.king_life >= ground.hut6_life):
                #         ground.hut6_life = ground.hut6_life - ground.king_damage
                #         if(ground.hut6_life >= 10 and ground.hut6_life <= 20):
                #             ground.hut6_color = self.gree
                #         elif(ground.hut6_life >= 4 and ground.hut6_life <= 10):
                #             ground.hut6_color = self.yell
                #         elif(ground.hut6_life >= 0 and ground.hut6_life <= 4):
                #             ground.hut6_color = self.rd
                #         else:
                #             ground.king_xcor = ground.huts_xcor6
                #             ground.hut6_color = self.blak
                #             ground.huts_xcor6 = -100
            elif(ground.king_ycor == ground.huts_ycor + 1 or ground.king_ycor == ground.huts_ycor - 1):
                #############################################################

                for h in ground.huts_arr:
                    if(ground.king_xcor == h.xcor):
                        if(ground.king_life >= h.life):
                            h.life = h.life - ground.king_damage
                            if(h.life >= 10 and h.life <= 20):
                                h.color = self.gree
                            elif(h.life >= 4 and h.life <= 10):
                                h.color = self.yell
                            elif(h.life >= 0 and h.life <= 4):
                                h.color = self.rd
                            else: 
                                ground.king_ycor = h.ycor
                                h.color = self.blak
                                h.xcor = -100
                        break
                
                #############################################################
                # if(ground.king_xcor == ground.huts_xcor1):
                #     if(ground.king_life >= ground.hut1_life):
                #         ground.hut1_life = ground.hut1_life - ground.king_damage
                #         if(ground.hut1_life >= 10 and ground.hut1_life <= 20):
                #             ground.hut1_color = self.gree
                #         elif(ground.hut1_life >= 4 and ground.hut1_life <= 10):
                #             ground.hut1_color = self.yell
                #         elif(ground.hut1_life >= 0 and ground.hut1_life <= 4):
                #             ground.hut1_color = self.rd
                #         else: 
                #             ground.king_ycor = ground.huts_ycor
                #             ground.hut1_color = self.blak
                #             ground.huts_xcor1 = -100
                # elif(ground.king_xcor == ground.huts_xcor2):
                #     if(ground.king_life >= ground.hut2_life):
                #         ground.hut2_life = ground.hut2_life - ground.king_damage
                #         if(ground.hut2_life >= 10 and ground.hut2_life <= 20):
                #             ground.hut2_color = self.gree
                #         elif(ground.hut2_life >= 4 and ground.hut2_life <= 10):
                #             ground.hut2_color = self.yell
                #         elif(ground.hut2_life >= 0 and ground.hut2_life <= 4):
                #             ground.hut2_color = self.rd
                #         else:
                #             ground.king_ycor = ground.huts_ycor
                #             ground.hut2_color = self.blak
                #             ground.huts_xcor2 = -100
                # elif(ground.king_xcor == ground.huts_xcor3):
                #     if(ground.king_life >= ground.hut3_life):
                #         ground.hut3_life = ground.hut3_life - ground.king_damage
                #         if(ground.hut3_life >= 10 and ground.hut3_life <= 20):
                #             ground.hut3_color = self.gree
                #         elif(ground.hut3_life >= 4 and ground.hut3_life <= 10):
                #             ground.hut3_color = self.yell
                #         elif(ground.hut3_life >= 0 and ground.hut3_life <= 4):
                #             ground.hut3_color = self.rd
                #         else:
                #             ground.king_ycor = ground.huts_ycor
                #             ground.hut3_color = self.blak
                #             ground.huts_xcor3 = -100
                # elif(ground.king_xcor == ground.huts_xcor4):
                #     if(ground.king_life >= ground.hut4_life):
                #         ground.hut4_life = ground.hut4_life - ground.king_damage
                #         if(ground.hut4_life >= 10 and ground.hut4_life <= 20):
                #             ground.hut4_color = self.gree
                #         elif(ground.hut4_life >= 4 and ground.hut4_life <= 10):
                #             ground.hut4_color = self.yell
                #         elif(ground.hut4_life >= 0 and ground.hut4_life <= 4):
                #             ground.hut4_color = self.rd
                #         else:
                #             ground.king_ycor = ground.huts_ycor
                #             ground.hut4_color = self.blak
                #             ground.huts_xcor4 = -100
                # elif(ground.king_xcor == ground.huts_xcor5):
                #     if(ground.king_life >= ground.hut5_life):
                #         ground.hut5_life = ground.hut5_life - ground.king_damage
                #         if(ground.hut5_life >= 10 and ground.hut5_life <= 20):
                #             ground.hut5_color = self.gree
                #         elif(ground.hut5_life >= 4 and ground.hut5_life <= 10):
                #             ground.hut5_color = self.yell
                #         elif(ground.hut5_life >= 0 and ground.hut5_life <= 4):
                #             ground.hut5_color = self.rd
                #         else:
                #             ground.king_ycor = ground.huts_ycor
                #             ground.hut5_color = self.blak
                #             ground.huts_xcor5 = -100
                # elif(ground.king_xcor == ground.huts_xcor6):
                #     if(ground.king_life >= ground.hut6_life):
                #         ground.hut6_life = ground.hut6_life - ground.king_damage
                #         if(ground.hut6_life >= 10 and ground.hut6_life <= 20):
                #             ground.hut6_color = self.gree
                #         elif(ground.hut6_life >= 4 and ground.hut6_life <= 10):
                #             ground.hut6_color = self.yell
                #         elif(ground.hut6_life >= 0 and ground.hut6_life <= 4):
                #             ground.hut6_color = self.rd
                #         else:
                #             ground.king_ycor = ground.huts_ycor
                #             ground.hut6_color = self.blak
                #             ground.huts_xcor6 = -100
        
        

        
        if(ground.king_xcor == ground.columns or ground.king_xcor==ground.rows):
            ground.king_xcor = 20
            ground.king_ycor = 150

        return direction