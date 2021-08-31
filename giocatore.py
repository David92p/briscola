from deck import Deck

#La classe si occupa di creare un giocatore con un mazzo di carte di tipo Briscola
class Giocatore:

    def __init__(self):
        self.carteGiocatore = Giocatore.inizioGioco()

    #Il seguente metodo prepara un giocatore ad una partita di briscola 
    @staticmethod
    def inizioGioco():
        giocatori = {}
        giocatori[input('Nome: ')] = []
        deck = Deck()
        for giocatore, carte in giocatori.items():
            for i in range(3):
                cartaPescata = Deck.consegnaCarta(deck)
                giocatori[giocatore].append(cartaPescata)
        return giocatori
            
    #Il seguente metodo ci permette di visualizzare a schermo attraverso un print il nome del giocatore istanziato con le rispettive carte        
    def stampaCarte(self):
        for nomeGiocatore, carte in self.carteGiocatore.items():
            print('Giocatore '+ nomeGiocatore + ':')
            print()
            print(carte)
            print()
        



#test
if __name__ == "__main__":
    deck = Deck() # Istanziamo un oggetto di tipo Deck
    giocatore1 = Giocatore() # Istanziamo un primo giocatore 
    Giocatore.stampaCarte(giocatore1) # Richiamiamo un metodo di stampa che l'avora sull'oggetto creato
    print()
    Deck.mostraDeck(deck) # stampiamo il mazzo di carte rimanente come debugging


    

  

