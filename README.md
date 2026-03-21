# Smart-revision-tool
# 🧠 Smart Revision Tool

A Python-based program that helps students revise faster by automatically generating flashcards from their notes. This tool transforms long text into concise question–answer pairs using basic NLP techniques.

---

## 📌 Features

- Converts plain text notes into flashcards
- Uses sentence tokenization and word tokenization
- Outputs Q/A pairs for quick revision
- Lightweight and beginner-friendly
- Runs from the command line (no GUI required)

---

## 🚀 Setup Instructions

### 1. Clone the Repository

```bash

git clone https://github.com/{your-username}/smart-revision-tool
cd smart-revision-tool

python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

pip install -r requirements.txt
```


## 📂 File Structure
```text
smart-revision-tool/
├── src/
│   └── main.py              # Main script to run the tool
├── data/
│   └── sample_notes.txt     # Example notes for testing
├── docs/
│   └── project_report.pdf   # Detailed project report
├── README.md                # This file
└── requirements.txt         # Python dependencies
```

## 🧪 How to Run
```bash
python src/main.py
```

## ✍️ Input Format
```python
notes = """
Photosynthesis converts light energy into chemical energy.
Acid rain is caused by sulfur dioxide and nitrogen oxides.
The nitrogen cycle involves fixation, nitrification, and denitrification.
"""
```

## 📤 Sample Output
```text
Q: What is the key idea in: 'Photosynthesis converts light energy into chemical energy.'?
A: Photosynthesis converts light energy into...

Q: What is the key idea in: 'Acid rain is caused by sulfur dioxide and nitrogen oxides.'?
A: Acid rain is caused by...

Q: What is the key idea in: 'The nitrogen cycle involves fixation, nitrification, and denitrification.'?
A: The nitrogen cycle involves fixation...
```

## 🛠 Technologies Used

- Python 3.x  
- NLTK (Natural Language Toolkit)  
- Google Colab (for development)


## 📈 Future Enhancements

- Add mnemonic generator  
- Save flashcards to CSV or JSON  
- Build a CLI interface for user input  
- Support multi-subject note parsing
