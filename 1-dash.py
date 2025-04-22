from plotly_bar import bar_fig 
from dash import dcc, Dash, html

app = Dash()

app.layout = html.Div(
    children =[
        html.H1('Total Sales by Country'),
        dcc.Graph(
            id = 'example-graph',
            figure = bar_fig
        )
    ]
)


if __name__ == '__main__':
    app.run(debug=True)
