import math
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

Kanada_koordinaten =[
    (49.160, -107.020), (49.165, -107.035), (49.167, -107.050), (49.166, -107.065),
    (49.161, -107.080), (49.152, -107.092), (49.140, -107.100), (49.125, -107.104),
    (49.108, -107.104), (49.090, -107.100), (49.075, -107.092), (49.065, -107.080),
    (49.060, -107.065), (49.061, -107.050), (49.068, -107.035), (49.080, -107.020),
    (49.095, -107.012), (49.112, -107.010), (49.128, -107.012), (49.138, -107.018),
    (49.147, -107.025), (49.152, -107.032), (49.155, -107.040), (49.156, -107.048),
    (49.154, -107.056), (49.150, -107.063), (49.143, -107.068), (49.134, -107.070),
    (49.124, -107.069), (49.115, -107.065), (49.108, -107.059),
    (49.160, -107.020), (49.165, -107.035), (49.167, -107.050), (49.166, -107.065),
    (49.161, -107.080), (49.152, -107.092), (49.140, -107.100), (49.125, -107.104),
    (49.108, -107.104), (49.090, -107.100), (49.075, -107.092), (49.065, -107.080),
    (49.060, -107.065), (49.061, -107.050), (49.068, -107.035), (49.080, -107.020),
    (49.095, -107.012), (49.112, -107.010), (49.128, -107.012), (49.138, -107.018),
    (49.147, -107.025), (49.152, -107.032), (49.155, -107.040), (49.156, -107.048),
    (49.154, -107.056), (49.150, -107.063), (49.143, -107.068), (49.134, -107.070),
    (49.124, -107.069), (49.115, -107.065), (49.108, -107.059)
]

def haversine(lat1, lon1, lat2, lon2):
      lat1, lon1, lat2, lon2 = map(math.radians, [lat1, lon1, lat2, lon2])
      dlat, dlon = lat2 - lat1, lon2 - lon1
      a = (math.sin(dlat/2)**2 + 
      math.cos(lat1) * math.cos(lat2) * math.sin(dlon/2)**2)
      c = 2 * math.asin(math.sqrt(a))
      r = 6371  # Erdradius in km
      return c * r



class Kanada:
    def __init__(self, koordinaten):
        
        self.koordinaten = koordinaten 
        self.area = len(koordinaten)
    
    def get_position_at_index(self, index):
        return self.koordinaten[index]
    def set_position_at_index(self, index, neue_pos):
        if 0<=index<self.area:
            self.koordinaten[index] = neue_pos
            print(f"Punkt {index} geändert zu {neue_pos}")
        else:
            print("Index außerhalb Bereich!")
    
    def change_selected(self, indices, dx=0, dy=0):
        for i in indices:
            if 0 <= i < self.area:
                x, y = self.koordinaten[i]
                self.koordinaten[i] = (x + dx, y + dy)
        print(f"Geänderte Indizes: {indices}")
   
    

   
