import gensim.downloader as api
print("loading pretrained vector\n")
word_vector = api.load("word2vec-google-news-300")
word = "king"
vector = word_vector[word]
print(f"The pretrained vectors of {word}:", vector[:10])
print("Length of the vector is", len(vector))
def find_similar(word, top_n=5):
    if word in word_vector:
        return word_vector.most_similar(word, topn=top_n)
    else:
        return f"{word} not in vocabulary"
print(f"Similar words to {word}")
print(find_similar(word))
def vector_arithmetic(word1, word2, word3, top_n=2):
    try:
        result = word_vector.most_similar(
            positive=[word1, word3],
            negative=[word2],
            topn=top_n
        )
        return result
    except KeyError as e:
        return str(e)
print("Vector arithmetic of king - man + woman =")

print(vector_arithmetic("king", "man", "woman"))