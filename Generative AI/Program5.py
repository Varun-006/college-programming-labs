import gensim.downloader as api
import random
print("Loading pre-trained word2vec model...")
model = api.load("word2vec-google-news-300")
seed_word = input("Enter a seed word: ")
if seed_word in model:
    similar_words = model.most_similar(seed_word, topn=5)
    print("\nSimilar words:")
    words = []
    for word, score in similar_words:
        print(f"{word} (Similarity: {score:.4f})")
        words.append(word)
    print("\nGenerated Paragraph:\n")
    paragraph = f"""
                The concept of {seed_word} connects deeply with ideas like
                {words[0]}, {words[1]}, and {words[2]}. In many situations,
                {words[3]} plays an important role, while {words[4]} influences the
                overall meaning. Together, these elements create a broader
                understanding of {seed_word}, making it powerful and meaningful in
                different contexts."""
    print(paragraph)
else:
    print("Word not found in vocabulary. Please try another word.")