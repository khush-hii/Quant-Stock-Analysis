def generate_buy_sell_signals(df, model):
    df['Predicted_Signal'] = model.predict(df[['EMA', 'RSI', 'MACD', 'SMA', 'Upper', 'Lower']])
    df['Signal'] = df['Predicted_Signal'].apply(lambda x: 'Buy' if x == 1 else 'Sell')
    return df

def process_alerts(df, alerts):
    alert_messages = []
    for alert in alerts.split(';'):
        condition = alert.strip()
        try:
            if eval(condition, {}, {'df': df}):
                alert_messages.append(f"Condition met: {condition}")
        except Exception as e:
            alert_messages.append(f"Error processing alert: {condition} - {str(e)}")
    return alert_messages
