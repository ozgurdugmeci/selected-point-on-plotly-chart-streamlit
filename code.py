# selected-point-on-plotly-chart-streamlit
obtain the value from charts made with streamlit
import streamlit as st
from bokeh.plotting import figure
import plotly.express as px
import pandas as pd
from streamlit_plotly_events import plotly_events



x = [1, 2, 3, 4, 5]
y = [6, 7, 2, 4, 5]

df=[]
df= pd.DataFrame(df)
df['year']= x
df['lifeExp']= y



p = figure(
 title='simple line example',
 x_axis_label='x',
 y_axis_label='y')

p.line(x, y, legend_label='Trend', line_width=2)

st.bokeh_chart(p, use_container_width=True)


'plotly'


# Writes a component similar to st.write()
#fig = px.line(x=[1], y=[1])
fig = px.line(df, x="year", y="lifeExp", title='Life expectancy in Canada')

selected_points = plotly_events(fig)

a=selected_points[0]
a=a['x']
a*4
