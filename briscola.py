from deck import Deck
from giocatore import Giocatore

from random import randint

from printer import Printer

# La classe ci occupa di creare un oggetto di gioco di tipo Briscola con una lista nel seguente ordine: Deck - Giocatore 1 - Giocatore 2


class Briscola:
    def __init__(self):
        self.giocoBriscola = Briscola.definisciPartita()

    @staticmethod
    def definisciPartita():
        briscola = []
        briscola.append(Deck())
        briscola.append(Deck.definisciBriscola(briscola[0]))
        briscola.append([])
        print('BENVENUTI NEL GIOCO DELLA BRISCOLA')
        for i in range(2):
            if i == 0:
                print("INSERISCI IL NOME DEL PRIMO GIOCATORE:")
                briscola[2].append(Giocatore())
            if i == 1:
                print("INSERISCI IL NOME DEL SECONDO GIOCATORE:")
                briscola[2].append(Giocatore())

        return briscola

    def inizio(self):

        random_start = randint(0, 1)
        print(
            f"INIZIERA' IL GIOCATORE {Giocatore.stampaNome(self.giocoBriscola[2][random_start])}")

        giocatore_1 = []
        giocatore_2 = []

        while True:
            try:
                first_start = input(
                    f"{Giocatore.stampaNome(self.giocoBriscola[2][random_start])} PREMI INVIO SE SEI PRONTO A GIOCARE!!")
                if first_start == "":
                    Giocatore.stampaCarte(v[random_start])
                    break

                else:
                    print(
                        f'VALORE NON RICONOSCIUTO - {Giocatore.stampaNome(self.giocoBriscola[2][random_start])} PREMI INVIO SE SEI PRONTO A GIOCARE')
            except ValueError:
                print(
                    f'VALORE NON RICONOSCIUTO - {Giocatore.stampaNome(self.giocoBriscola[2][random_start])} PREMI INVIO SE SEI PRONTO A GIOCARE')

        print(
            f"LA BRISCOLA DI GIOCO SARA' {Printer.stampaCarta(self.giocoBriscola[1])}")

    def test(self):

        Giocatore.stampaCarte(self.giocoBriscola[2][0])
        Giocatore.stampaCarte(self.giocoBriscola[2][1])


# test
# deck = Deck()
briscola = Briscola()  # Istanziamo un oggetto Briscola composto da un dizionario con 3 valori chiave nel seguente ordine - deck, briscola, giocatori
print(Briscola.test(briscola))
