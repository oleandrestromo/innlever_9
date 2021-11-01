# -*- coding: utf-8 -*-
"""
Created on Tue Oct 19 16:52:03 2021

@author: ole
"""

"""Som del av et spørrespill skal du lage en klasse for flervalgspørsmål (hele spillet er muligens øving 9 og 10). 
Et flervalgspørsmål skal ha en spørsmålstekst, ei liste med svaralternativer (hvert svaralternativ er en tekststreng)
, og et tall som sier hvilket av svaralternativene som er korrekt.Klassen skal ha en __str__ metode som returnerer 
en streng som inneholder spørsmålsteksten og nummerte svaralternativer på et lett leselig format.
 Klassen skal ha en sjekk_svar metode som tar som parameter et heltall som representerer hvilket svar brukeren 
 velger. Sjekk_svar metoden skal sjekke om svaret brukeren har oppgitt er korrekt. """

class Flervalgsspørsmål:
    def __init__(self, spørsmål, alt, rett_svar):
        self.spørsmål = spørsmål
        self.alt=alt
        self.rett_svar=rett_svar
        
        #spørsmåltekst
        #lista med svaralt. 
        #rett svar
    
    
    def  __str__(self):
        spørsmål=f""" {self.spørsmål} 
        1 {self.alt[0]}
        2 {self.alt[1]}
        3 {self.alt[2]}"""
        
        return spørsmål
        #retuner spørsmåltkst og nummerete svar alt. 
    
    def sjekk_svar(self,svaret):
        if str(self.rett_svar) == str(svaret):
            print("svaret er rett")
        else: 
            print ("svaret er feil")
        
        #sjekker om svaret er rett 
        
        
        
if __name__ == "__main__":
    spørsmål = "hva er norges høyeste fjell?"
    alt= ["kvitfjell","kjerrag","galdhøypiggen"]
    rett_svar = 3
    
    quiz = Flervalgsspørsmål(spørsmål, alt, rett_svar)
    print(str(quiz))
    svaret= input("svar: ")
    quiz.sjekk_svar(svaret)
    
    spørsmål = "hva er hovedstaden i svergie?"
    alt= ["stockholm","praha","berlin"]
    rett_svar = 1
    
    quiz = Flervalgsspørsmål(spørsmål, alt, rett_svar)
    print(str(quiz))
    svaret= input("svar: ")
    quiz.sjekk_svar(svaret)
    
