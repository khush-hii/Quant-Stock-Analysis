import pandas as pd

def backtest_strategy(data):
    # Assuming 'Position' is the trading signal based on generated buy/sell signals
    initial_capital = 100000  # Starting capital for the strategy
    data['Daily_Return'] = data['Close'].pct_change()  # Daily returns of the stock

    # Calculate strategy return based on the position (Buy/Sell)
    data['Strategy_Return'] = data['Daily_Return'] * data['Position']
    
    # Calculate cumulative returns for both strategy and market (benchmark)
    data['Cumulative_Market'] = (1 + data['Daily_Return']).cumprod() * initial_capital
    data['Cumulative_Strategy'] = (1 + data['Strategy_Return']).cumprod() * initial_capital

    return data['Cumulative_Strategy'], data['Cumulative_Market']

def calculate_metrics(data):
    # Performance metrics: Sharpe ratio and total return
    sharpe_ratio = data['Strategy_Return'].mean() / data['Strategy_Return'].std() * (252 ** 0.5)  # Annualized Sharpe ratio
    total_return = (data['Cumulative_Strategy'].iloc[-1] / data['Cumulative_Strategy'].iloc[0] - 1) * 100  # Total return in percentage
    return sharpe_ratio, total_return
