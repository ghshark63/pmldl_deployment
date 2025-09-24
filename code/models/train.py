import pandas as pd
from sklearn.datasets import load_diabetes
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor

import joblib
import os

def train_model():
    diabetes = load_diabetes()

    feature_names = diabetes.feature_names
    df = pd.DataFrame(diabetes.data, columns=feature_names)
    df['target'] = diabetes.target

    X = df.drop('target', axis=1)
    y = df['target']

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.1, random_state=42
    )

    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    os.makedirs('../../models', exist_ok=True)
    save_path = '../../models/trained_model.joblib'

    joblib.dump(model, save_path)

    print("Successfully saved model")

if __name__ == "__main__":
    train_model()