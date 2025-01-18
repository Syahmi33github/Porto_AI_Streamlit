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

    st.image('images/9f5946d6-d060-4aaa-b1c3-e64795227a1c.jpg', use_container_width=True)

    # Teks dengan format HTML dan CSS untuk warna putih, ukuran 12, dan rata kanan kiri
    st.markdown(
        """
        <p class="custom-text">
            This project aims to evaluate the performance of a BERT model variation 
            specifically designed for sentiment analysis, namely bert-base-uncased-sentiment, 
            in predicting sentiment on social media text, particularly Twitter. The model 
            classifies sentiment into three categories: positive, negative, and neutral. In 
            this experiment, the model's predicted results will be compared to the manually 
            labeled true ground truth to measure the model's accuracy in predicting sentiment correctly.
        </p>

        <p class="custom-text">
            Performance evaluation is conducted using the accuracy metric, which measures the proportion 
            of correct predictions compared to the total predictions. By comparing the predicted results 
            with the true ground truth, the study aims to provide a clear picture of the model's ability to 
            accurately predict sentiment, as well as identify potential improvements or further developments 
            needed to enhance the model's performance.
        </p>
        """, 
        unsafe_allow_html=True
    )

about_case()