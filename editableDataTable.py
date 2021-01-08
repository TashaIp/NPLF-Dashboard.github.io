import dash
import dash_html_components as html
import dash_core_components as dcc
import plotly.express as px
import pandas as pd
import plotly.graph_objects as go
from pandas import ExcelWriter
from pandas import ExcelFile
import plotly.graph_objects as plot
import dash_bootstrap_components as dbc
import dash_core_components as dcc
from plotly.subplots import make_subplots
import plotly
import dash_auth
from apps import year2020, year2021, year2022, year2023

from dash.dependencies import Input, Output
import numpy as np
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP], suppress_callback_exceptions=True)

# Keep this out of source code repository - save in a file or a database
VALID_USERNAME_PASSWORD_PAIRS = {
    'NashvillePLFoundation@gmail.com': 'Foundation2018'
}

auth = dash_auth.BasicAuth(
    app,
    VALID_USERNAME_PASSWORD_PAIRS
)

#layout = go.Layout()

fig7 = make_subplots(rows=3, cols=1, subplot_titles=("Twitter", "Facebook", "Linkedin"))
fig7.update_layout(height= 2300, width= 1300, title_text="Social Media Overview",)

#Twitter
df = pd.read_excel('NPLF Twitter Q1andQ2.xlsx')

fig1 = plot.Figure(data=plot.Scatter(x=df['Date'], y=df['impressions'], mode='lines+markers', ))
fig2 = plot.Figure(data=plot.Scatter(x=df['Date'], y=df['engagement rate'], mode='lines+markers', line_color="#ef5a41"))
fig3 = plot.Figure(
    data=plot.Scatter(x=df['Date'], y=df['detail expands'], mode='lines+markers', line_color="#00cc96"))
fig4 = plot.Figure(data=plot.Scatter(x=df['Date'], y=df['likes'], mode='lines+markers', line_color="#9467bd"))
fig5 = plot.Figure(data=plot.Scatter(x=df['Date'], y=df['media views'], mode='lines+markers', line_color="#ffa15a"))
fig6 = plot.Figure(data=plot.Scatter(x=df['Date'], y=df['media engagements'], mode='lines+markers', line_color="#1cd3f3"))
#fig7 = go.Figure()

trace1 = fig1['data'][0]
trace2 = fig2['data'][0]
trace3 = fig3['data'][0]
trace4 = fig4['data'][0]
trace5 = fig5['data'][0]
trace6 = fig6['data'][0]

fig7.add_trace(go.Scatter(trace1,
                            mode='lines+markers',
                            name='impressions'), row = 1, col = 1)
fig7.add_trace(go.Scatter(trace2,
                            mode='lines+markers', name='Engagement rate'), row = 1, col = 1)
fig7.add_trace(go.Scatter(trace3,
                            mode='lines+markers', name='Detail expands'), row = 1, col = 1)
fig7.add_trace(go.Scatter(trace4,
                            mode='lines+markers', name='Likes'), row = 1, col = 1)
fig7.add_trace(go.Scatter(trace5,
                            mode='lines+markers', name='Media Views'), row = 1, col = 1)
fig7.add_trace(go.Scatter(trace6,
                            mode='lines+markers', name='Media Engagements'), row = 1, col = 1)


#Facebook Posts
# layout = go.Layout(
#     title="Facebook"
# )
df1 = pd.read_excel('Facebook Posts Q1andQ2.xlsx')

fig1 = go.Figure(data=go.Scatter(x=df1['Posted'], y=df1['Lifetime Post Total Reach'], mode='lines+markers', ))
fig2 = go.Figure(data=go.Scatter(x=df1['Posted'], y=df1['Lifetime Post Total Impressions'], mode='lines+markers', line_color="#ef5a41"))
fig3 = go.Figure(data=go.Scatter(x=df1['Posted'], y=df1['Lifetime Engaged Users'], mode='lines+markers',line_color="#00cc96" ))
fig4 = go.Figure(data=go.Scatter(x=df1['Posted'], y=df1['Lifetime Matched Audience Targeting Consumers on Post'], mode='lines+markers',line_color="#9467bd" ))
fig5 = go.Figure(data=go.Scatter(x=df1['Posted'], y=df1['Lifetime Matched Audience Targeting Consumptions on Post'], mode='lines+markers', line_color="#ffa15a"))
fig6 = go.Figure(data=go.Scatter(x=df1['Posted'], y=df1['Lifetime Post Impressions by people who have liked your Page'], mode='lines+markers', line_color="#1cd3f3"))
fig8 = go.Figure(data=go.Scatter(x=df1['Posted'], y=df1['Lifetime Post reach by people who like your Page'], mode='lines+markers',line_color="#1cd3f3" ))
#fig8 = go.Figure()
fig7.add_trace(go.Scatter(x=df1['Posted'], y=df1['Lifetime Post Total Reach'],
                            mode='lines+markers',
                            name='Lifetime Post Total Reach'), row = 2, col = 1)
