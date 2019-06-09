from elementen import *
#de variable
DATA_SPELERS={}
MELDING=""

#geld



def coin_erbij(naam,aantal):
    delMel()
    global DATA_SPELERS
    global MELDING
    DATA_SPELERS[naam]["coins"]+=aantal
    if DATA_SPELERS[naam]["coins"]<0:
        MELDING="Er zijn "+str(DATA_SPELERS[naam]["coins"]*-1)+" coins niet meegeteld omdat je anders in de min komt"
        DATA_SPELERS[naam]["coins"]=0
        
def koop_star(naam):
    delMel()
    global MELDING
    if (DATA_SPELERS[naam]["coins"]-30)<0:
        MELDING=str(naam)+", je hebt niet genoeg geld voor een ster"
    else:
        star_erbij(naam,1)
        coin_erbij(naam,-30)
    
def steel_coin(naam,target,aantal):
    delMel()
    global MELDING
    if DATA_SPELERS[target]["coins"] == 0:
        MELDING=str(target)+", heeft geen coins om te stelen"
        return MELDING
    elif DATA_SPELERS[target]["coins"] < aantal and DATA_SPELERS[target]["coins"] != 0:
        aantal = DATA_SPELERS[target]["coins"]
    DATA_SPELERS[naam]["coins"]+=aantal
    DATA_SPELERS[target]["coins"]-=aantal
    
def steel_star(naam,target,aantal):
    delMel()
    global MELDING
    if DATA_SPELERS[naam]["coins"] < (aantal*35):
        MELDING=str(naam)+", je hebt niet genoeg coins om een star te stelen"
        return MELDING
    elif DATA_SPELERS[target]["stars"] == 0:
        MELDING=str(naam)+", "+target+" heeft geen sterren om te stelen"
        return MELDING
    else:   
        DATA_SPELERS[naam]["coins"]-=(aantal*35)
        DATA_SPELERS[naam]["stars"]+=aantal
        DATA_SPELERS[target]["stars"]-=aantal


def star_erbij(naam,aantal):
    delMel()
    global DATA_SPELERS
    DATA_SPELERS[naam]["stars"]+=aantal
    if DATA_SPELERS[naam]["stars"]<0:
        MELDING="Er zijn "+str(DATA_SPELERS[naam]["coins"]*-1)+" stars niet meegeteld niet meegeteld omdat je anders in de min komt"
        DATA_SPELERS[naam]["stars"]=0
       
#meldingen       
       
def delMel():
    global MELDING
    MELDING=""
    
def changeMel(input):
    global MELDING
    MELDING=input
    
    
def melding(x,y):
    global MELDING
    stroke(250,250,250)
    fill("#FFFFFF")
    rect(x-20,y,920,30*(1/0.24))
    textSize(30)
    textAlign(CENTER,TOP)
    fill("#FF0000")
    text(MELDING,x+880/2,y)
