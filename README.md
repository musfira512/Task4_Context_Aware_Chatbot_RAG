# Task 4: Context-Aware Chatbot Using RAG (Retrieval-Augmented Generation)

## Project Overview

This project is developed as part of the DevelopersHub AI/ML Engineering Internship (Advanced Tasks). The objective is to build a context-aware chatbot capable of retrieving relevant information from a custom knowledge base (PDF documents) and answering user queries using a Retrieval-Augmented Generation (RAG) approach.

The system uses semantic search with embeddings and a vector database to retrieve contextually relevant information, and a Streamlit-based interface for interaction.

---

## Objective

- Build a chatbot that can process and understand custom documents (PDF files)
- Convert document text into embeddings for semantic search
- Store embeddings in a vector database for efficient retrieval
- Retrieve relevant context based on user queries
- Provide context-aware responses
- Deploy the chatbot using Streamlit

---

## Key Features

- PDF document ingestion and text extraction
- Text chunking for efficient retrieval
- Semantic embeddings using SentenceTransformers
- Vector similarity search using FAISS
- Context-based retrieval system
- Interactive web interface using Streamlit
- Lightweight and dependency-stable architecture

---

## Technologies Used

- Python
- Streamlit
- PyPDF
- SentenceTransformers (all-MiniLM-L6-v2)
- FAISS (Facebook AI Similarity Search)
- NumPy

---

## Project Structure

Task4_RAG_Chatbot/

├── app.py                  # Streamlit application

├── notebook.ipynb         # Development notebook (Colab)

├── sample.pdf             # Knowledge base document

├── index.faiss            # Precomputed vector index

├── chunks.pkl             # Serialized text chunks

├── requirements.txt       # Dependencies

└── README.md              # Project documentation

---

## How It Works

### 1. Document Loading
The system loads a PDF document and extracts raw text using PyPDF.

### 2. Text Chunking
The extracted text is split into smaller chunks to improve retrieval accuracy.

### 3. Embedding Generation
Each chunk is converted into a dense vector representation using SentenceTransformers.

### 4. Vector Storage
All embeddings are stored in a FAISS index for efficient similarity search.

### 5. Query Processing
User queries are converted into embeddings and compared with stored vectors.

### 6. Context Retrieval
The most relevant chunks are retrieved based on similarity scores.

### 7. Response Generation
The retrieved context is displayed as the chatbot response.

---


---

## Example Queries

- What is this document about?
- Summarize the document
- What are the key points?
- Explain the main topic
- Provide an overview of the content

---

## Results

- Efficient semantic retrieval using FAISS
- Fast and accurate document search
- Context-aware responses
- Lightweight and stable deployment
- Fully functional RAG-based chatbot system

---

## Future Improvements

- Integration with large language models (LLMs)
- Persistent chat memory
- Multi-document support
- Improved UI with chat interface design
- Cloud deployment (Hugging Face Spaces / Render)

---

## Skills Gained

- Retrieval-Augmented Generation (RAG)
- Vector databases and similarity search
- Sentence embeddings
- Document processing pipelines
- Streamlit application deployment
- End-to-end AI system design

---

## Author

Musfira Zainab

AI/ML Intern

DevelopersHub Corporation

---

## License

This project is intended for educational purposes only.

