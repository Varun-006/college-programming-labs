import gensim.downloader as api
import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
print("Loading word2vec-google-news-300")
model = api.load("word2vec-google-news-300")
tech_words = [
    "computer",
    "laptop",
    "software",
    "internet",
    "AI",
    "robot",
    "chip",
    "network",
    "data",
    "server"
]
select_words = [word for word in tech_words if word in model]
print("Selected words are:", select_words)
word_vectors = np.array([model[word] for word in select_words])
pca = PCA(n_components=2)
reduced_vector = pca.fit_transform(word_vectors)
plt.figure(figsize=(10,10))
for i, word in enumerate(select_words):
    plt.scatter(reduced_vector[i,0], reduced_vector[i,1])
    plt.text(
        reduced_vector[i,0] + 0.02,
        reduced_vector[i,1],
        word
    )
plt.title("Word Embedding Visualization")
plt.xlabel("PCA Dimension 1")
plt.ylabel("PCA Dimension 2")
plt.show()
word = "computer"
def similar_word(word, top_n=5):
    if word in model:
        return model.most_similar(word, topn=top_n)
    else:
        return f"{word} not in vocabulary"
print(f"Similar words for {word} are")
print(similar_word(word))