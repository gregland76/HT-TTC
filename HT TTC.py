import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import webbrowser

# Fonction
# pour calculer le prix TTC
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


def mettre_a_jour_depuis_ht(event=None):
    prix_ht = _lire_nombre(entry_ht)
    taux_tva = _lire_nombre(entry_tva)
    if prix_ht is None or taux_tva is None:
        return

    prix_ttc = prix_ht * (1 + taux_tva / 100)
    _ecrire_nombre(entry_ttc, prix_ttc)


def mettre_a_jour_depuis_ttc(event=None):
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


def mettre_a_jour_depuis_tva(event=None):
    prix_ht = _lire_nombre(entry_ht)
    prix_ttc = _lire_nombre(entry_ttc)
    taux_tva = _lire_nombre(entry_tva)
    if taux_tva is None:
        return

    if prix_ht is not None:
        mettre_a_jour_depuis_ht()
    elif prix_ttc is not None:
        mettre_a_jour_depuis_ttc()


def calculer_ttc():
    # Compatibilite avec l'ancien comportement manuel.
    if entry_ttc.focus_get() == entry_ttc:
        mettre_a_jour_depuis_ttc()
    else:
        mettre_a_jour_depuis_ht()
# Fonction pour afficher les informations à propos de l'application
def creer_contenu_a_propos(parent):
    # Contenu de l'onglet dedie.
    label_nom = tk.Label(parent, text="Développé par Greg", font=("Arial", 12))
    label_nom.pack(pady=(12, 8))

    label_site = tk.Label(parent, text="Site : https://ti.gregland.net", font=("Arial", 10), fg="blue", cursor="hand2")
    label_site.pack(pady=5)
    label_site.bind("<Button-1>", lambda e: webbrowser.open("https://ti.gregland.net"))

    label_mail = tk.Label(parent, text="Email : gregory.hargous@gmail.com", font=("Arial", 10))
    label_mail.pack(pady=5)

# Création de la fenêtre principale
fenetre = tk.Tk()
fenetre.title("Calculateur de Prix TTC")  # Titre de la fenêtre
fenetre.resizable(False, False)  # Fenetre non redimensionnable

# Onglets: calcul principal, parametres TVA et a propos
notebook = ttk.Notebook(fenetre)
notebook.pack(fill="both", expand=True, padx=10, pady=10)

onglet_calcul = ttk.Frame(notebook)
onglet_parametres = ttk.Frame(notebook)
onglet_a_propos = ttk.Frame(notebook)
notebook.add(onglet_calcul, text="Calcul")
notebook.add(onglet_parametres, text="Parametres")
notebook.add(onglet_a_propos, text="À propos")

# HT et TTC sur la meme ligne dans l'onglet principal
label_ht = tk.Label(onglet_calcul, text="Prix HT (€) :")
label_ht.grid(row=0, column=0, padx=(0, 8), pady=10, sticky="w")
entry_ht = tk.Entry(onglet_calcul, width=14)
entry_ht.grid(row=0, column=1, padx=(0, 14), pady=10)

label_ttc = tk.Label(onglet_calcul, text="Prix TTC (€) :")
label_ttc.grid(row=0, column=2, padx=(0, 8), pady=10, sticky="w")
entry_ttc = tk.Entry(onglet_calcul, width=14)
entry_ttc.grid(row=0, column=3, padx=(0, 0), pady=10)

# Taux TVA deplace dans l'onglet parametres pour ne pas encombrer l'onglet principal
label_tva = tk.Label(onglet_parametres, text="Taux de TVA (%) :")
label_tva.grid(row=0, column=0, padx=10, pady=12, sticky="w")
entry_tva = tk.Entry(onglet_parametres, width=12)
entry_tva.grid(row=0, column=1, padx=10, pady=12, sticky="w")
entry_tva.insert(0, "20")  # Valeur par défaut à 20%

# Informations de l'onglet A propos
creer_contenu_a_propos(onglet_a_propos)

# Calcul automatique lors de la saisie
entry_ht.bind("<KeyRelease>", mettre_a_jour_depuis_ht)
entry_ttc.bind("<KeyRelease>", mettre_a_jour_depuis_ttc)
entry_tva.bind("<KeyRelease>", mettre_a_jour_depuis_tva)

# Lancement de la boucle principale de l'application
fenetre.mainloop()

