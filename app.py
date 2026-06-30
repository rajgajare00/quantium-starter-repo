import pandas as pd
import dash
from dash import dcc, html
import plotly.express as px

# Data load karna
df = pd.read_csv("data/formatted_sales_data.csv")

# Date ke hisaab se sort karna
df["Date"] = pd.to_datetime(df["Date"])
df = df.sort_values("Date")

# Date-wise total sales (saare regions combine)
daily_sales = df.groupby("Date")["Sales"].sum().reset_index()

# Line chart banana
fig = px.line(
    daily_sales,
    x="Date",
    y="Sales",
    title="Pink Morsel Sales Over Time",
    labels={"Date": "Date", "Sales": "Sales ($)"}
)

# Dash app banana
app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1("Soul Foods: Pink Morsel Sales Visualiser", style={"textAlign": "center"}),
    dcc.Graph(figure=fig)
])

if __name__ == "__main__":
    app.run(debug=True)