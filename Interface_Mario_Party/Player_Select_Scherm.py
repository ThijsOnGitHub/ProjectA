from elementen import *
from back_end_code import *
from telScherm import *
from Welk_Scherm import *
from shop_systeem import *
selectList=[]
showScoreBoard=False
showWelcome=True

melding=""


def selectSchermImg(personage,x,y,grootte):
    img(personage,x,y,grootte,grootte)
    clickArea(x,y,grootte,grootte,[select],[[personage]])
    if personage in selectList:
        img("Vinkje",x,y,grootte,grootte)
        
    


def selectScherm(x,y):
    background("#FFFFFF")
    textSize(30)
    textAlign(CENTER, CENTER)
    fill("#000000")
    text("Selecteer minimaal 2 spelers",x+1260//2,y+20)
    selectSchermImg("Blue Yoshi",x+100, y+100, 160)
    selectSchermImg("Luigi", x+300, y+100, 160)
    selectSchermImg("Mario", x+500, y+100, 160)
    selectSchermImg("Daisy", x+700, y+100, 160)
    selectSchermImg("Rosalie", x+900, y+100, 160)
    selectSchermImg("Waluigi", x+1100, y+100, 160)
    if scherm()=="welkom" and len(selectList)>1:
        button(x+(1260/2),y+400,50,150,[confirm],[[]],tekst="Doorgaan")
        
def select(personage):
    global selectList
    if personage in selectList:
        del selectList[selectList.index(personage)]
    else:
        selectList.append(personage)
        
def confirm():
    global DATA_SPELERS
    global showScoreBoard
    global showWelcome
    if len(selectList)>1:
        for personage in selectList:
            if personage=="Daisy":
                kleur="#c7a003"
            elif personage=="Mario":
                kleur="#a40006"
            elif personage=="Luigi":
                kleur="#587f30"
            elif personage=="Blue Yoshi":
                kleur="#4aa9e1"
            elif personage=="Waluigi":
                kleur="#553a5d"
            elif personage=="Rosalie":
                kleur="#ababab"
            DATA_SPELERS[personage]={"personage":personage,"kleur":kleur,"coins":0,"stars":0,"kaarten":[]}
        changeCoinPrice(len(DATA_SPELERS)*6)
        schermSwitch("scoreBoard")
    else:
        global melding
        melding="Je moet minimaal 2 personen selecteren"
