from .deck import Deck
from .giocatore import Giocatore
from .printer import Printer
from .definisci_giocata import ValutazioneCarte


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

    # il seguente metodo definisce se ha vinto il giocatore che ha fatto la prima mossa o il secondo giocatore che ha fatto la seconda mossa
    # Il metodo sfrutta un algoritmo importato che valuta le carte in base alla giocata
    def valutaPresa(self, turno, carta_giocatore_1, carta_giocatore_2):
        carte_presa = []

        while True:
            # turno quando il giocatore 1 ha giocato la prima carta
            if turno == 0:
                vincitore = ValutazioneCarte.valutaPresaBriscola(
                    self.giocoBriscola[1], carta_giocatore_1, carta_giocatore_2)
                carte_presa.append(turno)
                carte_presa.append(vincitore)
                # in caso di vincita della prima carta giocata
                if vincitore == 0:
                    # aggiungo la prima carta alle prese del giocatore 1
                    carte_presa.append(carta_giocatore_1)
                    # aggiungo la seconda carta alle prese del giocatore 1
                    carte_presa.append(carta_giocatore_2)
                    prima_carta_consegnata = Deck.consegnaCarta(
                        self.giocoBriscola[0])
                    # condizione in caso di 2 carte in mano al giocatore 1
                    if Giocatore.lunghezzaCarte(self.giocoBriscola[2][0]) == 2 and prima_carta_consegnata != '':
                        Giocatore.pescaCarta(
                            self.giocoBriscola[2][0], prima_carta_consegnata)
                    else:
                        return carte_presa

                    seconda_carta_consegnata = Deck.consegnaCarta(
                        self.giocoBriscola[0])
                    # condizione in caso di 2 carte in mano al giocatore perdente e deck vuoto - giocatore prende la briscola sul tavolo
                    if Giocatore.lunghezzaCarte(self.giocoBriscola[2][1]) == 2 and seconda_carta_consegnata == '':
                        Giocatore.pescaCarta(
                            self.giocoBriscola[2][1], self.giocoBriscola[1])
                    # condizione in caso di 2 carte in mano al giocatore perdente
                    elif Giocatore.lunghezzaCarte(self.giocoBriscola[2][1]) == 2:
                        Giocatore.pescaCarta(
                            self.giocoBriscola[2][1], seconda_carta_consegnata)

                    return carte_presa

                # in caso di vincita della seconda carta giocata
                elif vincitore == 1:
                    # aggiungo la prima carta alle prese del giocatore 2
                    carte_presa.append(carta_giocatore_1)
                    # aggiungo la seconda carta alle prese del giocatore 2
                    carte_presa.append(carta_giocatore_2)
                    prima_carta_consegnata = Deck.consegnaCarta(
                        self.giocoBriscola[0])
                    # condizione in caso di 2 carte in mano al giocatore 2
                    if Giocatore.lunghezzaCarte(self.giocoBriscola[2][1]) == 2 and prima_carta_consegnata != '':
                        Giocatore.pescaCarta(
                            self.giocoBriscola[2][1], prima_carta_consegnata)
                    else:
                        return carte_presa

                    seconda_carta_consegnata = Deck.consegnaCarta(
                        self.giocoBriscola[0])
                    # condizione in casa di 2 carte in mano al giocatore perdente e deck vuoto - giocatore prende la briscola sul tavolo
                    if Giocatore.lunghezzaCarte(self.giocoBriscola[2][0]) == 2 and seconda_carta_consegnata == '':
                        Giocatore.pescaCarta(
                            self.giocoBriscola[2][0], self.giocoBriscola[1])
                    # condizione in casa di 2 carte in mano al giocatore perdente
                    elif Giocatore.lunghezzaCarte(self.giocoBriscola[2][0]) == 2:
                        Giocatore.pescaCarta(
                            self.giocoBriscola[2][0], seconda_carta_consegnata)

                    return carte_presa

            # turno quando il giocatore 2 ha effettuato la prima giocata
            elif turno == 1:
                vincitore = ValutazioneCarte.valutaPresaBriscola(
                    self.giocoBriscola[1], carta_giocatore_2, carta_giocatore_1)
                carte_presa.append(turno)
                carte_presa.append(vincitore)
                # in caso di vincita della prima carta giocata
                if vincitore == 0:
                    # aggiungo la prima carta alle prese del giocatore 2
                    carte_presa.append(carta_giocatore_2)
                    # aggiungo la seconda carta alle prese del giocatore 2
                    carte_presa.append(carta_giocatore_1)
                    prima_carta_consegnata = Deck.consegnaCarta(
                        self.giocoBriscola[0])
                    # condizione in caso di 2 carte in mano al giocatore 2
                    if Giocatore.lunghezzaCarte(self.giocoBriscola[2][1]) == 2 and prima_carta_consegnata != '':
                        Giocatore.pescaCarta(
                            self.giocoBriscola[2][1], prima_carta_consegnata)
                    else:
                        return carte_presa

                    seconda_carta_consegnata = Deck.consegnaCarta(
                        self.giocoBriscola[0])
                    # condizione in casa di 2 carte in mano al giocatore perdente e deck vuoto - giocatore prende la briscola sul tavolo
                    if Giocatore.lunghezzaCarte(self.giocoBriscola[2][0]) == 2 and seconda_carta_consegnata == '':
                        Giocatore.pescaCarta(
                            self.giocoBriscola[2][0], self.giocoBriscola[1])
                    # condizione in casa di 2 carte in mano al giocatore perdente
                    elif Giocatore.lunghezzaCarte(self.giocoBriscola[2][0]) == 2:
                        Giocatore.pescaCarta(
                            self.giocoBriscola[2][0], seconda_carta_consegnata)

                    return carte_presa

                # in caso di vincita della seconda carta giocata
                elif vincitore == 1:
                    # aggiungo la prima carta alle prese del giocatore 1
                    carte_presa.append(carta_giocatore_2)
                    # aggiungo la seconda carta alle prese del giocatore 1
                    carte_presa.append(carta_giocatore_1)
                    prima_carta_consegnata = Deck.consegnaCarta(
                        self.giocoBriscola[0])
                    if Giocatore.lunghezzaCarte(self.giocoBriscola[2][0]) == 2 and prima_carta_consegnata != '':
                        Giocatore.pescaCarta(
                            self.giocoBriscola[2][0], prima_carta_consegnata)
                    # condizione in caso di 1 carta in mano al giocatore 1
                    else:
                        return carte_presa

                    seconda_carta_consegnata = Deck.consegnaCarta(
                        self.giocoBriscola[0])
                    # condizione in casa di 2 carte in mano al giocatore perdente e deck vuoto - giocatore prende la briscola sul tavolo
                    if Giocatore.lunghezzaCarte(self.giocoBriscola[2][1]) == 2 and seconda_carta_consegnata == '':
                        Giocatore.pescaCarta(
                            self.giocoBriscola[2][1], self.giocoBriscola[1])
                    # condizione in casa di 2 carte in mano al giocatore perdente
                    elif Giocatore.lunghezzaCarte(self.giocoBriscola[2][1]) == 2:
                        Giocatore.pescaCarta(
                            self.giocoBriscola[2][1], seconda_carta_consegnata)

                    return carte_presa

    # Il seguente metodo si occupa di mostrare a video le carte dei nostri giocatori attraverso i suoi metodi
    # Il metodo, dopo una valutazione di presa, si occupa di far proseguire il gioco fino all'esaurimento del deck
    def inizioGiocoBriscola(self):
        carte = 0
        turno = 0
        carte_primo = []
        carte_secondo = []

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

            risultato = Briscola.valutaPresa(
                self, turno, carta_giocatore_1, carta_giocatore_2)

            if risultato[0] == 0:
                if risultato[1] == 0:
                    carte_primo.append(risultato[2][1])
                    carte_primo.append(risultato[3][1])
                    print(
                        f'QUESTO GIRO PRENDE {Giocatore.stampaNome(self.giocoBriscola[2][0])}')
                    print()
                    turno = 0
                elif risultato[1] == 1:
                    carte_secondo.append(risultato[2][1])
                    carte_secondo.append(risultato[3][1])
                    print(
                        f'QUESTO GIRO PRENDE {Giocatore.stampaNome(self.giocoBriscola[2][1])}')
                    print()
                    turno = 1

                carte += 2

            elif risultato[0] == 1:
                if risultato[1] == 0:
                    carte_secondo.append(risultato[2][1])
                    carte_secondo.append(risultato[3][1])
                    print(
                        f'QUESTO GIRO PRENDE {Giocatore.stampaNome(self.giocoBriscola[2][1])}')
                    print()
                    turno = 1
                elif risultato[1] == 1:
                    carte_primo.append(risultato[2][1])
                    carte_primo.append(risultato[3][1])
                    print(
                        f'QUESTO GIRO PRENDE {Giocatore.stampaNome(self.giocoBriscola[2][0])}')
                    print()
                    turno = 0
                carte += 2

        # Inseriamo all'interno di una lista le carte raccolte dai giocatori per poterle conteggiare
        carte_prese = []
        carte_prese.append(carte_primo)
        carte_prese.append(carte_secondo)
        return carte_prese


# test
if __name__ == "__main__":
    gioco = Briscola()
    Briscola.inizioGiocoBriscola(gioco)
