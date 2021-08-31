#!/usr/bin/env python
# coding: utf-8

import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Output, Input
import pandas as pd
import plotly.express as px


# liste_data = [{'x':['19-20','20-21','21-22'],'y':[34,48,53],'type':'bar'}]
df = pd.read_csv("nsi_vdd_v2.csv")
#print(df[:])
#fig_hist = px.histogram(data_frame=df,x='Année',y='Effectif')
#fig_hist.show()

# fig_bar = px.bar(data_frame=df,x='Année',y='Effectif',color='Classe')
# fig_bar.show()

appb = dash.Dash(__name__)
appb.layout = html.Div([
     html.H1('Spécialité NSI au Lycée VDD',style={'textAlign': 'center', 'color': '#7FDBFF'}),
        html.Div([
         html.H3('Evolution des effectifs par niveau'),
         html.Div(dcc.Dropdown(id='niveau',
                  options=[{'label':n, 'value':n}
                                       for n in df.Classe.unique()],
                 value='Prem'),
              style={"width": "25%"}),
         dcc.Graph(id='graphe1', figure={})
             ]),
     html.Div([
         html.H3('Evolution des effectifs cumulés'),
         dcc.Graph(id='graphe2',figure=px.histogram(data_frame=df, x='Année', y='Effectif',color='Classe'))],
         style={"width": "80%"})
 ])

@appb.callback(
     Output(component_id='graphe1', component_property='figure'),
     Input(component_id='niveau', component_property='value')
 )
def interactive_graphing(value_niveau):
     dff = df[df.Classe==value_niveau]
     fig = px.bar(data_frame=dff, x='Année', y='Effectif')
     return fig

if __name__=='__main__':
     appb.run_server(debug=True, use_reloader=False)
