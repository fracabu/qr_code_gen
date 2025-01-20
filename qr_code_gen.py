import tkinter as tk
from tkinter import filedialog, messagebox
import qrcode
from PIL import Image

def genera_qr_code():
    """
    Genera un codice QR con i dati inseriti dall'utente e lo salva nel percorso specificato.
    """
    # Ottieni i dati e il percorso del file dall'interfaccia
    dati = entry_dati.get()
    percorso_file = entry_file.get()

    if not dati:
        messagebox.showerror("Errore", "Inserisci i dati da codificare nel QR code.")
        return

    if not percorso_file:
        messagebox.showerror("Errore", "Seleziona un percorso per salvare il QR code.")
        return

    # Crea il QR code
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )
    qr.add_data(dati)
    qr.make(fit=True)

    # Crea l'immagine del QR code
    qr_img = qr.make_image(fill_color="black", back_color="white").convert('RGB')

    # Salva l'immagine
    qr_img.save(percorso_file)
    messagebox.showinfo("Successo", f"QR code salvato con successo in {percorso_file}")


def seleziona_file():
    """
    Apre una finestra di dialogo per selezionare il percorso e il nome del file.
    """
    percorso_file = filedialog.asksaveasfilename(
        defaultextension=".png",
        filetypes=[("PNG files", "*.png"), ("JPEG files", "*.jpg"), ("All files", "*.*")]
    )
    if percorso_file:
        entry_file.delete(0, tk.END)
        entry_file.insert(0, percorso_file)


# Creazione della finestra principale
root = tk.Tk()
root.title("Generatore di QR Code")

# Creazione dei widget
label_dati = tk.Label(root, text="Inserisci i dati da codificare:")
entry_dati = tk.Entry(root, width=40)

label_file = tk.Label(root, text="Seleziona il percorso per salvare il QR code:")
entry_file = tk.Entry(root, width=40)
button_file = tk.Button(root, text="Sfoglia...", command=seleziona_file)

button_genera = tk.Button(root, text="Genera QR Code", command=genera_qr_code)

# Posizionamento dei widget nella finestra
label_dati.grid(row=0, column=0, padx=10, pady=5, sticky="w")
entry_dati.grid(row=0, column=1, padx=10, pady=5)

label_file.grid(row=1, column=0, padx=10, pady=5, sticky="w")
entry_file.grid(row=1, column=1, padx=10, pady=5)
button_file.grid(row=1, column=2, padx=10, pady=5)

button_genera.grid(row=2, column=1, pady=10)

# Avvio dell'interfaccia
root.mainloop()