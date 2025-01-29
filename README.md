# Porto_AI_Streamlit

Medium:
https://medium.com/@syahmisajid12

## 5. **Chatbot with Historical Memory Using Llama 3.2 and Streamlit**

This project implements a chatbot based on the **Llama 3.2** model equipped with **historical memory**, allowing the chatbot to remember and respond based on previous conversations. It is integrated with a **Streamlit** user interface, providing an interactive and user-friendly experience.

### Key Features

- **Llama 3.2 Model**: Utilizes the Llama 3.2 model to generate more relevant and intelligent responses.
- **Historical Memory**: The chatbot remembers past conversations, providing better context for each interaction.
- **Streamlit Interface**: A web-based interface using Streamlit for a more interactive and engaging user experience.
- **Langchain Integration**: Uses the Langchain framework to efficiently manage conversations and memory.

### Prerequisites

Make sure you have the following prerequisites before starting:

- Python 3.x
- `llama` version 3.2
- `langchain`
- `streamlit`
- Other required libraries (such as `torch`, `transformers`, etc.)

## 6. Chat with Your PDF - Streamlit Application

This is a Streamlit-based web application that allows users to upload a PDF document, chat with an AI assistant, and get answers based on the content of the PDF. The assistant utilizes the `ChatOllama` model and `langchain` components to process and respond to user queries.

### Features

- **Upload PDF**: Users can upload a PDF file that will be used as the context for answering questions.
- **Chat Interface**: A chat interface where users can ask questions based on the content of the uploaded PDF.
- **Contextual Responses**: The AI assistant answers based on the provided PDF content using a LLM model (Llama 3.2).
- **Chat History**: The app keeps track of the conversation history and allows for a new conversation.

### Requirements

Make sure to install the following dependencies:

- `streamlit`: For the app's frontend.
- `langchain_ollama`: For the integration with the Ollama language model.
- `langchain_core`: For the components that manage prompts and message history.
- `dotenv`: To load environment variables.
- `langchain_community`: For SQL message history and document loaders.
- `PyMuPDF`: To read and extract content from PDF files.

To install the required dependencies, you can use the following command:

```bash
pip install streamlit langchain_ollama langchain_core dotenv langchain_community PyMuPDF

```
