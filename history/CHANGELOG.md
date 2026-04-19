# Historique des modifications

## 2026-04-19
- Aide HTML enrichie avec maquette visuelle de l interface et exemples de calcul concrets.
- Fichier d aide HTML ajoute et bouton Aide integre dans l interface pour ouvrir la documentation locale.
- Validation de saisie ajoutee sur les champs numeriques pour empecher l entree de texte non numerique dans HT, TTC et TVA.
- Creation des dossiers de structure du projet : src, docs, tests, history.
- Analyse initiale du script HT TTC.py preparee.
- Calcul automatique ajoute pendant la saisie (sans bouton) pour HT -> TTC.
- Calcul bidirectionnel ajoute : saisie TTC -> recalcul HT selon le taux TVA.
- Import webbrowser ajoute pour corriger le lien cliquable dans la fenetre A propos.
- Interface reorganisee avec onglets : "Calcul" et "Parametres".
- Champs HT et TTC places sur la meme ligne dans l'onglet Calcul.
- Champ TVA deplace dans l'onglet Parametres pour ne pas etre visible en permanence.
- Interface rendue non redimensionnable (taille de fenetre fixe).
- Bouton "A propos" supprime et remplace par un onglet "A propos".
- Informations de presentation integrees directement dans l'onglet "A propos".
- README.md ajoute a la racine avec instructions d'installation et d'execution.
- README.md enrichi avec une description de depot plus complete et une section d'usage.
- Description courte ajoutee en tete du README.
- Description courte du README remplacee par le texte demande pour le depot.
- Structure du projet corrigee dans la documentation pour correspondre au contenu reel du depot.
- Fichier .gitignore ajoute pour exclure les caches Python du versionnement.
- Script principal refactore avec un point d'entree main() pour eviter l'execution de l'interface a l'import.
