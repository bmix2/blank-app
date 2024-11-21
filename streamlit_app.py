
import pip
import pymongo
import pandas as pd
from PIL import Image
from pymongo import MongoClient
import streamlit as st
st.set_page_config(page_title="Sentencias Automate",initial_sidebar_state="expanded")



def ConexionSqlSentenciasDB():
    client = MongoClient("mongodb+srv://jgonzalezl8:Sephiroth1@bigdata2024.zpsjf.mongodb.net/?retryWrites=true&w=majority&appName=BigData2024")
    db = client["BigData2023"]
    coleccion = db["sentencias"]
    sentencias = coleccion.find()
    return sentencias

def ConexionSqlSimilitudesDB():
    client = MongoClient("mongodb+srv://jgonzalezl8:Sephiroth1@bigdata2024.zpsjf.mongodb.net/?retryWrites=true&w=majority&appName=BigData2024")
    db = client["BigData2023"]
    coleccion = db["Similitudes"]
    similitudes = coleccion.find()
    return similitudes

def ConexionSqlSimilitudes2DB():
    client = MongoClient("mongodb+srv://jgonzalezl8:Sephiroth1@bigdata2024.zpsjf.mongodb.net/?retryWrites=true&w=majority&appName=BigData2024")
    db = client["BigData2023"]
    coleccion = db["Similitudes2"]
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

def BusquedaAnioProvidencia(palabra):
    
    # Conexión al cliente MongoDB
    client = MongoClient("mongodb+srv://jgonzalezl8:Sephiroth1@bigdata2024.zpsjf.mongodb.net/?retryWrites=true&w=majority&appName=BigData2024")
    db = client["BigData2023"]
    coleccion = db["sentencias"]
    
    # Consulta a la base de datos
    resultados = list(coleccion.find({"anio": {"$regex": palabra, "$options": "i"}}))
    
    # Convertir a DataFrame
    if resultados:
        df = pd.DataFrame(resultados)
    else:
        df = pd.DataFrame()  # DataFrame vacío si no hay resultados 
    return df

def BusquedaTextoProvidencia(palabra):
    
    # Conexión al cliente MongoDB
    client = MongoClient("mongodb+srv://jgonzalezl8:Sephiroth1@bigdata2024.zpsjf.mongodb.net/?retryWrites=true&w=majority&appName=BigData2024")
    db = client["BigData2023"]
    coleccion = db["sentencias"]
    
    # Consulta a la base de datos
    resultados = list(coleccion.find({"texto": {"$regex": palabra, "$options": "i"}}))
    
    # Convertir a DataFrame
    if resultados:
        df = pd.DataFrame(resultados)
    else:
        df = pd.DataFrame()  # DataFrame vacío si no hay resultados 
    return df

def BusquedaSimilitudProvidencia2(palabra):
    
    # Conexión al cliente MongoDB
    client = MongoClient("mongodb+srv://jgonzalezl8:Sephiroth1@bigdata2024.zpsjf.mongodb.net/?retryWrites=true&w=majority&appName=BigData2024")
    db = client["BigData2023"]
    coleccion = db["Similitudes2"]
    
    # Consulta a la base de datos
    resultados = list(coleccion.find({"providencia1": {"$regex": palabra, "$options": "i"}}))
    resultados2 = list(coleccion.find({"providencia2": {"$regex": palabra, "$options": "i"}}))
    for i in resultados2:
        resultados.append(i)

    # Convertir a DataFrame
    if resultados:
        df = pd.DataFrame(resultados)
    else:
        df = pd.DataFrame()  # DataFrame vacío si no hay resultados 
    return df

def BusquedaSimilitudProvidencia(palabra):
    
    # Conexión al cliente MongoDB
    client = MongoClient("mongodb+srv://jgonzalezl8:Sephiroth1@bigdata2024.zpsjf.mongodb.net/?retryWrites=true&w=majority&appName=BigData2024")
    db = client["BigData2023"]
    coleccion = db["Similitudes"]
    
    # Consulta a la base de datos
    resultados = list(coleccion.find({"providencia1": {"$regex": palabra, "$options": "i"}}))
    resultados2 = list(coleccion.find({"providencia2": {"$regex": palabra, "$options": "i"}}))
    for i in resultados2:
        resultados.append(i)

    # Convertir a DataFrame
    if resultados:
        df = pd.DataFrame(resultados)
    else:
        df = pd.DataFrame()  # DataFrame vacío si no hay resultados 
    return df

