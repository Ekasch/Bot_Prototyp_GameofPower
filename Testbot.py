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

Kauf = 0
Zölle = 0
Zölle1 = 0
Medicin= 5
Statdvortschritt=16
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

Fläche = 50_000
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
    Nahrungskonsum = 1.5 * Bevölkerung

    Export = Bevölkerung/Industrie**0.5 +Speziel
    Import = Bevölkerung / Industrie**.5 + (Bevölkerung/2)/Sozial**0.5 +Kauf
    Geld = Geld + Export-Import+Zölle*Import-Zölle1*Export
    Max_Bevölkerung= Fläche * Statdvortschritt
    
    



    print(Medicin)



    if Aktionen > 0:
        
        if Medicin<15:
            MInvestizion = MInvestizion + (Geld -Geld*0.9)
            Geld = Geld - Geld*0.1
        Medicin = 5+((MInvestizion**0.5)**0.5)/20

        if Infrastrucktur < 22:
            A = Bergbau
            
    
    Placeholder = input("> ")
    









# B=1
#>>> while True:
#...     B=B+12
#...     A=input(">")
#...     if A == "year":
#...         continue
#...     print(B)