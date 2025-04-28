#N-gram 


import nltk
import matplotlib.pyplot as plt
from nltk import ngrams
from nltk.tokenize import word_tokenize
from nltk.probability import FreqDist

nltk.download('punkt')

text = "Betty bought butter but the butter was bitter. So Betty bought better butter to make the bitter butter better."
tokens = word_tokenize(text.lower())

for n in [1, 2, 3]:
    freq = FreqDist(ngrams(tokens, n))
    top_n = freq.most_common(10)  # Show top 10 n-grams

    # Print n-grams
    print(f"\n{n}-grams:")
    for gram, count in top_n:
        print(f"{gram}: {count}")

    # Plot
    labels, counts = zip(*top_n)
    labels = [' '.join(g) for g in labels]  # Convert tuple to string

    plt.figure(figsize=(8, 4))
    plt.bar(labels, counts)
    plt.title(f"Top {n}-grams")
    plt.xticks(rotation=45, ha='right')
    plt.xlabel('N-gram')
    plt.ylabel('Frequency')
    plt.tight_layout()
    plt.show()



//libraries 
pip install --user -U nltk
python -m nltk.downloader popular
pip install -U pip setuptools wheel
pip install spacy
python -m spacy download en_core_web_sm