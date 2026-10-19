def carica_da_file(file_path):
    """Carica le foto dal file, creando un nuovo anno ogni volta che compare per la prima volta"""
    album = []
    try:
        with open(file_path, 'r') as f:
            titles = f.readline().strip().split(',')
            for i in range(len(titles)):
                titles[i] = titles[i].strip()
            for line in f:
                valori = line.strip().split(',')
                foto = {}
                for t in range(len(titles)):
                    if titles[t] == "anno" or titles[t] == "mese":
                        foto[titles[t]] = int(valori[t])
                    else:
                        foto[titles[t]] = valori[t]
                trovato = False
                for a in album:
                    if a[0] == foto["anno"]:
                        a[1].append(foto)
                        trovato = True
                        break
                if not trovato:
                    album.append([foto["anno"],[foto]])
    except FileNotFoundError:
        return None
    return album

def aggiungi_foto(album, codice, titolo, autore, mese, anno, file_path):
    """Aggiunge una foto all'album, creando l'anno al volo se non è ancora presente"""
    foto = {
        "codice" : codice,
        "titolo" : titolo ,
        "autore" : autore ,
        "mese" : mese ,
        "anno" : anno
    }
    if mese < 1 or mese > 12:
        return None

    for a in album:
        for b in a[1]:
            if b["codice"] == codice:
                return None
    try:
        with open(file_path, 'r') as f:
            pass
    except FileNotFoundError:
        return None
    with open(file_path, 'a') as f:
        f.write(f"{codice},{titolo},{autore},{mese},{anno}\n")
    trovato = False
    for a in album:
        if a[0] == foto["anno"]:
            a[1].append(foto)
            trovato = True
            break
    if not trovato:
        album.append([foto["anno"], [foto]])
    return foto



def cerca_foto(album, codice):
    """Cerca una foto nell'album dato il codice"""
    for a in album:
        for c in a[1]:
            if codice == c['codice']:
                risultato = f"Codice: {c['codice']}\nTitolo: {c['titolo']}\nAutore: {c['autore']}\nMese: {c['mese']}\nAnno: {c['anno']}"
                return risultato
    return None

def elenco_foto_anno_per_titolo(album, anno):
    """Ordina i titoli delle foto di un dato anno in ordine alfabetico"""
    titoli = []
    for a in album:
        if a[0] == anno:
            for f in a[1]:
                titoli.append(f['titolo'])
    if len(titoli) > 0:
        titoli.sort()
    else:
        titoli = None

    return titoli


def main():
    album = []
    while True:
        print("\n--- MENU ALBUM FOTOGRAFICO ---")
        print("1. Carica album da file")
        print("2. Aggiungi una nuova foto")
        print("3. Cerca una foto per codice")
        print("4. Elenco foto di un anno (ordinato per titolo)")
        print("5. Esci")

        scelta = input("Scegli un'opzione >> ").strip()

        if scelta == "1":
            while True:
                file_path = input("Inserisci il path del file da caricare: ").strip()
                album = carica_da_file(file_path)
                print(album)
                if album is not None:
                    break

        elif scelta == "2":
            if not album:
                print("Prima carica l'album da file.")
                continue

            codice = input("Codice della foto: ").strip()
            titolo = input("Titolo: ").strip()
            autore = input("Autore: ").strip()
            try:
                mese = int(input("Mese (1-12): ").strip())
                anno = int(input("Anno: ").strip())
            except ValueError:
                print("Errore: inserire valori numerici validi per mese e anno.")
                continue

            foto = aggiungi_foto(album, codice, titolo, autore, mese, anno, file_path)
            if foto:
                print(f"Foto aggiunta con successo!")
            else:
                print("Non è stato possibile aggiungere la foto.")

        elif scelta == "3":
            if not album:
                print("L'album è vuoto.")
                continue

            codice = input("Inserisci il codice della foto da cercare: ").strip()
            risultato = cerca_foto(album, codice)
            if risultato:
                print(f"Foto trovata!\n{risultato}")
            else:
                print("Foto non trovata.")

        elif scelta == "4":
            if not album:
                print("L'album è vuoto.")
                continue

            try:
                anno = int(input("Inserisci l'anno da consultare: ").strip())
            except ValueError:
                print("Errore: inserire un valore numerico valido.")
                continue

            titoli = elenco_foto_anno_per_titolo(album, anno)
            if titoli is not None:
                print(f'\nFoto del {anno}:')
                print("\n".join([f"- {titolo}" for titolo in titoli]))
            else:
                print(f"Nessuna foto trovata per l'anno {anno}.")

        elif scelta == "5":
            print("Uscita dal programma...")
            break
        else:
            print("Opzione non valida. Riprova.")


if __name__ == "__main__":
    main()
