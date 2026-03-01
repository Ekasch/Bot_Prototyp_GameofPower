Speziel = 0
MInvestizion = 0
IInvestition = 0
BInvestition = 0
EInvestition = 0
FInvestition = 0
NInvestition = 0
CTInvestition = 0
CInvestition = 0
SInvestition = 0
JInvestition = 0
SSInvestition = 0


#Koordinaten vom Kanada bot:
koordinaten =  [
   (56.80,-102.10),
   (55.94,-101.29),
   (55.10,-96.88),
   (54.69,-94.72),
   (52.74,-92.10),
   (48.96,-84.75),
   (47.34,-77.91),
   (46.93,-71.04),
   (48.35,-69.71),
   (48.96,-68.71),
   (49.28,-68.08),
   (49.37,-67.34),
   (49.88,-67.01),
   (50.25,-66.38),
   (50.28,-65.20),
   (50.33,-59.99),
   (51.35,-58.55),
   (51.49,-57.07),
   (52.20,-55.66),
   (53.69,-56.07),
   (54.21,-57.59),
   (54.89,-62.91),
   (56.44,-66.34),
   (57.17,-70.08),
   (59.44,-75.29),
   (59.96,-77.47),
   (58.70,-78.61),
   (57.88,-77.02),
   
]




Kauf = 0
Zölle = 0
Zölle1 = 0
Medicin= 5
Statdvortschritt= 50
Infrastrucktur = 5
Bergbau = 5
Energie = 5
Fabriken = 5
Nahrung = 5
Computertechnik = 5
Chemie = 5
Schulen = 5
Jobkultur = 5
Sozialstrucktur = 5
Industrie =(Infrastrucktur+Bergbau+Energie+Fabriken+Nahrung+Computertechnik+Chemie)/7
Sozial =(Medicin+Schulen+Jobkultur+Sozialstrucktur)/4
Soldaten =1000
Moral = (Sozial+Industrie)/200

Fläche = 200
Max_Bevölkerung= Fläche * Statdvortschritt
Bevölkerung = 10000



Militär = Soldaten 

Energieverbrauch = 1.200 *Bevölkerung
Nahrungskonsum = 1.5 * Bevölkerung
Export = Bevölkerung/Industrie**0.5 +Speziel
Import = Bevölkerung / Industrie**.5 + (Bevölkerung/2)/Sozial**0.5 +Kauf

Geld = 2_000_000_000
Geld = Geld + Export-Import+Zölle*Import-Zölle1*Export

while True:

    Infrastrucktur = 5+((IInvestition**0.5)**0.5)/20
    Bergbau = 5+((BInvestition**0.5)**0.5)/20
    Energie = 5+((EInvestition**0.5)**0.5)/20
    Fabriken = 5+((FInvestition**0.5)**0.5)/20
    Nahrung = 5+((NInvestition**0.5)**0.5)/20
    Computertechnik =5+((CTInvestition**0.5)**0.5)/20
    Chemie = 5+((Chemie**0.5)**0.5)/20
    Schulen = 5+((Schulen**0.5)**0.5)/20
    Jobkultur = 5+((JInvestition**0.5)**0.5)/20
    Sozialstrucktur =5+((SSInvestition**0.5)**0.5)/20
    Medicin = 5+((MInvestizion**0.5)**0.5)/20

    Industrie =(Infrastrucktur+Bergbau+Energie+Fabriken+Nahrung+Computertechnik+Chemie)/7
    Sozial =(Medicin+Schulen+Jobkultur+Sozialstrucktur)/4
    Moral = (Sozial+Industrie)/200
    
    Max_Bevölkerung= Fläche * Statdvortschritt
    Bevölkerung = Bevölkerung +((Bevölkerung/100)*Moral-(Bevölkerung/10)/Medicin) / Industrie/10
    if Bevölkerung > Max_Bevölkerung:
        Bevölkerung = Max_Bevölkerung

    Aktionen = (16*(Bevölkerung/2000)*(Moral*Moral**0.5))
    Energieverbrauch = 1.200 *Bevölkerung
    Nahrungskonsum = 1000 * Bevölkerung

    Export = Bevölkerung/Industrie**0.5 +Speziel
    Import = Bevölkerung / Industrie**.5 + (Bevölkerung/2)/Sozial**0.5 +Kauf
    Geld = Geld + Export-Import+Zölle*Import-Zölle1*Export
    Max_Bevölkerung= Fläche * Statdvortschritt
    
    Distance_wilderness =0
    a = ausbreiten
    for i,punkt in enumerate(koordinaten):
        print(f"Punkt{i+0.1}:({punkt["x"]},{punkt["y"]})")

    if a == ausbreiten:
       



    if Aktionen > 0:
        
        
        if Medicin<15:
            MInvestizion = MInvestizion + (Geld -Geld*0.9)
            Geld = Geld - Geld*0.1
        Medicin = 5+((MInvestizion**0.5)**0.5)/20

        if Distance_wilderness == 0:
            ausbreiten
             
            
    
    Placeholder = input("> ")
    









# B=1
#>>> while True:
#...     B=B+12
#...     A=input(">")
#...     if A == "year":
#...         continue
#...     print(B)