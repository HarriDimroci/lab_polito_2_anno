class Stand:
    def __init__(self,codice,m_quadri,padiglione,prezzo):
        self.codice = codice
        self.m_quadri = m_quadri
        self.padiglione = padiglione
        self.prezzo = prezzo
        self.occupato = False
    def calcola_prezzo(self):
        return self.prezzo

    def __str__(self):
        return f"Codice: {self.codice}, Prezzo: €{self.calcola_prezzo():.2f}"

class StandPreseExtra(Stand):
    def __init__(self,codice,m_quadri,padiglione,prezzo,prese_extra):
        super().__init__(codice, m_quadri, padiglione, prezzo)
        self.prese_extra = prese_extra
    def calcola_prezzo(self):
        return self.prezzo*(1+(0.07*self.prese_extra))

class StandPremium(Stand):
    def __init__(self,codice,m_quadri,padiglione,prezzo,premium):
        super().__init__(codice,m_quadri,padiglione,prezzo)
        self.premium = premium
    def calcola_prezzo(self):
        return self.prezzo+(self.prezzo*30/100)

class Espositore:
    def __init__(self,codice,nome,cognome):
        self.codice = codice
        self.nome = nome
        self.cognome = cognome
        self.stand_ass = None

class LingottoFiere:
    def __init__(self, nome):
        """Inizializza gli attributi e le strutture dati"""
        self.nome = nome
        self.stand = []
        self.espositori = []

    """Aggiungere setter e getter se necessari"""
    # TODO
    def get_nome(self):
        nome = self.nome
        return nome
    def set_nome(self,nuovo_nome):
        self.nome = nuovo_nome

    def carica_file_dati(self, file_path):
        """Carica stand ed espositori dal file CSV"""
        with open(file_path, 'r') as f:
            for l in f:
                line = l.strip().split(',')
                if line[0].startswith("ST"):
                    if len(line) == 4:
                        stand = Stand(
                            line[0], int(line[1]), int(line[2]), int(line[3])
                        )
                    elif line[4].isnumeric():
                        stand = StandPreseExtra(
                            line[0], int(line[1]), int(line[2]),
                            int(line[3]), int(line[4])
                        )
                    else:
                        stand = StandPremium(
                            line[0], int(line[1]), int(line[2]),
                            int(line[3]), line[4]
                        )
                    self.stand.append(stand)
                elif line[0].startswith("ES"):
                    espositore = Espositore(
                        line[0], line[1], line[2]
                    )
                    self.espositori.append(espositore)

    def assegna_stand_a_espositore(self, codice_stand, codice_espositore):
        """Associa uno stand a un espositore"""
        # TODO
        stand_trovato = None
        for s in self.stand:
           if s.codice == codice_stand:
               stand_trovato = s
               break
        if stand_trovato is None:
            print("Stand non trovato")
            return
        espositore_trovato = None
        for e in self.espositori:
           if e.codice == codice_espositore:
               espositore_trovato = e
               break
        if espositore_trovato is None:
            print("Espositore non trovato")
            return
        if stand_trovato.occupato:
            print("Stand occupato")
            return
        if espositore_trovato.stand_ass:
            print("Espositore occupato")
            return
        espositore_trovato.stand_ass = stand_trovato
        stand_trovato.occupato = True
        return True

    def elenca_espositori(self):
        """Stampa l'elenco degli espositori mostrando, per ognuno, lo stand a cui è associato, quando applicabile """
        # TODO
        for e in self.espositori:
            print(f"Nome: {e.nome}\nCognome:{e.cognome}")
            if e.stand_ass:
                print(f"Espone allo stand: {e.stand_ass.codice}")
            else:
                print("Nessuno stand assegnato")

    def stand_ordinati_per_prezzo(self):
        """Restituisce la lista ordinata degli stand in base al prezzo"""
        # TODO
        stand_ordinati = sorted(self.stand,key = lambda x:x.calcola_prezzo())
        return stand_ordinati
