#6. Use a pre-trained Hugging Face model to analyze sentiment in text. Assume a real world application, Load the sentiment analysis pipeline. Analyze the sentiment by giving sentences to input.
from transformers import pipeline 
sentiment_analyzer = pipeline("sentiment-analysis") 
sentences = [  
"The product quality is excellent and I love it.", 
"Worst experience ever. Completely disappointed.", 
"The service was average but acceptable.", 
"Fast delivery and great customer support!", 
"The item arrived damaged and late." 
] 
results = sentiment_analyzer(sentences) 
for sentence, result in zip(sentences, results): 
    print("Sentence:", sentence) 
    print("Predicted Sentiment:", result["label"]) 
    print("Confidence Score:", round(result["score"], 4)) 
    print("-" * 50)