
class Printer:

    def stampaCartegiocatore(carte):
        oriz = '+'+'-'*20+'+'
        if len(carte) == 1:
            print(oriz)
            print('+' + carte[0][1].upper().center(20, " ") + '+')
            print(oriz)
        elif len(carte) == 2:
            print(oriz, end=" ")
            print(oriz)
            print('+' + carte[0][1].upper().center(20, " ") + '+', end=" ")
            print('+' + carte[1][1].upper().center(20, " ") + '+')
            print(oriz, end=" ")
            print(oriz)
        elif len(carte) == 3:
            print(oriz, end=" ")
            print(oriz, end=" ")
            print(oriz)
            print('+' + carte[0][1].upper().center(20, " ") + '+', end=" ")
            print('+' + carte[1][1].upper().center(20, " ") + '+', end=" ")
            print('+' + carte[2][1].upper().center(20, " ") + '+')
            print(oriz, end=" ")
            print(oriz, end=" ")
            print(oriz)

    def stampaCarta(lista):
        oriz = '+'+'-'*20+'+'
        print(oriz)
        print('+' + lista[1].upper().center(20, " ") + '+')
        print(oriz)      

    
