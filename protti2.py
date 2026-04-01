# ## Esercizio 2
# Verifica un codice alfanumerico (solo lettere e cifre) con queste regole:
# - almeno 8 caratteri;
# - primo carattere maiuscolo;
# - almeno una lettera minuscola;
# - almeno una cifra;
# - contiene solo lettere e cifre (niente spazi o caratteri speciali);
# - non deve essere nella lista `CODICI_COMUNI = ["abc12345", "student01", "prova000", "admin999"]`.

# ### Istruzioni
# Definisci le funzioni:
# - `analizza_codice(codice: str) -> dict[str, int]`: conta quante lettere maiuscole, minuscole e cifre ci sono nel codice e restituisce un dizionario con queste chiavi:
# 	- `"maiuscole"`
# 	- `"minuscole"`
# 	- `"cifre"`
  
# 	Esempio: per `Abc12346` deve restituire qualcosa come `{"maiuscole": 1, "minuscole": 2, "cifre": 5}`.
# - `valida_codice(codice: str) -> bool`: controlla se il codice rispetta tutte le regole e restituisce `True` oppure `False`. 
# Per verificare che contenga solo lettere e cifre, 
# puoi controllare che la somma (maiuscole + minuscole + cifre) sia uguale alla lunghezza del codice.
# - `livello_codice(codice: str) -> int`: assegna un livello da 1 a 3 in base alla lunghezza e al numero di maiuscole o cifre.

# Nel `main()`, chiedi il codice e stampa:
# - `Valido (Livello X)` se è valido;
# - `Non valido` altrimenti.


def analizza_codice(codice: str) -> dict[str, int]:
    testo = input("inserisci un testo: ")
    if not testo:
        print("errore: testo vuoto")
        exit()
    num_maiuscole = len(testo)
    parole = testo.split()
    num_minuscole= len(minuscole)
    frasi = testo.split(".")
    num_cifre = len(cifre)


# def livello_codice(codice: str) -> int:
