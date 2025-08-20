# import dash
# from dash import html

# app = dash.Dash(__name__)

# app.layout = html.Div(children=[
#     html.H1("Hello, Quantium!"),
#     html.P("Your Dash setup is working")
# ])

# if __name__ == "__main__":
#     app.run(debug=True)

import dash
from dash import dcc, html
import pandas as pd
import plotly.express as px

# Load processed sales data
df = pd.read_csv("data/processed_sales.csv")

# Convert date column to datetime
df["date"] = pd.to_datetime(df["date"])

# Create line chart
fig = px.line(
    df,
    x="date",
    y="sales",  # adjust column name to match your processed file (e.g., revenue, quantity)
    title="Pink Morsel Sales Before and After Price Increase",
    labels={"date": "Date", "sales": "Sales"}
)

# Initialize Dash app
app = dash.Dash(__name__)

app.layout = html.Div(children=[
    html.H1("Pink Morsel Sales Visualiser", style={"textAlign": "center"}),

    dcc.Graph(
        id="sales-graph",
        figure=fig
    ),

    html.P("Price increase occurred on 15th January 2021.", style={"textAlign": "center"})
])

if __name__ == "__main__":
    app.run(debug=True)
