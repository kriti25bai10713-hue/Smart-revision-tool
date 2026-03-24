import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from collections import Counter

# Download required NLP assets
nltk.download('punkt', quiet=True)
nltk.download('stopwords', quiet=True)
nltk.download('averaged_perceptron_tagger', quiet=True)

class SmartRevisionTool:
    """
    A modular tool for generating flashcards from text notes.
    Includes validation, processing, and output modules.
    """
    
    def __init__(self):
        self.stop_words = set(stopwords.words('english'))

    def validate_data(self, text):
        """Module 1: Input Validation & Error Handling"""
        if not text or len(text.strip()) < 10:
            print("Error: Input text is too short or empty.")
            return False
        return True

    def preprocess_notes(self, text):
        """Module 2: Data Input & Cleaning"""
        sentences = sent_tokenize(text)
        return [s.strip() for s in sentences if len(s) > 5]

    def generate_qa(self, sentence):
        """Module 3: NLP Extraction Logic"""
        words = word_tokenize(sentence)
        tagged = nltk.pos_tag(words)
        
        # Identify Nouns (NN) or Proper Nouns (NNP) as keywords
        potential_keys = [word for word, pos in tagged 
                          if pos in ['NN', 'NNP'] and word.lower() not in self.stop_words]
        
        if not potential_keys:
            return None
            
        # Select the most frequent noun in the sentence as the answer
        answer = Counter(potential_keys).most_common(1)[0][0]
        question = sentence.replace(answer, "_______", 1)
        return {"question": question, "answer": answer}

    def save_revision_sheet(self, flashcards, filename="my_revision.txt"):
        """Module 4: Reporting & Analytics"""
        with open(filename, "w") as f:
            f.write("--- SMART REVISION FLASHCARDS ---\n\n")
            for i, card in enumerate(flashcards, 1):
                f.write(f"{i}. Q: {card['question']}\n   A: {card['answer']}\n\n")
        return f"File saved: {filename} with {len(flashcards)} cards."

# --- Main Execution Workflow ---
if __name__ == "__main__":
    tool = SmartRevisionTool()
    sample_notes = """
    Artificial Intelligence is the simulation of human intelligence by machines. 
    Python is the most popular language for machine learning. 
    Neural networks are inspired by the biological brain.
    """
    
    if tool.validate_data(sample_notes):
        sentences = tool.preprocess_notes(sample_notes)
        cards = []
        for s in sentences:
            qa = tool.generate_qa(s)
            if qa: cards.append(qa)
        
        print(tool.save_revision_sheet(cards))
