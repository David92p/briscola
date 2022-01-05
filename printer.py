
class Printer:

    def stampaCartegiocatore(carte):
<<<<<<< HEAD
        oriz = '+'+'-'*25+'+'
        if len(carte) == 1:
            print(oriz)
            print('+' + carte[0][1].upper().center(25, " ") + '+')
=======
        oriz = '+'+'-'*20+'+'
        if len(carte) == 1:
            print(oriz)
            print('+' + carte[0][1].upper().center(20, " ") + '+')
>>>>>>> giocatore
            print(oriz)
        elif len(carte) == 2:
            print(oriz, end=" ")
            print(oriz)
<<<<<<< HEAD
            print('+' + carte[0][1].upper().center(25, " ") + '+', end=" ")
            print('+' + carte[1][1].upper().center(25, " ") + '+')
=======
            print('+' + carte[0][1].upper().center(20, " ") + '+', end=" ")
            print('+' + carte[1][1].upper().center(20, " ") + '+')
>>>>>>> giocatore
            print(oriz, end=" ")
            print(oriz)
        elif len(carte) == 3:
            print(oriz, end=" ")
            print(oriz, end=" ")
            print(oriz)
<<<<<<< HEAD
            print('+' + carte[0][1].upper().center(25, " ") + '+', end=" ")
            print('+' + carte[1][1].upper().center(25, " ") + '+', end=" ")
            print('+' + carte[2][1].upper().center(25, " ") + '+')
=======
            print('+' + carte[0][1].upper().center(20, " ") + '+', end=" ")
            print('+' + carte[1][1].upper().center(20, " ") + '+', end=" ")
            print('+' + carte[2][1].upper().center(20, " ") + '+')
>>>>>>> giocatore
            print(oriz, end=" ")
            print(oriz, end=" ")
            print(oriz)

    def stampaCarta(lista):
<<<<<<< HEAD
        oriz = '+'+'-'*25+'+'
        print(oriz)
        print('+' + lista[1].upper().center(25, " ") + '+')
        print(oriz)
=======
        oriz = '+'+'-'*20+'+'
        print(oriz)
        print('+' + lista[1].upper().center(20, " ") + '+')
        print(oriz)      

    
>>>>>>> giocatore
