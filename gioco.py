from deck import Deck
from giocatore import Giocatore

from random import randrange


# La classe ci occupa di creare un oggetto di gioco di tipo Briscola con una lista nel seguente ordine: Deck - Giocatore 1 - Giocatore 2 
class Briscola:
    def __init__(self):
        self.briscola = Briscola.inizioGioco()

    # Il metodo ci aiuta a completare la nostra lista con i dati richiesti nell'ordine sopra descritto, inoltre ci da la possibilità di 
    # inserire i nomi dei giocatori partecipanti al gioco
    @staticmethod
    def inizioGioco():
        briscola = []
        briscola.append(Deck())
        for giocatore in range(2):
            briscola.append(Giocatore())
        return briscola

    # test
    def giochiamo(self):
        Deck.mostraDeck(self.briscola[0])
        print()
        Giocatore.stampaCarte(self.briscola[1])
        print()
        Giocatore.stampaCarte(self.briscola[2])
    

# test
deck = Deck()
briscola = Briscola()
Briscola.giochiamo(briscola)
print(Briscola.cartaBriscola(briscola))
Deck.mostraDeck(deck)




