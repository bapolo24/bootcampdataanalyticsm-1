import streamlit as st
import pandas as pd
st.title("bootcamps data analytics for oil& gas")
st.sidebar.title("parametros")

modulos= st.sidebar.selectbox("seleccione un modulo", ["introduccion a variables", "Funciones"])

if modulos=="introduccion a variables":


pozo="spe-001"
petroleo_bpd=1250
agua_bpd=350.50
status= True
liquido_total_bpd=petroleo_bpd+agua_bpd
corte_agua_pct=(agua_bpd)/(liquido_total_bpd)*100
st.write(pozo)
st.write(petroleo_bpd)
st.write(agua_bpd)
st.write(liquido_total_bpd)
st.write(corte_agua_pct)

st.sidebar.title("parametros")

elif modulos=="funciones":

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
    relacion_presion= presion_fondo/presion_yacimiento
    caudal= round(caudal_maximo*(1-0.2*relacion_presion-0.8*relacion_presion**2), decimales)
    
    return (round(caudal,decimales))
    caudal_maximo=st.number_input("ingrese el caudal maximo")
    

