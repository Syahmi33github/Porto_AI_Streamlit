import streamlit as st

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
    unsafe_allow_html=True
)

import streamlit as st
import os

from dotenv import load_dotenv # langfuse or opik
from langchain_ollama import ChatOllama

from langchain_core.prompts import (
                                        SystemMessagePromptTemplate,
                                        HumanMessagePromptTemplate,
                                        ChatPromptTemplate,
                                        MessagesPlaceholder
                                        )

from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_community.chat_message_histories import SQLChatMessageHistory

from langchain_core.output_parsers import StrOutputParser
from langchain_community.document_loaders import PyMuPDFLoader

load_dotenv('./../.env')

# Tampilkan teks dengan warna putih menggunakan kelas CSS
st.markdown('<div class="title">Chat with Your PDF</div>', unsafe_allow_html=True)
# st.markdown('<div class="content">Hello', unsafe_allow_html=True)

# ========================= Upload File =========================
SAVE_FOLDER = "file_pdf"
os.makedirs(SAVE_FOLDER, exist_ok=True)

uploaded_file = st.file_uploader("Choose a PDF file", type=["pdf"], accept_multiple_files=False)

if uploaded_file is not None:
    file_path = os.path.join(SAVE_FOLDER, uploaded_file.name)
    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    st.session_state["file_path"] = file_path  # Simpan ke session_state
    st.success(f"File saved to: {file_path}")

# ========================= Upload File =========================

# ========================= Read File =========================
if "file_path" in st.session_state:
    file_path = st.session_state["file_path"]
    # st.write("File path:", file_path)

    file_size = os.path.getsize(file_path)
    # st.write(f"File size: {file_size} bytes")

    # Load PDF
    loader = PyMuPDFLoader(file_path)
    docs = loader.load()

    st.write(f"Number of pages: {len(docs)}")

    def format_docs(docs):
        return "\n\n".join([x.page_content for x in docs])

    context = format_docs(docs)
    # st.write(f"Number of pages: {context}")
    # st.write(docs[0].page_content)

# ========================= Read File =========================

base_url = "http://localhost:11434"
model = 'llama3.2:3b'

# user_id = st.text_input("Enter your user id", "laxmikant")
user_id = "chat_pdf"

def get_session_history(session_id):
    return SQLChatMessageHistory(session_id, "sqlite:///chat_history.db")

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

if st.button("Start New Conversation"):
    st.session_state.chat_history = []
    history = get_session_history(user_id)
    history.clear()

for message in st.session_state.chat_history:
    with st.chat_message(message['role']):
        st.markdown(message['content'])


### LLM Setup
llm = ChatOllama(base_url=base_url, model=model)

system = SystemMessagePromptTemplate.from_template("""You are helpful AI assistant who answer user question based on the provided context. 
                                                    Do not answer in more than {words} words""")

human_prompt = """Answer user question based on the provided context ONLY! If you do not know the answer, just say "I don't know".
            ### Context:
            {context}

            ### Question:
            {input}

            ### Answer:"""

human = HumanMessagePromptTemplate.from_template(human_prompt)

messages = [system, MessagesPlaceholder(variable_name='history'), human]

prompt = ChatPromptTemplate(messages=messages)

chain = prompt | llm | StrOutputParser()


runnable_with_history = RunnableWithMessageHistory(chain, get_session_history, 
                                                   input_messages_key='input', 
                                                   history_messages_key='history')

def chat_with_llm(session_id, input):
    for output in runnable_with_history.stream({'context': context, 'input': input, 'words': 50}, config={'configurable': {'session_id': session_id}}):

        yield output

st.markdown("""
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
""", unsafe_allow_html=True)

prompt = st.chat_input("What is up?")
# st.write(prompt)

if prompt:
    # Update the height after user input
    st.markdown("""
        <style>
            .st-emotion-cache-1p2n2i4 {
                height: unset !important;
            }
        </style>
    """, unsafe_allow_html=True)

    st.session_state.chat_history.append({'role': 'user', 'content': prompt})

    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        response = st.write_stream(chat_with_llm(user_id, prompt))

    st.session_state.chat_history.append({'role': 'assistant', 'content': response})