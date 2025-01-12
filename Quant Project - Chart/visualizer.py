import plotly.express as px

def plot_interactive_stock_data(df):
    fig = px.line(df, x=df.index, y=['Close', 'EMA', 'Upper', 'Lower'], title="Stock Data with Indicators")
    fig.show()
