from deck import Deck
from giocatore import Giocatore

from random import randrange


# La classe ci occupa di creare un oggetto di gioco di tipo Briscola con una lista nel seguente ordine: Deck - Giocatore 1 - Giocatore 2 
class Briscola:
    def __init__(self):
        self.briscola = Briscola.inizioGioco()

    
    @staticmethod
    def inizioGioco():
        briscola = []
        briscola.append(Deck())
        for giocatore in range(2):
            if giocatore == 0:
                print("INSERISCI IL NOME DEL PRIMO GIOCATORE:")
                print()
                briscola.append(Giocatore())
            if giocatore == 1:
                print("INSERISCI IL NOME DEL SECONDO GIOCATORE:")
                print()
                briscola.append(Giocatore())
        return briscola



# test
briscola = Briscola()


