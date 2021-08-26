from random import shuffle, randrange

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
        self.deck = Deck.mescolaDeck()


    #Il metodo si occupa di restituire un dizionario del nostro deck in modalità disordinata
    @staticmethod
    def mescolaDeck():
        deck = {}
        for seme, carte in Deck.deckOrdinato.items():
            shuffle(carte)
            deck[seme] = carte
        return deck

    #Il metodo si occupa di scegliere unn carta random dal nostro deck e consegnarla ad un possibile giocatore
    def consegnaCarta(self):
        n = randrange(0, 4)
        for i, seme in enumerate(self.deck):
            if i == n:
                for k, mazzo in self.deck.items():
                    if seme == k:
                        indiceCarta = randrange(0, len(self.deck[k]))
                        cartaAssegnata = mazzo[indiceCarta]
                        del mazzo[indiceCarta]
                        return cartaAssegnata

    #Questo metodo è un controllo del nostro deck prima e dopo aver effettuato una giocata
    def mostraDeck(self):
        for carte in self.deck.values():
            print(carte)


    #Questo metodo definisci la briscola che comanderà il gioco - stampiamo a video il valore della briscola salvando anche un indice di riferimento pe ril seguito del gioco
    def definisciBriscola(self):
        n = randrange(0, 4)
        briscola = []
        briscola.append(n)
        for i, seme in enumerate(self.deck):
            if i == n:
                for k, mazzo in self.deck.items():
                    if seme == k:
                        indiceCarta = randrange(0, len(self.deck[k]))
                        briscola.append(mazzo[indiceCarta])
                        del mazzo[indiceCarta]
                        return briscola[1]



#test
if __name__ == "__main__":
    deck = Deck() # Istanziamo un oggetto di tipo Deck
    Deck.mostraDeck(deck) # Stampiamo il deck come debugging
    print()
    print(Deck.definisciBriscola(deck)) # Definiamo una briscola all'inizio del gioco
    print()
    print(Deck.consegnaCarta(deck)) # Consegnamo 3 carte ad un possibile giocatore 
    print()
    Deck.mostraDeck(deck) # Proviamo a stampare il deck come debugging
    
    
    
    

        