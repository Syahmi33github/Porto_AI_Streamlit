import streamlit as st
import os  # Import modul os untuk membaca environment variable

# Menambahkan CSS dengan beberapa opsi warna
st.markdown(
    """
    <style>
    /* Latar belakang aplikasi */
    .stApp {
        background-color: #1E1E2F; /* Latar belakang abu-abu gelap */
        color: white;
    }
    .stButton>button {
        color: white;
        background-color: #4CAF50;  /* Mengatur warna latar belakang tombol */
    }
    .title {
        color: white;
        font-size: 4em;
        text-align: center;
        display: flex;
        justify-content: center;
        align-items: center;
    }
    .content {
        color: white;
        font-size: 1em;
    }
    label {
        color: white !important;
    }
    input {
        color: white !important;
        background-color: black !important; /* Jika ingin kotak input hitam */
    }
    ::placeholder { /* Untuk placeholder teks */
        color: white !important;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

from dotenv import load_dotenv
from langchain_openai import ChatOpenAI  # Mengganti ChatOllama dengan ChatOpenAI

from langchain_core.prompts import (
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate,
    ChatPromptTemplate,
    MessagesPlaceholder,
)

from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_community.chat_message_histories import SQLChatMessageHistory

from langchain_core.output_parsers import StrOutputParser

# Memuat environment variable dari file .env
load_dotenv("./../.env")

# Tampilkan teks dengan warna putih menggunakan kelas CSS
st.markdown('<div class="title">What can I help with?</div>', unsafe_allow_html=True)

# user_id = st.text_input("Enter your user id", "laxmikant")
user_id = "laxmikant"


def get_session_history(session_id):
    return SQLChatMessageHistory(session_id, "sqlite:///chat_history.db")


if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

if st.button("Start New Conversation"):
    st.session_state.chat_history = []
    history = get_session_history(user_id)
    history.clear()

for message in st.session_state.chat_history:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

### LLM Setup
# Menggunakan API key dari environment variable
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    st.error(
        "OpenAI API key tidak ditemukan. Pastikan Anda telah menambahkan OPENAI_API_KEY di file .env."
    )
    st.stop()

llm = ChatOpenAI(model="gpt-4o-mini", api_key=api_key)  # Menggunakan API key

system = SystemMessagePromptTemplate.from_template("You are helpful assistant.")
human = HumanMessagePromptTemplate.from_template("{input}")

messages = [system, MessagesPlaceholder(variable_name="history"), human]

prompt = ChatPromptTemplate(messages=messages)

chain = prompt | llm | StrOutputParser()

runnable_with_history = RunnableWithMessageHistory(
    chain,
    get_session_history,
    input_messages_key="input",
    history_messages_key="history",
)


def chat_with_llm(session_id, input):
    for output in runnable_with_history.stream(
        {"input": input}, config={"configurable": {"session_id": session_id}}
    ):
        yield output


st.markdown(
    """
<style> 
    .st-emotion-cache-128upt6 {
        background-color: transparent !important;
    }
            
    .st-emotion-cache-1flajlm{
        color: white        
    }
            
    .st-emotion-cache-1p2n2i4 {
        height: 500px 
    }
            
    .st-emotion-cache-8p7l3w {
        text-align: right;
    }
</style>
""",
    unsafe_allow_html=True,
)

prompt = st.chat_input("What is up?")

if prompt:
    # Update the height after user input
    st.markdown(
        """
        <style>
            .st-emotion-cache-1p2n2i4 {
                height: unset !important;
            }
        </style>
    """,
        unsafe_allow_html=True,
    )

    st.session_state.chat_history.append({"role": "user", "content": prompt})

    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        response = st.write_stream(chat_with_llm(user_id, prompt))

    st.session_state.chat_history.append({"role": "assistant", "content": response})
