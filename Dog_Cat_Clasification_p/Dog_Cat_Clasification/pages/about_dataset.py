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

def about_dataset():
    st.title(f"About Dataset")
    # st.header('Snowflake Healthcare App')

    # Teks dengan format HTML dan CSS untuk warna putih, ukuran 12, dan rata kanan kiri
    st.markdown(
        """
        <p class="custom-text">
            Dataset yang digunakan dalam penelitian ini berasal dari Kaggle yang bernama Animal Faces-HQ (AFHQ), 
            terdiri dari 16.130 gambar berkualitas tinggi. Ada tiga domain kelas, masing-masing menyediakan sekitar 5000 gambar. 
            Kelas-kelas tersebut adalah: Cat, Dog, Wildlife
        </p>
        """, 
        unsafe_allow_html=True
    )

    st.image('images/catdog_images.png', use_container_width=True)
    
    st.markdown(
        """
        <h4 class="custom-text">
            Proporsisi Data
        </h4>

        <p class="custom-text">
            Dataset ini terdiri dari total 16.130 gambar dengan proporsi kelas yang "seimbang", sehingga 
            memastikan analisis dan pelatihan model tidak bias terhadap salah satu kelas. Data dibagi menjadi 
            14.630 gambar untuk data training dan 1.500 gambar untuk data validasi. Pembagian ini dirancang untuk 
            memastikan model dapat dilatih secara optimal dan dievaluasi dengan akurat pada data yang tidak dilihat 
            selama pelatihan.
        </p>
        """, 
        unsafe_allow_html=True
    )

    col_data, col2_data, = st.columns([2, 3])
    
    with col_data:
        st.image('images/proporsisi_class.png', use_container_width=True)

    with col2_data:
        st.image('images/proporsisi_data.png', use_container_width=True)

about_dataset()