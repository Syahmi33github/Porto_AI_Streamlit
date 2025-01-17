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
    st.title(f"About Case")
    # st.header('Snowflake Healthcare App')

    # Teks dengan format HTML dan CSS untuk warna putih, ukuran 12, dan rata kanan kiri
    st.markdown(
        """
        <p class="custom-text">
            Proyek ini bertujuan untuk mengembangkan sebuah sistem klasifikasi muka hewan 
            menggunakan deep learning dan transfer learning. Sistem ini akan mampu membedakan 
            antara tiga jenis hewan yaitu kucing, anjing, dan binatang buas berdasarkan gambar 
            muka mereka. Dengan menggunakan teknik deep learning dan transfer learning, proyek 
            ini akan mencapai tingkat akurasi yang tinggi dalam mengenali dan mengklasifikasikan 
            hewan-hewan tersebut.
        </p>
        """, 
        unsafe_allow_html=True
    )

    st.image('images/Cat-and-Dog-Classification-80.jpg', use_container_width=True)
    
    st.markdown(
        """
        <p class="custom-text">
            Tujuan dari proyek ini adalah sebagai berikut:
        </p>

        <ul class="custom-text">
            <li>Membangun model klasifikasi yang mampu mengenali dan membedakan gambar muka kucing, anjing, dan binatang buas dengan tingkat akurasi tinggi.</li>
            <li>Menerapkan teknik deep learning dan transfer learning untuk memanfaatkan pengetahuan yang sudah ada dari model-model yang telah dilatih sebelumnya.</li>
            <li>Mengembangkan sebuah sistem yang dapat diintegrasikan ke dalam aplikasi atau platform lain untuk penggunaan praktis.</li>
        </ul>

        <p class="custom-text">
            Kumpulan data ini, juga dikenal sebagai Animal Faces-HQ (AFHQ), terdiri dari 16.130 gambar berkualitas tinggi dengan resolusi 512×512. 
            Ada tiga domain kelas, masing-masing menyediakan sekitar 5000 gambar. Dengan memiliki beberapa (tiga) domain dan beragam gambar dari 
            berbagai keturunan per setiap domain, AFHQ menetapkan masalah terjemahan gambar-ke-gambar yang menantang. Kelas-kelas tersebut adalah:
        </p>

        <ul class="custom-text">
           <li>Cat</li>
           <li>Dog</li>
           <li>Wildlife</li>
        </ul>
        """, 
        unsafe_allow_html=True
    )

about_case()