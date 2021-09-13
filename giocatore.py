from deck import Deck

# La classe si occupa di creare un giocatore con un mazzo di carte di tipo Briscola
class Giocatore:

    def __init__(self):
        self.carteGiocatore = Giocatore.definisciGiocatore()

    # Il seguente metodo prepara un giocatore ad una partita di briscola 
    @staticmethod
    def definisciGiocatore():
        giocatori = {}
        giocatori[input('Inserisci il tuo nome Giocatore: ')] = []
        deck = Deck()
        for giocatore, carte in giocatori.items():
            for i in range(3):
                cartaPescata = Deck.consegnaCarta(deck)
                giocatori[giocatore].append(cartaPescata)
        return giocatori
            
    # Il seguente metodo ci permette di visualizzare a schermo attraverso un print il nome del giocatore istanziato con le rispettive carte        
    def stampaCarte(self):
        for nomeGiocatore, carte in self.carteGiocatore.items():
            print('Giocatore '+ nomeGiocatore + ':')
            print()
            print(carte)
            print()

    # Il seguente metodo ci permette di scegliere e restituire una carta tra quelle in mano dell'oggetto Giocatore
    def giocaCarta(self):
        print('NUMERO CARTE GIOCABILI:')
        print()
        for carte in self.carteGiocatore.values():
            for numero, carta in enumerate(carte, 1):
                print(f'Numero {numero} = {carta}')
                print()

        while True:
            try:
                numero = int(input('INSERISCI IL NUMERO DI CARTA CHE DESIDERI GIOCARE: '))
                if numero == 1 or numero == 2 or numero == 3:
                    for carte in self.carteGiocatore.values():
                        for index, carta in enumerate(carte, 1):
                            if index == numero:
                                return carta
                else:
                    print()
                    print('Valore non riconosciuto')
                    print()
            except ValueError:
                print()
                print("Utilizza la tastiera numerica")
                print()




        



#test
if __name__ == "__main__":
    deck = Deck() # Istanziamo un oggetto di tipo Deck
    giocatore1 = Giocatore() # Istanziamo un primo giocatore 
    Giocatore.stampaCarte(giocatore1) # Richiamiamo un metodo di stampa che lavora sull'oggetto creato
    print()
    Deck.mostraDeck(deck) # Stampiamo il mazzo di carte rimanente come debugging
    print()
    print(Giocatore.giocaCarta(giocatore1)) # Stampiamo la carta che desideriamo giocare


    

  

