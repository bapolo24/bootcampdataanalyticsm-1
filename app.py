import streamlit as st
import pandas as pd
st.title("bootcamps data analytics for oil& gas")

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
