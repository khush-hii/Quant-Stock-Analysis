import pandas as pd
import numpy as np

def calculate_ema(df, span=14):
    df['EMA'] = df['Close'].ewm(span=span, adjust=False).mean()
    return df

def calculate_bollinger_bands(df, window=20, num_std_dev=2):
    df['SMA'] = df['Close'].rolling(window=window).mean()
    df['std'] = df['Close'].rolling(window=window).std()
    df['Upper'] = df['SMA'] + (df['std'] * num_std_dev)
    df['Lower'] = df['SMA'] - (df['std'] * num_std_dev)
    return df

def calculate_rsi(df, window=14):
    delta = df['Close'].diff()
    gain = delta.where(delta > 0, 0)
    loss = -delta.where(delta < 0, 0)
    avg_gain = gain.rolling(window=window).mean()
    avg_loss = loss.rolling(window=window).mean()
    rs = avg_gain / avg_loss
    df['RSI'] = 100 - (100 / (1 + rs))
    return df

def calculate_macd(df, fast=12, slow=26, signal=9):
    df['MACD'] = df['Close'].ewm(span=fast, adjust=False).mean() - df['Close'].ewm(span=slow, adjust=False).mean()
    df['MACD_signal'] = df['MACD'].ewm(span=signal, adjust=False).mean()
    return df
