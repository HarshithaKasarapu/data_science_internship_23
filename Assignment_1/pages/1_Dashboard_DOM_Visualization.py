import streamlit as st
from matplotlib import image
import pandas as pd
import plotly.express as px
import os

# absolute path to this file
FILE_DIR = os.path.dirname(os.path.abspath(__file__))
# absolute path to this file's root directory
PARENT_DIR = os.path.join(FILE_DIR, os.pardir)
# absolute path of directory_of_interest
dir_of_interest = os.path.join(PARENT_DIR, "resources")

IMAGE_PATH = os.path.join(dir_of_interest, "images", "dom.jpg")
DATA_PATH = os.path.join(dir_of_interest, "data", "dom_change_percent.csv")

st.title("Dashboard - Domestic Food Prices after COVID-19")

img = image.imread(IMAGE_PATH)
st.image(img)

df = pd.read_csv(DATA_PATH)
st.dataframe(df)

country = st.selectbox("Select the country", df['country'].unique())

col1, col2 = st.columns(2)

fig_1 = px.histogram(df[df['country'] == country], x="post_covid")
col1.plotly_chart(fig_1, use_container_width=True)

fig_2 = px.box(df[df['country'] == country], y="commodity")
col2.plotly_chart(fig_2, use_container_width=True)

fig_3 = px.scatter(df, x="post_covid", y="yearly", color="country")
fig_3

fig_4 = px.ecdf(df, x="price_type", color="country")
fig_4

fig_5 = px.bar(df, x="price_type", y="market", color="country", barmode="group")
fig_5

fig_6 = px.scatter_matrix(df, dimensions=["price_type","market" , "commodity", "post_covid", "yearly"], color="country")
fig_6
