import streamlit as st
import numpy as np
import tensorflow as tf
import tensorflow_hub as hub
from PIL import Image
from tensorflow.keras.models import load_model
import os

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
    unsafe_allow_html=True
)

def about_predict():
    st.title(f"Prediksi Data Anda")

    # Teks dengan format HTML dan CSS untuk warna putih, ukuran 12, dan rata kanan kiri
    st.markdown(
        """
        <h4 class="custom-text">
            Unggah Data Anda
        </h4>
        """, 
        unsafe_allow_html=True
    )

    # Unggah gambar
    uploaded_file = st.file_uploader("Unggah gambar Anda di sini", type=["jpg", "png", "jpeg"], label_visibility="collapsed")

    if uploaded_file is not None:
        # Membaca file yang diunggah
        image = Image.open(uploaded_file)
        
        # Menampilkan gambar
        st.image(image, caption="Gambar yang Anda unggah", use_container_width=True)
        
        # Menampilkan informasi gambar
        st.write("Dimensi gambar:", image.size)
        st.write("Format gambar:", image.format)

        # Memuat model dari file .h5
        model = load_model('data_and_model/efficientnet_finetuned.h5', custom_objects={'KerasLayer': hub.KerasLayer})
        class_names = np.array(['cat', 'dog', 'wild'])  # List nama kelas dari subdirektori

        # Fungsi untuk memproses gambar dan membuat prediksi
        def preprocess_image(image, img_shape=224):
            image = image.resize((img_shape, img_shape))  # Mengubah ukuran gambar
            img_array = np.array(image)  # Mengonversi menjadi array NumPy
            img_array = img_array / 255.0  # Normalisasi ke rentang [0, 1]
            return img_array

        # Fungsi untuk prediksi
        def predict_class(image, model, class_names):
            image_array = preprocess_image(image)
            image_array = np.expand_dims(image_array, axis=0)  # Menambahkan dimensi batch
            prediction = model.predict(image_array)
            predicted_class = class_names[np.argmax(prediction)]  # Mendapatkan kelas dengan probabilitas tertinggi
            return predicted_class

        pred_class = predict_class(image, model, class_names)

        st.markdown(
            f"""
            <h2 class="custom-text">
                Prediksi: {pred_class}
            </h2>
            """, 
            unsafe_allow_html=True
        )

# Menjalankan aplikasi prediksi
about_predict()