from deck import Deck
from giocatore import Giocatore


# La classe ci occupa di creare un oggetto di gioco di tipo Briscola con una lista nel seguente ordine: Deck - Giocatore 1 - Giocatore 2 
class Briscola:
    def __init__(self):
        self.briscola = Briscola.inizioGioco()

    
    @staticmethod
    def inizioGioco():
        briscola = {}
        briscola['deck'] = Deck()
        briscola['briscola'] = Deck.definisciBriscola(Deck())
        briscola['giocatori'] = []
        for giocatore in range(2):
            if giocatore == 0:
                print("INSERISCI IL NOME DEL PRIMO GIOCATORE:")
                print()
                briscola['giocatori'] = Giocatore()
                print()
            if giocatore == 1:
                print("INSERISCI IL NOME DEL SECONDO GIOCATORE:")
                print()
                briscola['giocatori'] = Giocatore()
                print()
        return briscola

    """
    def test(self):
        for chiave, valore in self.briscola.items():
            if chiave == 'deck':
                Deck.mostraDeck(valore)
            if chiave == 'briscola':
                print(chiave, valore)
            if chiave == 'giocatori':
                print(valore)"""

    





# test
deck = Deck()
briscola = Briscola() # Istanziamo un oggetto Briscola composto da un dizionario con 3 valori chiave nel seguente ordine - deck, briscola, giocatori




