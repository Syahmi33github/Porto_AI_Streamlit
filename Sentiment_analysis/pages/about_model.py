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

    st.image('images/roberta_sentiment.jpg', use_container_width=True)

    # Teks dengan format HTML dan CSS untuk warna putih, ukuran 12, dan rata kanan kiri
    st.markdown(
        """
        <p class="custom-text">
            In this experiment, the model used is a variation of the BERT model specifically 
            designed for sentiment analysis. Using this model, sentiment predictions are 
            generated and compared with the original labels in the dataset. This comparison is 
            performed to measure the model's accuracy in predicting sentiment correctly.
        </p>
        """, 
        unsafe_allow_html=True
    )

    st.image('images/right_predict.png', use_container_width=True)

    st.markdown(
        """
        <h4 class="custom-text">
            Result
        </h4>

        <ul class="custom-text">
            <li>positive    875</li>
            <li>negative    740</li>
            <li>neutral     668 </li>
        </ul>

        <p class="custom-text">
            Resulting in a final dataset of 2,283 rows.
        </p>
        """, 
        unsafe_allow_html=True
    )

    spare_prop_data, col_prop_data, spare_prop_data2, = st.columns([1, 3, 1])
    
    with col_prop_data:
        st.image('images/Number of Predicted Results of Roberta Model.png', use_container_width=True)
    
    st.markdown(
        """
        <h4 class="custom-text">
            Accuracy (Comparison with Labels in The Dataset)
        </h4>

        <p class="custom-text">
            Because the labels in the dataset only use positive and negative, the neutral label will not be used. 
            Hasil perbandingan yang didapat, akurasi mencapai 82.9%
        </p>
        """, 
        unsafe_allow_html=True
    )

    spare_akurasi, col_akurasi, spare_akurasi2, = st.columns([1, 3, 1])
    
    with col_akurasi:
        st.image('images/akurasi.png', use_container_width=True)

    st.markdown(
        """
        <h4 class="custom-text">
            Wrong Predict
        </h4>
        """, 
        unsafe_allow_html=True
    )

    st.image('images/wrong_predict.png', use_container_width=True)

    st.markdown(
        """
        <p class="custom-text">
            The incorrect prediction is actually debatable because the original sentiment is completely accurate, such as:
        </p>

        <ul class="custom-text">
            <li>"Lampin' in the Hamptons...... Wishing I was with her !!!!!!!" should be positive</li>
            <li>"Do. We. Really. Need. Another. Social. Network. FIGHT BACK! Say NO to Tagged.com!" should be negative</li>
            <li>"Yeahh but im being slow to reply atm joshypearson" should be negative </li>
        </ul>
        """, 
        unsafe_allow_html=True
    )

about_case()