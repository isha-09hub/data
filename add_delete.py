#Add,Delete


import spacy

nlp = spacy.load("en_core_web_sm")

def morphology_table(word):
    doc = nlp(word)
    token = doc[0]
    root = token.lemma_

    print(f"\nMorphology Table for: {word}")
    print("-" * 35)
    print(f"{'Step':<8} | {'Word'}")
    print("-" * 35)
    print(f"{'Start':<8} | {word}")
    print(f"{'Root':<8} | {root}")
    print(f"{'Add':<8} | {word}")

# Take input from user
word = input("Enter a word: ")
morphology_table(word)



//libraries 
pip install --user -U nltk
python -m nltk.downloader popular
pip install -U pip setuptools wheel
pip install spacy
python -m spacy download en_core_web_sm