import subprocess

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
    st.title(f"Enhancing Image Resolution with Real-ESRGAN: A Deep Learning Approach for High-Quality Visual Restoration")
    # st.header('Snowflake Healthcare App')

    st.markdown(
        """
        <p class="custom-text">
            High-quality images play a crucial role in various fields, from photography and graphic design to video processing. 
            However, not all images we have are of sufficient resolution. One of the best solutions to this problem is Real-ESRGAN 
            (Real-Enhanced Super-Resolution Generative Adversarial Network), an advanced deep learning model designed to enhance the 
            resolution of real-world images. This article will discuss what Real-ESRGAN is, how to use it, and an example of its implementation.
        </p>
            """, 
        unsafe_allow_html=True
    )

    st.image('images/image/maxresdefault.jpg', use_container_width=True)

    st.markdown(
        """
        <p class="custom-text">
            High-quality images play a crucial role in various fields, from photography and graphic design to video processing. 
            However, not all images we have are of sufficient resolution. One of the best solutions to this problem is Real-ESRGAN 
            (Real-Enhanced Super-Resolution Generative Adversarial Network), an advanced deep learning model designed to enhance the 
            resolution of real-world images. This article will discuss what Real-ESRGAN is, how to use it, and an example of its implementation.
        </p>

        <h2 class="custom-text">
            What is Real-ESRGAN?
        </h2>

        <p class="custom-text">
            Real-ESRGAN is an extension of ESRGAN, a generative model based on GAN (Generative Adversarial Networks) for image super-resolution. 
            Real-ESRGAN is specifically designed to handle real-world images that often contain noise or artifacts due to compression. By using 
            a broad and diverse dataset, Real-ESRGAN can generate high-resolution images with realistic details.
        </p>

        <h4 class="custom-text">
            Key Features of Real-ESRGAN:
        </h4>

        <ul class="custom-text">
            <li><b>Noise Handling Capability:</b> This model can process low-quality images without distorting image details.</li>
            <li><b>Suitable for Real-World Applications:</b> From restoring old photos to enhancing video quality.</li>
            <li><b>Scalability:</b> Supports image enlargement up to 4x or more.</li>
        </ul>

        <h2 class="custom-text">
            Case Study: Restoring Old Photos
        </h2>

        <p class="custom-text">
            For example, you might have an old photo with low quality due to age or digital compression. With Real-ESRGAN, 
            you can restore the photo to get sharper details. The steps are the same as described above. 
            The results will look like this:
        </p>

        <ul class="custom-text">
            <li><b>Input:</b> An old photo with low resolution.</li>
            <li><b>Output:</b> A high-resolution photo with improved details.</li>
        </ul>

        <h2 class="custom-text">
            Result
        </h2>
        """, 
        unsafe_allow_html=True
    )

    st.image('images/image/Screenshot 2025-01-23 020850.png', use_container_width=True)
    st.image('images/image/Screenshot 2025-01-23 020914.png', use_container_width=True)
    st.image('images/image/Screenshot 2025-01-23 020923.png', use_container_width=True)

about_case()

# python Real-ESRGAN/inference_realesrgan.py -n RealESRGAN_x4plus -i D:/Tugas/Portofolio/Real-ESRGAN_Improve_Resolution/images/low_resolution --outscale 4 --fp32 --output D:/Tugas/Portofolio/Real-ESRGAN_Improve_Resolution/images/high_resolution