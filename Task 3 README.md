# TASK 3 Improved AI-Based FAQ Question Answering System

## 1. Project Overview

The Improved AI-Based FAQ Question Answering System is a Python-based chatbot developed as part of the AI Internship at SWYNEX Technologies. It uses a pretrained Sentence Transformer model (`all-MiniLM-L6-v2`) to understand user questions and retrieve the most relevant answers from a predefined college FAQ dataset.

The project improves the initial FAQ prototype by introducing semantic similarity evaluation, threshold comparison, failure-case testing, and a simple interactive interface using Gradio.

## 2. Objectives

- Improve FAQ retrieval using a pretrained semantic embedding model.
- Evaluate the system using sample questions and test cases.
- Compare different similarity thresholds.
- Identify incorrect matches and unsupported questions.
- Provide a simple chatbot interface for users.

## 3. Technologies Used

- **Python** – Core programming language
- **Sentence Transformers** – Semantic text embeddings
- **all-MiniLM-L6-v2** – Pretrained sentence embedding model
- **PyTorch** – Model support and computation
- **Pandas** – Evaluation results and data handling
- **Gradio** – Interactive chatbot interface
- **Google Colab** – Development and execution environment

## 4. Features

- Semantic understanding of user questions.
- Retrieval of predefined FAQ answers.
- Similarity threshold-based answer selection.
- Evaluation using in-scope and out-of-scope questions.
- Comparison of multiple similarity thresholds.
- Failure-case analysis.
- Interactive chatbot interface.

## 5. Project Structure

```text
Improved-AI-FAQ-Question-Answering-System/
│
├── Task3_FAQ_Chatbot.ipynb
├── README.md
└── requirements.txt
```

## 6. Installation

Install the required libraries:

```bash
pip install sentence-transformers torch pandas gradio
```

## 7. How to Run

1. Open `Task3_FAQ_Chatbot.ipynb` in Google Colab.
2. Run the notebook cell containing the complete implementation.
3. Allow the pretrained model to download and load.
4. Review the evaluation results and failure-case analysis.
5. Open the Gradio interface link generated after execution.
6. Enter a question to test the FAQ chatbot.

**Note:** An internet connection is required initially to download the pretrained model. No Gemini API key or paid API is required.

## 8. Model and Methodology

The system uses the pretrained `all-MiniLM-L6-v2` Sentence Transformer model to convert FAQ entries and user questions into numerical embeddings. Cosine similarity is then used to identify the closest matching FAQ.

If the similarity score meets the configured threshold, the corresponding predefined answer is returned. Otherwise, the chatbot displays a fallback response.

The system retrieves existing answers; it does not generate new answers using a generative AI model.

## 9. Evaluation

The prototype includes:
- In-scope question retrieval evaluation.
- Out-of-scope question rejection evaluation.
- Similarity threshold comparison.
- Failure-case testing.

Actual evaluation scores depend on the notebook execution and test results.

## 10. Limitations

- The FAQ dataset contains illustrative college-related information.
- Answers are limited to the available FAQ entries.
- Ambiguous questions may produce incorrect matches.
- Similarity scores do not guarantee factual correctness.
- The temporary Gradio sharing link is available only while the notebook session remains active.

## 11. Future Enhancements

- Expand the FAQ dataset with verified institutional information.
- Add multilingual question support.
- Improve retrieval using a larger and more diverse evaluation dataset.
- Integrate a verified college website or database.
- Deploy the chatbot as a permanent web application.

## 12. Conclusion

This project demonstrates an improved semantic FAQ retrieval system using a pretrained Sentence Transformer model. Evaluation examples, threshold comparison, failure-case analysis, and a Gradio interface make the prototype more practical and easier to assess.

## Author
M. Ayshwarya