fig7.add_trace(go.Scatter(x=df1['Posted'], y=df1['Lifetime Post Total Impressions'],
                            mode='lines+markers',
                            name='Lifetime Post Total Impressions'), row = 2, col = 1)
fig7.add_trace(go.Scatter(x=df1['Posted'], y=df1['Lifetime Engaged Users'],
                            mode='lines+markers',
                            name='Lifetime Engaged Users'), row = 2, col = 1)
fig7.add_trace(go.Scatter(x=df1['Posted'], y=df1['Lifetime Matched Audience Targeting Consumers on Post'],
                            mode='lines+markers',
                            name='Lifetime Matched Audience Targeting Consumers on Post'), row = 2, col = 1)
fig7.add_trace(go.Scatter(x=df1['Posted'], y=df1['Lifetime Matched Audience Targeting Consumptions on Post'],
                            mode='lines+markers',
                            name='Lifetime Matched Audience Targeting Consumptions on Post'), row = 2, col = 1)

#Linkedin
#Data Frames and Sheet Names
df2 = pd.read_excel('NPLF LinkedIn Q1.xlsx', sheet_name = [0,1,2,3,4])
df3 = pd.read_excel('NPLF LinkedIn Q1.xlsx', sheet_name = 'Company size')
df4 = pd.read_excel('NPLF LinkedIn Q1.xlsx', sheet_name = 'Update metrics (aggregated)')
df5 = pd.read_excel('NPLF LinkedIn Q1.xlsx', sheet_name = 'Industry')
df6 = pd.read_excel('NPLF LinkedIn Q1.xlsx', sheet_name = 'Seniority')

fig1 = plot.Figure(data=plot.Scatter(y=df4["Date"], x=df4["Impressions (organic)"], mode='lines+markers', ))
fig2 = plot.Figure(data=plot.Scatter(y=df4['Date'], x=df4['Impressions (sponsored)'], mode='lines+markers', line_color="#ef5a41"))
fig3 = plot.Figure(data=plot.Scatter(y=df4['Date'], x=df4['Unique impressions (organic)'], mode='lines+markers', line_color="#00cc96"))
fig4 = plot.Figure(data=plot.Scatter(y=df4['Date'], x=df4['Clicks (organic)'], mode='lines+markers', line_color="#9467bd"))
fig5 = plot.Figure(data=plot.Scatter(y=df4['Date'], x=df4['Clicks (sponsored)'], mode='lines+markers', line_color="#ffa15a"))
fig6 = plot.Figure(data=plot.Scatter(y=df4['Date'], x=df4['Reactions (organic)'], mode='lines+markers', line_color="#1cd3f3"))
fig8 = plot.Figure(data=plot.Scatter(y=df4['Date'], x=df4['Engagement rate (organic)'], mode='lines+markers', line_color="#F5A10E"))
fig9 = plot.Figure(data=plot.Scatter(y=df4['Date'], x=df4['Engagement rate (sponsored)'], mode='lines+markers', line_color="#0EF596"))

#Quarter 1 (april to june)

fig7.add_trace(plot.Scatter(x=df4['Date'], y=df4['Impressions (organic)'],
                            mode='lines+markers',
                            name= 'Impressions (organic)'), row = 3, col = 1)
fig7.add_trace(plot.Scatter(x=df4['Date'], y=df4['Impressions (sponsored)'],
                            mode='lines+markers', name='Impressions (sponsored)'), row = 3, col = 1)
