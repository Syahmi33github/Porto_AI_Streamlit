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

    st.image('images/data_ori.png', use_container_width=True)

    # Teks dengan format HTML dan CSS untuk warna putih, ukuran 12, dan rata kanan kiri
    st.markdown(
        """
        <p class="custom-text">
            The dataset used in this experiment originates from Kaggle, named Sentiment140, 
            developed by Akazanova. The original dataset consists of 1.6 million rows with positive 
            and negative labels. In this experiment, a sample of 2,500 data points was used, 
            with a proportion of positive labels totaling 1,287 (51.2%) and negative labels 
            totaling 1,213 (48.8%).
        </p>
        """, 
        unsafe_allow_html=True
    )

    spare_data, col_data, spare_data2, = st.columns([1, 3, 1])
    
    with col_data:
        st.image('images/proporsisi_data.png', use_container_width=True)

    st.markdown(
        """
        <h4 class="custom-text">
            Preprocessing data
        </h4>
        
        <p class="custom-text">
            Several preprocessing steps were carried out,
        </p>

        <ul class="custom-text">
            <li>including renaming the labels from 0 to negative and 4 to positive.</li>
            <li>The data was cleaned by removing tag characters and text containing "https".</li>
            <li>Filtering was performed to include only English-language data using the "langdetect" library. </li>
        </ul>

        <p class="custom-text">
            Resulting in a final dataset of 2,283 rows.
        </p>
        """, 
        unsafe_allow_html=True
    )

    st.image('images/data_cleaning.png', use_container_width=True)

about_dataset()