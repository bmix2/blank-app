
import pip
import pymongo
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

def BusquedaProvidencia (palabra):
    from pymongo import MongoClient
    client = MongoClient("mongodb+srv://jgonzalezl8:Sephiroth1@bigdata2024.zpsjf.mongodb.net/?retryWrites=true&w=majority&appName=BigData2024")
    db = client["BigData2023"]
    coleccion = db["sentencias"]
    for documento in coleccion.find({"providencia": {"$regex": palabra, "$options": "i"}}):
        print(documento)
    return documento

def BusquedaTipoProvidencia (palabra):
    from pymongo import MongoClient
    client = MongoClient("mongodb+srv://jgonzalezl8:Sephiroth1@bigdata2024.zpsjf.mongodb.net/?retryWrites=true&w=majority&appName=BigData2024")
    db = client["BigData2023"]
    coleccion = db["sentencias"]
    for documento in coleccion.find({"tipo": {"$regex": palabra, "$options": "i"}}):
        print(documento)
    return documento

def BusquedaAnio (palabra):
    from pymongo import MongoClient
    client = MongoClient("mongodb+srv://jgonzalezl8:Sephiroth1@bigdata2024.zpsjf.mongodb.net/?retryWrites=true&w=majority&appName=BigData2024")
    db = client["BigData2023"]
    coleccion = db["sentencias"]
    for documento in coleccion.find({"anio": {"$regex": palabra, "$options": "i"}}):
        print(documento)
    return documento

def main(): 

    #CONSULTANDO LA BASE DE DATOS DE SENTENCIA
    sentencias = ConexionSqlSentenciasDB() #cargando todos los registros de sentencia
     #CONSULTANDO LA BASE DE DATOS DE SIMILITUDES
    similitudes = ConexionSqlSimilitudesDB() #cargando todos los registros de similitudes

    st.title("🎈 My new app")
    st.write(
        " [docs.streamlit.io](https://docs.streamlit.io/)."
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
 