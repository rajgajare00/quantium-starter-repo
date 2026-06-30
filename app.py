import pandas as pd
import dash
from dash import dcc, html, Input, Output
import plotly.express as px

# Data load karna
df = pd.read_csv("data/formatted_sales_data.csv")
df["Date"] = pd.to_datetime(df["Date"])
df = df.sort_values("Date")

# Dash app banana
app = dash.Dash(__name__)

# Color theme
colors = {
    "background": "#FDF0F5",
    "text": "#9D174D",
    "accent": "#EC4899"
}

app.layout = html.Div(
    style={
        "backgroundColor": colors["background"],
        "fontFamily": "Arial, sans-serif",
        "padding": "40px"
    },
    children=[
        html.H1(
            "Soul Foods: Pink Morsel Sales Visualiser",
            style={
                "textAlign": "center",
                "color": colors["text"],
                "marginBottom": "10px"
            }
        ),
        html.P(
            "Were sales higher after the Pink Morsel price increase on 15th Jan 2021?",
            style={
                "textAlign": "center",
                "color": colors["text"],
                "fontSize": "16px",
                "marginBottom": "30px"
            }
        ),
        html.Div(
            style={"textAlign": "center", "marginBottom": "20px"},
            children=[
                dcc.RadioItems(
                    id="region-radio",
                    options=[
                        {"label": "North", "value": "north"},
                        {"label": "East", "value": "east"},
                        {"label": "South", "value": "south"},
                        {"label": "West", "value": "west"},
                        {"label": "All", "value": "all"},
                    ],
                    value="all",
                    inline=True,
                    style={"color": colors["text"], "fontSize": "16px"},
                    inputStyle={"marginRight": "5px", "marginLeft": "15px"}
                )
            ]
        ),
        html.Div(
            style={
                "backgroundColor": "white",
                "borderRadius": "12px",
                "padding": "20px",
                "boxShadow": "0px 4px 12px rgba(0,0,0,0.1)"
            },
            children=[
                dcc.Graph(id="sales-line-chart")
            ]
        )
    ]
)

# Callback: radio button select hote hi chart update ho
@app.callback(
    Output("sales-line-chart", "figure"),
    Input("region-radio", "value")
)
def update_chart(selected_region):
    if selected_region == "all":
        filtered_df = df
    else:
        filtered_df = df[df["Region"] == selected_region]

    daily_sales = filtered_df.groupby("Date")["Sales"].sum().reset_index()

    fig = px.line(
        daily_sales,
        x="Date",
        y="Sales",
        title=f"Pink Morsel Sales — Region: {selected_region.capitalize()}",
        labels={"Date": "Date", "Sales": "Sales ($)"}
    )
    fig.update_traces(line_color=colors["accent"])
    fig.update_layout(
        plot_bgcolor="white",
        paper_bgcolor="white",
        title_font_color=colors["text"]
    )
    return fig

if __name__ == "__main__":
    app.run(debug=True)