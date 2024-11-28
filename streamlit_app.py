
import pip
import pymongo
import pandas as pd
from PIL import Image
from pymongo import MongoClient
import streamlit as st
import unicodedata

st.set_page_config(page_title="Sentencias Automate",initial_sidebar_state="expanded")

def generar_regex_tildes(palabra):
    equivalencias = {
        "a": "[aá]",
        "e": "[eé]",
        "i": "[ií]",
        "o": "[oó]",
        "u": "[uúü]",
        "n": "[nñ]",
        "A": "[AÁ]",
        "E": "[EÉ]",
        "I": "[IÍ]",
        "O": "[OÓ]",
        "U": "[UÚÜ]",
        "N": "[NÑ]"
    }

    # Reemplazar cada carácter por su equivalencia con y sin tildes
    regex = ''.join(equivalencias.get(c, c) for c in palabra)
    return regex

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

def BusquedaProvidencia(palabra):
    
    # Conexión al cliente MongoDB
    client = MongoClient("mongodb+srv://jgonzalezl8:Sephiroth1@bigdata2024.zpsjf.mongodb.net/?retryWrites=true&w=majority&appName=BigData2024")
    db = client["BigData2023"]
    coleccion = db["sentencias"]
    
    # Consulta a la base de datos
    resultados = list(coleccion.find({"providencia": {"$regex": palabra, "$options": "i"}},{'_id': 0}))
    
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
    resultados = list(coleccion.find({"tipo": {"$regex": palabra, "$options": "i"}},{'_id': 0}))
    
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
    resultados = list(coleccion.find({"anio": {"$regex": palabra, "$options": "i"}},{'_id': 0}))
    
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

    # Generar la expresión regular para la palabra
    regex_palabra = generar_regex_tildes(palabra)

    # Consultar en la colección
    resultados = list(coleccion.find({"texto": {"$regex": regex_palabra, "$options": "i"}}, {'_id': 0}))
    
    # Convertir a DataFrame
    if resultados:
        df = pd.DataFrame(resultados)
    else:
        df = pd.DataFrame()  # DataFrame vacío si no hay resultados 
    return df

def BusquedaSimilitudProvidenciaUmbral(palabra, umbral):
    
    # Conexión al cliente MongoDB
    client = MongoClient("mongodb+srv://jgonzalezl8:Sephiroth1@bigdata2024.zpsjf.mongodb.net/?retryWrites=true&w=majority&appName=BigData2024")
    db = client["BigData2023"]
    coleccion = db["Similitudes"]
    
    # Consulta a la base de datos
    resultados =  list(coleccion.find({"providencia1": {"$regex": palabra, "$options": "i"}, "index_simm": {"$gt": umbral}},{'_id': 0}))
    resultados2 = list(coleccion.find({"providencia2": {"$regex": palabra, "$options": "i"}, "index_simm": {"$gt": umbral}},{'_id': 0}))
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
   
    resultados = list(coleccion.find({"providencia1": {"$regex": palabra, "$options": "i"}},{'_id': 0}))
    resultados2 = list(coleccion.find({"providencia2": {"$regex": palabra, "$options": "i"}},{'_id': 0}))
    for i in resultados2:
        resultados.append(i)

    # Convertir a DataFrame
    if resultados:
        df = pd.DataFrame(resultados)
    else:
        df = pd.DataFrame()  # DataFrame vacío si no hay resultados 
    return df

