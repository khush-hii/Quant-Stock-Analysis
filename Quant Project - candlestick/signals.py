def generate_buy_sell_signals(df, model):
    df['Predicted_Signal'] = model.predict(df[['EMA', 'RSI', 'MACD', 'SMA', 'Upper', 'Lower']])
    df['Signal'] = df['Predicted_Signal'].apply(lambda x: 'Buy' if x == 1 else 'Sell')
    return df
