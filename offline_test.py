#!/usr/bin/env python3
from plotly import tools, offline
import plotly.plotly as py
import plotly.graph_objs as go

trace1 = go.Scatter(
    x=[0, 1, 2],
    y=[10, 11, 12]
)
trace2 = go.Scatter(
    x=[2, 3, 4],
    y=[100, 110, 120],
)
trace3 = go.Scatter(
    x=[3, 4, 5],
    y=[1000, 1100, 1200],
)
fig = tools.make_subplots(rows=3, cols=1, specs=[[{}], [{}], [{}]],
                          shared_xaxes=True, shared_yaxes=True,
                          vertical_spacing=0.001)
fig.append_trace(trace1, 3, 1)
fig.append_trace(trace2, 2, 1)
fig.append_trace(trace3, 1, 1)

fig['layout'].update(height=600, width=600, title='Stacked Subplots with Shared X-Axes')
#plot_url = py.plot(fig, filename='stacked-subplots-shared-xaxes')
offline.plot(fig, filename='stacked-subplots-shared-xaxes.html')