def FuncionGraficarV6(df):
    import networkx as nx
    import matplotlib.pyplot as plt

    if not df.empty:
        # Verificar y renombrar columnas
        df.columns = ["providencia1", "providencia2", "similitud"]

        # Eliminar duplicados
        df = df.drop_duplicates(subset=["providencia1", "providencia2", "similitud"])

        # Crear un grafo vacío
        G = nx.Graph()

        # Manejar el caso de un solo registro
        if len(df) == 1:
            # Obtener los valores del único registro
            origen = df.iloc[0]["providencia1"]
            destino = df.iloc[0]["providencia2"]
            similitud = df.iloc[0]["similitud"]

            # Agregar nodos
            G.add_node(origen)
            G.add_node(destino)

            # Agregar siempre la arista entre los dos nodos
            G.add_edge(origen, destino, weight=similitud)

        # Manejar el caso de múltiples registros
        elif len(df) > 1:
            # Agregar aristas con pesos para registros con similitud > 0.5
            for _, row in df.iterrows():
                origen = row["providencia1"]
                destino = row["providencia2"]
                similitud = row["similitud"]

                if similitud > 0.5:
                    G.add_edge(origen, destino, weight=similitud)

        # Verificar si el grafo tiene nodos
        if len(G.nodes) == 0:
            print("No hay relaciones significativas (similitud > 0.5) para graficar.")
            return

        # Obtener posiciones de los nodos
        pos = nx.spring_layout(G)

        # Extraer pesos de las aristas
        edges = G.edges(data=True)
        weights = [d['weight'] for (u, v, d) in edges]

        # Normalizar pesos para controlar grosor
        if weights:
            min_weight = min(weights)
            max_weight = max(weights)
            normalized_weights = [(w - min_weight) / (max_weight - min_weight) * 2 + 0.5 for w in weights]
        else:
            normalized_weights = [10000]  # Asignar un grosor por defecto

        # Configurar visualización en pantalla completa
        plt.figure(figsize=(16, 9))  # Tamaño personalizado para ocupar la pantalla completa
        plt.subplots_adjust(left=0, right=1, top=1, bottom=0)  # Quitar márgenes

        # Dibujar nodos
        nx.draw_networkx_nodes(G, pos, node_size=700, node_color='lightblue')

        # Dibujar aristas con grosor ajustado
        nx.draw_networkx_edges(G, pos, width=normalized_weights, edge_color='red')

        # Dibujar etiquetas de nodos
        nx.draw_networkx_labels(G, pos, font_size=12, font_color='black', font_weight='bold')

        # Dibujar etiquetas de aristas (pesos)
        edge_labels = nx.get_edge_attributes(G, 'weight')
        nx.draw_networkx_edge_labels(G, pos, edge_labels={(u, v): f"{d:.2f}" for (u, v), d in edge_labels.items()})

        # Mostrar el grafo
        plt.title("Grafo de Similitudes", fontsize=16)
        plt.axis('off')  # Ocultar ejes
        plt.show()
    else:
        print("El DataFrame está vacío. Por favor, proporcione datos válidos.")



def main(): 
    
    menu =["INICIO","SENTENCIAS(Busqueda por Nombre)","SENTENCIAS(Busqueda por Tipo)","SENTENCIAS(Busqueda por Año)","SENTENCIAS(Busqueda por Texto)","SIMILITUDES y NODOS (BASE SUMINISTRADA)"]
    st.sidebar.header("SetenceApp ⚖️", divider="gray")
    eleccion = st.sidebar.selectbox("MENU PRINCIPAL",menu)

    
    if eleccion =="INICIO":
        
        st.title("SentenceApp - Sentencias a tu alcance.")
        st.write(
            " <- Nuestro Menú "
        )
        img = Image.open("Portada2.jpeg")
        st.image(img,use_column_width="True")


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
    

    elif eleccion == "SIMILITUDES y NODOS (BASE SUMINISTRADA)":

        st.subheader("SIMILITUDES: Busqueda x Providencia (Base de datos JSON suministrada) (Visualizacion de Nodos)")
        nombre_providencia2 = st.text_input("Ingrese nombre de la providencia para mostrar sus similitudes", key = 3)

        st.subheader("Umbral Minimo para la busqueda: ")
        simPick = st.slider('Seleccione el umbral inferior para generar los nodos', 
            min_value= 0.1,
            max_value = 100.0,
            value=0.5,
            step=0.01
        )

        dfConsulted = BusquedaSimilitudProvidenciaUmbral(nombre_providencia2,simPick)

        st.dataframe(
           dfConsulted
        )
        st.subheader(
            "VISUALIZACION DE NODOS: ", divider="gray"
        )
        st.pyplot(
            FuncionGraficarV6(dfConsulted)
        )
        

main()
 