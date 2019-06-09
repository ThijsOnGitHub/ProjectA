from Player_Select_Scherm import *
from elementen import *
from back_end_code import *
from Welk_Scherm import *
from random import *

global teken
global uitbeeld
opdrachten = ['Starwars','Lord of the rings','Shrek','Wolf of wallstreet','Deadpool','Angry Birds','Spiderman homecoming','Avengers infinity war','Ezel','Varken','Dinosaurus','Kip','Konijn','Mol','Schaap','Beer','Games','Mario Kart','Mario Party','Pacman','H1z1','Fortnite','Pubg']
def welkekiesik():
    typetjes = ('Uitbeelden','Tekenen')
    type = choice(typetjes)
    return type
def welkekiesik2():
    global opdrachten
    opdracht = choice(opdrachten)
    return opdracht
def Opdracht_Scherm(x,y,klaarmaken):
    if klaarmaken:
        background("#FFFFFF") 
        img("mario-pose3",x+270,y-200,200,200)
        text(welkekiesik(),x+330,y+50)
        text(welkekiesik2(),x+330,y+100)
    button(x+100,y+150,40,200,[schermSwitch],[["scoreBoard"]],"Geen winnaar")
    button(x+400,y+150,40,200,[schermSwitch],[["opdrachtscherm1"]],"Kies winnaars")


def opdrachtscherm1(x,y):
    text("Kies winnaar: Uitbeelder/Tekenaar",x+330,y-100)
    button(x+250,y+150,40,200,[schermSwitch],[["scoreBoard"]],"Geen winnaar")
    uitslag=kiesUitSpelersRij(x+335,y-50,150,150,20,DATA_SPELERS.keys())
    if uitslag != None:
        DATA_SPELERS[uitslag]["coins"]+=8
        schermSwitch("opdrachtscherm2")
def opdrachtscherm2(x,y):
    text("Kies winnaar: Rader",x+330,y-100)
    button(x+250,y+150,40,200,[schermSwitch],[["scoreBoard"]],"Geen winnaar")
    uitslag=kiesUitSpelersRij(x+335,y-50,150,150,20,DATA_SPELERS.keys())
    if uitslag != None:
        DATA_SPELERS[uitslag]["coins"] += 10
        schermSwitch("scoreBoard")
