import streamlit as st

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

def about_case():
    st.title(f"About Model")
    # st.header('Snowflake Healthcare App')

    st.image('images/cnn.png', use_container_width=True)

    # Teks dengan format HTML dan CSS untuk warna putih, ukuran 12, dan rata kanan kiri
    st.markdown(
        """
        <p class="custom-text">
            Dalam penelitian ini, tiga model digunakan untuk mengevaluasi kinerja klasifikasi: 
            Base Model berbasis CNN, serta dua model pre-trained, yaitu ResNet dan EfficientNet. 
            Hasil evaluasi menunjukkan bahwa Base Model mencapai akurasi sebesar 0,9213, sedangkan 
            ResNet memberikan peningkatan akurasi signifikan hingga 0,998, dan EfficientNet mencatatkan 
            kinerja tertinggi dengan akurasi 0,9993. 
        </p>
        """, 
        unsafe_allow_html=True
    )

    col_model, col2_model, = st.columns([1, 1])
    
    with col_model:
        st.image('images/resnet.jpg', use_container_width=True)
    
    with col2_model:
        st.image('images/EfficientNet.jpg', use_container_width=True)

    st.markdown(
        """
        <p class="custom-text">
            Analisis ini mengindikasikan bahwa model pre-trained memiliki kemampuan generalisasi yang jauh lebih baik 
            dibandingkan Base Model, berkat arsitektur yang lebih kompleks dan bobot awal yang sudah terlatih pada dataset 
            besar. EfficientNet unggul karena efisiensi pemakaian parameter dan keunggulannya dalam menyeimbangkan skala 
            resolusi, kedalaman, dan lebar jaringan.
        </p>
        """, 
        unsafe_allow_html=True
    )

    spare_hasil, col_data, spare2_hasil, = st.columns([1, 3, 1])
    
    with col_data:
        st.image('images/hasil_akurasi_model.png', use_container_width=True)
about_case()