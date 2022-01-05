from deck import Deck
from printer import Printer

# La classe si occupa di creare un giocatore con un mazzo di carte di tipo Briscola


class Giocatore:

    def __init__(self):
        self.giocatore = Giocatore.definisciGiocatore()

    # Il seguente metodo prepara un giocatore ad una partita di briscola
    @staticmethod
    def definisciGiocatore():
        giocatore = {}
        giocatore[input()] = []
        deck = Deck()
        for carte in giocatore.values():
            for i in range(3):
                carta = Deck.consegnaCarta(deck)
                carte.append(carta)
        return giocatore

    # Il seguente metodo ci permette di visualizzare a schermo attraverso un print il nome del giocatore istanziato con le rispettive carte
    def stampaCarte(self):
        for nomeGiocatore, carte in self.giocatore.items():
            print('Giocatore ' + nomeGiocatore.upper() + ':')
            print()
            Printer.stampaCartegiocatore(carte)

    def lunghezzaCarte(self):
        for carte in self.giocatore.values():
            if len(carte) == 3:
                return 3
            elif len(carte) == 2:
                return 2
            elif len(carte) == 1:
                return 1
            elif len(carte) == 0:
                return 0

    def stampaNome(self):
        for nome in self.giocatore.keys():
            return nome.upper()

    # La funzione si occupa di aggiungere una carta al nostro oggetto
    def pescaCarta(self, carta):
        for carte in self.giocatore.values():
            carte.append(carta)

    # Il seguente metodo ci permette di scegliere e restituire una carta tra quelle in mano dell'oggetto Giocatore
    def giocaCarta(self):
        print('NUMERO CARTE GIOCABILI:')
        print()
        for carte in self.giocatore.values():
            for numero, carta in enumerate(carte, 1):
                print(f'{numero} = {carta}')
                print()

            while True:
                try:
                    numero = int(
                        input('INSERISCI IL NUMERO DI CARTA CHE DESIDERI GIOCARE: '))

                    if len(carte) == 3 and (numero == 1 or numero == 2 or numero == 3):
                        for index, carta in enumerate(carte, 1):
                            if index == numero:
                                cartaGiocata = carta
                                del carte[index-1]
                                return cartaGiocata

                    elif len(carte) == 2 and (numero == 1 or numero == 2):
                        for index, carta in enumerate(carte, 1):
                            if index == numero:
                                cartaGiocata = carta
                                del carte[index-1]
                                return cartaGiocata

                    elif len(carte) == 1 and numero == 1:
                        for index, carta in enumerate(carte, 1):
                            if index == numero:
                                cartaGiocata = carta
                                del carte[index-1]
                                return cartaGiocata
                    else:
                        print()
                        print('Valore non riconosciuto')
                        print()
                except ValueError:
                    print()
                    print("Utilizza la tastiera numerica")
                    print()


# test
if __name__ == "__main__":
    deck = Deck()
    giocatore1 = Giocatore()  # Istanziamo un primo giocatore
    Giocatore.stampaCarte(giocatore1)  # Stampiamo le carte del giocatore
    # Stampiamo a video il return della funzione tramite le funzione Printer
    Printer.stampaCarta(Giocatore.giocaCarta(giocatore1))
    # Stampiamo le carte del giocatore rimanenti come debugging
    Giocatore.stampaCarte(giocatore1)
    Printer.stampaCarta(Giocatore.giocaCarta(giocatore1))
    # Stampiamo le carte del giocatore rimanenti come debugging
    Giocatore.stampaCarte(giocatore1)
    Printer.stampaCarta(Giocatore.giocaCarta(giocatore1))
    # Stampiamo le carte del giocatore rimanenti come debugging
    Giocatore.stampaCarte(giocatore1)
