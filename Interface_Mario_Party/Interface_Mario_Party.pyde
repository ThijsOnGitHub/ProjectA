from telScherm import *
from elementen import *
from Player_Select_Scherm import *
from Welk_Scherm import *
from shop_systeem import *
from kaart_systeem import *
from Opdracht_Scherm import *
from Winner_Systeem import *
def setup():
    global click
    click=False
    size(1820,1000)
    background("#FFFFFF")

def draw():
    if scherm()=="scoreBoard":
        background("#FFFFFF")
        scoreBoard(50,20,True)
        schermSwitch("scoreBoard1")
    elif scherm()=="scoreBoard1":
        scoreBoard(50,20,False)
    elif scherm()=="welkom":
        selectScherm(225,100)
    elif scherm()=="shopScherm":
        background("#FFFFFF")
        welkomShop(800,300)
    elif "shopVan" in scherm() and not("1" in scherm()):
        background("#FFFFFF")
        shopScherm(0,90,scherm().replace("shopVan",""),True)
    elif "shopVan" in scherm():
        background("#FFFFFF")
        shopScherm(0,90,scherm().replace("shopVan","").replace("1",""),False)
    elif scherm()=="vraagScherm":
        vraagScherm(800,300,True)
        schermSwitch("vraagScherm1")
    elif scherm()=="vraagScherm1":
        vraagScherm(800,300,False)
    elif scherm()=="antwoordScherm":
        antwoordScherm(800,300,True)
        schermSwitch("antwoordScherm1")
    elif scherm()=="antwoordScherm1":
        antwoordScherm(800,300,False)
    elif "InfoOverInteractieItem:" in scherm():
        shopItemInteractie(200,100,scherm().split("van")[0].replace("InfoOverInteractieItem:",""),scherm().split("van")[1],True)
    elif "InteractieItem:" in scherm():
        shopItemInteractie(200,100,scherm().split("van")[0].replace("InteractieItem:",""),scherm().split("van")[1].replace("InteractieItem:",""))
    elif scherm() == "opdrachtScherm":
        Opdracht_Scherm(500,300,True)
        schermSwitch("opdrachtScherm4")
    elif scherm() == "opdrachtScherm4":
        Opdracht_Scherm(500,300,False)
    elif scherm() == "opdrachtscherm1":
        background("#FFFFFF")
        opdrachtscherm1(500,300)
    elif scherm() == "opdrachtscherm2":
        background("#FFFFFF")
        opdrachtscherm2(500,300)
    elif scherm() =="winnerScreen":
        background("#FFFFFF")
        winnerScreen(0,0)
    elif scherm() == "end":
        pass
        
        
    
        
