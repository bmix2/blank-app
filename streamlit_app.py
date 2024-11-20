
import pip
import pymongo
import pandas as pd
from pymongo import MongoClient
import streamlit as st
st.set_page_config(page_title="Sentencias Automate")


def ConexionSqlSentenciasDB():
    client = MongoClient("mongodb+srv://jgonzalezl8:Sephiroth1@bigdata2024.zpsjf.mongodb.net/?retryWrites=true&w=majority&appName=BigData2024")
    db = client["BigData2023"]
    coleccion = db["sentencias"]
    sentencias = coleccion.find()
    return sentencias

def ConexionSqlSimilitudesDB():
    client = MongoClient("mongodb+srv://jgonzalezl8:Sephiroth1@bigdata2024.zpsjf.mongodb.net/?retryWrites=true&w=majority&appName=BigData2024")
    db = client["Simulitud"]
    coleccion = db["Similitudes"]
    similitudes = coleccion.find()
    return similitudes

def BusquedaProvidencia(palabra):
    
    # Conexión al cliente MongoDB
    client = MongoClient("mongodb+srv://jgonzalezl8:Sephiroth1@bigdata2024.zpsjf.mongodb.net/?retryWrites=true&w=majority&appName=BigData2024")
    db = client["BigData2023"]
    coleccion = db["sentencias"]
    
    # Consulta a la base de datos
    resultados = list(coleccion.find({"providencia": {"$regex": palabra, "$options": "i"}}))
    
    # Convertir a DataFrame
    if resultados:
        df = pd.DataFrame(resultados)
    else:
        df = pd.DataFrame()  # DataFrame vacío si no hay resultados 
    return df

def BusquedaTipoProvidencia(palabra):
    
    # Conexión al cliente MongoDB
    client = MongoClient("mongodb+srv://jgonzalezl8:Sephiroth1@bigdata2024.zpsjf.mongodb.net/?retryWrites=true&w=majority&appName=BigData2024")
    db = client["BigData2023"]
    coleccion = db["sentencias"]
    
    # Consulta a la base de datos
    resultados = list(coleccion.find({"tipo": {"$regex": palabra, "$options": "i"}}))
    
    # Convertir a DataFrame
    if resultados:
        df = pd.DataFrame(resultados)
    else:
        df = pd.DataFrame()  # DataFrame vacío si no hay resultados 
    return df

def main(): 

    #CONSULTANDO LA BASE DE DATOS DE SENTENCIA
    sentencias = ConexionSqlSentenciasDB() #cargando todos los registros de sentencia
     #CONSULTANDO LA BASE DE DATOS DE SIMILITUDES
    similitudes = ConexionSqlSimilitudesDB() #cargando todos los registros de similitudes

    st.title("🎈 My new app")
    st.write(
        " [docs.streamlit.io](https://docs.streamlit.io/)."
    )

    st.subheader("SENTENCIAS: Busqueda por Nombre de providencia")
    nombre_providencia = st.text_input("Ingrese el nombre de la providencia", key = 1)
    st.dataframe(
        BusquedaProvidencia(nombre_providencia)
    )

    st.subheader("SENTENCIAS: Busqueda por tipo de providencia")
    tipo_providencia = st.text_input("Ingrese el tipo de la providencia", key = 2)
    st.dataframe(
        BusquedaTipoProvidencia(tipo_providencia)
    )


    
    st.subheader("SENTENCIAS: Busqueda dinamica")
    st.dataframe(
        sentencias
    )

    st.subheader("SIMILITUDES: Busqueda dinamica")
    st.dataframe(
        similitudes
    )
    
main()
 