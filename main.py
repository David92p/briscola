from briscola.briscola import Briscola
from briscola.giocatore import Giocatore
from briscola.definisci_giocata import ValutazioneCarte

import argparse


def arcade(s):

    while True:
        print(
            """
        ECCO I GIOCHI DISPONIBILI NELLA NOSTRA CONSOLE:

        1. BRISCOLA

        """
        )

        try:
            n = int(input(
                'SELEZIONA IL NUMERO DEL GIOCO A CUI VUOI GIOCARE OPPURE PREMI ZERO PER USCIRE '))

            if n == 1:
                gioco = Briscola()
                carte_prese = Briscola.inizioGiocoBriscola(gioco)
                punteggio = ValutazioneCarte.conteggioPuntiBriscola(
                    carte_prese)
                print(
                    f'Punteggio {Giocatore.stampaNome(gioco.giocoBriscola[2][0])}: {punteggio[0]}')
                print(
                    f'Punteggio {Giocatore.stampaNome(gioco.giocoBriscola[2][1])}: {punteggio[1]}')
                print()
                if punteggio[0] > punteggio[1]:
                    print(
                        f'COMPLIMENTI A {Giocatore.stampaNome(gioco.giocoBriscola[2][0])} CHE SI AGGIUDICA LA PARTITA')
                    print()
                elif punteggio[0] < punteggio[1]:
                    print(
                        f'COMPLIMENTI A {Giocatore.stampaNome(gioco.giocoBriscola[2][1])} CHE SI AGGIUDICA LA PARTITA')
                    print()
                else:
                    print(
                        f'INCREDIBILE MA ABBIAMO UN PAREGGIO, ENTRAMBI AVETE FATTO 60 PUNTI !!!')
                    print()
            elif n == 0:
                print('CI VEDIAMO PRESTO !!')
                break
            else:
                print()
                print(
                    'Un pò di pazienza, con il tempo arriveranno altri giochi sulla nostra console')
                print()

        except ValueError:
            print()
            print("Utilizza la tastiera numerica")
            print()


parser = argparse.ArgumentParser(
    description="""
        BENVENUTI NELLA NOSRA CONSOLE DI CARTE DA TAVOLO!!!

        ECCO I GIOCHI DISPONIBILI NELLA NOSTRA CONSOLE:

        1. BRISCOLA

        """)
parser.add_argument(
    "-s", "-start", type=int,  help="INSERISCI IL NUMERO DEL GIOCO A CUI VUOI GIOCARE", choices=[1])
args = parser.parse_args()

# test
if __name__ == "__main__":
    arcade(args)
