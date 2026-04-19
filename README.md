# HT-TTC

Application Python (Tkinter) pour calculer automatiquement les prix HT et TTC selon un taux de TVA.

HT-TTC est une petite application de bureau en Python avec Tkinter qui permet de convertir rapidement un prix HT en prix TTC, ou l'inverse, en appliquant un taux de TVA personnalisable. Le projet vise un usage simple et immediat, avec une interface legere organisee en onglets pour le calcul, les parametres et les informations generales.

## Description du depot

Ce depot contient un calculateur HT/TTC autonome, pense pour des besoins quotidiens de facturation, de verification tarifaire ou de simulation rapide. L'application met a jour les montants en temps reel pendant la saisie et ne depend d'aucune bibliotheque externe autre que Tkinter, generalement inclus avec Python.

## Fonctionnalites

- Calcul HT -> TTC en temps reel pendant la saisie.
- Calcul TTC -> HT en temps reel pendant la saisie.
- Taux de TVA configurable (valeur par defaut: 20).
- Bouton d'aide ouvrant une documentation HTML locale.
- Interface avec onglets:
  - `Calcul`
  - `Parametres`
  - `A propos`

## Prerequis

- Python 3.10+
- Tkinter (inclus par defaut avec Python sur la plupart des installations)

## Lancer l'application

Depuis la racine du projet:

```bash
python "HT TTC.py"
```

## Usage

1. Saisir un montant HT pour obtenir automatiquement le TTC.
2. Ou saisir un montant TTC pour recalculer automatiquement le HT.
3. Ajuster le taux de TVA depuis l'onglet Parametres.

## Structure du projet

```text
HT TTC.py
aide.html
README.md
history/
  CHANGELOG.md
```

## Historique

L'historique des changements est maintenu dans:

- `history/CHANGELOG.md`
