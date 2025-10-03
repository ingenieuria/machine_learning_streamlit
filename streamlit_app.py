import streamlit as st
import pandas as pd 

#Titre de notre application 
st.title("Application de ML .🤖")

st.info("Cette application est un modèle de machine learning")

train = pd.read_csv("data/train.csv")
train