#4. Use word embeddings to improve prompts for Generative AI model. Retrieve similar words using word embeddings. Use the similar words to enrich a GenAI prompt. Use the AI model to generate responses for the original and enriched prompts. Compare the outputs in terms of detail and relevance. 
import gensim.downloader as api
from transformers import pipeline
import torch
word_vectors = api.load("word2vec-google-news-300")
generator = pipeline("text-generation", model="gpt2")
original_prompt = "Describe the beautiful landscape during sunset."
keywords = ["beautiful", "landscape", "sunset"]
similar_words = []
for word in keywords:
    if word in word_vectors:
        similar_words += [w[0] for w in word_vectors.most_similar(word, topn=2)]
enriched_prompt = original_prompt + " includes details like: " + ", ".join(similar_words) + "."
original_output = generator(original_prompt, max_new_tokens=20)
enriched_output = generator(enriched_prompt, max_new_tokens=20)
print("Original prompt:")
print(original_prompt)
print("\nEnriched prompt:")
print(enriched_prompt)
print("\nOriginal output:")
print(original_output)
print("\nEnriched output:")
print(enriched_output)