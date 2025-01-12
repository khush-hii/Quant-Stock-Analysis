from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.impute import SimpleImputer
import numpy as np

def train_random_forest(df):
    imputer = SimpleImputer(strategy='mean')
    df[['EMA', 'RSI', 'MACD', 'SMA', 'Upper', 'Lower']] = imputer.fit_transform(df[['EMA', 'RSI', 'MACD', 'SMA', 'Upper', 'Lower']])
    
    features = ['EMA', 'RSI', 'MACD', 'SMA', 'Upper', 'Lower']
    X = df[features]
    y = np.where(df['Close'].shift(-1) > df['Close'], 1, 0)

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)
    print(f'Accuracy: {accuracy_score(y_test, y_pred)}')

    return model
