from .deck import Deck
from .printer import Printer

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
    def restituisciCarte(self):
        for carte in self.giocatore.values():
            Printer.stampaCartegiocatore(carte)

    # Il metodo restituisce la lunghezza delle carte in mano al giocatore
    def lunghezzaCarte(self):
        for carte in self.giocatore.values():
            return len(carte)

    # La funzione ci permette di stampare il nome a video del nostro Oggetto in maiuscolo
    def stampaNome(self):
        for nome in self.giocatore.keys():
            return nome.upper()

    # La funzione si occupa di aggiungere una carta al nostro oggetto Giocatore selezionata dal Deck
    def pescaCarta(self, carta):
        for carte in self.giocatore.values():
            carte.append(carta)

    # Il seguente metodo dopo aver stampato a video la sequenza delle carte numerandola, restiuisce una delle carte selezionate attraverso un imput
    def giocaCarta(self):
        Giocatore.restituisciCarte(self)
        print('NUMERO CARTE GIOCABILI:')
        print()
        for carte in self.giocatore.values():
            for numero, carta in enumerate(carte, 1):
                print(f'Numero {numero} = {carta[1]}')
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
                            return carta

                elif len(carte) == 2 and (numero == 1 or numero == 2):
                    for index, carta in enumerate(carte, 1):
                        if index == numero:
                            cartaGiocata = carta
                            del carte[index-1]
                            return carta

                elif len(carte) == 1 and numero == 1:
                    for index, carta in enumerate(carte, 1):
                        if index == numero:
                            cartaGiocata = carta
                            del carte[index-1]
                            return carta
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
    # Istanziamo un primo giocatore
    giocatore1 = Giocatore()
    # Stampiamo le carte del giocatore
    Giocatore.restituisciCarte(giocatore1)
    # Stampiamo la carta giocata
    Giocatore.giocaCarta(giocatore1)
    # Stampiamo le carte del giocatore rimanenti come debugging
    Giocatore.restituisciCarte(giocatore1)
