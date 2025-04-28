#Semantic 



import nltk
from nltk.corpus import wordnet as wn
from prettytable import PrettyTable

nltk.download('wordnet')
nltk.download('omw-1.4')

def get_semantics_relations(w1, w2):
    s1, s2 = wn.synsets(w1), wn.synsets(w2)
    if not s1 or not s2:
        return f"Semantic relation could not be determined for {w1} and {w2}"
    
    s1, s2 = s1[0], s2[0]
    return {
        'Word 1': w1,
        'Word 2': w2,
        'Definition 1': s1.definition(),
        'Definition 2': s2.definition(),
        'Hypernyms 1': ', '.join(l.name() for h in s1.hypernyms() for l in h.lemmas()),
        'Hyponyms 1': ', '.join(l.name() for h in s1.hyponyms() for l in h.lemmas()),
        'Hypernyms 2': ', '.join(l.name() for h in s2.hypernyms() for l in h.lemmas()),
        'Hyponyms 2': ', '.join(l.name() for h in s2.hyponyms() for l in h.lemmas()),
        'Similarity': s1.wup_similarity(s2)
    }

w1 = input("Enter first word: ")
w2 = input("Enter second word: ")

relations = get_semantics_relations(w1, w2)

print()

if isinstance(relations, dict):
    table = PrettyTable()
    table.field_names = ["Feature", "Details"]
    for k, v in relations.items():
        table.add_row([k, v])
    print(table)
else:
    print(relations)



//libraries 
pip install --user -U nltk
python -m nltk.downloader popular
pip install -U pip setuptools wheel
pip install spacy
python -m spacy download en_core_web_sm