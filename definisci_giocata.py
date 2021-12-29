
class ValutazioneCarte:

    def valutaPresaBriscola(cartaBriscola, carta1, carta2):
        conteggioDeck = [["Asso Coppe", "3 di Coppe", "Re di Coppe", "Cavallo di Coppe", "Donna di Coppe", "7 di Coppe",
                          "6 di Coppe", "5 di Coppe", "4 di Coppe", "2 di Coppe"],
                         ["Asso Spade", "3 di Spade", "Re di Spade", "Cavallo di Spade", "Donna di Spade", "7 di Spade",
                          "6 di Spade", "5 di Spade", "4 di Spade", "2 di Spade"],
                         ["Asso Bastoni", "3 di Bastoni", "Re di Bastoni", "Cavallo di Bastoni", "Donna di Bastoni", "7 di Bastoni",
                          "6 di Bastoni", "5 di Bastoni", "4 di Bastoni", "2 di Bastoni"],
                         ["Asso Denari", "3 di Denari", "Re di Denari", "Cavallo di Denari", "Donna di Denari", "7 di Denari",
                          "6 di Denari", "5 di Denari", "4 di Denari", "2 di Denari"]]

        # condizione se nessuno dei due giocatori giocano una carta briscola
        if cartaBriscola[0] != carta1[0] and cartaBriscola[0] != carta2[0]: 
            # in caso di nessuna carta briscola da entrambe le parti vince il giocatore 1 che ha effettuato la prima giocata
            if carta1[0] != carta2[0]:
                return 0
            # in caso di carte diverse si contano i punti di validità della carta
            elif carta1[0] == carta2[0]:
                listaCarte = conteggioDeck[carta1[0]]
                index_prima_carta = listaCarte.index(carta1[1])
                index_seconda_carta = listaCarte.index(carta2[1])
                if index_prima_carta < index_seconda_carta:
                    return 0
                else:
                   return 1
        
        # condizione se tutti e due giocatori giocano una carta briscola
        elif cartaBriscola[0] == carta2[0] and cartaBriscola[0] == carta1[0]:
            listaCarte = conteggioDeck[carta1[0]]
            index_prima_carta = listaCarte.index(carta1[1])
            index_seconda_carta = listaCarte.index(carta2[1])
            if index_prima_carta < index_seconda_carta:
                return 0
            else:
                return 1

        # condizione se giocatore 1 gioca una carta briscola
        elif cartaBriscola[0] == carta1[0] and cartaBriscola[0] != carta2[0]:
            return 0
        # condizione se giocatore 2 gioca una carta briscola
        elif cartaBriscola[0] != carta1[0] and cartaBriscola[0] == carta2[0]:
            return 1


# test
if __name__ == "__main__":
    x = [1, "7 di Spade"]
    y = [2, "3 di Bastoni"]
    z = [1, "2 di Spade"]

    value = ValutazioneCarte.valutaPresaBriscola(x, y, z)
    print(value)
