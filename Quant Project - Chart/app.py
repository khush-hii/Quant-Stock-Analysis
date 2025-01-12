from flask import Flask, render_template, request
from data_handler import fetch_stock_data
from indicators import calculate_ema, calculate_rsi, calculate_bollinger_bands, calculate_macd
from ml_model import train_random_forest
from visualizer import plot_interactive_stock_data
from signals import generate_buy_sell_signals, process_alerts

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/results', methods=['POST'])
def results():
    ticker = request.form['ticker']
    start_date = request.form['start_date']
    end_date = request.form['end_date']
    
    # Fetch stock data
    df = fetch_stock_data(ticker, start_date, end_date)
    
    # Calculate technical indicators
    df = calculate_ema(df)
    df = calculate_rsi(df)
    df = calculate_bollinger_bands(df)  # Ensure Bollinger Bands are calculated
    print("After Bollinger Bands:", df.columns)  # Debug print
    df = calculate_macd(df)
    
    # Train machine learning model and generate signals
    model = train_random_forest(df)
    df = generate_buy_sell_signals(df, model)
    
    # Plot interactive graph
    plot_interactive_stock_data(df)
    
    return render_template('results.html', ticker=ticker, data=df.to_html())


if __name__ == '__main__':
    app.run(debug=True)
