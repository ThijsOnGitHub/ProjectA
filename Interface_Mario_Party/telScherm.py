from elementen import *
from back_end_code import *
from Welk_Scherm import * 
from shop_systeem import *
mario=loadImage("Mario.png")

beurt=25
    
def aftellen():
    global beurt 
    beurt=beurt-1
    if beurt==0:
        schermSwitch("winnerScreen")
        

def telrij(x,y,personage,naam,klaarmaken):
    global DATA_SPELERS
    #textSize(30)
    #textAlign(LEFT,CENTER)
    #stroke("#FFFFFF")
    #fill("#FFFFFF")
    #rect(x+220,y,80,50)
    #fill("#050505")
    #text(DATA_SPELERS[naam]["coins"],x+220,y+10)
    refText2(DATA_SPELERS[naam]["coins"],x+220,y+10,80,30)
    #fill("#FFFFFF")
    #rect(x+720,y,80,50)
    #fill("#050505")
    refText2(DATA_SPELERS[naam]["stars"],x+720,y+10,70,30)
    #stroke("#000000")
    #buttons
    button(x+300,y,50,50,[coin_erbij],[(naam,-3)],"-3")
    button(x+360,y,50,50,[coin_erbij],[(naam,-1)],"-1")
    button(x+420,y,50,50,[coin_erbij],[(naam,1)],"+1")
    button(x+480,y,50,50,[coin_erbij],[(naam,5)],"+3")
    button(x+540,y,50,50,[coin_erbij],[(naam,5)],"+5")
    button(x+600,y,50,50,[coin_erbij],[(naam,10)],"+10")
    button(x+770,y,50,50,[star_erbij],[(naam,-1)],"-1")
    button(x+830,y,50,50,[koop_star],[[naam]],"+1")
    #button(x+970,y,50,50,[stelen],[[naam,20,"coin"]],"+20")
    #button(x+1030,y,50,50,[stelen],[[naam,1,"star"]],"+1")
    locatie=x+180
    for item in DATA_SPELERS[naam]["kaarten"]:
        shopItem(locatie,y+60,50,item,personage,klaarmaken)
        locatie+=60
    locatie = x+950
    for speler in DATA_SPELERS:
        if naam != speler:
            locatie += 60
            button(locatie,y,50,50,[steel_star],[[naam,speler,1]],"+1",buttonKleur=DATA_SPELERS[speler]["kleur"])
    locatie = x+950
    for speler in DATA_SPELERS:
        if naam != speler:
            locatie += 60
            button(locatie,y+60,50,50,[steel_coin],[[naam,speler,15]],"+15",buttonKleur=DATA_SPELERS[speler]["kleur"])
    #tekst
    #indicatoren
    #namen
    if klaarmaken:
        textAlign(LEFT,CENTER)
        text("Items:",x+100,y+80)
        imageMode(CORNER)
        textAlign(RIGHT,CENTER)
        text(naam,x+90,y+20)   
        img(personage,x+100,y,50,50)
        img("Coin",x+160,y,50,50)
        img("Star",x+660,y,50,50)
        img("Boo Star",x+930,y,50,50)
        img("Boo Coin",x+930,y+60,50,50)
        
def scoreBoard(x,y,klaarmaken):
    if klaarmaken:
        background("#FFFFFF")
        textSize(30)
        textAlign(CENTER,TOP)
        fill("#050505")
        text("Score Board",x+1260/2,y)
    global DATA_SPELERS
    global beurt
    y+=50
    for naam in DATA_SPELERS:
        telrij(x,y,DATA_SPELERS[naam]["personage"],naam,klaarmaken)
        y+=120
    melding(x,y+10)
    stroke("#030303")
    button(x+(1000//2),y+100,50,100,[schermSwitch],[["shopScherm"]],tekst="Shop")
    button(x+(1000//2+150),y+100,50,100,[schermSwitch],[["vraagScherm"]],tekst="Vraag")
    button(x+(1000//2+300),y+100,50,130,[schermSwitch],[["opdrachtScherm"]],tekst="Opdracht")
    if klaarmaken:
        text("klik hier aan het eind van elke ronde", x+200,y+180) 
    button(x+150,y+100,50,50,[aftellen],[[]],tekst=beurt)

        
def shopItem(x,y,groote,item,personage,klaarmaken):
    if klaarmaken:
        imageMode(CORNER)
        img(item,x,y,groote,groote)
    clickArea(x,y,groote,groote,[schermSwitch],[["InteractieItem:"+item+"van"+personage]])
    

    
    
