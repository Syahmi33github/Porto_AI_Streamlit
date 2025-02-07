# Porto_AI_Streamlit

Medium:
https://medium.com/@syahmisajid12

## 1. Credit Card Fraud Detection

### Introduction

This article discusses how to detect credit card fraud using machine learning, focusing on imbalanced datasets where legitimate transactions far outnumber fraudulent ones.

### Dataset & Problem

The dataset from Kaggle includes features such as transaction distance, retailer information, and whether the transaction was online or used a chip/PIN. The main issue is class imbalance, with fraudulent transactions being much less frequent than legitimate ones.

### Solution

To address the class imbalance:

- **Random Forest/Decision Tree**: Assign higher weights to the minority class.
- **Oversampling/Undersampling**: SMOTE increases the minority class size, while undersampling reduces the majority class size.

### Models Used

- Random Forest
- Decision Tree
- Logistic Regression
- KNN
- SVM

### Results

#### Without Pre-processing

- **Random Forest** showed the best performance.
- **Other models** (Logistic Regression, KNN, SVM) underperformed due to difficulties in learning fraud patterns.

#### With Oversampling (SMOTE)

- **Random Forest**: F1-score of 0.9952.
- **Decision Tree**: F1-score of 0.9670.
- **Logistic Regression**: F1-score of 0.7524.
- **KNN**: F1-score of 0.6618.
- **SVM**: F1-score of 0.6010.

### Conclusion

Random Forest is the most effective model for detecting fraud, particularly when combined with oversampling techniques like SMOTE.

### Requirements

- Python 3.x
- Libraries: Pandas, NumPy, Scikit-learn, SMOTE (imbalanced-learn)

## 2. Animal Face Classification Using Deep Learning & Transfer Learning

### Introduction

This project develops an animal face classification system using deep learning and transfer learning. The model classifies images of **cats, dogs, and wild animals** with high accuracy, leveraging pre-trained models to improve performance.

### Dataset

- **Source**: Animal Faces-HQ (AFHQ) from Kaggle.
- **Size**: 16,130 high-resolution images (512×512).
- **Class Distribution**:
  - **Cat** (~5,000 images)
  - **Dog** (~5,000 images)
  - **Wildlife** (~5,000 images)
- **Split**: 14,630 images for training, 1,500 for validation.

### Models & Performance

Three models were tested:

1. **Base CNN Model**: Accuracy **0.9213**
2. **ResNet**: Accuracy **0.9980**
3. **EfficientNet**: Accuracy **0.9993** (Best performance)

Pre-trained models like **EfficientNet** outperform the Base Model due to better generalization, optimized parameter efficiency, and balanced network architecture.

### Conclusion

EfficientNet achieves the highest accuracy, demonstrating the power of **transfer learning** in animal face classification.

### Requirements

- Python 3.x
- TensorFlow / Keras
- OpenCV
- NumPy & Pandas

## 3. Sentiment Analysis on Twitter Using BERT-Base-Uncased-Sentiment

### Introduction

This project evaluates the **bert-base-uncased-sentiment** model for **Twitter sentiment analysis**, classifying tweets as **positive, negative, or neutral**. The model's performance is assessed using **accuracy** by comparing predictions to true labels.

### Dataset

- **Source**: Sentiment140 (Kaggle)
- **Size**: 2,500 tweets (filtered from 1.6M)
- **Label Distribution**:
  - **Positive**: 1,287 (51.2%)
  - **Negative**: 1,213 (48.8%)
- **Preprocessing**:
  - Renamed labels (0 → negative, 4 → positive)
  - Removed tags & links
  - Filtered non-English tweets
  - Final dataset: **2,283 tweets**

### Model & Performance

- Model: **bert-base-uncased-sentiment**
- Results:
  - **Positive**: 875
  - **Negative**: 740
  - **Neutral**: 668
- Accuracy (positive/negative only): **82.9%**
- Some predictions were debatable due to context ambiguity.

### Conclusion

The model performs well but struggles with nuanced sentiment. Future improvements could refine handling of **neutral cases** and **ambiguous expressions**.

### Requirements

- Python 3.x
- Transformers (Hugging Face)
- Pandas & NumPy

## 4. Enhancing Image Resolution with Real-ESRGAN

### Introduction

Real-ESRGAN (Real-Enhanced Super-Resolution GAN) is a deep learning model designed to **enhance image resolution** while preserving details. It is widely used for **photo restoration, video enhancement, and noise reduction** in real-world images.

### What is Real-ESRGAN?

Real-ESRGAN extends **ESRGAN**, a **GAN-based** model for **image super-resolution**. Unlike traditional methods, it effectively processes **compressed or noisy images**, making it ideal for real-world applications.

#### Key Features:

- **Noise Handling**: Enhances low-quality images while maintaining details.
- **Real-World Applications**: Useful for restoring **old photos**, enhancing **video quality**, and improving **compressed images**.
- **Scalability**: Supports up to **4× image enlargement**.

### Case Study: Restoring Old Photos

#### Example:

- **Input**: A low-resolution, aged photo.
- **Output**: A high-resolution, sharp image with improved details.

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

## 7. Web Scraping and Question Answering with LangChain

This project demonstrates how to scrape web content and use a Language Model (LLM) to answer questions based on the scraped text. The application utilizes `langchain`, `dotenv`, and `llama3.2:3b` to process and summarize the content.

### Requirements

To run the project, you need the following Python libraries. You can install them using the provided `requirements.txt`.

- `dotenv`
- `langchain_community`
- `langchain_ollama`
- `langchain_core`

