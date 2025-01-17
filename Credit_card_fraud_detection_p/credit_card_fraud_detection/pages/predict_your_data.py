import streamlit as st

import pandas as pd
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

def predict_your_data():
    st.title(f"Predict Your Data")

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

    loaded_model = load_model('data_and_model/Credit_card_smote')
    predictions = predict_model(loaded_model, data=data_df)

    result = predictions['prediction_label'].iloc[0]
    result_final = "Penipuan Terdeteksi" if result == 1 else "Bukan Penipuan"
    
    # Menampilkan Hasil Prediksi
    # st.write(result_final)

    if result_final == "Penipuan Terdeteksi":
        st.markdown(f'<div class="predict_result_red">{result_final}</div>', unsafe_allow_html=True)
        st.image('images/credit-card-fraud-top-5ce50f46733c4339ce64a61b.jpg', use_container_width=True)
    else:
        st.markdown(f'<div class="predict_result_green">{result_final}</div>', unsafe_allow_html=True)
        # Menampilkan gambar dengan latar belakang transparan
        st.image('images/secure-people-protection-human-privacy-person-safety-profile-security-safe-logo-design-vector.jpg', use_container_width=True)

predict_your_data()