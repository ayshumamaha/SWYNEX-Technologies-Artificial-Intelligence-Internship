# TASK 2 AI-Based FAQ Question Answering System Using Sentence Transformers

## 1. Project Overview

This project is a Python-based FAQ chatbot developed as part of the Artificial Intelligence Internship at SWYNEX Technologies. It uses the pretrained `all-MiniLM-L6-v2` Sentence Transformer model to understand user questions and retrieve relevant answers using semantic similarity.

The application runs without requiring a Gemini API key or paid AI API.

## 2. Objectives

- Integrate a pretrained AI language model.
- Generate semantic embeddings for FAQ questions.
- Identify relevant answers using cosine similarity.
- Support differently worded questions.
- Handle unsupported queries through a similarity threshold.

## 3. Technologies Used

- Python
- Sentence Transformers
- all-MiniLM-L6-v2
- PyTorch
- Cosine Similarity
- Google Colab

## 4. Features

- Pretrained Sentence Transformer model.
- Semantic question matching.
- FAQ-based answer retrieval.
- Similarity score display.
- Fallback response for unsupported questions.
- No external paid API key required.

## 5. Installation

Install the required libraries:

```bash
pip install sentence-transformers torch
```

## 6. How to Run

1. Open Google Colab.
2. Create a new notebook.
3. Install the required libraries.
4. Copy the project code into a notebook cell.
5. Run the cells.
6. Wait for the pretrained model to load.
7. Enter questions and view the retrieved answers.

**Note:** An internet connection is required initially to download the pretrained model.

## 7. Project Structure

```text
AI-Based-FAQ-Question-Answering-System/
│
├── FAQ_Chatbot.ipynb
├── requirements.txt
└── README.md
```

## Author
M.Ayshwarya
