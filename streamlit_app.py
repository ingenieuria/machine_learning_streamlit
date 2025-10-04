import streamlit as st
import pandas as pd 

#Titre de notre application 
st.title("Application de ML .🤖")

st.info("Cette application est un modèle de machine learning")

with st.expander("Données"):
    st.write('**La donnée brute**')
    train = pd.read_csv("data/train.csv", index_col="PassengerId")
    train
    
    st.write("**X**")
    X = train.drop(labels=["Survived"], axis=1)
    X
    
    st.write("**y**")
    y = train.Survived
    y
    
    with st.expander("Visualisation de données"):
        st.scatter_chart(data=train, x="Age", y="Fare", color="Survived")