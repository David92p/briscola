from random import shuffle, randint, sample

#la seguente classe si occupa di gestire un deck di briscola
class Deck:

    #Di seguito un dizionario composto da chiave-seme e valore-carte Briscola
    deckOrdinato = {"Coppe": ["Asso Coppe","2 di Coppe","3 di Coppe", "4 di Coppe", "5 di Coppe",
                               "6 di Coppe", "7 di Coppe", "Donna di Coppe", "Cavallo di Coppe", "Re di Coppe"],
                "Spade": ["Asso Spade","2 di Spade","3 di Spade", "4 di Spade", "5 di Spade",
                          "6 di Spade", "7 di Spade", "Donna di Spade", "Cavallo di Spade", "Re di Spade"],
                "Bastoni": ["Asso Bastoni","2 di Bastoni","3 di Bastoni", "4 di Bastoni", "5 di Bastoni",
                            "6 di Bastoni", "7 di Bastoni", "Donna di Bastoni", "Cavallo di Bastoni", "Re di Bastoni"],
                "Denari": ["Asso Denari","2 di Denari","3 di Denari", "4 di Denari", "5 di Denari",
                        "6 di Denari", "7 di Denari", "Donna di Denari", "Cavallo di Denari", "Re di Denari"]
            }

    def __init__(self):
        self.deckBriscola = Deck.mescolaDeck()


    #Il metodo si occupa di restituire un dizionario del nostro deck in modalità disordinata
    @staticmethod
    def mescolaDeck():
        deck = {}
        for seme, carte in Deck.deckOrdinato.items():
            shuffle(carte)
            deck[seme] = carte
        return deck

    def definisciBriscola(self):
        cartaBriscola = []
        n = randint(0, 3)
        cartaBriscola.append(n)
        for i, seme in enumerate(self.deckBriscola):
            if i == n:
                for k, mazzo in self.deckBriscola.items():
                    if seme == k:
                        indiceCarta = randint(0, 9)
                        cartaBriscola.append(mazzo[indiceCarta])
                        del mazzo[indiceCarta]
                        return cartaBriscola

    # Il metodo si occupa di scegliere una carta random dal nostro deck e consegnarla ad un possibile giocatore
    def consegnaCarta(self):
        while True:
            while True:
                if len(self.deckBriscola["Coppe"]) == 0 and len(self.deckBriscola["Spade"]) == 0 and len(self.deckBriscola["Bastoni"]) == 0 and len(self.deckBriscola["Denari"]) == 0:
                    return ''
                else:
                    sequenzaIndice = sample(range(4), 4)
                    carta = []
                    for el in sequenzaIndice: 
                        for i, seme in enumerate(self.deckBriscola):
                            if i == el:
                                if len(self.deckBriscola[seme]) == 0:
                                    break
                                else:
                                    for chiave, valori in self.deckBriscola.items():
                                        if chiave == seme:
                                            indiceCarta = randint(0, len(valori)-1)
                                            carta.append(i)
                                            carta.append(valori[indiceCarta])
                                            del valori[indiceCarta]
                                            return carta

    

    #Questo metodo è un controllo del nostro deck prima e dopo aver effettuato una giocata
    def mostraDeck(self):
        for carte in self.deckBriscola.values():
            print(carte)


# test
if __name__ == "__main__":
    deck = Deck()  # Creiamo un'istanza di tipo deck di briscola
    # Utiliziamo il metodo 'mostraDeck' per stampare a video il deck
    Deck.mostraDeck(deck)
    print()
    # Definiamo una briscola di gioco 
    print(Deck.definisciBriscola(deck))
    print()
    # Consegnamo una carta dal deck
    print(Deck.consegnaCarta(deck))
    print()
    # Mostriamo a video il deck utile come debugging
    Deck.mostraDeck(deck)