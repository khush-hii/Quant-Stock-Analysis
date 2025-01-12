

# Stock Prediction Web Application

This **Stock Prediction Web Application** leverages machine learning models and technical indicators to analyze historical stock data and provide actionable insights, including buy and sell signals. The application integrates **Flask** for the web interface, **Yahoo Finance API** for stock data fetching, and **Random Forest** for machine learning-based stock price prediction. The project also includes **interactive visualizations** powered by **Plotly** for intuitive data analysis.

### Key Features
- **Stock Data Fetching**: Automatically fetches historical stock data from Yahoo Finance based on user input.
- **Technical Indicators**: Calculates and displays popular stock indicators like **Simple Moving Average (SMA)**, **Exponential Moving Average (EMA)**, **Relative Strength Index (RSI)**, **Moving Average Convergence Divergence (MACD)**, and **Bollinger Bands**.
- **Machine Learning Prediction**: Utilizes **Random Forest** algorithm to predict stock price trends based on historical data.
- **Buy/Sell Signal Generation**: Generates buy/sell signals by combining predictions with technical indicators.
- **Interactive Visualization**: Provides detailed, interactive charts displaying stock data and indicators, using **Plotly** for better user interaction.
- **Web Interface**: Built using **Flask**, providing an easy-to-use web interface to input stock tickers, date ranges, and view results.

---

## Tech Stack
- **Backend**: Python, Flask
- **Machine Learning**: Scikit-learn, Random Forest
- **Data Handling**: Pandas, Yahoo Finance API
- **Visualization**: Plotly
- **Web Styling**: HTML, JS, CSS (Custom Styled)

---

## Installation Guide

### Prerequisites
- Python 3.x installed
- Virtual environment (recommended for dependency management)


---

## Usage

### Running the Flask Application
1. **Start the Flask Server**  
   To run the Flask app locally, execute the following command:
   ```bash
   python app.py
   ```
   By default, this will start the server on [http://127.0.0.1:5000/](http://127.0.0.1:5000/).

2. **Access the Web Application**  
   Open your browser and go to the following URL:
   ```
   http://127.0.0.1:5000/
   ```
   Here, you will be presented with a form where you can input the following parameters:
   - **Stock Ticker** (e.g., `AAPL`, `TSLA`)
   - **Start Date** (e.g., `2021-01-01`)
   - **End Date** (e.g., `2022-01-01`)

3. **View Results**  
   Once you submit the form:
   - The app will fetch historical stock data for the given stock ticker and date range.
   - It will then calculate the technical indicators: **SMA**, **EMA**, **RSI**, **MACD**, **Bollinger Bands**.
   - The **Random Forest** model will predict stock price trends and generate potential **buy/sell signals**.
   - The results are displayed as interactive plots with overlaid technical indicators.

---

## Project Structure

```
quant_project/
│
├── app.py                # Main Flask application to handle user input and visualize results
├── data_handler.py       # Fetches stock data using Yahoo Finance API
├── indicators.py         # Calculates technical indicators (SMA, EMA, RSI, MACD, Bollinger Bands)
├── signals.py            # Generates buy/sell signals based on the model predictions and technical indicators
├── backtester.py         # Simulates stock strategy performance using historical data
├── visualizer.py         # Generates interactive charts using Plotly
├── ml_model.py           # Random Forest model for stock price prediction
├── requirements.txt      # Python dependencies
├── static/               # Folder containing static assets (CSS)
│   └── style.css         # Custom styling for web pages
├── templates/            # HTML templates for user input and displaying results
│   ├── index.html        # Input form for stock ticker and date range
│   └── results.html      # Page for displaying results and visualizations
└── README.md             # Project documentation
```

---

### Modules Overview

1. **app.py**  
   The main Flask app that handles user inputs, integrates all modules, and displays the results on the web interface.

2. **data_handler.py**  
   This module fetches the stock data from Yahoo Finance using the `yfinance` package, based on user input (stock ticker and date range).

3. **indicators.py**  
   Contains functions to compute popular technical indicators like **SMA**, **EMA**, **RSI**, **MACD**, and **Bollinger Bands**.

4. **signals.py**  
   Generates buy/sell signals based on the analysis of technical indicators and machine learning predictions.

5. **backtester.py**  
   Provides a backtesting framework that simulates how well the strategy would have performed with historical data.

6. **visualizer.py**  
   Handles the generation of interactive stock visualizations using **Plotly**, including candlestick charts and indicators.

7. **ml_model.py**  
   Trains the **Random Forest** model on historical stock data to predict future price movements.

8. **static/style.css**  
   Custom CSS to style the HTML pages, ensuring a smooth and visually appealing user experience.

9. **templates/index.html**  
   The input form where users can provide the stock ticker, start date, and end date for analysis.

10. **templates/results.html**  
    Displays the results of the analysis, including stock predictions, buy/sell signals, technical indicators, and interactive charts.

---

## Future Enhancements & Roadmap

- **Additional Technical Indicators**: Implement more complex indicators such as **Fibonacci Retracement**, **Ichimoku Cloud**, and advanced versions of **MACD**.
- **Advanced Machine Learning Models**: Experiment with time-series forecasting models like **LSTM** (Long Short-Term Memory) networks for improved predictions.
- **User Authentication**: Add authentication to allow users to save their analysis and track investment performance over time.
- **Real-Time Stock Data**: Integrate real-time stock data fetching using APIs like **Alpha Vantage** or **IEX Cloud**.
- **Performance Metrics**: Include financial performance metrics such as **Sharpe Ratio**, **Max Drawdown**, and **Profit Factor** to evaluate the strategy.

---

## Contributing

We welcome contributions to the project! If you have an idea to improve the application, feel free to fork the repository and submit a pull request. Please discuss major changes with the maintainers before submitting a pull request.

---

## Acknowledgments

- **Flask** for creating the web framework.
- **Plotly** for providing interactive charting capabilities.
- **yfinance** for fetching historical stock data from Yahoo Finance.
- **Scikit-learn** for machine learning model training and evaluation.

---
