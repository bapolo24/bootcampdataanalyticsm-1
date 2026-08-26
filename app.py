import streamlit as st
import pandas as pd

from funciones_calculo import (calcular_liquido,calcular_bsw,calcular_gor)
from funciones_datos import (filtrar_pozo,resumen_dataframe)
from clases_pozo import Pozo, campo



st.title("bootcamps data analytics for oil& gas")
st.sidebar.title("parametros")

modulos = st.sidebar.selectbox("seleccione un modulo", ["introduccion a variables", "Funciones", "POO", "importacion de librerias"])

if modulos == "introduccion a variables":

    pozo = "spe-001"
    petroleo_bpd = 1250
    agua_bpd = 350.50
    status = True
    liquido_total_bpd = petroleo_bpd + agua_bpd
    corte_agua_pct = (agua_bpd) / (liquido_total_bpd) * 100
    
    st.write(pozo)
    st.write(petroleo_bpd)
    st.write(agua_bpd)
    st.write(liquido_total_bpd)
    st.write(corte_agua_pct)
    
    st.sidebar.title("parametros")

elif modulos == "Funciones":
    
    def calcular_caudal_vogel(caudal_maximo=1000, presion_yacimiento=3000, presion_fondo=200, decimales=3):
        """
        Calcula el caudal de petróleo mediante la ecuación de Vogel.

        Parámetros:
        caudal_maximo (float): Caudal máximo teórico del pozo, BPD.
        presion_yacimiento (float): Presión promedio del yacimiento, psi.
        presion_fondo (float): Presión de fondo fluyente, psi.
        decimales (int): Número de decimales del resultado.

        Retorna:
        float: Caudal estimado de petróleo, BPD.

        """
        relacion_presion = presion_fondo / presion_yacimiento
        caudal = round(caudal_maximo * (1 - 0.2 * relacion_presion - 0.8 * relacion_presion**2), decimales)
        
        return (round(caudal, decimales))

    caudal_maximo = st.number_input("ingrese el caudal maximo", min_value=0, max_value=5000, value=1200)
    presion_yacimiento = st.number_input("ingrese la presion de yacimiento", min_value=0, max_value=5000, value=3000)
    presion_fondo = st.number_input("ingrese la presion de fondo", min_value=0, max_value=9000, value=1500)
    decimales = st.slider("seleccione la cantidad de decimales para el resultado", min_value=0, max_value=4, value=2)

    caudal = calcular_caudal_vogel(caudal_maximo, presion_yacimiento, presion_fondo, decimales)
    st.write("el caudal es:", caudal)

elif modulos == "POO":
    class pozo:
        def __init__(self, nombre, campo, petroleo, agua):
            self.n = nombre
            self.c = campo
            self.p = petroleo
            self.a = agua
        
        def mostrar_informacion(self):
            st.write("pozo:", self.n)
            st.write("campo:", self.c)
            st.write("petroleo:", self.p, "bpd")
            st.write("agua:", self.a, "bad")
        
        def produccion_total(self):
            total_produccion = self.p + self.a
            return total_produccion
        
        def proyectar_produccion(self, dias):
            produccion_proyectada = (self.p + self.a) * dias
            return produccion_proyectada

    nombre_pozo = st.text_input("ingrese nombre de pozo")
    nombre_campo = st.text_input("ingrese nombre de campo del pozo")
    petroleo = st.number_input("ingrese la produccion de petroleo", min_value=0, max_value=5000, value=1000)
    agua = st.number_input("ingrese la produccion de agua", min_value=0, max_value=9000, value=200)

    pozo = pozo(nombre_pozo, nombre_campo, petroleo, agua)
    st.write(pozo.mostrar_informacion())
    st.write(pozo.produccion_total())
    
    dias = st.number_input("ingrese los dias de produccion", min_value=0, max_value=365, value=30)
    st.write(pozo.proyectar_produccion(dias))

elif modulos == "importacion de librerias":
    st.title("aplicacion moduular con funciones")
    st.header ("1.uso de funciones")
    petroleo = st.number_input(
    "Producción de petróleo",
    min_value=0.0,
    value=800.0
    )
    
    agua = st.number_input(
        "Producción de agua",
        min_value=0.0,
        value=200.0
    )
    
    dias = st.number_input(
        "Días",
        min_value=1,
        value=30
    )
    
    if st.button("Calcular"):
        liquido = calcular_liquido(
            petroleo,
            agua
        )
    
        bsw = calcular_bsw(
            petroleo,
            agua
        )
    
        proyeccion = proyectar_produccion(
            petroleo,
            dias
        )
    
        st.write("Producción líquida:", liquido)
        st.write("BSW:", round(bsw, 2), "%")
        st.write("Producción proyectada:", proyeccion)
    
    
    st.header("2. Crear un objeto Pozo")
    
    nombre = st.text_input(
        "Nombre del pozo",
        value="PZ-001"
    )
    
    campo = st.text_input(
        "Campo",
        value="SPE"
    )
    
    gas = st.number_input(
        "Producción de gas",
        min_value=0.0,
        value=450.0
    )
    
    if st.button("Crear objeto"):
        pozo = Pozo(
            nombre,
            campo,
            petroleo,
            agua,
            gas
        )
    
        st.write("Objeto creado:")
        st.write(pozo.mostrar_informacion())
    
        st.write(
            "Producción líquida:",
            pozo.produccion_liquida()
        )
    
        st.write(
            "BSW:",
            round(pozo.bsw(), 2)
        )
    
        st.write(
            "GOR:",
            round(pozo.gor(), 2)
        )
    
    
    st.header("3. Composición de clases")
    
    pozo_1 = Pozo(
        "PZ-001",
        "SPE",
        800,
        200,
        450
    )
    
    pozo_2 = Pozo(
        "PZ-002",
        "SPE",
        650,
        250,
        380
    )
    
    campo = Campo("SPE")
    
    campo.agregar_pozo(pozo_1)
    campo.agregar_pozo(pozo_2)
    
    st.write(
        "Cantidad de pozos:",
        campo_auc.cantidad_pozos()
    )
    
    st.write(
        "Producción total de petróleo:",
        campo.produccion_petroleo_total()
    )
    
    st.dataframe(
        pd.DataFrame(
            campo.listar_pozos()
        )
    )
    
    
    st.header("4. Funciones aplicadas a datos")
    
    datos = pd.DataFrame({
        "pozo": [
            "PZ-001",
            "PZ-001",
            "PZ-002",
            "PZ-002"
        ],
        "petroleo": [
            800,
            790,
            650,
            640
        ]
    })
    
    st.dataframe(datos)
    
    pozo_seleccionado = st.selectbox(
        "Seleccione un pozo",
        datos["pozo"].unique()
    )
    
    resultado = filtrar_pozo(
        datos,
        pozo_seleccionado
    )
    
    st.write("Datos filtrados:")
    st.dataframe(resultado)
    
    st.write(
        "Resumen:",
        resumen_dataframe(datos)
    )
     
