from elementen import *
from back_end_code import *
from Welk_Scherm import *


def winnerScreen(x,y):
    deLijst=sorted(sorted(DATA_SPELERS.items(),key=lambda x:x[1]["coins"]),key=lambda x:x[1]["stars"])
    deLijst.reverse()
    RANKING=deLijst

    
    
    if len(RANKING)> 2 :
        if RANKING[0][1]["coins"] == RANKING[1][1]["coins"] and RANKING[0][1]["coins"] == RANKING[2][1]["coins"]  and RANKING[0][1]["stars"] == RANKING[1][1]["stars"] and RANKING[0][1]["stars"] == RANKING[2][1]["stars"]:
            place(750,50,RANKING[0][1],"Je hebt GEWONNEN!!!")
            place(250,500,RANKING[1][1],"Je hebt GEWONNEN!!!")
            place(1250,500,RANKING[2][1],"Je hebt GEWONNEN!!!")
        elif RANKING[0][1]["coins"] == RANKING[1][1]["coins"] and RANKING[0][1]["stars"] == RANKING[1][1]["stars"]:
            place(750,50,RANKING[0][1],"Je hebt GEWONNEN!!!")
            place(250,500,RANKING[1][1],"Je hebt GEWONNEN!!!")
            place(1250,500,RANKING[2][1],"Je bent 2e")
        elif RANKING[1][1]["coins"] == RANKING[2][1]["coins"] and RANKING[1][1]["stars"] == RANKING[2][1]["stars"]:
            place(750,50,RANKING[0][1],"Je hebt GEWONNEN!!!")
            place(250,500,RANKING[1][1],"Je bent 2e")
            place(1250,500,RANKING[2][1],"Je bent 2e")
        else:
            place(750,50,RANKING[0][1],"Je hebt GEWONNEN!!!")
            place(250,500,RANKING[1][1],"Je bent 2e")
            place(1250,500,RANKING[2][1],"Je bent 3e")
            
    elif RANKING[0][1]["coins"] == RANKING[1][1]["coins"] and RANKING[0][1]["stars"] == RANKING[1][1]["stars"]:
        place(750,50,RANKING[0][1],"Je hebt GEWONNEN!!!")
        place(250,500,RANKING[1][1],"Je hebt GEWONNEN!!!")

    else:
        place(750,50,RANKING[0][1],"Je hebt GEWONNEN!!!")
        place(250,500,RANKING[1][1],"Je bent 2e")


    schermSwitch("end")



def place(x,y,placeData,tekst):
    imageMode(CENTER)
    img(placeData["personage"],x+150,y+50,75,75)
    textSize(30)
    textAlign(CENTER,CENTER)
    text(tekst,x+150,y+125)
    img("Star", x+75,y+200,50,50)
    text(placeData["stars"], x+75,y+240)
    img("Coin", x+225,y+200,50,50)
    text(placeData["coins"], x+225,y+240)
