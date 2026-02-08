from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from dotenv import load_dotenv
import os

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id = "meta-llama/Llama-3.1-8B-Instruct", 
    task = "text-generation"
    )

model = ChatHuggingFace(llm = llm)

response = model.invoke("Who is the famous cricketer ever since 2000?")

print(response.content)