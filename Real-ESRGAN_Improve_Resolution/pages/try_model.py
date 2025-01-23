import subprocess

import os
import streamlit as st
from PIL import Image

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
    unsafe_allow_html=True
)

def try_model():
    st.title(f"Try Real-ESRGAN")
    # st.header('Snowflake Healthcare App')

    # ================================ Unggah Gambar ================================
    
    # Pastikan folder "image/low_resolution" ada
    folder_path = "images/low_resolution"
    os.makedirs(folder_path, exist_ok=True)

    # Teks dengan format HTML dan CSS untuk warna putih, ukuran 12, dan rata kanan kiri
    st.markdown(
        """
        <h3 class="custom-text">
            Upload Image
        </h3>
        """, 
        unsafe_allow_html=True
    )

    # Widget upload file
    uploaded_file = st.file_uploader("Unggah gambar", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        # Tampilkan gambar
        image = Image.open(uploaded_file)
        st.image(image, caption="Gambar yang diunggah", use_container_width=True)

        # Simpan file ke folder
        file_path = os.path.join(folder_path, uploaded_file.name)
        with open(file_path, "wb") as f:
            f.write(uploaded_file.getbuffer())
        
        st.success(f"Image successfully uploaded")


    # ================================ Unggah Gambar ================================

    command = [
        "python", "Real-ESRGAN/inference_realesrgan.py",
        "-n", "RealESRGAN_x4plus",
        "-i", "D:/Tugas/Portofolio/Real-ESRGAN_Improve_Resolution/images/low_resolution",
        "--outscale", "4",
        "--fp32",
        "--output", "D:/Tugas/Portofolio/Real-ESRGAN_Improve_Resolution/images/high_resolution"
        ]

    subprocess.run(command)

    st.markdown(
        """
        <h2 class="custom-text">
            Result:
        </h2>
            """, 
        unsafe_allow_html=True
    )

    file_name = uploaded_file.name
    # Menghilangkan ekstensi file dari nama asli dan menambahkan '_out.png'
    output_file_name = f'images/high_resolution/{file_name.rsplit(".", 1)[0]}_out.png'

    st.image(output_file_name, use_container_width=True)


try_model()

# python Real-ESRGAN/inference_realesrgan.py -n RealESRGAN_x4plus -i D:/Tugas/Portofolio/Real-ESRGAN_Improve_Resolution/images/low_resolution --outscale 4 --fp32 --output D:/Tugas/Portofolio/Real-ESRGAN_Improve_Resolution/images/high_resolution