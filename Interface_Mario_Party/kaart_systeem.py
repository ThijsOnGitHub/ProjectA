from Player_Select_Scherm import *
from elementen import *
from back_end_code import *
from Welk_Scherm import *
import random

laatsteVraag = ""

def loadJSON(file):
    return loadJSONObject(file)

def randomVraagNummer():
    global gebruiktenVragen
    global laatsteVraag
    vraagNummer = random.randint(1, 57)
    laatsteVraag = vraagNummer
    return vraagNummer
    
def vraagScherm(x,y,klaarmaken):
    if klaarmaken:
        background("#FFFFFF")
        img("Lucky Block",x,y-200,200,200)
        json = loadJSON("data/vragen.json")
        if randomVraagNummer:
            randomVraag = json.getJSONObject("vraag " + str(randomVraagNummer()))
            vraag = randomVraag.getString("vraag")
        
        text(vraag,x+100,y+100)
        
    button(x-40,y+300,40,140,[schermSwitch],[["antwoordScherm"]],"Antwoord")
    button(x+140,y+300,40,100,[schermSwitch],[["scoreBoard"]],"Terug")
    
def antwoordScherm(x,y,klaarmaken):
    if klaarmaken:
        background("#FFFFFF")
        json = loadJSON("data/vragen.json")
        randomVraag = json.getJSONObject("vraag " + str(laatsteVraag))
        antwoord = randomVraag.getString("antwoord")
        
        text("Juiste antwoord:",x+100,y-200)
        text(antwoord,x+100,y-150)
        text("Kies de winnaar:",x+100,y-80)
    
    button(x,y+300,40,200,[schermSwitch],[["scoreBoard"]],"Geen winnaar")
    uitslag=kiesUitSpelersRij(x+100,y,150,150,20,DATA_SPELERS.keys())
    if uitslag != None:
        DATA_SPELERS[uitslag]["coins"]+=10
        schermSwitch("scoreBoard")

   
