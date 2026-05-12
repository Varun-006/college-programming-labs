#3. Train a custom Word2Vec model on a small dataset. Train embeddings on a domain specific corpus (e.g., legal, medical) and analyze how embeddings capture domain specific semantics.  
from gensim.models import Word2Vec
legal_corpus = [
    ["court", "judge", "lawyer", "case", "trial", "justice"],
    ["police", "arrest", "criminal", "court", "evidence"],
    ["law", "constitution", "rights", "citizen", "justice"],
    ["justice", "verdict", "trial", "evidence", "lawyer"],
    ["crime", "punishment", "prison", "criminal", "law"],
    ["legal", "contract", "agreement", "law", "court"]
]
model = Word2Vec(
    sentences=legal_corpus,
    vector_size=50,
    window=3,
    min_count=1,
    workers=4
)
def get_similar_words(word, top_n=5):
    if word in model.wv:
        return model.wv.most_similar(word, topn=top_n)
    else:
        return f"{word} not found in vocabulary"
print("Similar words to 'judge':")
print(get_similar_words("judge"))
print("\nSimilar words to 'law':")
print(get_similar_words("law"))