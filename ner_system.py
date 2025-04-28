#Ner System 



import spacy
from sklearn.metrics import precision_score, recall_score, f1_score

nlp = spacy.load('en_core_web_sm')

def extract_entities(text):
    return [ent.text for ent in nlp(text).ents]

def evaluate(true, pred):
    y_true = [1 if t in pred else 0 for t in true]
    y_pred = [1] * len(true)
    return precision_score(y_true, y_pred, zero_division=0), recall_score(y_true, y_pred, zero_division=0), f1_score(y_true, y_pred, zero_division=0)

text = input("Enter a sentence: ")
true_entities = input("Enter true entities (comma separated): ").split(",")

predicted = extract_entities(text)

print("\nPredicted Entities:", predicted)

precision, recall, f1 = evaluate([e.strip() for e in true_entities], predicted)

print(f"\nPrecision: {precision:.2f}, Recall: {recall:.2f}, F1 Score: {f1:.2f}")





//libraries 
pip install --user -U nltk
python -m nltk.downloader popular
pip install -U pip setuptools wheel
pip install spacy
python -m spacy download en_core_web_sm