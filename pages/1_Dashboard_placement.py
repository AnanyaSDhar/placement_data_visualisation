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

IMAGE_PATH = os.path.join(dir_of_interest, "images", "placement-services.png")
DATA_PATH = os.path.join(dir_of_interest, "data", "Placement_Data_Full_Class.csv")

st.title("Dashboard - Placement")

img = image.imread(IMAGE_PATH)
st.image(img)

df = pd.read_csv(DATA_PATH)
st.dataframe(df)

status = st.selectbox("Select the Status:", df['status'].unique())

col1, col2 = st.columns(2)

fig_1 = px.histogram(df[df['status'] == status], x="degree_percentage")
col1.plotly_chart(fig_1, use_container_width=True)

fig_2 = px.histogram(df[df['status'] == status], x="degree_type")
col1.plotly_chart(fig_2, use_container_width=True)

fig_3 = px.box(df[df['status'] == status], y="Employ_test_percentage")
col2.plotly_chart(fig_3, use_container_width=True)

fig_4 = px.scatter(df[df['status'] == status], x= "salary", y="Employ_test_percentage")
col2.plotly_chart(fig_4, use_container_width=True)
