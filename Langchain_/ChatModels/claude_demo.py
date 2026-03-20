from langchain_anthropic import ChatAnthropic
from dotenv import load_dotenv
import os

load_dotenv()

model = ChatAnthropic()

response = model.invoke("Who is the most famous Indian cricketer in 20s?")

print(response.content)