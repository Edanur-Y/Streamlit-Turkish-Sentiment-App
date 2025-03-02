import streamlit as st
import torch
from transformers import pipeline

torch.classes.__path__ = []

# Set page title and description
st.set_page_config(
    page_title="Duygu Analizi Uygulaması", page_icon=":pencil2:", layout="wide"
)

# Add a title and a description
st.title("Duygu Analizi Uygulaması")
st.write("Model; film, kitap, DVD, elektronik ve mutfak ürünlerinin değerlendirmeleriyle eğitilmiştir.")

# Initialize the Hugging Face model
model = pipeline("text-classification", model="savasy/bert-base-turkish-sentiment-cased")

# Create input parameters
for i in range(1,7):
    st.sidebar.markdown("#")
input_text = st.sidebar.chat_input("Cümle girin.")

for i in range(1,10):
    st.sidebar.markdown("#")

url="https://huggingface.co/savasy/bert-base-turkish-sentiment-cased"
st.sidebar.write(
    "Bu uygulama Hugging Face'den savasy'nin [bert-base-turkish-sentiment-cased](%s) modelini kullanarak duygu analizi yapar." % url
)


# Create a button to generate text
#generate_button = st.sidebar.button("Gönder")

st.markdown('##')
# Generate and display text when the button is clicked
if input_text:
    with st.spinner("Analiz ediliyor..."):
        output_text = model(input_text)[0]['label']
        score = model(input_text)[0]['score']
    st.write("**Girdi**:", input_text)

    st.markdown("#### Sonuç:")
    if output_text == "positive":
        st.write("***Pozitif*** 🙂")
    else:
        st.write("***Negatif*** 🙁")

    formatted_string = "{:.3f}".format(score)
    # format to two decimal places
    formatted_score = float(formatted_string)
    for i in range(1,4):
        st.markdown('#')
    st.write("Skor:", formatted_score)


