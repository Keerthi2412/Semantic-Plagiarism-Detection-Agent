# Semantic-Plagiarism-Detection-Agent
CODEATHON-2.0
# 🔍 Semantic Plagiarism Detection Agent

A web-based AI-powered plagiarism detection system that identifies
semantic similarity and paraphrased content instead of relying only
on exact word matching.

---

## 🎯 Problem Statement

Traditional plagiarism detection systems primarily compare exact
words and phrases. Students can avoid detection by paraphrasing,
restructuring sentences, or using AI tools to rewrite existing content.

This project detects similarity based on the meaning of the text.

---

## 💡 Solution

The system compares a submitted document against a reference document.

The documents are:

1. Processed and converted into text
2. Divided into sections
3. Converted into semantic embeddings
4. Compared using cosine similarity
5. Matched section-by-section
6. Assigned an overall similarity percentage
7. Classified into plagiarism risk levels

---

## 🚀 Features

- PDF document processing
- DOCX document processing
- TXT document processing
- Semantic text embeddings
- Paraphrase detection
- Section-level comparison
- Matching section identification
- Similarity percentage
- Plagiarism risk classification
- Web-based interface
- AI-generated/paraphrased content analysis

---

## 🧠 Technology Stack

### Frontend

- HTML
- CSS
- JavaScript

### Backend

- Python
- Flask

### Machine Learning

- Sentence Transformers
- all-MiniLM-L6-v2
- Cosine Similarity
- Scikit-learn

### Document Processing

- PyPDF
- python-docx

---

## 🏗️ Architecture

```text
              Submitted Document
                       |
                       v
               Document Processing
                       |
                       v
                 Section Splitting
                       |
                       v
              Semantic Embeddings
                       |
                       v
                Similarity Engine
                       ^
                       |
                 Reference Document
                       |
                       v
              Matching Sections
                       |
                       v
                Similarity Score
                       |
                       v
                 Risk Analysis
                       |
                       v
                Plagiarism Report
