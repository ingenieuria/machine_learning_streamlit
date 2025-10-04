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
    X = train.drop(labels=["Survived", "Ticket"], axis=1)
    X
    
    st.write("**y**")
    y = train.Survived
    y
    
with st.expander("Visualisation de données"):
    st.scatter_chart(data=train, x="Age", y="Fare", color="Survived")
    
#Préparation de données
with st.sidebar:
    st.header("Nos features")
    
    pclass = st.slider("Selectionnez votre class", min_value=1, max_value=3, value=1, step=1)
    st.write(f"Pclass : {pclass}")
    
    name = st.selectbox("Title",("Mr", "Miss", "Rev", "Llord"))
    st.write(f"Titles : {name}")  
    
    sex = st.selectbox("Sex", ("male", "female"))
    

    age = st.slider("Selectionnez votre âge", min_value=0.0, max_value=100.0, value=0.0, step=0.1)
    st.write(f"Age : {age}")
    
    sibsp = st.slider("Nombre de frères/soeurs (SibSp)", min_value=1, max_value=10, value=0, step=1)
    st.write(f"SibSp : {sibsp}")
    
    parch = st.slider("Nombre de parents/enfants (Parch)", min_value=1, max_value=10, value=0, step=1)
    st.write(f"Parch : {parch}")
    
    fare = st.slider("Prix du billet (Fare)", min_value=0.0, max_value=100.0, value=0.0, step=0.1)
    st.write(f"Fare : {fare}")
    
    embarked = st.selectbox("Pord d'embarguement", ("S", "C", "Q"))
    
    
#Creation d'un DataFrame pour nos features
data_df = {    
    "pclass":pclass,
    "name" : name,
    "sex" :sex,
    "age" :age,
    "sibsp" :sibsp,
    "parch" :parch,
    "fare" :fare,
    "embarked" :embarked
        }

input_df = pd.DataFrame(data_df, index=[0])
input_titanic = pd.concat([input_df, X], axis=0)

with st.expander("Les inout features"):
    st.write("**Input penguin**")
    input_df
    st.write("**Combine titanic data**")
    input_titanic
    
   
    
    
    