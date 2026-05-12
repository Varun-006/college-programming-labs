#7. Summarize long texts using a pre-trained summarization model using Hugging face model. Load the summarization pipeline. Take a passage as input and obtain the summarized text.

from transformers import AutoTokenizer 
from transformers import AutoModelForSeq2SeqLM 
tokenizer=AutoTokenizer.from_pretrained("facebook/bart-large-cnn") 
model=AutoModelForSeq2SeqLM.from_pretrained("facebook/bart-large-cnn") 
input=tokenizer("""Amazon Rainforest Facts | One Tree Planted The Amazon rainforest is 
the world’s largest tropical rainforest, spanning 6.7 million square kilometers across nine 
South American nations, primarily Brazil. Often called the "lungs of the planet, " this vital 
ecosystem stores roughly 123 billion metric tonnes of carbon and hosts one in ten known 
species on Earth, including 40,000 plant types. However, it faces severe threats from 
deforestation, ranching, and climate change, which endanger its biodiversity and indigenous 
communities""",    return_tensors="pt",max_length=1024,truncation=True) 
summary_ids=model.generate(input["input_ids"],max_length=60,min_length=25) 
print(tokenizer.decode(summary_ids[0],skip_special_tokens=True))