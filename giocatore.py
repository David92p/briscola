from deck import Deck

#La classe si occupa di creare un giocatore con un mazzo di carte di tipo Briscola
class Giocatore:

    def __init__(self):
        self.carteGiocatore = Giocatore.inizioGioco()

    #Il seguente metodo prepara un giocatore ad una partita di briscola 
    @staticmethod
    def inizioGioco():
        carte = []
        deck = Deck()
        for carta in range(3):
            cartaPescata = Deck.consegnaCarta(deck)
            carte.append(cartaPescata)
        return carte
            
            
    def stampaCarte(self):
        cartePescate = ""
        for carta in self.carteGiocatore:
            cartePescate +=  carta +"  "
        print("*"*70)
        print("|"+" "*68+"|")
        print("|", end="")
        print(cartePescate.center(68, " "), end="")
        print("|")
        print("|"+" "*68+"|")
        print("*"*70)



#test
if __name__ == "__main__":
    deck = Deck()
    giocatore1 = Giocatore()
    giocatore2 = Giocatore()
    print()
    Deck.mostraDeck(deck)
    print()
    Giocatore.stampaCarte(giocatore1)
    print()
    Giocatore.stampaCarte(giocatore2)
    print()
    Deck.mostraDeck(deck)

    

  

