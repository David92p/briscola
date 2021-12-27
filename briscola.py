from deck import Deck
from giocatore import Giocatore
from printer import Printer

from random import randint


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
        print()
        for i in range(2):
            if i == 0:
                print("INSERISCI IL NOME DEL PRIMO GIOCATORE:")
                briscola[2].append(Giocatore())
            if i == 1:
                print("INSERISCI IL NOME DEL SECONDO GIOCATORE:")
                briscola[2].append(Giocatore())
                print()

        return briscola

    def definisciPresa(self, prima_carta, seconda_carta):
        conteggioDeck = [["Asso Coppe", "3 di Coppe", "Re di Coppe", "Cavallo di Coppe", "Donna di Coppe", "7 di Coppe",
                          "6 di Coppe", "5 di Coppe", "4 di Coppe", "2 di Coppe"],
                         ["Asso Spade", "3 di Spade", "Re di Spade", "Cavallo di Spade", "Donna di Spade", "7 di Spade",
                          "6 di Spade", "5 di Spade", "4 di Spade", "2 di Spade"],
                         ["Asso Bastoni", "3 di Bastoni", "Re di Bastoni", "Cavallo di Bastoni", "Donna di Bastoni", "7 di Bastoni",
                          "6 di Bastoni", "5 di Bastoni", "4 di SBastoni", "2 di Bastoni"],
                         ["Asso Denari", "3 di Denari", "Re di Denari", "Cavallo di Denari", "Donna di Denari", "7 di Denari",
                          "6 di Denari", "5 di Denari", "4 di Denari", "2 di Denari"]]

        # condizione se nessuno dei due giocatori o entrambi giocano una carta briscola
        if self.giocoBriscola[1][0] != prima_carta[0] and self.giocoBriscola[1][0] != seconda_carta[0] or self.giocoBriscola[1][0] == seconda_carta[0] and self.giocoBriscola[1][0] == prima_carta[0]:
            # in caso di nessuna carta briscola da entrambe le parti vince il giocatore 1 che ha effettuato la prima giocata
            if prima_carta[0] != seconda_carta[0]:
                return 0
            # in caso di carte diverse o entrambi briscole si contano i punti di validità della carta
            elif prima_carta[0] == seconda_carta[0]:
                listaCarte = conteggioDeck[prima_carta[0]]
                index_prima_carta = listaCarte.index(prima_carta[1])
                print(index_prima_carta)
                index_seconda_carta = listaCarte.index(seconda_carta[1])
                print(index_seconda_carta)
                if index_prima_carta < index_seconda_carta:
                    return 0
                else:
                    return 1
        # condizione se giocatore 1 gioca una carta briscola
        elif self.giocoBriscola[1][0] == prima_carta[0] and self.giocoBriscola[1][0] != seconda_carta[0]:
            return 0
        # condizione se giocatore 2 gioca una carta briscola
        elif self.giocoBriscola[1][0] == seconda_carta[0] and self.giocoBriscola[1][0] != prima_carta[0]:
            return 1

    def definisciGiocata(self):
        carte = 0
        carte_giocatore_1 = []
        carte_giocatore_2 = []
        while carte < 40:
            turno = randint(0, 1)
            giocata = 1
            carte_giocate = []
            while giocata < 3:
                try:
                    giocatore = input(
                        f"{Giocatore.stampaNome(self.giocoBriscola[2][turno])} PREMI INVIO SE SEI PRONTO A GIOCARE!!")
                    print()
                    if giocatore == "":
                        Giocatore.stampaCarte(
                            self.giocoBriscola[2][turno])
                        print()
                        print("LA BRISCOLA DI GIOCO SARA'")
                        Printer.stampaCarta(self.giocoBriscola[1])
                        carta = Giocatore.giocaCarta(
                            self.giocoBriscola[2][turno])
                        carte_giocate.append(carta)
                        if turno == 0:
                            turno = 1
                        else:
                            turno = 0

                        carta_consegnata = Deck.consegnaCarta(
                            self.giocoBriscola[0])
                        Giocatore.pescaCarta(
                            self.giocoBriscola[2][turno], carta_consegnata)

                        giocata += 1

                    else:
                        print(
                            f'VALORE NON RICONOSCIUTO - {Giocatore.stampaNome(self.giocoBriscola[2][turno])} PREMI INVIO SE SEI PRONTO A GIOCARE')
                except ValueError:
                    print(
                        f'VALORE NON RICONOSCIUTO - {Giocatore.stampaNome(self.giocoBriscola[2][turno])} PREMI INVIO SE SEI PRONTO A GIOCARE')

                vincitore = Briscola.definisciPresa(
                    self.giocoBriscola, carte_giocate[0], carte_giocate[1])
                if vincitore == 0:
                    carte_giocatore_1.append(carte_giocate[0])
                    carte_giocatore_1.append(carte_giocate[1])
                    turno = 0
                if vincitore == 1:
                    carte_giocatore_2.append(carte_giocate[0])
                    carte_giocatore_2.append(carte_giocate[1])
                    turno = 1

                carte_giocate.clear()
                giocata = 1
                carte += 1


if __name__ == "__main__":
    gioco = Briscola()
    Briscola.definisciGiocata(gioco)
