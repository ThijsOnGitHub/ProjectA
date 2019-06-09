from elementen import *
from back_end_code import *
from Welk_Scherm import *
import random
kaartenInShop=[]
coinStealPrijzen={}

ShowTheLuck=False
coinsGewonnen=0

def LuckyBlock(x,y,personage):
    button(x+1400//2-190//2,y+600,50,190,[DATA_SPELERS[personage]["kaarten"].remove,schermSwitch,setPrijs],[["Lucky Block"],["InteractieItem:"+"Lucky Block1"+"van"+personage],[]],tekst="In je prijs",tekstKleur="#000000")
    button(x+1400//2-190//2,y+700,50,190,[schermSwitch],[["scoreBoard"]],tekst="Annuleren",tekstKleur="#000000")
   
def setPrijs():
    global coinsGewonnen
    coinsGewonnen=random.randint(0,1)
    if coinsGewonnen==1:
        coinsGewonnen=30
        
def LuckyBlock1(x,y,personage):
    if coinsGewonnen==0:
        Items["Lucky Block1"]["tekst"]="Helaas je hebt geen Coins Gewonnen"
    else:
        Items["Lucky Block1"]["tekst"]="Je hebt "+str(coinsGewonnen)+" coins gewonnen!"
    button(x+1400//2-190//2,y+700,50,190,[coin_erbij,schermSwitch],[[personage,coinsGewonnen],["scoreBoard"]],tekst="In het geld",tekstKleur="#000000")
    
    
def starTrap(x,y,personage):
    textAlign(CENTER,CENTER)
    fill("#000000")
    textSize(20)
    text("Tik hieronder de persoon aan die is getrapped",x+1400//2,y+570)
    uitkomst=kiesUitSpelersRij(x+1400//2,y+620,50,50,10,set(DATA_SPELERS.keys())-{personage})
    if uitkomst!=None:
        if DATA_SPELERS[uitkomst]["stars"]<=0:
            changeMel("Helaas je trap is geactiveerd door iemand zonder Stars")
        else:
            star_erbij(uitkomst,-1)
            star_erbij(personage,1)
        DATA_SPELERS[personage]["kaarten"].remove("Star Trap")
        schermSwitch("scoreBoard")
    button(x+1400//2-190//2,y+700,50,190,[schermSwitch],[["scoreBoard"]],tekst="Annuleren",tekstKleur="#000000")
    
def coinSteal(x,y,personage):
    button(x+1400//2+190-190//2,y+700,50,190,[DATA_SPELERS[personage]["kaarten"].remove,schermSwitch],[["Coin Steal"],["InteractieItem:"+"Coin Steal1"+"van"+personage]],tekst="Kaart inzetten",tekstKleur="#000000")
    button(x+1400//2-190-190//2,y+700,50,190,[schermSwitch],[["scoreBoard"]],tekst="Annuleren",tekstKleur="#000000")
    
def aantalCoinsPrijs(persoon):
    global coinStealPrijzen
    coinStealPrijzen[persoon]=random.randint(1,6)*2
        
def steelAlleCoins(persoon):
    global coinStealPrijzen
    for personage in coinStealPrijzen.keys():
        steel_coin(persoon,personage,coinStealPrijzen[personage])
        print(persoon,personage,coinStealPrijzen[personage])
        del coinStealPrijzen[personage]
    
    
def coinSteal1(x,y,personage):
    global coinStealPrijzen 
    x1=x+1400//2
    y1=y+500
    breedte=50
    hoogte=50
    tussenRuimte=10
    imageMode(CORNER)
    uitslag=kiesUitSpelersRij(x1,y1,breedte,hoogte,tussenRuimte,set(DATA_SPELERS.keys())-{personage})
    totaalLen=(len(set(DATA_SPELERS.keys())-{personage})*(breedte+tussenRuimte))-tussenRuimte
    x1=x1-totaalLen//2
    if uitslag!=None and not(uitslag in  coinStealPrijzen.keys() ) :
        aantalCoinsPrijs(uitslag)
    for item in set(DATA_SPELERS.keys())-{personage}:
        textAlign(CENTER,TOP)
        textSize(30)
        if item in coinStealPrijzen:
            text(coinStealPrijzen[item],x1+25,y1+70)
        x1+=breedte+tussenRuimte
    if (len(DATA_SPELERS)-1)==len(coinStealPrijzen):
        som=0
        for i in coinStealPrijzen.values():
            som+=i
        text("Dat is in totaal "+str(som)+" coins voor "+personage ,x+1400//2,y+620)
        button(x+1400//2-200//2,y+700,50,200,[steelAlleCoins,schermSwitch],[[personage],["scoreBoard"]],tekst="Steel alle Coins",tekstKleur="#000000")


    
       
    
    
    

Items={"Star Trap":{"prijs":20,"aantal":2,"extra":starTrap,"tekst":"Deze val mag ergens op de map gelegd worden op een bepaalde tegel.\n Als een speler hierop komt wordt een van zijn sterren aan de aankoper van deze val gegeven.\n Deze val kan 1x geactiveerd worden en wordt daarna van het bord verwijderd. \n"},
       "Lucky Block":{"prijs":10,"tekst":"Bij het luckyblock heb je een 50 procent kans om 30 coins te krijgen.\n Je klikt op de knop om te kijken of je je 30 wint coins." ,"extra":LuckyBlock},
       "Freeze Ray":{"prijs":15,"tekst":"Met dit Item kun je een speler die je zelf kiest een beurt laten vastvriezen\n (wat dus betekent dat de speler de volgende beurt overslaat).\n Deze speler moet elke beurt de dobbelsteen gooien om\n uit deze bevriezing te komen.\n Als de Speler 3 of hoger gooit mag de speler volgende beurt weer lopen.\n Zo niet mag de speler het de volgende beurt weer proberen."},
       "Coin Steal":{"prijs":10000,"tekst":"Alle spelers behalve jij moeten een dobbelsteen gooien.\n Het aantal ogen x2 is het aantal coins dat je moet afgeven aan de Koper van dit Item.","extra":coinSteal},
       "Double Roll":{"prijs":5,"tekst":"Wanneer je dit item inzet mag je 2 dobbelstenen gooien in plaats van 1 je volgende beurt."},
       "Teleporter":{"prijs":5,"tekst":"Teleporteer naar de start."},
       "Reverse Roll":{"prijs":10,"tekst":"Na een opdracht heb je de mogelijkheid dit item in te zetten (voor iedereen heeft gegooid).\n Wanneer je dit item inzet moet iedereen behalve de persoon die dit item heeft\n ingezet plaatsen teruglopen in plaats van vooruit."},
       "Shield":{"prijs":20,"tekst":"Je bent immuun voor het eerst volgende negatieve shop item of ongelukstegel of coinsteal.\n (Na het gebruik verlies je het shield)"},
       "Lucky Block1":{"NewName":"Lucky Block","prijs":0,"tekst":"","extra":LuckyBlock1},
       "Coin Steal1":{"NewName":"Coin Steal","prijs":0,"tekst":"Dit is de prijs die iedereen moet betalen aan de eigenaar van de kaart","extra":coinSteal1}}

fakeItems={"Lucky Block1":{"image":"Coin"},"Coin Steal1":{"image":"Coin"}}

def changeCoinPrice(input):
    global Items
    Items["Coin Steal"]["prijs"]=input
    
 
def welkomShop(x,y):
    global kaartenInShop
    global fakeItems
    text("Kies je karakter",x,y-50)
    uitslag=kiesUitSpelersRij(x,y,150,150,20,DATA_SPELERS.keys())
    if uitslag != None:    
        #kaarten=["Coin Steal","Double Roll","Freeze Ray","Lucky Block","Reverse Roll","Shield","Star Trap","Teleporter"]
        if Items["Star Trap"]["aantal"]==0:
            fakeItems["Star Trap"]={"image":"Coin"}
        elif "Star Trap" in fakeItems.keys():
            del fakeItems["Star Trap"]
        kaartenInShop=random.sample(set(Items.keys())-set(fakeItems.keys()), 3)
        schermSwitch("shopVan"+uitslag)


def kaart(x,y,kaart,personage,klaarmaken):
    global DATA_SPELERS
    if klaarmaken:
        breedte=300
        stroke("#030303")
        fill("#FFFFFF")
        rect(x,y,300,500,20)
        textAlign(CENTER,CENTER)
        fill("#000000")
        textSize(30)
        text(kaart,x+breedte//2,y+40)
        imageMode(CENTER)
        img(kaart,x+breedte//2,y+200,250,250)
        text(str(Items[kaart]["prijs"])+" coins",x+breedte//2,y+350)
        button(x+300//2-50//2,y+380,50,50,[schermSwitch],[["InfoOverInteractieItem:"+kaart+"van"+personage]],tekst="?",tekstKleur="#000000")
    if Items[kaart]["prijs"]>DATA_SPELERS[personage]["coins"]:
        button(x+25,y+440,40,250,[],[[]],"Niet genoeg Coins",buttonOverKleur="#FF0000")
    else:
        button(x+100,y+440,40,100,[coin_erbij,lambda x:DATA_SPELERS[x]["kaarten"].append(kaart),schermSwitch,aantalStarTrapVeranderd],[[personage,Items[kaart]["prijs"]*-1],[personage],["scoreBoard"],[-1,kaart]],"Kopen")

def aantalStarTrapVeranderd(aantal,item):
    if item=="Star Trap":
        global Items
        Items["Star Trap"]["aantal"]+=aantal
    

def shopScherm(x,y,personage,klaarmaken):
    if klaarmaken:
        img(personage,x+800,y,70,70)
        text("Coins:"+str(DATA_SPELERS[personage]["coins"]),x+800,y+70)
        lengte=len(DATA_SPELERS[personage]["kaarten"])*60+35
        text("Items:",x+800-lengte/2,y+120)
        locatie=x+800-lengte/2+40
        for item in DATA_SPELERS[personage]["kaarten"]:
            shopItem(locatie,y+100,50,item,personage)
            locatie+=60
    button(x+600+200,y+750,40,100,[schermSwitch],[["scoreBoard"]],"Terug")
    x=x+300
    for item in kaartenInShop:
        kaart(x,y+150,item,personage,klaarmaken)
        x+=400
        
def shopItem(x,y,groote,item,personage):
    imageMode(CORNER)
    img(item,x,y,groote,groote)
    
#shop items iteractie

def shopItemInteractie(x,y,item,personage,onlyInfo=False):
    fill("#FFFFFF")
    rect(x,y,1400,800,20)
    textAlign(CENTER,CENTER)
    textSize(30)
    fill("#000000")
    imageMode(CENTER)
    if item in fakeItems:
        if "image" in fakeItems[item].keys():
            img(fakeItems[item]["image"],x+1400//2,y+250,200,200)
        if "NewName" in Items[item].keys():
            text(Items[item]["NewName"],1400//2+x,y+50)
        else:
            text(item,1400//2+x,y+50)
    else:
        text(item,1400//2+x,y+50)
        img(item,x+1400//2,y+250,200,200)
    textAlign(CENTER,TOP)
    textSize(30)
    text(Items[item]["tekst"],x+1400//2,y+400)
    textAlign(CENTER,CENTER)
    if onlyInfo:
        button(x+1400//2-190//2,y+700,50,190,[schermSwitch],[["shopVan"+personage]],tekst="Sluiten",tekstKleur="#000000")
    else:
        if "extra" in Items[item].keys():
            Items[item]["extra"](x,y,personage)
        else:
            button(x+1400//2+190-190//2,y+700,50,190,[DATA_SPELERS[personage]["kaarten"].remove,schermSwitch,aantalStarTrapVeranderd],[[item],["scoreBoard"],[1,item]],tekst="Kaart Inzetten",tekstKleur="#000000")
            button(x+1400//2-190-190//2,y+700,50,190,[schermSwitch],[["scoreBoard"]],tekst="Annuleren",tekstKleur="#000000")

    
