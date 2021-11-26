import matplotlib.pyplot as plt
import numpy as np

# niet aankomen
#=======================================

# colors
rood = "#ff0000"
oranje = "#ffa500"
geel = "#ffff00"
groen = "#008000"
blauw = "#0000ff"
paars = "#800080"

# grafiek tekenen

def grafiekFunctie(grafiek):
    x = [0]
    y = [0]
    
    x.append(grafiek[0])
    y.append(grafiek[1])
    
    if len(grafiek) > 2:
        plt.plot(x, y, grafiek[2])
    else:
        plt.plot(x, y)

#=====================================

# modelinstellingen

iteraties = 150

# standaardwaarden
interval = 0.01
tijd = 0
nummer = 0

# modelregels
for i in range(iteraties):
    nummer += 1
    tijd += interval
    
    grafiek = [nummer, tijd]
    
    grafiekFunctie(grafiek)
    
# grafieksinstellingen
plt.xlim(0, 150) # x-as lengte
plt.ylim(0, 1.5) # y-as lengte
plt.xlabel("nummer") # x-as naam
plt.ylabel("tijd (seconde)") # y-as naam

# UITDAGING:
# - Kun je tot 1,2 seconde gaan (i.p.v. tot 1,5)?
# - Kun je in leinere stapjes tot 1,5 seconde gaan?
# - Verander de variabele 'tijd' in de afkorting 't'. Probeer of je de boel exact hetzelfde aan de praat krijgt.
# - Nadat je dit begrepen hebt, dit zelf in elkaar sleutelen vanuit het bestand "leeg.htm".

plt.show()
