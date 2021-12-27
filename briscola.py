from deck import Deck
from giocatore import Giocatore
from printer import Printer
from definisci_giocata import ValutazioneCarte

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

    def definisciGiocata(self):
        carte = 0
        carte_giocatore_1 = []
        carte_giocatore_2 = []
        while carte < 34:
            turno = randint(0, 1)
            giocata = 1
            
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
                        carta = Giocatore.giocaCarta(self.giocoBriscola[2][turno])
                        Printer.stampaCarta(carta)
                        
                        if turno == 0:
                            carta_primo = carta
                            turno = 1
                        else:
                            carta_secondo = carta
                            turno = 0

                        giocata += 1

                    else:
                        print(
                            f'VALORE NON RICONOSCIUTO - {Giocatore.stampaNome(self.giocoBriscola[2][turno])} PREMI INVIO SE SEI PRONTO A GIOCARE')
                except ValueError:
                    print(
                        f'VALORE NON RICONOSCIUTO - {Giocatore.stampaNome(self.giocoBriscola[2][turno])} PREMI INVIO SE SEI PRONTO A GIOCARE')

            vincitore = ValutazioneCarte.valutaPresaBriscola(
                self.giocoBriscola, carta_primo, carta_secondo)

            if vincitore == 0:
                carte_giocatore_1.append(carta_primo)
                carte_giocatore_1.append(carta_secondo)
                prima_carta_consegnata = Deck.consegnaCarta(self.giocoBriscola[0])
                Giocatore.pescaCarta(self.giocoBriscola[2][0], prima_carta_consegnata)
                seconda_carta_consegnata = Deck.consegnaCarta(self.giocoBriscola[0])
                if seconda_carta_consegnata == '':
                    Giocatore.pescaCarta(self.giocoBriscola[2][1], self.giocoBriscola[1])
                else:
                    Giocatore.pescaCarta(self.giocoBriscola[2][1], seconda_carta_consegnata)
                
                turno = 0
                print('PRENDE IL PRIMO GIOCATORE')
            
            if vincitore == 1:
                carte_giocatore_2.append(carta_primo)
                carte_giocatore_2.append(carta_secondo)
                prima_carta_consegnata = Deck.consegnaCarta(self.giocoBriscola[0])
                Giocatore.pescaCarta(self.giocoBriscola[2][1], prima_carta_consegnata)
                seconda_carta_consegnata = Deck.consegnaCarta(self.giocoBriscola[0])
                if seconda_carta_consegnata == '':
                    Giocatore.pescaCarta(self.giocoBriscola[2][0], self.giocoBriscola[1])
                else:
                    Giocatore.pescaCarta(self.giocoBriscola[2][0], seconda_carta_consegnata)

                turno = 1
                print('PRENDE IL SECONDO GIOCATORE')


            giocata = 1
            carte += 2
        

        print('fine gioco')
        print(carte_giocatore_1)     
        print(carte_giocatore_2)          
            
            
            


if __name__ == "__main__":
    gioco = Briscola()
    Briscola.definisciGiocata(gioco)
