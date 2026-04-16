# AI Resume Screening System with Tracing

## 📌 Project Overview
This project is an AI-powered Resume Screening System built to evaluate candidate resumes against a specific Job Description (JD). It goes beyond basic keyword matching by utilizing Large Language Models (LLMs) to extract skills, compare them to job requirements, generate a fit score (0-100), and provide a detailed explanation for the scoring logic. 

This system was built to demonstrate production-level LLM engineering, specifically focusing on pipeline modularity, prompt constraints, and step-by-step tracing for debugging.

## 🛠️ Tech Stack & Tools
* **Language:** Python
* **Framework:** LangChain (LCEL)
* **Model:** HuggingFace (`Qwen/Qwen2.5-7B-Instruct`)
* **Observability:** LangSmith (Mandatory tracing enabled)
* **IDE:** VS Code

## 🏗️ Pipeline Architecture
The system follows a strict, modular pipeline to ensure explainable AI outputs:
`Resume Input` → `Skill & Tool Extraction` → `Requirement Matching` → `Scoring` → `Explanation Generation` → `LangSmith Trace`

### Folder Structure
```text
📁 resume_screening_system
 ├── 📁 chains
 │    └── resume_chain.py         # Contains the LCEL pipeline and model initialization
 ├── 📁 prompts
 │    ├── extraction_prompt.py    # Strict instructions for extracting skills/tools
 │    └── evaluation_prompt.py    # Logic for matching, scoring, and explaining
 ├── .env                         # API keys and LangSmith configuration (Not uploaded)
 ├── .gitignore                   # Security rules
 └── main.py                      # Execution script with dummy candidates
