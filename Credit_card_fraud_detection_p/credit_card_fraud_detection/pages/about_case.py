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

    st.image('images/credit-card-activity.jpg', use_container_width=True)

    # Teks dengan format HTML dan CSS untuk warna putih, ukuran 12, dan rata kanan kiri
    st.markdown(
        """
        <p class="custom-text">
            Dengan pesatnya perkembangan pembayaran digital, kemajuan ini juga diikuti 
            oleh peningkatan Penipuan dan Aktivitas para pelaku kejahatan siber. Angka kejahatan 
            siber sangat mengkhawatirkan dan mengindikasikan bahwa penipuan masih menjadi masalah besar, 
            baik pada transaksi Card-Present maupun Card-Not-Present.
            Di tengah dunia digital yang semakin kompleks, di mana triliunan transaksi kartu 
            terjadi setiap hari, mendeteksi penipuan menjadi tantangan yang sangat besar. 
            Data yang digunakan dalam penelitian ini berasal dari sebuah institusi yang tidak 
            disebutkan namanya.
        </p>
        """, 
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <p class="custom-text">
            Di tengah dunia digital yang semakin kompleks, di mana triliunan transaksi kartu 
            terjadi setiap hari, mendeteksi penipuan menjadi tantangan yang sangat besar. 
            Data yang digunakan dalam penelitian ini berasal dari sebuah institusi yang tidak 
            disebutkan namanya.
        </p>
        """, 
        unsafe_allow_html=True
    )

about_case()