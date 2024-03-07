import os
from dotenv import load_dotenv

load_dotenv(dotenv_path="/home/juanfe/GitHub/Docs/Azure Open AI/.env")

from openai import AzureOpenAI
    
client = AzureOpenAI(
    api_key=os.getenv("AZURE_OPENAI_API_KEY"),  
    api_version=os.getenv("API_VERSION"),
    azure_endpoint = os.getenv("ENDPOINT")
    )
    
deployment_name= os.getenv('GPT4_NAME')
    
# Send a completion call to generate an answer
start_phrase = 'Write a tagline for an ice cream shop. '
response = client.completions.create(model=deployment_name, prompt=start_phrase, max_tokens=10)
print(start_phrase+response.choices[0].text)

"""
curl https://ai-cc-desa.openai.azure.com/openai/deployments/NAME/completions?api-version=2024-02-15-preview\
  -H "Content-Type: application/json" \
  -H "api-key: " \
  -d "{
  \"prompt\": \"Once upon a time\",
  \"max_tokens\": 5
}"

"""




from langchain_openai import AzureOpenAI
from dotenv import load_dotenv
import os

load_dotenv(dotenv_path="/home/juanfe/GitHub/Docs/Azure Open AI/.env")

llm = AzureOpenAI(
    deployment_name=os.getenv('GPT4_NAME')
)

llm.invoke("Tell me a joke")