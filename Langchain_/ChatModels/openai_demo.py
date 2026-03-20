from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os

load_dotenv()

model = ChatOpenAI()

response = model.invoke("Who is the most famous cricketer from India?")

print(response.content)