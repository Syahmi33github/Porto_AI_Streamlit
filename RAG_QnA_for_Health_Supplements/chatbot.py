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
        font-size: 3em;
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

import os
import warnings
from dotenv import load_dotenv

os.environ['KMP_DUPLICATE_LIB_OK'] = 'True'
warnings.filterwarnings("ignore")

load_dotenv()

from langchain_ollama import OllamaEmbeddings

import faiss
from langchain_community.vectorstores import FAISS 
from langchain_community.docstore.in_memory import InMemoryDocstore
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_community.chat_message_histories import SQLChatMessageHistory

from langchain_ollama import ChatOllama 
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough 
from langchain_core.prompts import ChatPromptTemplate

from langchain import hub

# load_dotenv('./../.env')

# Tampilkan teks dengan warna putih menggunakan kelas CSS
st.markdown('<div class="title">Chatbot - Health Supplements</div>', unsafe_allow_html=True)
# st.markdown('<div class="content">Hello', unsafe_allow_html=True)

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
embeddings = OllamaEmbeddings(model='nomic-embed-text', base_url='http://localhost:11434')

db_name = "health_supplements"
db_path = fr"D:\Tugas\Portofolio\RAG_QnA_for_Health_Supplements\{db_name}"

vector_store = FAISS.load_local(db_path, embeddings, allow_dangerous_deserialization=True)

retriever = vector_store.as_retriever(search_type = 'similarity', 
                                      search_kwargs = {'k': 3})
                                      
llm = ChatOllama(model='llama3.2:3b', base_url='http://localhost:11434')
def format_docs(docs):
    return '\n\n'.join([doc.page_content for doc in docs])

# print(context)
prompt = """
    You are an assistant for question-answering tasks. Use the following pieces of retrieved context to answer the question.
    If you don't know the answer, just say that you don't know.
    Answer in bullet points. Make sure your answer is relevant to the question and it is answered from the context only.
    Question: {question} 
    Context: {context} 
    Answer:
"""

prompt = ChatPromptTemplate.from_template(prompt)

rag_chain = (
    {"context": retriever|format_docs, "question": RunnablePassthrough()}
    | prompt
    | llm
    | StrOutputParser()
)

def chat_with_llm(session_id, input):
    for output in rag_chain.stream(input, config={'configurable': {'session_id': session_id}}):

        yield output

def add_newline_after_bullet(text):
    return text.replace("•", "\n• ")


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

    # with st.chat_message("assistant"):
    #     response = st.write_stream(chat_with_llm(user_id, prompt))
    #     response = add_space_after_bullet(response)
    #     print(response)
    with st.chat_message("assistant"):
        response_container = st.empty()  # Buat placeholder untuk update teks secara real-time
        response_list = []  # Menyimpan teks yang diterima bertahap
        
        for chunk in chat_with_llm(user_id, prompt):  
            response_list.append(chunk)  # Simpan setiap bagian teks
            full_response = "".join(response_list)  # Gabungkan hasil sementara
            formatted_response = add_newline_after_bullet(full_response)  # Format teks

            response_container.markdown(formatted_response)  # Update tampilan secara streaming

    st.session_state.chat_history.append({'role': 'assistant', 'content': formatted_response})