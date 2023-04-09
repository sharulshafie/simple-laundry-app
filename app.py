import streamlit as st 
from PIL import Image
import time


st.set_page_config('Laundry App')
st.markdown('<h1 style="text-align:center;">Laundry App</h1>', unsafe_allow_html=True)

image = Image.open('img-selfservicelaundry.jpg')
st.image(image)

berat = st.number_input('Sila isi berat (KG)', max_value=(25.00), step=(0.00))
trigger = True

if berat > 0:
    trigger = False
    
wang = st.number_input('Sila isi wang', disabled=trigger)

wangRate = 2
wangPay = wangRate * berat

st.text(f"Bayaran: RM {wangPay}")
st.text(f"Wang yang dimasukkan: RM {wang}")

if wang > wangPay:
    wangBalance = wang - wangPay
    st.text(f"Wang yang dimasukkan: RM {wangBalance}")

suhu = st.selectbox('Sila masukkan suhu', ('Sejuk', 'Suam', 'Panas'), disabled=trigger)

startButton = st.button('START')

if startButton == True:
    if berat == 0 and wang == 0:
        st.warning('Sila isi berat baju!')
    elif wang == 0:
        st.warning('Sila masukkan wang!')
    elif wang < wangPay:
        st.warning('Wang tidak mengcukupi!')
    else: 
        progressText = "Baju sedang dibasuh. Sila tunggu."
        progressBar = st.progress(0, text=progressText)
        
        for percentage_complete in range(100):
            time.sleep(0.1)
            progressBar.progress(percentage_complete + 1, text=progressText)
        
        st.success('Baju sudah dibasuh. Sila ambil baju anda.', icon='✅')
            