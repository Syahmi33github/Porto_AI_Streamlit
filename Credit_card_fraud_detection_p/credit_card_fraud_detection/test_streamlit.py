import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

from pycaret.classification import *

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

with st.sidebar:
    selected = st.selectbox(
        "Menu",
        options=["About Case", "Dataset", "Model", "Predict Your Data"],
    )

# Membaca data
df = pd.read_csv("credit_card_fraud_1000.csv")

if selected == "About Case":
    st.title(f"{selected}")
    # st.header('Snowflake Healthcare App')

    st.image('credit-card-activity.jpg', use_container_width=True)

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

elif selected == "Dataset":
    st.title(f"{selected}")

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
        st.image('maxresdefault (6).jpg', use_container_width=True)
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
        st.image('imbalanced.jpg', use_container_width=True)
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

elif selected == "Model":
    st.title(f"{selected}")

    st.markdown(
        """
        <p class="custom-text">
        Pada eksperimen ini, model yang digunakan meliputi 
        </p>
        <ul class="custom-text">
            <li>Random Forest</li>
            <li>Decision Tree</li>
            <li>Logistic Regression</li>
            <li>K-Nearest Neighbors (KNN)</li>
            <li>Support Vector Machine (SVM)</li>
        </ul>
        <p class="custom-text">
        Dalam tugas dengan dataset yang tidak seimbang, metrik F1-score sangat cocok digunakan 
        karena mempertimbangkan keseimbangan antara precision dan recall. Hal ini penting untuk 
        memastikan model tidak hanya akurat dalam memprediksi kelas mayoritas, tetapi juga mampu 
        mendeteksi kelas minoritas (transaksi penipuan) secara andal.
        </p>

        <h3 class="custom-text">
        Eksperimen 1 (Tanpa Pre-processing)
        </h3>
        """, 
        unsafe_allow_html=True
    )

    st.image('vz1f8191.Ensemble-of-decision-trees.png', use_container_width=True)

    st.markdown(
        """
        <p class="custom-text">
        Tanpa Teknik Oversampling, Random Forest mendapat hasil terbaik dalam eksperimen ini, 
        dengan F1-score tertinggi karena pendekatannya yang robust terhadap ketidakseimbangan data. 
        Sebaliknya, Logistic Regression, KNN, dan SVM menunjukkan performa yang lebih rendah karena 
        keterbatasan mereka dalam mempelajari pola kompleks pada data fraud. Hal ini menegaskan 
        pentingnya memilih model yang dapat menangani distribusi data yang tidak seimbang secara efektif.
        </p>
        """, 
        unsafe_allow_html=True
    )

    st.image('model_without_prep.png', use_container_width=True)

    st.markdown(
        """
        <p class="custom-text">
        Tapi apakah Hasilnya Masih dapat Ditingkatkan dengan Teknik Oversampling?
        </p>
        """, 
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <h3 class="custom-text">
        Eksperimen 2 (+ Teknik Oversampling Smote)
        </h3>
        """, 
        unsafe_allow_html=True
    )

    col1_result, spare_result, col2_result, = st.columns([10, 1, 10])
    
    with col1_result:
        st.image('imbalanced.jpg', use_container_width=True)

    with spare_result:
        st.markdown(
            """
            <p class="custom-text">
            +
            </p>
            """, 
            unsafe_allow_html=True
        )
    with col2_result:
        st.image('vz1f8191.Ensemble-of-decision-trees.png', use_container_width=True)

    st.markdown(
        """
        <p class="custom-text">
        Penerapan SMOTE secara signifikan meningkatkan performa model deteksi penipuan, 
        terutama pada F1-score, yang mencerminkan keseimbangan precision dan recall. 
        Random Forest mencapai F1-score 0.9949, menunjukkan hasil hampir sempurna, 
        sementara Decision Tree meningkat menjadi 0.9642. 
        Model seperti Logistic Regression dan KNN juga mengalami peningkatan, 
        masing-masing menjadi 0.7450 dan 0.6508, berkat distribusi data yang lebih seimbang. 
        Meskipun SVM masih memiliki F1-score terendah 0.5850, 
        peningkatannya menunjukkan efektivitas SMOTE dalam membantu model menangkap pola pada kelas fraud yang sebelumnya terabaikan.
        </p>
        """, 
        unsafe_allow_html=True
    )
    
    st.image('model_smote&drop_kolom.png', use_container_width=True)

    st.markdown(
        """
        <p class="custom-text">
        Kesimpulannya, Random Forest dan Decision Tree sangat cocok untuk kasus data tidak seimbang 
        seperti deteksi penipuan, karena keduanya mampu menangani distribusi data yang tidak merata 
        secara efektif. Tanpa oversampling, Random Forest menunjukkan performa terbaik. Dengan 
        penerapan SMOTE, performa kedua model meningkat signifikan, dengan Random Forest mencapai 
        F1-score hampir sempurna (0.9949) dan Decision Tree meningkat menjadi 0.9642, menjadikannya 
        pilihan andal untuk mendeteksi pola pada kelas minoritas.
        </p>
        """, 
        unsafe_allow_html=True
    )


elif selected == "Predict Your Data":
    st.title(f"{selected}")

    # Membuat kolom
    col1, spacer, col2, spacer2, col3 = st.columns([2, 1, 2, 1, 2])
    with col1:
        st.markdown('<div class="custom-label">Jarak Transaksi dari Rumah:</div>', unsafe_allow_html=True)  # Label kustom
        st.markdown('')
        distance_from_home = st.number_input("Enter a number", min_value=0, max_value=100, key="distance_from_home", label_visibility="collapsed")
        st.write(f"You entered: {distance_from_home}")
    with col2:
        st.markdown('<div class="custom-label">Jarak dari Transaksi Terakhir:</div>', unsafe_allow_html=True)  # Label kustom
        st.markdown('')
        distance_from_last_transaction = st.number_input("Enter a number", min_value=0, max_value=100, key="distance_from_last_transaction", label_visibility="collapsed")
        st.write(f"You entered: {distance_from_last_transaction}")
    with col3:
        st.markdown('<div class="custom-label">Perbandingan Jumlah Transfer dengan Nilai Tengah Transaksi:</div>', unsafe_allow_html=True)  # Label kustom
        ratio_to_median_purchase_price = st.number_input("Enter a number", min_value=0, max_value=100, key="ratio_to_median_purchase_price", label_visibility="collapsed")
        st.write(f"You entered: {ratio_to_median_purchase_price}")

    # Membuat kolom kedua
    col4, spacer3, col5, spacer4, col6 = st.columns([2, 1, 2, 1, 2])
    with col4:
        st.markdown('<div class="custom-label">Transaksi Menggunakan Chip (kartu kredit)</div>', unsafe_allow_html=True)  # Label kustom
        used_chip = st.selectbox("Pilih opsi:", ["Ya", "Tidak"], key="used_chip", label_visibility="collapsed")
        used_chip_int = 1 if used_chip == "Ya" else 0
        st.write(f"You entered: {used_chip}")
    with col5:
        st.markdown('<div class="custom-label">Transaksi Menggunakan Nomor PIN', unsafe_allow_html=True)  # Label kustom
        used_pin_number = st.selectbox("Pilih opsi:", ["Ya", "Tidak"], key="used_pin_number", label_visibility="collapsed")
        used_pin_number_int = 1 if used_pin_number == "Ya" else 0
        st.write(f"You entered: {used_pin_number}")
    with col6:
        st.markdown('<div class="custom-label">Transaksi Merupakan Pesanan Online.</div>', unsafe_allow_html=True)  # Label kustom
        online_order = st.selectbox("Pilih opsi:", ["Ya", "Tidak"], key="online_order", label_visibility="collapsed")
        online_order_int = 1 if online_order == "Ya" else 0
        st.write(f"You entered: {online_order}")

    data = []
    data.append(distance_from_home)
    data.append(distance_from_last_transaction)
    data.append(ratio_to_median_purchase_price)
    data.append(used_chip_int)
    data.append(used_pin_number_int)
    data.append(online_order_int)

    data_df = pd.DataFrame([data], columns=['distance_from_home', 'distance_from_last_transaction', 'ratio_to_median_purchase_price', 'used_chip', 'used_pin_number', 'online_order'])

    loaded_model = load_model('Credit_card_smote')
    predictions = predict_model(loaded_model, data=data_df)

    result = predictions['prediction_label'].iloc[0]
    result_final = "Penipuan Terdeteksi" if result == 1 else "Bukan Penipuan"
    
    # Menampilkan Hasil Prediksi
    # st.write(result_final)

    if result_final == "Penipuan Terdeteksi":
        st.markdown(f'<div class="predict_result_red">{result_final}</div>', unsafe_allow_html=True)
        st.image('credit-card-fraud-top-5ce50f46733c4339ce64a61b.jpg', use_container_width=True)
    else:
        st.markdown(f'<div class="predict_result_green">{result_final}</div>', unsafe_allow_html=True)
        # Menampilkan gambar dengan latar belakang transparan
        st.image('secure-people-protection-human-privacy-person-safety-profile-security-safe-logo-design-vector.jpg', use_container_width=True)