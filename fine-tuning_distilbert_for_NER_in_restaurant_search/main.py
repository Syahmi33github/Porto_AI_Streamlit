import streamlit as st
import pandas as pd
import numpy as np

from transformers import pipeline

# Menambahkan CSS dengan beberapa opsi warna
st.markdown(
    """
    <style>
    /* Latar belakang aplikasi */
    .stApp {
        background-color: #1E1E2F; /* Latar belakang abu-abu gelap */
        color: #EAEAEA; /* Teks abu-abu terang */
    }
    /* Sidebar */
    .css-1d391kg {
        background-color: #2B2D42; /* Sidebar biru keabu-abuan */
    }
    /* Warna teks dan ikon di sidebar */
    .css-1cpxqw2, .css-qri22k {
        color: #F8F8F2; /* Teks dan ikon putih */
    }
    /* Warna hover untuk menu di sidebar */
    .css-qri22k:hover {
        color: #FFD700; /* Warna kuning keemasan saat hover */
    }
    .custom-label {
        color: white; /* Ganti dengan warna yang diinginkan */
        # font-weight: bold; /* Opsi: membuat label tebal */
        font-size: 14px; /* Opsi: mengatur ukuran font */
    }
    .predict_result_green {
        font-size: 40px;
        font-weight: bold;
        text-align: center;
        color: green;
    }
    .predict_result_red {
        font-size: 40px;
        font-weight: bold;
        text-align: center;
        color: red;
    }
    .custom-text {
        color: white;
        font-size: 12px;
        text-align: justify;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.title("Entity Predictions:")
classifier = pipeline(
    "token-classification",
    model="model/content/ner_distilbert",
    aggregation_strategy="simple",
)


text = st.text_area("Enter some text")

if st.button("Predict"):
    data = classifier(text)

    result = [
        {"word": item["word"], "entity_group": item["entity_group"]} for item in data
    ]

    for item in result:
        st.markdown(
            f"""
            <div style="border:1px solid #ddd; padding:10px; border-radius:5px; margin-bottom:5px;">
                <strong>Word:</strong> {item["word"]} <br>
                <strong>Entity:</strong> {item["entity_group"]}
            </div>
            """,
            unsafe_allow_html=True,
        )
    st.write()
