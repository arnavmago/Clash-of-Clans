from src.input_ import *
from src.Ground import Village
from os import system
from src.king import king
from src.barbarians import Barbarians
from src.barbarians1 import Barbarians1
from src.barbarians2 import Barbarians2

village = Village()
comp=0
while(village.ongoing):
    inp = village.king.motion(village)
    barbarian = village.barbarians.inc()
    barbarian1 = village.barbarians1.inc()
    barbarian2 = village.barbarians2.inc()

    print(inp)
    if(inp == 'q'):
        system("clear")
        comp=1
        break
    else:
        village.render()
if(comp==1):
    print("Game is paused")
elif(village.win==0):
    print("Defeat")
elif(village.win==1):
    system("clear")
    print("Victory")    