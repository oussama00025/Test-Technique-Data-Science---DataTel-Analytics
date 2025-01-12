from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, mean_absolute_error
import matplotlib.pyplot as plt

# Variables explicatives et cibles
features = ['marketing_score', 'competition_index', 'customer_satisfaction',
            'purchasing_power_index', 'weather_condition', 'tech_event',
            '5g_phase', 'store_traffic', 'public_transport']

targets = ['jPhone_Pro_revenue', 'Kaggle_Pixel_5_revenue', 'Planet_SX_revenue']

# Prétraitement des données
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, mean_absolute_error
import pandas as pd
import numpy as np

# Gestion des colonnes catégoriques : Encodage avec pd.get_dummies()
data = pd.get_dummies(data, columns=['weather_condition', 'tech_event', '5g_phase', 'public_transport'], drop_first=True)

# Gestion des valeurs manquantes : Remplacement par la moyenne (ou une autre stratégie)
data.fillna(data.mean(), inplace=True)

# Vérification des colonnes disponibles après transformation
features = ['marketing_score', 'competition_index', 'customer_satisfaction',
            'purchasing_power_index', 'store_traffic'] + \
           [col for col in data.columns if col.startswith(('weather_condition_', 'tech_event_', '5g_phase_', 'public_transport_'))]

targets = ['jPhone_Pro_revenue', 'Kaggle_Pixel_5_revenue', 'Planet_SX_revenue']

# Modélisation pour chaque modèle de smartphone
models_predictions = {}

for target in targets:
    print(f"\nModélisation pour : {target}")
    y = data[target].dropna()  # Retirer les valeurs NaN de la cible
    X = data.loc[y.index, features]  # Sélectionner les mêmes indices pour les variables explicatives
    
    # Division en ensembles d'entraînement et de test
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Modélisation avec RandomForest
    model = RandomForestRegressor(random_state=42)
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    
    # Évaluation des performances
    rmse = mean_squared_error(y_test, y_pred, squared=False)
    mae = mean_absolute_error(y_test, y_pred)
    print(f"RMSE : {rmse:.2f}, MAE : {mae:.2f}")
    
    # Sauvegarder le modèle
    models_predictions[target] = {
        'model': model,
        'rmse': rmse,
        'mae': mae
    }


# Générer des dates pour janvier à mars 2025
future_dates = pd.date_range(start="2025-01-01", end="2025-03-31")
future_data = pd.DataFrame(index=future_dates)

# Remplir avec des données fictives pour les variables explicatives
future_data[features] = np.random.uniform(0, 1, size=(len(future_dates), len(features)))

# Prévisions
for target in targets:
    future_data[target] = models_predictions[target]['model'].predict(future_data[features])

# Sauvegarde des prévisions
future_data.reset_index(inplace=True)
future_data.rename(columns={'index': 'date'}, inplace=True)
future_data.to_csv('predictions_q1_2025.csv', index=False)
print("Prévisions sauvegardées dans 'predictions_q1_2025.csv'.")

