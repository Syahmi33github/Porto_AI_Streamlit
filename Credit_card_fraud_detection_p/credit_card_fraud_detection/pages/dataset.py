import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

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

def dataset():
    # Membaca data
    df = pd.read_csv("data_and_model/credit_card_fraud_1000.csv")
    
    st.title(f"Dataset & Problem About Dataset")

    st.markdown(
        """
        <p class="custom-text">
        Dataset yang digunakan berasal dari Kaggle dengan jumlah 9 kolom:
        </p>
        <ul class="custom-text">
            <li>distance_from_home : Jarak dari rumah ke lokasi transaksi dilakukan.</li>
            <li>distance_from_last_transaction : Jarak dari lokasi transaksi terakhir dilakukan.</li>
            <li>ratio_to_median_purchase_price : Rasio harga transaksi yang dibeli terhadap harga pembelian median.</li>
            <li>repeat_retailer : Apakah transaksi dilakukan dari pengecer yang sama.</li>
            <li>used_chip : Apakah transaksi dilakukan menggunakan chip (kartu kredit).</li>
            <li>used_pin_number : Apakah transaksi dilakukan dengan menggunakan nomor PIN.</li>
            <li>online_order : Apakah transaksi merupakan pesanan online.</li>
            <li>fraud : Apakah transaksi tersebut merupakan penipuan.</li>
        </ul>
        <p class="custom-text">
        Contoh 5 Data Pertama :
        </p>
        """, 
        unsafe_allow_html=True
    )

    st.write(df.head())

    st.markdown(
        """
        <h2 class="custom-text">
        Problem
        </h2>

        <p class="custom-text">
        Masalah utama dalam dataset deteksi penipuan kartu kredit adalah ketidakseimbangan kelas, 
        di mana transaksi sah jauh lebih banyak daripada transaksi fraud. Hal ini menyebabkan 
        model cenderung lebih fokus pada kelas mayoritas, sehingga kurang efektif dalam mendeteksi transaksi penipuan.
        </p>
        """, 
        unsafe_allow_html=True
    )

    # Menghitung frekuensi nilai unik
    category_counts = df['fraud'].value_counts()
    label_fraud = ["no fraud", "fraud"]
    
    spacer_data, col1_data, spacer2_data = st.columns([1, 2, 1])
    with col1_data:
        # Mengatur ukuran pie chart (misalnya, lebar 8, tinggi 8)
        fig, ax = plt.subplots(figsize=(8, 8))  # Mengubah ukuran plot sesuai kebutuhan

        # Membuat pie chart dan mengatur ukuran label
        ax.pie(
            x=category_counts, 
            labels=label_fraud, 
            explode=[0.0, 0.2], 
            autopct='%1.1f%%', 
            startangle=90,
            labeldistance=1.1,  # Mengatur jarak label
            textprops={'fontsize': 16, 'color': 'white'}  # Mengatur ukuran font label
        )
        # ax.set_title('Distribution of Categories', fontsize=16, color='white') 

        # Menghilangkan latar belakang putih
        fig.patch.set_alpha(0)
        ax.patch.set_alpha(0)

        # Menampilkan plot di Streamlit
        st.pyplot(fig)

    st.markdown(
        """
        <h2 class="custom-text">
        Solusi
        </h2>

        <p class="custom-text">
        Masalah ketidakseimbangan kelas pada dataset penipuan kartu kredit dapat diselesaikan menggunakan beberapa solusi, diantaranya:
        </p>
        """, 
        unsafe_allow_html=True
    )

    col1_solution, col2_solution, = st.columns([1, 1])

    with col1_solution:
        st.image('images/maxresdefault (6).jpg', use_container_width=True)
        st.markdown(
            """
            <ul class="custom-text">
                <li>Solusi pertama adalah menggunakan model seperti Random Forest atau Decision Tree. 
                Model ini dipilih karena kemampuannya dalam menangani data yang tidak seimbang dengan 
                memberikan bobot lebih tinggi pada kelas minoritas selama pelatihan. Selain itu, 
                algoritma ini secara inheren mampu menangani hubungan kompleks antara fitur dan 
                memberikan interpretasi yang lebih baik melalui fitur penting (feature importance), 
                sehingga mendukung identifikasi transaksi penipuan secara efektif.</li>
            </ul>
            """, 
            unsafe_allow_html=True
        )

    with col2_solution:
        st.image('images/imbalanced.jpg', use_container_width=True)
        st.markdown(
            """
            <ul class="custom-text">
                <li>Solusi kedua adalah dengan menerapkan teknik oversampling atau undersampling. 
                Oversampling, seperti menggunakan Synthetic Minority Oversampling Technique (SMOTE), 
                meningkatkan jumlah sampel pada kelas minoritas untuk memperbaiki proporsi data. 
                Sebaliknya, undersampling mengurangi jumlah sampel pada kelas mayoritas 
                agar seimbang dengan kelas minoritas. Kedua teknik ini membantu model belajar pola 
                dari kedua kelas secara lebih adil, sehingga meningkatkan akurasi dan 
                kemampuan deteksi penipuan tanpa bias terhadap kelas mayoritas.</li>
            </ul>
            """, 
            unsafe_allow_html=True
        )

dataset()