from deck import Deck
from giocatore import Giocatore
from printer import Printer
from definisci_giocata import ValutazioneCarte


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

    def definisciGiocata(self):
        carte = 0
        turno = 0
        carte_primo = []
        carte_secondo = []
        # if Giocatore.stampaCarte(self.giocoBriscola[2][turno]) == 0:
        #   return 'FINE GIOCO'

        while carte < 40:
            giocata = 1
            print("LA BRISCOLA DI GIOCO SARA'")
            Printer.stampaCarta(self.giocoBriscola[1])
            while giocata < 3:
                try:
                    giocatore = input(
                        f"{Giocatore.stampaNome(self.giocoBriscola[2][turno])} PREMI INVIO SE SEI PRONTO A GIOCARE!!")
                    print()
                    if giocatore == "":
                        if turno == 0:
                            carta = Giocatore.giocaCarta(
                                self.giocoBriscola[2][turno])
                            carta_giocatore_1 = carta
                            Printer.stampaCarta(carta_giocatore_1)
                            turno = 1

                        elif turno == 1:
                            carta = Giocatore.giocaCarta(
                                self.giocoBriscola[2][turno])
                            carta_giocatore_2 = carta
                            Printer.stampaCarta(carta_giocatore_2)
                            turno = 0

                        giocata += 1

                    else:
                        print(
                            f'VALORE NON RICONOSCIUTO - {Giocatore.stampaNome(self.giocoBriscola[2][turno])} PREMI INVIO SE SEI PRONTO A GIOCARE')
                except ValueError:
                    print(
                        f'VALORE NON RICONOSCIUTO - {Giocatore.stampaNome(self.giocoBriscola[2][turno])} PREMI INVIO SE SEI PRONTO A GIOCARE')

            while True:
                if turno == 0:
                    vincitore = ValutazioneCarte.valutaPresaBriscola(
                        self.giocoBriscola[1], carta_giocatore_1, carta_giocatore_2)
                    if vincitore == 0:
                        carte_primo.append(carta_giocatore_1)
                        carte_primo.append(carta_giocatore_2)
                        prima_carta_consegnata = Deck.consegnaCarta(
                            self.giocoBriscola[0])
                        Giocatore.pescaCarta(
                            self.giocoBriscola[2][0], prima_carta_consegnata)
                        seconda_carta_consegnata = Deck.consegnaCarta(
                            self.giocoBriscola[0])
                        if seconda_carta_consegnata == '' and Giocatore.lunghezzaCarte(self.giocoBriscola[2][turno]) == 2:
                            Giocatore.pescaCarta(
                                self.giocoBriscola[2][1], self.giocoBriscola[1])
                        elif Giocatore.lunghezzaCarte(self.giocoBriscola[2][turno]) == 1:
                            break
                        else:
                            Giocatore.pescaCarta(
                                self.giocoBriscola[2][1], seconda_carta_consegnata)

                        turno = 0
                        print(
                            f'QUESTO GIRO PRENDE {Giocatore.stampaNome(self.giocoBriscola[2][0])}')

                    elif vincitore == 1:
                        carte_secondo.append(carta_giocatore_1)
                        carte_secondo.append(carta_giocatore_2)
                        prima_carta_consegnata = Deck.consegnaCarta(
                            self.giocoBriscola[0])
                        Giocatore.pescaCarta(
                            self.giocoBriscola[2][1], prima_carta_consegnata)
                        seconda_carta_consegnata = Deck.consegnaCarta(
                            self.giocoBriscola[0])
                        if seconda_carta_consegnata == '':
                            Giocatore.pescaCarta(
                                self.giocoBriscola[2][0], self.giocoBriscola[1])
                        else:
                            Giocatore.pescaCarta(
                                self.giocoBriscola[2][0], seconda_carta_consegnata)

                        turno = 1
                        print(
                            f'QUESTO GIRO PRENDE {Giocatore.stampaNome(self.giocoBriscola[2][1])}')

                    print()

                    giocata = 1
                    carte += 2
                    break

                elif turno == 1:
                    vincitore = ValutazioneCarte.valutaPresaBriscola(
                        self.giocoBriscola[1], carta_giocatore_2, carta_giocatore_1)
                    if vincitore == 0:
                        carte_secondo.append(carta_giocatore_2)
                        carte_secondo.append(carta_giocatore_1)
                        prima_carta_consegnata = Deck.consegnaCarta(
                            self.giocoBriscola[0])
                        Giocatore.pescaCarta(
                            self.giocoBriscola[2][1], prima_carta_consegnata)
                        seconda_carta_consegnata = Deck.consegnaCarta(
                            self.giocoBriscola[0])
                        if seconda_carta_consegnata == '':
                            Giocatore.pescaCarta(
                                self.giocoBriscola[2][0], self.giocoBriscola[1])
                        else:
                            Giocatore.pescaCarta(
                                self.giocoBriscola[2][0], seconda_carta_consegnata)

                        turno = 1
                        print(
                            f'QUESTO GIRO PRENDE {Giocatore.stampaNome(self.giocoBriscola[2][1])}')

                    elif vincitore == 1:
                        carte_primo.append(carta_giocatore_2)
                        carte_primo.append(carta_giocatore_1)
                        prima_carta_consegnata = Deck.consegnaCarta(
                            self.giocoBriscola[0])
                        Giocatore.pescaCarta(
                            self.giocoBriscola[2][0], prima_carta_consegnata)
                        seconda_carta_consegnata = Deck.consegnaCarta(
                            self.giocoBriscola[0])
                        if seconda_carta_consegnata == '':
                            Giocatore.pescaCarta(
                                self.giocoBriscola[2][1], self.giocoBriscola[1])
                        else:
                            Giocatore.pescaCarta(
                                self.giocoBriscola[2][1], seconda_carta_consegnata)

                        turno = 0
                        print(
                            f'QUESTO GIRO PRENDE {Giocatore.stampaNome(self.giocoBriscola[2][0])}')

                    print()

                    giocata = 1
                    carte += 2
                    break

        print(carta_giocatore_1)
        print(carta_giocatore_2)
        print('fine gioco')


if __name__ == "__main__":
    gioco = Briscola()
    Briscola.definisciGiocata(gioco)
