import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from pathlib import Path
import webbrowser


def _texte_nombre_partiel_valide(texte):
    if texte == "":
        return True

    separateur_trouve = False
    for index, caractere in enumerate(texte):
        if caractere.isdigit():
            continue

        if caractere == "-":
            if index != 0:
                return False
            continue

        if caractere in ",.":
            if separateur_trouve:
                return False
            separateur_trouve = True
            continue

        return False

    return True


def _lire_nombre(champ):
    texte = champ.get().strip().replace(",", ".")
    if texte in ("", "-", ".", "-."):
        return None
    try:
        return float(texte)
    except ValueError:
        return None


def _ecrire_nombre(champ, valeur):
    champ.delete(0, tk.END)
    champ.insert(0, f"{valeur:.2f}")


def ouvrir_aide():
    chemin_aide = Path(__file__).with_name("aide.html")
    if not chemin_aide.exists():
        messagebox.showerror("Erreur", "Le fichier d'aide est introuvable.")
        return

    webbrowser.open(chemin_aide.resolve().as_uri())


def creer_contenu_a_propos(parent):
    label_nom = tk.Label(parent, text="Développé par Greg", font=("Arial", 12))
    label_nom.pack(pady=(12, 8))

    label_site = tk.Label(
        parent,
        text="Site : https://ti.gregland.net",
        font=("Arial", 10),
        fg="blue",
        cursor="hand2",
    )
    label_site.pack(pady=5)
    label_site.bind("<Button-1>", lambda event: webbrowser.open("https://ti.gregland.net"))

    label_mail = tk.Label(parent, text="Email : gregory.hargous@gmail.com", font=("Arial", 10))
    label_mail.pack(pady=5)


def mettre_a_jour_depuis_ht(entry_ht, entry_ttc, entry_tva, event=None):
    prix_ht = _lire_nombre(entry_ht)
    taux_tva = _lire_nombre(entry_tva)
    if prix_ht is None or taux_tva is None:
        return

    prix_ttc = prix_ht * (1 + taux_tva / 100)
    _ecrire_nombre(entry_ttc, prix_ttc)


def mettre_a_jour_depuis_ttc(entry_ht, entry_ttc, entry_tva, event=None):
    prix_ttc = _lire_nombre(entry_ttc)
    taux_tva = _lire_nombre(entry_tva)
    if prix_ttc is None or taux_tva is None:
        return

    denominateur = 1 + taux_tva / 100
    if denominateur == 0:
        messagebox.showerror("Erreur", "Le taux de TVA ne peut pas etre egal a -100%.")
        return

    prix_ht = prix_ttc / denominateur
    _ecrire_nombre(entry_ht, prix_ht)


def mettre_a_jour_depuis_tva(entry_ht, entry_ttc, entry_tva, event=None):
    prix_ht = _lire_nombre(entry_ht)
    prix_ttc = _lire_nombre(entry_ttc)
    taux_tva = _lire_nombre(entry_tva)
    if taux_tva is None:
        return

    if prix_ht is not None:
        mettre_a_jour_depuis_ht(entry_ht, entry_ttc, entry_tva)
    elif prix_ttc is not None:
        mettre_a_jour_depuis_ttc(entry_ht, entry_ttc, entry_tva)


def main():
    fenetre = tk.Tk()
    fenetre.title("Calculateur de Prix TTC")
    fenetre.resizable(False, False)
    valider_nombre = fenetre.register(_texte_nombre_partiel_valide)

    notebook = ttk.Notebook(fenetre)
    notebook.pack(fill="both", expand=True, padx=10, pady=10)

    onglet_calcul = ttk.Frame(notebook)
    onglet_parametres = ttk.Frame(notebook)
    onglet_a_propos = ttk.Frame(notebook)
    notebook.add(onglet_calcul, text="Calcul")
    notebook.add(onglet_parametres, text="Parametres")
    notebook.add(onglet_a_propos, text="À propos")

    label_ht = tk.Label(onglet_calcul, text="Prix HT (€) :")
    label_ht.grid(row=0, column=0, padx=(0, 8), pady=10, sticky="w")
    entry_ht = tk.Entry(
        onglet_calcul,
        width=14,
        validate="key",
        validatecommand=(valider_nombre, "%P"),
    )
    entry_ht.grid(row=0, column=1, padx=(0, 14), pady=10)

    label_ttc = tk.Label(onglet_calcul, text="Prix TTC (€) :")
    label_ttc.grid(row=0, column=2, padx=(0, 8), pady=10, sticky="w")
    entry_ttc = tk.Entry(
        onglet_calcul,
        width=14,
        validate="key",
        validatecommand=(valider_nombre, "%P"),
    )
    entry_ttc.grid(row=0, column=3, padx=(0, 0), pady=10)

    bouton_aide = ttk.Button(onglet_calcul, text="Aide", command=ouvrir_aide)
    bouton_aide.grid(row=1, column=0, columnspan=4, pady=(0, 10))

    label_tva = tk.Label(onglet_parametres, text="Taux de TVA (%) :")
    label_tva.grid(row=0, column=0, padx=10, pady=12, sticky="w")
    entry_tva = tk.Entry(
        onglet_parametres,
        width=12,
        validate="key",
        validatecommand=(valider_nombre, "%P"),
    )
    entry_tva.grid(row=0, column=1, padx=10, pady=12, sticky="w")
    entry_tva.insert(0, "20")

    creer_contenu_a_propos(onglet_a_propos)

    entry_ht.bind(
        "<KeyRelease>",
        lambda event: mettre_a_jour_depuis_ht(entry_ht, entry_ttc, entry_tva, event),
    )
    entry_ttc.bind(
        "<KeyRelease>",
        lambda event: mettre_a_jour_depuis_ttc(entry_ht, entry_ttc, entry_tva, event),
    )
    entry_tva.bind(
        "<KeyRelease>",
        lambda event: mettre_a_jour_depuis_tva(entry_ht, entry_ttc, entry_tva, event),
    )

    fenetre.mainloop()


if __name__ == "__main__":
    main()

