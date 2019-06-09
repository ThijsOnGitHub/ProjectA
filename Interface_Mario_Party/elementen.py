#kies rij uit spelers
'''
def kiesRijItem(x,y,breedte,hoogte,personage):
    img(personage,x,y,breedte,hoogte)

def kiesUitSpelersRij(x,y,breedte,hoogte,tussenRuimte):
    global DATA_SPELERS
    print(DATA_SPELERS)
    for item in DATA_SPELERS.keys():
        kiesRijItem(item,x,y,breedte,hoogte)
        x+=breedte+tussenRuimte
'''

    


global click
click={"x":-1,"y":-1}

def getclick():
    global click
    return click

def setClick(input):
    global click
    click=input

#Alles voor de button
def button(x,y,Hoogte,Breedte,functies,argumenten, tekst="",tekstKleur="#050505",buttonKleur="#FCFFFE",buttonOverKleur="#AFAFAF",tekstSize=26,alignRect=CORNER):
    global click
    #print(argumenten)
    textSize(26)
    if mouseX >= x and mouseX <= x+Breedte and mouseY >=y and mouseY <=y+Hoogte:
        fill(buttonOverKleur)
    else:
        fill(buttonKleur)
    rect(x,y,Breedte,Hoogte)
    textAlign(CENTER,CENTER)
    fill(tekstKleur)
    text(tekst,x+(Breedte/2),y+(Hoogte/2))
    stroke("#030303")
    rectMode(alignRect)
    if click["x"] >= x and click["x"] <= x+Breedte and click["y"] >=y and click["y"] <=y+Hoogte: #and click+710>millis() and  millis()>click:
        click={"x":-1,"y":-1}
        for i in range(0,len(functies)):
            functies[i](*argumenten[i])

        


def mousePressed():
    global click
    click={"x":mouseX,"y":mouseY}
    
def clickArea(x,y,Hoogte,Breedte,functies,argumenten):
    global click
    #print(argumenten)
    if click["x"] >= x and click["x"] <= x+Breedte and click["y"] >=y and click["y"] <=y+Hoogte: #and click+710>millis() and  millis()>click:
        click={"x":-1,"y":-1}
        for i in range(0,len(functies)):
            functies[i](*argumenten[i])
            
#alles voor img functie
def img(foto,x,y,*formaat):
    image(loadImage(str(foto)+".png"),x,y,*formaat)
    
#alles voor invulvakje
def vakje():
    if mouseX >= x and mouseX <= x+Breedte and mouseY >=y and mouseY <=y+Hoogte and click == True:
        click=False
        for i in range(0,len(functies)):
            functies[i](*argumenten[i])
# rij met personges om om te klikken
# return None er niemand is gelikt en return naam speler als er op geklikt is

def kiesRijItem(x,y,Breedte,Hoogte,personage):
    global click
    img(personage,x,y,Breedte,Hoogte)
    if click["x"] >= x and click["x"] <= x+Breedte and click["y"] >=y and click["y"] <=y+Hoogte: #and click+710>millis() and  millis()>click:
        click={"x":-1,"y":-1}
        return personage

def kiesUitSpelersRij(x,y,breedte,hoogte,tussenRuimte,selectie=["Blue Yoshi","Luigi","Mario","Daisy","Rosalie","Waluigi"]):
    global DATA_SPELERS
    totaalLen=(len(selectie)*(breedte+tussenRuimte))-tussenRuimte
    x=x-totaalLen//2
    imageMode(CORNER)
    for item in selectie:
        if kiesRijItem(x,y,breedte,hoogte,item)==item:
            return item
        x+=breedte+tussenRuimte



def refText(tekst,x,y,textgroote):
    tekst=str(tekst)
    textSize(textgroote)
    textAlign(LEFT,TOP)
    stroke("#FFFFFF")
    fill("#FFFFFF")
    rect(x,y,textgroote*len(tekst),textgroote*(1/0.24))
    fill("#050505")
    text(tekst,x,y)
    stroke("#000000")
    
def refText2(tekst,x,y,breedte,textgroote):
    tekst=str(tekst)
    textSize(textgroote)
    textAlign(LEFT,TOP)
    stroke("#FFFFFF")
    fill("#FFFFFF")
    rect(x,y,breedte,textgroote*1)
    fill("#050505")
    text(tekst,x,y)
    stroke("#000000")
