# -*- coding: utf-8 -*-
"""
Created on Tue Nov  2 09:27:02 2021

@author: ole
"""




class Flervalgsspørsmål:
    def __init__(self, sporsmal, korrekte_svar, alternativ):
        self.sporsmal = sporsmal
        self.korrekte_svar = korrekte_svar
        self.alternativ = alternativ
        
    
    def  __str__(self):
        sporsmal=f""" 
       {self.sporsmal} 
1. {self.alternativ[0]}
2. {self.alternativ[1]}
3. {self.alternativ[2]}
4. {self.alternativ[3]}
5. {self.alternativ[3]}
"""
        return sporsmal
    
    def sjekk_svar(self, svaret):
        if str(svaret) == str(self.korrekte_svar[0][1]):
            return True
        else:
            return False
        
def les_fila():
     with open("sporsmaalsfil.txt", "r", encoding = "UTF-8") as fila:
            sporsmal_liste = list()
            for linje in fila:
              spalt = linje.split(":")
              sporsmal = spalt[0]
              korrekte_svar = spalt[1].split(":")
              alternativ = spalt[2].split(",")
              sporsmal_liste.append(Flervalgsspørsmål(sporsmal, korrekte_svar, alternativ))
            return sporsmal_liste
            
if __name__ == "__main__":
    spiller1 = input("Navnet ditt? : ")
    spiller2 = input("Navnet ditt? : ")
    korrekte_svar = 0
    sporsmal_liste = les_fila()
    
    for sporsmalene in sporsmal_liste:
            print(str(sporsmalene))
           
            bruker1_svar = input(f"{spiller1} svar: ")
            if sporsmalene.sjekk_svar(bruker1_svar):
                print("Korrekt!")
                korrekte_svar += 1
            else:
                print("Feil!")
            print(f"Du har {korrekte_svar} riktige av {len(sporsmal_liste)} mulige.")
            
            bruker2_svar = input(f"{spiller2} svar: ")
            if sporsmalene.sjekk_svar(bruker2_svar):
                print("Korrekt!")
                korrekte_svar += 1
            else:
                print("Feil!")
            print(f"Du har {korrekte_svar} riktige av {len(sporsmal_liste)} mulige.")