import yfinance as yf

def fetch_stock_data(ticker, start_date, end_date):
    df = yf.download(ticker, start=start_date, end=end_date)
    if df.empty:
        raise ValueError(f"No data found for ticker {ticker}. Please check the ticker symbol.")
    return df
