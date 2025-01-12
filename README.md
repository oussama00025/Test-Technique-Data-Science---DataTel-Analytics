# Projet : Prévision des Revenus de Ventes de Smartphones

## Contexte

DataTel, un opérateur télécom majeur, souhaite optimiser ses revenus en prévoyant les ventes de smartphones pour le premier trimestre 2025. Ce projet vise à analyser les données historiques, à identifier les patterns de ventes et à construire un modèle de prévision robuste.

---

## Structure du Projet

Voici la structure du projet :

- **data/** :
  - `raw/` : Contient les données brutes.
  - `processed/` : Contient les données transformées et prêtes à l'analyse.

- **notebooks/** :
  - `01_exploration.ipynb` : Analyse exploratoire des données.
  - `02_modeling.ipynb` : Modélisation et prévision des revenus.

- **src/** :
  - `data_processing.py` : Script pour le nettoyage et le pré-traitement des données.
  - `feature_engineering.py` : Script pour la création des nouvelles variables (features).
  - `models.py` : Code pour entraîner et évaluer les modèles de prévision.

- **presentation/** :
  - `results.pdf` : Présentation synthétique des résultats obtenus.

- **README.md** : Documentation du projet (vous êtes ici).

---

## Instructions

### 1. Préparation des Données

- Placez les fichiers de données brutes dans le dossier `data/raw/`.
- Exécutez les scripts ou notebooks pour transformer et préparer les données, qui seront sauvegardées dans `data/processed/`.

### 2. Analyse et Modélisation

- Lancez le notebook `01_exploration.ipynb` pour explorer les données et identifier les patterns importants.
- Lancez ensuite `02_modeling.ipynb` pour construire et évaluer les modèles prédictifs.

### 3. Présentation

- Les résultats finaux seront présentés dans `presentation/results.pdf`.
- Ajoutez les recommandations opérationnelles à partir des insights obtenus.

---

## Environnement Requis

Pour reproduire ce projet, vous aurez besoin des éléments suivants :

- **Langage** : Python 3.8+
- **Bibliothèques** :
  - pandas
  - numpy
  - matplotlib
  - seaborn
  - scikit-learn
  - xgboost
  - joblib

### Installation des Bibliothèques

```bash
pip install pandas numpy matplotlib seaborn scikit-learn xgboost joblib
```

---

## Auteurs

- Auteur : Fouad Oussama



