import streamlit as st
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

    # Inisialisasi pipeline untuk sentiment analysis
    sentiment_analysis = pipeline(
        "sentiment-analysis", 
        model="cardiffnlp/twitter-roberta-base-sentiment"
    )

    # Masukkan string yang ingin dianalisis
    # Create an input text box
    user_input = st.text_input("Enter some text:")

    # Analisis sentimen pada string
    result = sentiment_analysis(user_input)

    sentiment = ""
    
    if result[0]['label'] == "LABEL_0":
        sentiment = "negative"
    elif result[0]['label'] == "LABEL_1":
        sentiment = "neutral"
    else:
        sentiment = "positive"

        # Teks dengan format HTML dan CSS untuk warna putih, ukuran 12, dan rata kanan kiri
    st.markdown(
        f"""
        <h4 class="custom-text">
            Text: {user_input}
        </h4>

        <h3 class="custom-text">
            Sentiment : {sentiment})
        </h3>
        """, 
        unsafe_allow_html=True
    )

# Menjalankan aplikasi prediksi
about_predict()