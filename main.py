import pickle
import streamlit as st
import plotly.graph_objects as go
#import pandas as pd
st.header("PRODUCTS")
df = pickle.load(open('df.pkl','rb'))

trace = go.Table(
    header=dict(values=list(df[['Title', 'Price','Popularity']].columns),
                fill_color='paleturquoise',
                align='left',font=dict(color='black', size=15),
    height=40),
    cells=dict(values=[df.Title, df.Price, df.Popularity],
               fill_color='lavender',
               align='left',font=dict(color='black', size=15),
    height=30))

fig=go.Figure(data=[trace])
fig.update_layout(margin=dict(l=20, r=20, t=20, b=20),paper_bgcolor="white")
st.write(fig)