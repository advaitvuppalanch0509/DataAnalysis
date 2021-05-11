import pandas as pd
import csv
import plotly.graph_objects as go

pf=pd.read_csv("datapp.csv")

print(pf.groupby("level")["attempt"].mean())
fig = go.Figure(go.Scatter(
            x=['Level 1', 'Level 2', 'Level 3', 'Level 4'],
            y=pf.groupby("level")["attempt"].mean(),
            orientation='v'))

fig.show()