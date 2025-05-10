# Mini-projet - Extraction d'information médicale

Ce projet universitaire a pour but d'extraire automatiquement des entités médicales (noms de médicaments) et de repérer les posologies à partir du contenu des 26 pages
HTML du dossier « VIDAL », en utilisant **Python** et **UNITEX**.

---

## 📌 Étapes du projet

### Étape 1 - Extraction initiale (`extraire.py`)
- Extraction des substances actives à partir de pages HTML du dossier "VIDAL".
- Génération d'un dictionnaire au format **DELAF** nommé `subst.dic` (encodé en UTF-16 LE BOM).
- Génération d’un fichier `infos1.txt` contenant :
  - Le nombre de médicaments par lettre.
  - Le total global.

### Étape 2 - Enrichissement (`enrichir.py`)
- Analyse du fichier `corpus-medical.txt` pour identifier de nouveaux noms de médicaments.
- Mise à jour de `subst.dic` (trié, sans doublons).
- Création de :
  - `subst_corpus.dic` (les nouveaux ajouts sans tri, minuscules).
  - `infos2.txt` : statistiques sur tous les médicaments du corpus.
  - `infos3.txt` : statistiques uniquement sur ceux retenus pour enrichir `subst.dic`.

### Étape 3 - Extraction de posologies avec UNITEX
- Création d’un graphe `posologie.grf` exploitant l’étiquette `<N+subst>`.
- Extraction via `unitex.py`.
- Visualisation des résultats dans `concord.html`.

---

## 🗂️ Contenu du dépôt

- `extraire.py` : extraction depuis VIDAL (non joint ici si pas demandé)
- `enrichir.py` : enrichissement du dictionnaire
- `subst.dic` : dictionnaire final
- `subst_corpus.dic` : médicaments extraits du corpus
- `infos2.txt` et `infos3.txt` : statistiques détaillées
- `posologie.grf` : graphe UNITEX
- `concord.html` : extrait HTML des posologies trouvées

---

## ▶️ Exécution rapide

```bash
python enrichir.py corpus-medical.txt
