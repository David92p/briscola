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

    

    def inizio(self):
        random_start = randint(0, 1)
        print(
            f"INIZIERA' IL GIOCATORE {Giocatore.stampaNome(self.giocoBriscola[2][random_start])}")

        conteggio = [self.giocoBriscola[1]]
        giocatore_1 = []
        giocatore_2 = []

        while True:
            try:
                first_start = input(
                    f"{Giocatore.stampaNome(self.giocoBriscola[2][random_start])} PREMI INVIO SE SEI PRONTO A GIOCARE!!")
                print()
                if first_start == "":
                    Giocatore.stampaCarte(self.giocoBriscola[2][random_start])
                    print()
                    print("LA BRISCOLA DI GIOCO SARA'")
                    Printer.stampaCarta(self.giocoBriscola[1])
                    break
                else:
                    print(
                        f'VALORE NON RICONOSCIUTO - {Giocatore.stampaNome(self.giocoBriscola[2][random_start])} PREMI INVIO SE SEI PRONTO A GIOCARE')
            except ValueError:
                print(
                    f'VALORE NON RICONOSCIUTO - {Giocatore.stampaNome(self.giocoBriscola[2][random_start])} PREMI INVIO SE SEI PRONTO A GIOCARE')

    
            

    def test(self,prima_carta, seconda_carta):
        conteggioDeck = [["Asso Coppe", "3 di Coppe", "Re di Coppe", "Donna di Coppe", "Cavallo di Coppe", "7 di Coppe",
                            "6 di Coppe", "5 di Coppe", "4 di Coppe", "2 di Coppe"],
                        ["Asso Spade", "3 di Spade", "Re di Spade", "Donna di Spade", "Cavallo di Spade", "7 di Spade",
                            "6 di Spade", "5 di Spade", "4 di Spade", "2 di Spade"],
                        ["Asso Bastoni", "3 di Bastoni", "Re di Bastoni", "Donna di Bastoni", "Cavallo di Bastoni", "7 di Bastoni",
                            "6 di Bastoni", "5 di Bastoni", "4 di SBastoni", "2 di Bastoni"],
                        ["Asso Denari", "3 di Denari", "Re di Denari", "Donna di Denari", "Cavallo di Denari", "7 di Denari",
                            "6 di Denari", "5 di Denari", "4 di Denari", "2 di Denari"]]
 
        if self.giocoBriscola[1][0] != prima_carta[0] and self.giocoBriscola[1][0] != seconda_carta[0]:
            if prima_carta[0] != seconda_carta[0]:
               return 0
            elif prima_carta[0] == seconda_carta[0] or self.giocoBriscola[1][0] == seconda_carta[0] and self.giocoBriscola[1][0] == prima_carta[0]:
                listaCarte = conteggioDeck[prima_carta[0]]
                index_prima_carta = listaCarte.index(prima_carta[1])
                index_seconda_carta = listaCarte.index(seconda_carta[1])
                if index_prima_carta < index_seconda_carta:
                        return 0
                else:
                    return 1
        elif self.giocoBriscola[1][0] == prima_carta[0] and self.giocoBriscola[1][0] != seconda_carta[0]:
            return 0
        elif self.giocoBriscola[1][0] == seconda_carta[0] and self.giocoBriscola[1][0] != prima_carta[0]:
            return 1
        


# test
# deck = Deck()
briscola = Briscola()  # Istanziamo un oggetto Briscola composto da un dizionario con 3 valori chiave nel seguente ordine - deck, briscola, giocatori
#Briscola.inizio(briscola)
Briscola.inizio(briscola)
print(Briscola.test(briscola, [1,"Cavallo di Spade"],[3, "Re di Denari"]))