
# 🧠 Smart Revision Tool: NLP Flashcard Generator

## 📌 Project Overview
The Smart Revision Tool is an AI-powered educational utility designed to transform dense academic notes into concise Question-and-Answer pairs. By utilizing Natural Language Processing (NLP), the tool identifies key concepts and automates the creation of flashcards to facilitate active recall.

## 🚀 Features
* **Text Preprocessing**: Cleans and tokenizes raw text notes into structured sentences.
* **NLP-Based QA Generation**: Uses Part-of-Speech (POS) tagging to identify nouns and create "fill-in-the-blank" questions.
* **Modular Architecture**: Built with separate modules for validation, processing, and exporting to ensure maintainability.
* **Automated Export**: Generates a formatted study sheet (`.txt`) for offline revision.

## 🚀 Future Enhancements
To further increase the complexity and utility of the Smart Revision Tool, the following features are planned for future releases:

1. **Integration with Large Language Models (LLMs)**: Replace basic NLTK rule-based logic with advanced models like GPT-4 or Llama-3 to generate more natural and contextually aware questions.
2. **Support for OCR (Optical Character Recognition)**: Implement an image-to-text module using Tesseract or EasyOCR to allow students to generate flashcards directly from photos of handwritten notes.
3. **Mnemonic Generator**: Add a feature that uses AI to create helpful acronyms or memory aids for complex terms identified during the keyword extraction process.
4. **Export to Anki/Quizlet**: Develop a module to export generated flashcards in CSV or JSON formats compatible with popular spaced-repetition software like Anki.
5. **Multi-Language Support**: Expand the NLP pipeline to support automated flashcard generation in languages other than English, such as Spanish, French, or Hindi.
6. **Graphical User Interface (GUI)**: Transition from a command-line tool to a full desktop application using Tkinter or PyQt for a more accessible user experience.

## 🛠 Technologies Used
* **Language**: Python 3.x
* **Library**: NLTK (Natural Language Toolkit)
* **Environment**: Google Colab / Local CLI
* **Version Control**: Git/GitHub

## 📂 File Structure
Following academic standards for modular implementation:
```text
smart-revision-tool/
├── src/
│   ├── main.py              # Application entry point
│   ├── processor.py         # NLP & Keyword extraction logic
│   ├── validator.py         # Input validation & error handling
│   └── exporter.py          # File I/O and reporting modules
├── data/
│   └── sample_notes.txt     # Test data for evaluation
├── docs/
│   └── system_architecture.png # Visual design artifact
├── README.md                # Project documentation [cite: 83]
├── statement.md             # Problem statement & scope [cite: 95]
└── requirements.txt         # Project dependencies
```

## Clone the Repository:
```bash
git clone [https://github.com/your-username/smart-revision-tool.git](https://github.com/your-username/smart-revision-tool.git)
cd smart-revision-tool
```
## Create a Virtual Environment:
```bash
# Create the environment
python -m venv venv

# Activate on Windows:
venv\Scripts\activate

# Activate on macOS/Linux:
source venv/bin/activate
```
## Install Dependencies:
```bash
pip install nltk
```
## How to Run
```bash
python src/main.py
```


