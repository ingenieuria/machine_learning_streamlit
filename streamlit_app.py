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
    
#Préparation de données
with st.sidebar:
    st.header("Nos features")
    "Pclass","Age","SibSp","Parch","Fare",
    sex = st.selectbox("Sex", ("male", "female"))
    embarked = st.selectbox("Embarked", ("S", "C", "Q"))
    pclass = st.slider("Selectionnez votre class", min_value=1, max_value=3, value=1, step=1)
    st.write(f"Pclass : {pclass}")
    age = st.slider("Selectionnez votre âge", min_value=0, max_value=100, value=0, step=0.1)
    st.write(f"Age : {age}")
    
    #","SibSp","Parch","Fare"
    
    
    