def main(): 

    #CONSULTANDO LA BASE DE DATOS DE SENTENCIA
    #sentencias = ConexionSqlSentenciasDB() #cargando todos los registros de sentencia
    
    #CONSULTANDO LA BASE DE DATOS DE SIMILITUDES
    #similitudes = ConexionSqlSimilitudesDB() #cargando todos los registros de similitudes

    #CONSULTANDO LA BASE DE DATOS DE SIMILITUDES2
    #similitudes2 = ConexionSqlSimilitudes2DB() #cargando todos los registros de similitudes

    
    menu =["INICIO","SENTENCIAS(Busqueda por Nombre)","SENTENCIAS(Busqueda por Tipo)","SENTENCIAS(Busqueda por Año)","SENTENCIAS(Busqueda por Texto)","SIMILITUDES (BASE SUMINISTRADA)","SIMILITUDES (BASE PROPIA)"]
    st.sidebar.header("SetenceApp 🧑‍⚖️")
    eleccion = st.sidebar.selectbox("MENU PRINCIPAL",menu)
    if eleccion =="INICIO":
        img = Image.open("Captura.PNG")
        st.image(img,use_column_width="True")
        st.title("🧑‍⚖️ SentenceApp - Sentencias a tu alcance...")
        st.write(
            " [docs.streamlit.io](https://docs.streamlit.io/)."
        )


    elif eleccion == "SENTENCIAS(Busqueda por Nombre)":

        st.subheader("SENTENCIAS: Busqueda por Nombre de providencia")
        nombre_providencia = st.text_input("Ingrese el nombre de la providencia", key = 1)
        st.dataframe(
            BusquedaProvidencia(nombre_providencia)
        )
        

    elif eleccion == "SENTENCIAS(Busqueda por Tipo)":
        
        st.subheader("SENTENCIAS: Busqueda por tipo de providencia")
        opcionTipo = st.selectbox('Seleccione el tipo de Sentencia', 
            ['Auto','Tutela','Constitucionalidad']
        )

        st.dataframe(
            BusquedaTipoProvidencia(opcionTipo)
        )


    elif eleccion == "SENTENCIAS(Busqueda por Año)":

        st.subheader("SENTENCIAS: Busqueda por año")
        opcionAnio = st.slider('Seleccione el año de la Sentencia', 
            min_value= 1990,
            max_value =2050,
            value=2009,
            step=1
        )
        st.dataframe(
            BusquedaAnioProvidencia(""+(str(opcionAnio))), width=800
        )
    elif eleccion == "SENTENCIAS(Busqueda por Texto)":

        st.subheader("SENTENCIAS: Busqueda por texto de providencia")
        nombre_providencia = st.text_area("Ingrese el texto que desea buscar en la providencia", key = 2, height=100)
        st.dataframe(
            BusquedaTextoProvidencia(nombre_providencia)
        )
    
    elif eleccion == "SIMILITUDES (BASE SUMINISTRADA)":
        st.subheader("SIMILITUDES: Busqueda x Providencia (Base de datos JSON suministrada)")
        nombre_providencia2 = st.text_input("Ingrese nombre de la providencia para mostrar sus similitudes", key = 3)
        st.dataframe(
            BusquedaSimilitudProvidencia(nombre_providencia2)
        )

    elif eleccion == "SIMILITUDES (BASE PROPIA)":
        st.subheader("SIMILITUDES: Busqueda x Providencia (Base de datos calculada)")
        nombre_providencia2 = st.text_input("Ingrese nombre de la providencia para mostrar sus similitudes", key = 4)
        st.dataframe(
            BusquedaSimilitudProvidencia2(nombre_providencia2)
        )

main()
 