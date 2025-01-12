
# data_processing.py
# Script contenant des fonctions pour le nettoyage et la transformation des données.

import pandas as pd

def load_data(file_path):
    """Charge un fichier CSV et retourne un DataFrame pandas."""
    try:
        data = pd.read_csv(file_path)
        print(f"Données chargées avec succès depuis {file_path}")
        return data
    except Exception as e:
        print(f"Erreur lors du chargement des données : {e}")
        return None

def clean_data(data):
    """Nettoie un DataFrame pandas : gère les valeurs manquantes et les doublons."""
    if data is None:
        print("Les données sont vides. Impossible de nettoyer.")
        return None
    # Gestion des valeurs manquantes
    data = data.dropna(thresh=len(data.columns) * 0.5, axis=0)  # Supprime les lignes avec plus de 50% de valeurs manquantes
    data.fillna(method='ffill', inplace=True)  # Remplissage avec la méthode forward-fill

    # Suppression des doublons
    data = data.drop_duplicates()
    print("Nettoyage des données terminé.")
    return data

def save_processed_data(data, output_path):
    """Sauvegarde le DataFrame nettoyé dans un fichier CSV."""
    if data is None:
        print("Pas de données à sauvegarder.")
        return
    try:
        data.to_csv(output_path, index=False)
        print(f"Données nettoyées sauvegardées dans {output_path}")
    except Exception as e:
        print(f"Erreur lors de la sauvegarde des données : {e}")
