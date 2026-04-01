# ## Esercizio 1
# Chiedi quanti numeri inserire (`n > 0`), leggi i numeri e salvali in una lista.

# Il programma deve:
# - creare una lista con i numeri positivi e pari;
# - contare i numeri dispari negativi;
# - calcolare la media assoluta dei numeri;
# - stampare lista inserita, lista filtrata, conteggio e media.

# ### Esempio
# Input: `2, -3, 4, -5, 6`

# Output:
# - `Lista inserita: [2, -3, 4, -5, 6]`
# - `Positivi pari: [2, 4, 6]`
# - `Conteggio dispari negativi: 2`
# - `Media assoluta: 4.0`

# ---

n: int = int(input("quanti numeri vuoi inserire?: "))
if n <= 0:
    print("errore devi inserire un numero positivo")
else:
    lista_numeri = []
    lista_pari = []
    lista_dispari = []
    
    for _ in range(n):
        n_inserito: int = int(input("inserisci un numero:"))
        lista_numeri.append(n_inserito)
    print(f"la mia lista{lista_numeri}")

    
    for num in lista_numeri:
        if num > 0 and num %2 == 0:
            lista_pari.append(num)
        conteggio_numeri_pari = 0

    for num in lista_numeri:
        if num > 0 and num %2 != 0:
            lista_dispari.append(num)
        conteggio_numeri_dispari = 0


    

    

    
    somma: int = 0
    for numero in lista_numeri:
        somma = somma + numero
    print(f"la somma è {somma}")
    if n != 0:
        media_assoluta: float = somma /n
    else:
        media: float = 0.0

    if lista_numeri == []:
        print("la lista è vuota")

    print(f"la media è: {media_assoluta:.2f}")
    print(f"numeri pari: {lista_pari}")
    print(f"i numeri dispari: {lista_dispari}")
 




