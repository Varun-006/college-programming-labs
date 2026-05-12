#8. Install langchain, cohere (for key), langchain-community. Get the apikey( By logging into Cohere and obtaining the cohere key). Load a text document from your google drive. Create a prompt template to display the output in a particular manner.

import os 
from langchain_cohere import ChatCohere 
from langchain_core.prompts import ChatPromptTemplate 
import getpass 
import gdown 

# Set Cohere API Key 
if not os.environ.get("COHERE_API_KEY"): 
    os.environ["COHERE_API_KEY"] = getpass.getpass("Enter Cohere API Key: ") 

# Import LangChain Cohere Model 
from langchain_cohere import ChatCohere 
from langchain_core.prompts import ChatPromptTemplate 

# Load Cohere Model 
model = ChatCohere(model="command-r7b-12-2024") 

# Create Prompt Template 
prompt = ChatPromptTemplate.from_template(
    "Generate a motivational quote about {topic}"
) 

# Create Chain 
chain = prompt | model 

# Invoke the model 
response = chain.invoke({"topic": "GenAI"}) 

print(response.content) 

# Google Drive File ID 
file_id = "1BPgmF8od-gvK0GeDyaeAwCrSGpgvwXFN" 
file_path = "ai_agents_info.txt" 

# Download file from Google Drive 
gdown.download(
    f"https://drive.google.com/uc?export=download&id={file_id}",
    file_path,
    quiet=False
) 

# Read the document 
with open(file_path, "r", encoding="utf-8") as file: 
    document_text = file.read() 

print("\nContent of the Document:\n") 
print(document_text)