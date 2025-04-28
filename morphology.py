#Morphology 


import nltk
from nltk.stem import WordNetLemmatizer

nltk.download('punkt')
nltk.download('wordnet')

prefixes = ['un', 're', 'dis', 'pre', 'mis', 'in', 'im', 'non', 'over', 'under', 'inter', 'sub', 'trans', 'super', 'semi', 'anti', 'co', 'de']
suffixes = ['ing', 'ed', 'ness', 'ly', 'able', 'ible', 'ment', 'tion', 'sion', 'er', 'or', 'ist', 'al', 'ous', 'ive', 'ity', 'y', 'en', 'ize', 'ise']

lemmatizer = WordNetLemmatizer()

def morphology_table(word):
    original = word
    prefix = ''
    suffix = ''
    core = word

    # Detect prefix
    for p in prefixes:
        if core.startswith(p):
            prefix = p
            core = core[len(p):]
            break

    # Detect suffix
    for s in suffixes:
        if core.endswith(s):
            suffix = s
            core = core[:-len(s)]
            break

    # Lemmatize core
    root = lemmatizer.lemmatize(core)

    print(f"\n[Morphology Table for '{original}']")
    print(f"{'Action':<10} | {'Morpheme':<10} | {'Result'}")
    print("-" * 35)
    print(f"{'Start':<10} | {'-':<10} | {original}")
    
    if suffix:
        print(f"{'Delete':<10} | {suffix:<10} | {prefix + core}")
    if prefix:
        print(f"{'Delete':<10} | {prefix:<10} | {core}")
    
    print(f"{'Root':<10} | {'-':<10} | {root}")

    if prefix:
        print(f"{'Add':<10} | {prefix:<10} | {prefix + root}")
    if suffix:
        print(f"{'Add':<10} | {suffix:<10} | {prefix + root + suffix}")

# Test
morphology_table("unhappiness")
morphology_table("happily")
morphology_table("disagreeable")




//libraries 
pip install --user -U nltk
python -m nltk.downloader popular
pip install -U pip setuptools wheel
pip install spacy
python -m spacy download en_core_web_sm


