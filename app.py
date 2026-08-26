import streamlit as st
import pandas as pd

st.title("bootcamps data analytics for oil& gas")
st.sidebar.title("parametros")

modulos = st.sidebar.selectbox("seleccione un modulo", ["introduccion a variables", "Funciones", "POO"])

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
            print("pozo:", self.n)
            print("campo:", self.c)
            print("petroleo:", self.p, "bpd")
            print("agua:", self.a, "bad")
        
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
    st.write(pozo_obj.mostrar_informacion())
    st.write(pozo_obj.produccion_total())
    dias = st.number_input("ingrese los dias de produccion", min_value=0, max_value=365, value=30)
    st.write(pozo.proyectar_produccion(dias))


 
 
