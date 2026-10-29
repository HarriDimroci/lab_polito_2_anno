import flet as ft
from alert import AlertManager
from deposito_strumenti import DepositoStrumenti

FILE_STRUMENTI = "strumenti.csv"

def main(page: ft.Page):
    page.title = "Lab05"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.theme_mode = ft.ThemeMode.DARK

    # --- ALERT ---
    alert = AlertManager(page)

    # --- LA LOGICA DELL'APPLICAZIONE E' PRESA DAL DEPOSITO DI STRUMENTI DEL LAB03 ---
    deposito = DepositoStrumenti("Deposito Strumenti Musicali", "Alessandro Visconti")
    try:
        deposito.carica_file_strumenti(FILE_STRUMENTI)  # Carica il file
    except FileNotFoundError as e:
        alert.show_alert(f"❌ {e}")  # Fa apparire una finestra che mostra l'errore

    # --- UI ELEMENTI ---

    # Text per mostrare il nome e il responsabile del deposito
    txt_titolo = ft.Text(value=deposito.nome, size=38, weight=ft.FontWeight.BOLD)
    txt_responsabile = ft.Text(
        value=f"Responsabile: {deposito.get_responsabile()}",
        size=16,
        weight=ft.FontWeight.BOLD
    )

    # TextField per responsabile
    input_responsabile = ft.TextField(value=deposito.get_responsabile(), label="Responsabile")

    # ListView per mostrare la lista di strumenti aggiornata
    lista_strumenti = ft.ListView(expand=True, spacing=5, padding=10, auto_scroll=True)

    # Tutti i TextField per le info necessarie per aggiungere un nuovo strumento (tipo, marca, anno, contatore posti)
    # TODO
    input_tipo = ft.TextField(hint_text="Tipo", text_size = 15, width = 100)
    input_marca = ft.TextField(hint_text="Marca",text_size = 15, width = 100)
    input_anno = ft.TextField(hint_text="Anno",text_size = 15, width =100)
    counter = ft.TextField(value="0", hint_text="0",width = 50 )
    # Handlers + e - prezzo

    # --- FUNZIONI APP ---
    def aggiorna_lista_strumenti():
        lista_strumenti.controls.clear()
        for strumento in deposito.strumenti_ordinati_per_marca():
            stato = "✅" if strumento.disponibile else "⛔"
            lista_strumenti.controls.append(ft.Text(f"{stato} {strumento}"))
        lista_strumenti.update()

    # --- HANDLERS APP ---
    def cambia_tema(e):
        page.theme_mode = ft.ThemeMode.DARK if toggle_cambia_tema.value else ft.ThemeMode.LIGHT
        toggle_cambia_tema.label = "Tema scuro" if toggle_cambia_tema.value else "Tema chiaro"

    def conferma_responsabile(e):
        deposito.set_responsabile(input_responsabile.value)
        txt_responsabile.value = f"Responsabile: {deposito.get_responsabile()}"

    # Handlers per la gestione dei pulsanti utili all'inserimento di un nuovo strumento
    # TODO
    def increase_counter(e):
        counter.value = int(counter.value)
        counter.value += 1
    def decrease_counter(e):
        counter.value = int(counter.value)
        counter.value -= 1

    def cancellation(e):
        input_tipo.value = ""
        input_tipo.update()
        input_marca.value = ""
        input_marca.update()
        input_anno.value = 0
        input_anno.update()
        counter.value = 0
        counter.update()

    def check_valori(e):
        aggiorna = True
        try:
            input_anno.value = int(input_anno.value)
        except (ValueError, TypeError):
            alert.show_alert(message="Inserire un anno valido!")
            aggiorna = False

        try:
            counter.value = float(counter.value)
        except (ValueError, TypeError):
            alert.show_alert(message="Inserire un valore numerico valido!")
            aggiorna = False

        return aggiorna

    def aggiungi_aggiorna(e):
        aggiorna = check_valori(e)
        if aggiorna:
            deposito.aggiungi_strumento(input_tipo.value, input_marca.value, input_anno.value, counter.value)
            cancellation(e)
            aggiorna_lista_strumenti()

    # --- EVENTI ---
    toggle_cambia_tema = ft.Switch(label="Tema scuro", value=True, on_change=cambia_tema)
    pulsante_conferma_responsabile = ft.Button("Conferma", on_click=conferma_responsabile)

    # Pulsanti per la gestione dell'inserimento di un nuovo strumento
    # TODO
    submit_nuovo_strumento = ft.Button("Aggiungere strumento", on_click=aggiungi_aggiorna)
    high_value = ft.Button("+", on_click=increase_counter)
    low_value = ft.Button("-", on_click=decrease_counter)

    # --- LAYOUT ---
    page.add(
        toggle_cambia_tema,

        # Sezione 1
        txt_titolo,
        txt_responsabile,
        ft.Divider(),

        # Sezione 2
        ft.Text("Modifica Informazioni", size=20),
        ft.Row(spacing=200,
               controls=[input_responsabile, pulsante_conferma_responsabile],
               alignment=ft.MainAxisAlignment.CENTER),
        ft.Divider(),

        # Sezione 3
        # TODO
        ft.Text("Aggiungere strumento", size=20),
        ft.Row(spacing = 40,
               controls=[input_tipo, input_marca, input_anno,  high_value,counter, low_value],
               alignment = ft.MainAxisAlignment.CENTER
               ),
        submit_nuovo_strumento,
        ft.Divider(),

        # Sezione 4
        ft.Text("Strumenti", size=20),
        lista_strumenti,
    )
    aggiorna_lista_strumenti()

ft.run(main)
