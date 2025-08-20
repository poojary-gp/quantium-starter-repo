# import dash
# from dash import html

# app = dash.Dash(__name__)

# app.layout = html.Div(children=[
#     html.H1("Hello, Quantium!"),
#     html.P("Your Dash setup is working")
# ])

# if __name__ == "__main__":
#     app.run(debug=True)

# import dash
# from dash import dcc, html
# import pandas as pd
# import plotly.express as px

# # Load processed sales data
# df = pd.read_csv("data/processed_sales.csv")

# # Convert date column to datetime
# df["date"] = pd.to_datetime(df["date"])

# # Create line chart
# fig = px.line(
#     df,
#     x="date",
#     y="sales",  # adjust column name to match your processed file (e.g., revenue, quantity)
#     title="Pink Morsel Sales Before and After Price Increase",
#     labels={"date": "Date", "sales": "Sales"}
# )

# # Initialize Dash app
# app = dash.Dash(__name__)

# app.layout = html.Div(children=[
#     html.H1("Pink Morsel Sales Visualiser", style={"textAlign": "center"}),

#     dcc.Graph(
#         id="sales-graph",
#         figure=fig
#     ),

#     html.P("Price increase occurred on 15th January 2021.", style={"textAlign": "center"})
# ])

# if __name__ == "__main__":
#     app.run(debug=True)



import dash
from dash import dcc, html, Input, Output
import pandas as pd
import plotly.express as px

# Load processed sales data
df = pd.read_csv("data/processed_sales.csv")
df["date"] = pd.to_datetime(df["date"])

# Define color scheme per region
region_colors = {
    "north": "#1f77b4",  # blue
    "east": "#ff7f0e",   # orange
    "south": "#2ca02c",  # green
    "west": "#d62728",   # red
    "all": "#9467bd"     # purple
}

# Initialize Dash app
app = dash.Dash(__name__)

app.layout = html.Div(style={
    "fontFamily": "Arial, sans-serif",
    "backgroundColor": "#f9f9f9",
    "padding": "20px"
}, children=[
    html.H1("Pink Morsel Sales Visualiser", 
            style={"textAlign": "center", "color": "#2c3e50"}),

    html.Div([
        html.Label("Filter by Region:", style={"fontWeight": "bold"}),
        dcc.RadioItems(
            id="region-filter",
            options=[
                {"label": "North", "value": "north"},
                {"label": "East", "value": "east"},
                {"label": "South", "value": "south"},
                {"label": "West", "value": "west"},
                {"label": "All", "value": "all"}
            ],
            value="all",  # default option
            inline=True,
            style={"margin": "10px"}
        )
    ], style={"textAlign": "center", "marginBottom": "20px"}),

    dcc.Graph(id="sales-graph"),

    html.P("Note: Price increase occurred on 15th January 2021.", 
           style={"textAlign": "center", "fontStyle": "italic", "color": "#555"})
])


# Callback to update chart based on selected region
@app.callback(
    Output("sales-graph", "figure"),
    Input("region-filter", "value")
)
def update_chart(selected_region):
    if selected_region == "all":
        filtered_df = df
        fig = px.line(
            filtered_df,
            x="date",
            y="sales",  
            color="region",  # Show all regions with their own colors
            title="Pink Morsel Sales (All Regions)",
            labels={"date": "Date", "sales": "Sales"},
            color_discrete_map=region_colors
        )
    else:
        filtered_df = df[df["region"].str.lower() == selected_region]
        fig = px.line(
            filtered_df,
            x="date",
            y="sales",
            title=f"Pink Morsel Sales ({selected_region.capitalize()})",
            labels={"date": "Date", "sales": "Sales"},
            color_discrete_sequence=[region_colors[selected_region]]
        )

    fig.update_layout(
        plot_bgcolor="white",
        paper_bgcolor="#f9f9f9",
        font=dict(color="#2c3e50")
    )
    return fig


if __name__ == "__main__":
    app.run(debug=True)