fig7.add_trace(plot.Scatter(x=df4['Date'], y=df4['Unique impressions (organic)'],
                            mode='lines+markers', name='Unique impressions (organic)'), row = 3, col = 1)
fig7.add_trace(plot.Scatter(x=df4['Date'], y=df4['Clicks (organic)'],
                            mode='lines+markers', name='Clicks (organic)'), row = 3, col = 1)
fig7.add_trace(plot.Scatter(x=df4['Date'], y=df4['Clicks (sponsored)'],
                            mode='lines+markers', name='Clicks (sponsored)'), row = 3, col = 1)
fig7.add_trace(plot.Scatter(x=df4['Date'], y=df4['Reactions (organic)'],
                            mode='lines+markers', name='Reactions (organic)'), row = 3, col = 1)
fig7.add_trace(plot.Scatter(x=df4['Date'], y=df4['Engagement rate (organic)'],
                            mode='lines+markers', name='Engagement rate (organic)'), row = 3, col = 1)
fig7.add_trace(plot.Scatter(x=df4['Date'], y=df4['Engagement rate (sponsored)'],
                            mode='lines+markers', name='Engagement rate (sponsored)'), row = 3, col = 1)
                            



#fig7.show()

# default rangeslider/graph values
min_value = '2020-01-01'
max_value = '2020-12-01'
dates = pd.date_range(min_value, max_value, freq='MS').strftime("%Y-%b").tolist()
date_mark = {i: dates[i] for i in range(0, 12)}

# date slider labels
def set_rangeslider(minValue, maxValue):
    print("enter set_rangeSlider", minValue, maxValue)
    df['Date'] = pd.to_datetime(df.Date)
    dates = pd.date_range(minValue, maxValue, freq='MS').strftime("%Y-%b").tolist()
    # print(dates)
    date_mark = {i: dates[i] for i in range(0, 12)}
    # print(date_mark)
    return date_mark, dates
# default rangeslider/graph values
min_value = '2020-01-01'
max_value = '2020-12-01'
dates = pd.date_range(min_value, max_value, freq='MS').strftime("%Y-%b").tolist()
date_mark = {i: dates[i] for i in range(0, 12)}



# navbar definition
sticky_navbar = dbc.NavbarSimple(
    children=[
        dbc.DropdownMenu(
            children=[
                dbc.DropdownMenuItem("Years", header=True),
                dbc.DropdownMenuItem("2020", href='/apps/year2020'),
                dbc.DropdownMenuItem("2021", href='/apps/year2021'),
                dbc.DropdownMenuItem("2022", href='/apps/year2022'),
                dbc.DropdownMenuItem("2023", href='/apps/year2023'),
            ],
            nav=True,
            in_navbar=True,
            label="Years",
        ),
    ],
    brand="Nashville Public Library Foundation",
    color="dark",
    dark=True,
    sticky="top",
)

badge = html.Div(
    [
        dbc.Badge("NPLF Marketing Dashboard"),
    ],
    className="badge",
)

# button group definitions
vertical_navbar = dbc.ButtonGroup(
    [
        dbc.Button("Overview", href="/apps/second"),
        dbc.Button("Reach"),
        dbc.Button("Impressions"),
        dbc.Button("Visits"),
        dbc.Button("Leads"),
        dbc.Button("Customers by Marketing"),
        dbc.Button("Conversions"),

    ],
    vertical=True,
    className="navbar-vertical",
)

# app and layout definition
app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    sticky_navbar,
    html.Div(id='page-content'),
])

# page navigation ---------------------------------------------------------
@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    print(pathname)
    if pathname == '/apps/year2021':
        return year2021.app.layout
    elif pathname == '/apps/year2022':
        return year2022.app.layout
    elif pathname == '/apps/year2023':
        return year2023.app.layout
    else:
        return year2020.app.layout

# first section -- Twitter ------------------------------------------------

@app.callback(Output(component_id='slider-one', component_property='marks'), [Input('slider-one', 'value'), Input("generate-button-one", "n_clicks"), Input("min-input-one", "value"), Input("max-input-one", "value")])
def on_button_click(X, n, minValue, maxValue):
    global date_mark
    changed_id = [p['prop_id'] for p in dash.callback_context.triggered][0]

    if 'generate-button-one' in changed_id:
        min_value = minValue
        max_value = maxValue
        new_date_mark = set_rangeslider(minValue, maxValue)[0]
        date_mark = new_date_mark
        return new_date_mark
    else: 
        return date_mark


