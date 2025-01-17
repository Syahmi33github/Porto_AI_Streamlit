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

def model():
    st.title(f"About Model and Result")

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

    st.image('images/vz1f8191.Ensemble-of-decision-trees.png', use_container_width=True)

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

    st.image('images/model_without_prep.png', use_container_width=True)

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
        st.image('images/imbalanced.jpg', use_container_width=True)

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
        st.image('images/vz1f8191.Ensemble-of-decision-trees.png', use_container_width=True)

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
    
    st.image('images/model_smote&drop_kolom.png', use_container_width=True)

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

model()