### Setup

1. Clone this repository or download the project files.

2. Create a `.env` file to configure the environment variables if necessary.

3. Install the required libraries:

   ```bash
   pip install -r requirements.txt
   ```

## 8. RAG Chatbot for Health Supplements Q&A

### Description

This project aims to build a **Retrieval-Augmented Generation (RAG)** chatbot that can answer user questions about health supplements. The chatbot uses PDF documents as the main source of information, which are then converted into a vector database for faster and more accurate information retrieval.

### Features

- Retrieve information about health supplements based on PDF documents.
- Uses **FAISS** for vector storage and search.
- Integrates **Ollama** for embeddings and **Streamlit** for the user interface.
- The chatbot provides relevant and accurate answers based on context retrieved from documents.

### Requirements

Before running this project, ensure you have the following dependencies installed:

- Python
- PyMuPDF
- langchain
- faiss-cpu
- python-dotenv
- streamlit

You can install these dependencies using `pip`:

```bash
pip install PyMuPDF langchain faiss-cpu streamlit
```

## 9. LLM-SQL Integration with LangChain

This project demonstrates the integration of Large Language Models (LLMs) with SQL databases using the LangChain framework. It utilizes _Ollama's LLaMA_ model to query a MySQL database by converting natural language questions into SQL queries.

### Prerequisites

Before you start, make sure to have the following installed and configured:

- **Python** (3.7 or higher)
- **MySQL Database**: Ensure you have a MySQL server running and accessible.
- **LangChain**: Python library for building language model applications.
- **Ollama**: LLaMA model for natural language processing.

## 10. Fine-Tuning BERT for Multi-Class Emotion Recognition

### Introduction

This project fine-tunes the BERT-base-uncased model for multi-class emotion recognition on tweets. The goal is to classify emotions into multiple categories and evaluate model performance using accuracy and F1-score.

### Model & Performance

**Model:** BERT-base-uncased

### Results:

- **Accuracy:** 92%
- **F1-score (weighted avg):** 92%
- The model struggles slightly with ambiguous emotions like surprise and fear.

### How to Download the Model

To download the fine-tuned BERT model, use the following script:

```python
import gdown

file_id = "1C8xKvnVr5qQWGth73s-yymmC0m_Lrpvl"  # ID file dari link Drive
output = "bert-model.zip"  # Nama file output

gdown.download(f"https://drive.google.com/uc?id={file_id}", output, quiet=False)
```

### Conclusion

Fine-tuning BERT for emotion recognition yields high accuracy but faces challenges with overlapping emotions. Future improvements could explore context-aware models to handle subtle emotional differences better. 🚀

## 11. Fine-Tuning DistilBERT vs. BERT for Fake News Detection

### Introduction

This project compares the performance of BERT and DistilBERT for the task of fake news detection using a real-world dataset. The goal is to evaluate both models in terms of accuracy, F1-score, training time, and testing time, highlighting the trade-offs between computational efficiency and performance.

### Data Overview

The dataset consists of fake and real news articles, with columns including title, author, text, and label (0 for real news, 1 for fake news). The dataset has 18,281 samples, split as follows:

- **Training Set:** 12,796 samples
- **Testing Set:** 3,656 samples
- **Validation Set:** 1,829 samples

### Model & Performance

**Models:**

- BERT (bert-base-uncased)
- DistilBERT (distilbert-base-uncased)

**Evaluation Metrics:**

- **Accuracy**
- **F1-score** (weighted average)
- **Training Time**
- **Testing Time**

### Results:

- **BERT (bert-base-uncased):**

  - **Test Accuracy:** 96.44%
  - **Test F1 Score:** 96.44%
  - **Testing Runtime:** 16.97 seconds
  - **Training Time:** 895.35 seconds

- **DistilBERT (distilbert-base-uncased):**
  - **Test Accuracy:** 96.47%
  - **Test F1 Score:** 96.47%
  - **Testing Runtime:** 9.14 seconds
  - **Training Time:** 494.78 seconds

DistilBERT performs slightly better in terms of testing time and training time, while both models exhibit similar performance in accuracy and F1-score.

### How to Download the Model

To download the fine-tuned DistilBERT model, use the following script:

```python
import gdown

file_id = "1BwvAVbsDzMsU-UMRh1gKBYST-wd6wRyE"  # ID file dari link Drive
output = "distilbert-model.zip"  # Nama file output

gdown.download(f"https://drive.google.com/uc?id={file_id}", output, quiet=False)
```

## 12. Fine-Tuning DistilBERT for Named Entity Recognition (NER) in Restaurant Search

### Introduction

This project fine-tunes DistilBERT for Named Entity Recognition (NER) in restaurant search, enhancing entity extraction from user queries to improve search accuracy.

### Data Overview

The dataset is in BIO format, containing labeled tokens for training and testing:

- **Training Set:** 83.2%
- **Testing Set:** 16.8%

### Model & Performance

**Model Used:**

- DistilBERT (distilbert-base-uncased)

**Evaluation Metrics:**

- **Accuracy**

### Results

- **Epoch 1:** 91.07%
- **Epoch 2:** 91.57%
- **Epoch 3:** 91.89%

The model shows consistent performance improvements across epochs.

### How to Use the Model

To test the fine-tuned model, use the following script:

```python
import gdown

file_id = "18czl4uSDAxGxguS1rTM9JQ39UTtO8pPx"  # ID file dari link Drive
output = "distilbert-model.zip"  # Nama file output

gdown.download(f"https://drive.google.com/uc?id={file_id}", output, quiet=False)

```
