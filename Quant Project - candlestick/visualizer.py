import plotly.graph_objects as go

def plot_interactive_stock_data(df):
    fig = go.Figure()

    fig.add_trace(go.Candlestick(
        x=df.index,
        open=df['Open'],
        high=df['High'],
        low=df['Low'],
        close=df['Close'],
        name='Candlestick'
    ))

    fig.add_trace(go.Scatter(
        x=df.index,
        y=df['EMA'],
        mode='lines',
        name='EMA'
    ))

    fig.update_layout(
        title='Stock Data with EMA',
        xaxis_title='Date',
        yaxis_title='Price',
        template='plotly_dark'
    )
    fig.show()