route = Kanada(Kanada_koordinaten)
    

    #elif action == 's':
       #indices = list(map(int, input("Indizes (komma-separiert): ").split(',')))               Weiß nicht ob ich das brauche
       #dx, dy = map(float, input("dx,dy: ").split(','))
       #route.change_selected(indices, dx, dy)



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
Export = Bevölkerung/Industrie**0.5 
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
    Chemie = 5+((CInvestition)**0.5)/20
    Schulen = 5+((SInvestition**0.5)**0.5)/20
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

    Export = Bevölkerung/Industrie**0.5 
    Import = Bevölkerung / Industrie**.5 + (Bevölkerung/2)/Sozial**0.5 +Kauf
    Geld = Geld + Export-Import+Zölle*Import-Zölle1*Export
    Max_Bevölkerung= Fläche * Statdvortschritt
    
    Soldaten_Trupp =  Soldaten 
    Soldaten_Trupp_position = (1,1)
    Soldaten_Trupp_geschwindigkeit = 3


    if Aktionen > 0:
        
        
        if Medicin<15:
            MInvestizion = MInvestizion + (Geld -Geld*0.9)
            Geld = Geld - Geld*0.1
        Medicin = 5+((MInvestizion**0.5)**0.5)/20


        if Soldaten < Bevölkerung/50:
            Soldaten=Bevölkerung/50
            Bevölkerung=Bevölkerung-Bevölkerung/50
        
        if Soldaten > 200:
             print("Ich greife die Wilden an")
            
                   
             kampf_runde = 0
             while True:
                 kampf_runde += 1
                 print(f"\n--- KAMPF RUNDE {kampf_runde} ---")
                 print("Route-Status:", [route.get_position_at_index(i) for i in [0,5,10,-1]])
                 
                 
                 idx=int(input("Welche Richtung"))
                 action = input("Aktion (v=vorrücken/r=zurückziehen/a=angreifen/q=zurückziehen): ")
                 Ziel1 = float(input("Wohin x: "))
                 Ziel2 = float(input("Wohin y:"))
                 if Soldaten_Trupp_position == idx:
                     Soldaten_Trupp_position = idx 
                 elif Soldaten_Trupp_position != idx:
                     def haversine(lat1, lon1, lat2, lon2):
                        lat1, lon1, lat2, lon2 = map(math.radians, [lat1, lon1, lat2, lon2])
                        dlat, dlon = lat2 - lat1, lon2 - lon1
                        a = (math.sin(dlat/2)**2 + 
                        math.cos(lat1) * math.cos(lat2) * math.sin(dlon/2)**2)
                        c = 2 * math.asin(math.sqrt(a))
                        r = 6371  # Erdradius in km
                        return c * r

                     
                     start = route.get_position_at_index(idx)  # (lat, lon)
                     Ziel = (49.0, -107.0)       # Beispielziel

                     dist = haversine(
                     start[0], start[1],     # lat1, lon1
                     Ziel[0], Ziel[1]        # lat2, lon2
                        )
                     print("Distanz in km:", dist)
                     
                    
                        
            

                 if action == 'q':
                    print("🛡️ Rückzug!")
                    break
            
              #   elif action == 'v':  # VORRÜCKEN (Land gewinnen)
                    
                   # dx = float(input("dx: "))
                   # dy = float(input("dy: "))
                  #  route.set_position_at_index(idx, (route.koordinaten[idx][0]+dx, 
                  #                       route.koordinaten[idx][1]+dy))
                   # Fläche += strecke * 100  # Gesamtfläche erhöhen!
                  #  Max_Bevölkerung = Fläche * Statdvortschritt

                 
                     
            
                 elif action == 'a':  # VOLLER ANGRIFF
                    erfolg = Soldaten > 500  # Erfolg basierend auf Truppen
                    if erfolg:
                        
                        Fläche += 15
                        
                        
                    else:
                     print("💥 SCHLACHTNiederlage!")
                     Soldaten *= 0.8  # 20% Verluste
        
        # Truppenverluste pro Runde
                 Soldaten -= Soldaten * 0.02  # 2% Verluste pro Runde
                 if Soldaten < 100:
                   print("☠️ Armee vernichtet!")
                   break
      #         print("Ich greife die Wilden an")
     #     print(f"mit",Soldaten"Soldaten")
      #     while True:
        #        print("\nRoute-Status:", [route.get_position_at_index(i) for i in [0,5,10,-1]])
        #        action = input("Aktion (i=index ändern/s=selected verschieben/q=quit): ")
    #
         #       if action == 'q':
          #         break
            #    elif action == 'i':
             #       idx = int(input("Index: "))
                 #   dx = float(input("dx: "))
                #    dy = float(input("dy: "))
                  #  route.set_position_at_index(idx, (route.koordinaten[idx][0]+dx, 
                     #                  route.koordinaten[idx][1]+dy))




    print(Medicin)   
    print(Geld)    
    
    Placeholder = input("> ")
    









# B=1
#>>> while True:
#...     B=B+12
#...     A=input(">")
#...     if A == "year":
#...         continue
#...     print(B)