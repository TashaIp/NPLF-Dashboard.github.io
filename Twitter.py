import dash
import dash_html_components as html
import dash_core_components as dcc
import plotly.express as px
import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile
import plotly.graph_objects as go
import plotly
from plotly.subplots import make_subplots


excel_file = 'NPLF Twitter Q1.xls'
#df = pd.read_excel(excel_file)
df = pd.read_excel('NPLF Twitter Q1.xls', sheet_name = [0,1,2])
df2 = pd.read_excel('NPLF Twitter Q1.xls', sheet_name = 'NPLF Twitter April')
df3 = pd.read_excel('NPLF Twitter Q1.xls', sheet_name = 'NPLF Twitter May')
df4 = pd.read_excel('NPLF Twitter Q1.xls', sheet_name = 'NPLF Twitter June')
print(df)

#fig = make_subplots(rows=2, cols=2, column_widths=[0.5, 0.5],
#                    subplot_titles=("Engagements in April", "Engagements in May", "engagements in June",))

fig1 = px.bar(df2, x=df2.Date, y=df2.engagements, title = "Engagements in April")
fig1.show()

fig2 = px.bar(df3, x=df3.Date, y=df3.engagements, title = "Engagements in May")
fig2.show()

fig3 = px.bar(df4, x=df4.Date, y=df4.engagements, title = "Engagements in June")
fig3.show()

fig4 = px.bar(df2, x=df2.Date, y=df2.likes, title = "Likes in April")
fig4.show()

fig5 = px.bar(df3, x=df3.Date, y=df3.likes, title = "Likes in May")
fig5.show()

fig5 = px.bar(df4, x=df4.Date, y=df4.likes, title = "Likes in June")
fig5.show()

fig6 = px.bar(df2, x=df2.Date, y=df2.impressions, title = "Impressions in April")
fig6.show()

fig7 = px.bar(df3, x=df3.Date, y=df3.impressions, title = "Impressions in May")
fig7.show()

fig8 = px.bar(df4, x=df4.Date, y=df4.impressions, title = "Impressions in June")
fig8.show()



#fig.add_trace(
#    go.Scatter(x=df['Date'] , y = df[ 'engagements'], mode='lines+markers', line_color="#9467bd"),
#    row=1, col=2
#)
#fig.add_trace(
#   go.Scatter(x=df['Date'] , y = df[ 'engagements'], mode='lines+markers', line_color="#ef5a41"),
#    row=2, col=1
#)
#fig.add_trace(
#    go.Scatter(x=df['Date'] , y = df[ 'engagements'], mode='lines+markers', line_color="#ef5a41"),
 #   row=2, col=2
#)


fig.update_layout(
autosize=False,
    width=2000,
    height=1500,
    margin=dict(
        l=50,
        r=50,
        b=100,
        t=100,
        pad=20
    ),
    paper_bgcolor="LightSteelBlue",
    title=go.layout.Title(
        text="Facebook Page Quarter 2",
        xref="paper",
        x=0
    ),
    xaxis=go.layout.XAxis(
        title=go.layout.xaxis.Title(
            text="Daily Page Engaged Users",
            font=dict(
                family="Comissioner, sans-serif",
                size=18,
                color="#7f7f7f"
            )
        )
    ),
    yaxis=go.layout.YAxis(
        title=go.layout.yaxis.Title(
            text="Date",
            font=dict(
                family="Comissioner, sans-serif",
                size=18,
                color="#7f7f7f"
            )
        )
    )
)
fig.show()



layout = plot.Layout(
    title="Facebook"
)


fig1 = plot.Figure(data=plot.Scatter(x=df['Date'], y=df['Facebook Advertising'], mode='lines+markers', ))
fig2 = plot.Figure(data=plot.Scatter(x=df['Date'], y=df['Facebook Reach'], mode='lines+markers', line_color="#ef5a41"))
fig3 = plot.Figure(data=plot.Scatter(x=df['Date'], y=df['Google Analytics'], mode='lines+markers', line_color="#00cc96"))
fig4 = plot.Figure(data=plot.Scatter(x=df['Date'], y=df['Twitter Reach'], mode='lines+markers', line_color="#9467bd"))
fig5 = plot.Figure(data=plot.Scatter(x=df['Date'], y=df['LinkedIn Reach'], mode='lines+markers', line_color="#ffa15a"))
fig6 = plot.Figure(data=plot.Scatter(x=df['Date'], y=df['Email Marketing'], mode='lines+markers', line_color="#1cd3f3"))
fig7 = plot.Figure()
fig7.add_trace(plot.Scatter(x=df['Date'], y=df['Facebook Advertising'],
                    mode='lines+markers',
                    name='Facebook Advertising'))
fig7.add_trace(plot.Scatter(x=df['Date'], y=df['Facebook Reach'],
                    mode='lines+markers', name='Facebook Reach'))
fig7.add_trace(plot.Scatter(x=df['Date'], y=df['Google Analytics'],
                    mode='lines+markers', name='Google Analytics'))
fig7.add_trace(plot.Scatter(x=df['Date'], y=df['Twitter Reach'],
                    mode='lines+markers', name='Twitter Reach'))
fig7.add_trace(plot.Scatter(x=df['Date'], y=df['LinkedIn Reach'],
                    mode='lines+markers', name='LinkedIn Reach'))
fig7.add_trace(plot.Scatter(x=df['Date'], y=df['Email Marketing'],
                    mode='lines+markers', name='Email Marketing'))


app = dash.Dash(__name__)
app.layout = html.Div([
    html.Div([
            html.H3('Facebook Page Quarter 2'),
            dcc.Graph(
                id='g7',
                figure=data,
        )], className="heading bottom"),

    html.Div([
        html.Div([
            html.H3('Facebook Advertising'),
            dcc.Graph(
                id='g1',
                figure=fig1)],
        className="heading"),

        html.Div([
            html.H3('Facebook Reach'),
            dcc.Graph(
                id='g2', figure=fig2)],
        className="heading"),
    ],
    className="row top"),

    html.Div([
        html.Div([
            html.H3('Google Analytics'),
            dcc.Graph(
                id='g3',
                figure=fig3)],
        className="heading"),

        html.Div([
            html.H3('Twitter Reach'),
            dcc.Graph(
                id='g4',
                figure=fig4)],
                className="heading")],
        className="row"),

    html.Div([
        html.Div([
            html.H3('LinkedIn Reach'),
            dcc.Graph(
                id='g5',
                figure=fig5)],
        className="heading"),

        html.Div([
            html.H3('Email Marketing'),
            dcc.Graph(
                id='g6',
                figure=fig6)],
        className="heading")],
    className="row"),

    # html.Div([
    #         html.H3('Summary'),
    #         dcc.Graph(
    #             id='g7',
    #             figure=fig7,
    #     )], className="heading bottom"),

    html.Div([
        html.H5('Source: Nashville Public Library Foundation Official Records')
    ], className="source")
],  className="container",)

if __name__ == "__main__":
    app.run_server(debug=True)

