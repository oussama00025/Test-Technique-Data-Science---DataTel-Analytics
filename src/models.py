# Visualisation des revenus
def plot_revenue_trends(data):
    plt.figure(figsize=(15, 7))
    for model in ['jPhone_Pro_revenue', 'Kaggle_Pixel_5_revenue', 'Planet_SX_revenue']:
        plt.plot(data.index, data[model], label=model)
    plt.xlabel('Index')
    plt.ylabel('Revenus')
    plt.title('Tendances des revenus par modèle de smartphone')
    plt.legend()
    plt.show()

plot_revenue_trends(data)


# Importer des modèles supplémentaires
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import GradientBoostingRegressor
from xgboost import XGBRegressor
from sklearn.metrics import mean_squared_error, r2_score

# Fonction pour entraîner et évaluer plusieurs modèles
def train_and_evaluate_models(X_train, y_train, X_test, y_test):
    models = {
        "Linear Regression": LinearRegression(),
        "Random Forest": RandomForestRegressor(random_state=42),
        "Gradient Boosting": GradientBoostingRegressor(random_state=42),
        "XGBoost": XGBRegressor(random_state=42),
    }
    
    results = {}
    for model_name, model in models.items():
        model.fit(X_train, y_train)
        predictions = model.predict(X_test)
        rmse = np.sqrt(mean_squared_error(y_test, predictions))
        r2 = r2_score(y_test, predictions)
        results[model_name] = {"RMSE": rmse, "R2": r2}
        print(f"{model_name}: RMSE = {rmse:.2f}, R² = {r2:.2f}")
    return results

# Entraînement et évaluation
results = train_and_evaluate_models(X_train, y_train, X_test, y_test)

# Résultats des modèles
results_df = pd.DataFrame(results).T
print(results_df)


