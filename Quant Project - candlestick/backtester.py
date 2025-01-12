import pandas as pd

# Backtesting strategy to simulate performance
def backtest_strategy(data):
    initial_capital = 100000  # Initial investment
    data['Daily_Return'] = data['Close'].pct_change()
    data['Strategy_Return'] = data['Daily_Return'] * data['Position']

    # Calculate cumulative returns for strategy and market
    data['Cumulative_Market'] = (1 + data['Daily_Return']).cumprod() * initial_capital
    data['Cumulative_Strategy'] = (1 + data['Strategy_Return']).cumprod() * initial_capital

    return data['Cumulative_Strategy'], data['Cumulative_Market']

# Performance metrics: Sharpe ratio and total return
def calculate_metrics(data):
    sharpe_ratio = data['Strategy_Return'].mean() / data['Strategy_Return'].std() * (252 ** 0.5)  # Annualized Sharpe ratio
    total_return = (data['Cumulative_Strategy'].iloc[-1] / data['Cumulative_Strategy'].iloc[0] - 1) * 100  # Total return percentage
    return sharpe_ratio, total_return
