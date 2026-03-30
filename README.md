# 📘 Quiz Application with Document-Based Question Generation and LLM Evaluation

## 🚀 Project Overview

This project is an AI-powered Quiz Application that generates questions from a user-provided document (PDF/Text) and evaluates answers using a Large Language Model (LLM).

The system automatically reads the uploaded document, understands the content, generates meaningful questions, and provides feedback along with scoring.

---

## ❓ Problem Understanding

Traditional quiz systems require manual question creation, which is time-consuming and not scalable.
This project solves that by:

* Automatically generating questions from documents
* Evaluating answers intelligently using AI
* Providing instant feedback and results

---

## 🔍 Research Findings

* LLMs like Mistral and transformer models can generate high-quality questions
* Chunking helps in processing large documents efficiently
* Prompt engineering improves relevance of generated questions
* Local models (via Ollama) reduce dependency on paid APIs

---

## 🛠️ Approach Taken

1. **Document Upload**

   * User uploads a PDF or text file

2. **Text Extraction**

   * Extract content using PDF/text processing libraries

3. **Question Generation**

   * Use LLM to generate questions from extracted content

4. **Answer Evaluation**

   * Compare user answers with expected answers using LLM

5. **Feedback System**

   * Provide score and explanation

---

## 🔄 Alternatives Tried

* Used OpenAI API (rejected due to cost)
* Tried different prompting techniques for better questions
* Tested chunk-based vs full-document processing
* Experimented with multiple LLMs (Mistral, HuggingFace models)

---

## ⚠️ Challenges Faced

* Generating relevant and non-repetitive questions
* Handling large PDFs efficiently
* Model producing irrelevant outputs initially
* Integration with frontend (Gradio responsiveness issues)
* Setting up local LLM (Ollama errors and configuration)

---

## 📚 Learnings

* Practical use of LLMs in real-world applications
* Importance of prompt engineering
* Handling unstructured data (PDFs)
* Debugging model and API-related issues
* Building end-to-end AI applications

---

## ✨ Features

* 📄 Upload PDF/Text documents
* 🤖 Automatic question generation
* 🧠 AI-based answer evaluation
* 📊 Score and feedback generation
* 💻 Simple UI using Gradio

---

## 🧰 Tech Stack

* Python
* Gradio (Frontend)
* Transformers / LLM
* Ollama (Local model - Mistral)
* PyPDF / document processing libraries

---

## ▶️ How to Run

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the Application

```bash
python main.py
```

### 4. Open in Browser

Gradio will provide a local URL (e.g., http://127.0.0.1:7860)

---

## 📂 Project Structure

```
├── main.py
├── requirements.txt
├── README.md
├── sample_docs/
└── utils/
```

---

## 🔐 Note

* Do not expose API keys or tokens publicly
* Use environment variables for sensitive data

---

## 📌 Future Improvements

* Improve question relevance using better prompts
* Add support for multiple document formats
* Enhance UI/UX
* Add user authentication
* Store quiz history

---

## 👨‍💻 Author

Badarish Malagi

---

## 📎 GitHub Repository
https://github.com/badarishm/Quiz-Application-with-Document-Based-Question-Generation-and-LLM-Evaluation


