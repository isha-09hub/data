#POS



import spacy

nlp = spacy.load("en_core_web_sm")

doc = nlp(input("Enter a sentence: "))

for token in doc:
    print(f"{token.text}: {token.pos_}")


//libraries 
pip install --user -U nltk
python -m nltk.downloader popular
pip install -U pip setuptools wheel
pip install spacy
python -m spacy download en_core_web_sm