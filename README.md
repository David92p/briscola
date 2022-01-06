# BRISCOLA


CLASSE DECK:

-	Definisce un oggetto dizionario con chiave = seme (str) e valore = carte (lista)

-	Metodi: <br>
        *	Mescola Deck - Possibilità di mescolare i valori delle chiavi <br>
        *	Definisci Briscola - Possibilità di selezionare una carta in modo casuale e definirla, in questo caso, come carta/seme di briscola  <br>
        *	Consegna Carta - Possibilità di fare il return di un valore casuale all’interno delle chiavi <br>
        *	Mostra Deck - Possibilità di mostrare il deck a video – Utile per debugging <br>
        

CLASSE GIOCATORE:

-	Definisce un oggetto giocatore con chiave = nome giocatore (str) e valore = 3 carte (lista)

-	Metodi: <br>
        *	Definisci Giocatore - Permette di chiedere un input utile come nome giocatore e consegnare 3 carte dall'oggetto Deck <br>
        *	Restituisci carte - Permette di stampare a video le 3 carte dell'oggetto giocatore   <br>
        *	Lunghezza Carte - Restituisci il numero delle carte in mano del Giocatore   <br>
        *	Stampa Nome - Permette di stampare il nome del giocatore in maiuscolo   <br>
        *	Pesca Carta - Permette di inserire una carta passata come valore alla lista care del nostro giocatore   <br>
        *	Gioca Carta - Restituisce una carta tra quelle selezionate nell'elenco <br>


CLASSE PRINTER:

-	La Classe si occupa di stampare a video le carte

-	Metodi: <br>
        *	Stampa Carte Giocatore - Permette di stampare le carte del giocatore a seconda della sua quantità <br>
        *	Stampa Carta - Stampa una singola carta  <br>
        
       

