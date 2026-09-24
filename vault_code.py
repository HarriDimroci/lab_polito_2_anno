import random

# Costanti del gioco
CODICE_MIN = 1
CODICE_MAX = 50
TENTATIVI_BASE = 6
TENTATIVI_MIN = 3
MAX_LIVELLO = 3


def dai_indizio(tentativo, codice):
    """Restituisce un indizio confrontando il tentativo con il codice segreto"""
    # TODO
    if tentativo < codice:
        indizio = "Più alto"
    else:
        indizio = "Più basso"
    return indizio


def stampa_tentativi(n, usati):
    """Stampa la riga dei tentativi: O = disponibile, X = già usato"""
    # TODO
    tentativi = []
    for i in range(n):
        if i < usati:
            tentativi.append("X")
        else:
            tentativi.append("O")
    print(" ".join(tentativi))

def gestisci_livello(livello):
    """ Gestisce un singolo livello del gioco.
    Ritorna:
    * True se il giocatore indovina il codice
    * False se il giocatore esaurisce i tentativi.

    NB: Le funzioni dai_indizio() e stampa_tentativi() vanno chiamate dentro questa funzione
    """

    # Inizializzazioni
    n = TENTATIVI_BASE - livello
    if n < TENTATIVI_MIN:
        n = TENTATIVI_MIN

    codice = random.randint(CODICE_MIN, CODICE_MAX)
    print(codice)
    usati = 0

    # TODO
    print(f"Livello {livello}) {n} tentativi")
    completato = False
    while usati < n:
        stampa_tentativi(n,usati)
        try:
            tentativo = int(input("Tentativo: "))
        except ValueError:
            print("Inserisci un numero")
            usati += 1
            continue
        if tentativo < CODICE_MIN or tentativo > CODICE_MAX:
            print("Tentativo invalido")
            usati += 1
            continue
        if tentativo == codice:
            print("Accesso consentito!")
            completato = True
            break
        else:
            usati += 1
        indizio = dai_indizio(tentativo,codice)
        print(indizio)
    if not completato:
        print("GAME OVER")
        stampa_tentativi(n,usati)
    return completato


def main():
    print("=== Benvenuto in Vault Code ===")
    livello = 0

    while livello <= MAX_LIVELLO:
        completato = gestisci_livello(livello)
        if completato:
            livello += 1
        else:
            break
    if livello > MAX_LIVELLO:
        print("WIN!!!")
if __name__ == "__main__":
    main()
