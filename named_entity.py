#Named Entity 


import spacy

# Make sure the model is downloaded
try:
    nlp = spacy.load('en_core_web_sm')
except:
    import spacy.cli
    spacy.cli.download('en_core_web_sm')
    nlp = spacy.load('en_core_web_sm')

# Take input
text = input("Enter a sentence: ")

# Process text
doc = nlp(text)

# Print named entities
if doc.ents:
    for ent in doc.ents:
        print(f"Entity: {ent.text}, Label: {ent.label_}")
else:
    print("No named entities found.")





//libraries 
pip install --user -U nltk
python -m nltk.downloader popular
pip install -U pip setuptools wheel
pip install spacy
python -m spacy download en_core_web_sm