@app.callback(Output('g7', 'figure'), [Input('slider-one', 'value'), Input("generate-button-one", "n_clicks"), Input('slider-one', 'marks')])
def update_graph(X, n, dates):
    # print("X: ", X)
    # print("n: ", n)
    # print("dates: ", dates)
    dates = list(dates.values())
    # print("dates as list", dates)

    df2 = df[(df.Date >= dates[X[0]]) & (df.Date <= dates[X[1]])]
    trace_1 = go.Scatter(x=df2.Date, y=df2['impressions'],
                        name='impressions',
                        line=dict(width=2,
                                    color='#00cc96'))
    trace_2 = go.Scatter(x=df2.Date, y=df2['engagement rate'],
                        name='engagement rate',
                        line=dict(width=2,
                                    color='#FF5733'))
    trace_3 = go.Scatter(x=df2.Date, y=df2['detail expands'],
                        name='detail expands',
                        line=dict(width=2,
                                    color='#D7BDE2'))
    trace_4 = go.Scatter(x=df2.Date, y=df2['likes'],
                        name='likes',
                        line=dict(width=2,
                                    color='#9467bd'))
    trace_5 = go.Scatter(x=df2.Date, y=df2['media views'],
                        name='media views',
                        line=dict(width=2,
                                    color='#ffa15a'))
    trace_6 = go.Scatter(x=df2.Date, y=df2['media engagements'],
                        name='media engagements',
                        line=dict(width=2,
                                    color='#1cd3f3'))
    fig1 = go.Figure(data=[trace_1, trace_2, trace_3, trace_4, trace_5, trace_6], layout=layout)
    return fig1

# second section -- Facebook ------------------------------------------------

@app.callback(Output(component_id='slider-two', component_property='marks'), [Input('slider-two', 'value'), Input("generate-button-two", "n_clicks"), Input("min-input-two", "value"), Input("max-input-two", "value")])
def on_button_click_2(X, n, minValue, maxValue):
    global date_mark
    changed_id = [p['prop_id'] for p in dash.callback_context.triggered][0]

    if 'generate-button-one' in changed_id:
        min_value = minValue
        max_value = maxValue
        new_date_mark = set_rangeslider(minValue, maxValue)[0]
        date_mark = new_date_mark
        return new_date_mark
    else: 
        return date_mark


# @app.callback(Output('g8', 'figure'), [Input('slider-two', 'value'), Input("generate-button-two", "n_clicks"), Input('slider-two', 'marks')])
# def update_graph_2(X, n, dates):
#     print("X: ", X)
#     print("n: ", n)
#     print("dates: ", dates)
#     dates = list(dates.values())
#     print("dates as list", dates)

#     df2 = df[(df.Date >= dates[X[0]]) & (df.Date <= dates[X[1]])]
#     trace_1 = go.Scatter(x=df2.Date, y=df2['impressions'],
#                         name='impressions',
#                         line=dict(width=2,
#                                     color='#00cc96'))
#     trace_2 = go.Scatter(x=df2.Date, y=df2['engagement rate'],
#                         name='engagement rate',
#                         line=dict(width=2,
#                                     color='#FF5733'))
#     trace_3 = go.Scatter(x=df2.Date, y=df2['detail expands'],
#                         name='detail expands',
#                         line=dict(width=2,
#                                     color='#D7BDE2'))
#     trace_4 = go.Scatter(x=df2.Date, y=df2['likes'],
#                         name='likes',
#                         line=dict(width=2,
#                                     color='#9467bd'))
#     trace_5 = go.Scatter(x=df2.Date, y=df2['media views'],
#                         name='media views',
#                         line=dict(width=2,
#                                     color='#ffa15a'))
#     trace_6 = go.Scatter(x=df2.Date, y=df2['media engagements'],
#                         name='media engagements',
#                         line=dict(width=2,
#                                     color='#1cd3f3'))
#     fig2 = go.Figure(data=[trace_1, trace_2, trace_3, trace_4, trace_5, trace_6], layout=layout)
#     return fig2

if __name__ == '__main__':
    app.run_server(debug=True)
