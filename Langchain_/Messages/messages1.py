from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv
import os

load_dotenv()

os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")

model = ChatGroq(model = "llama-3.3-70b-versatile", max_retries = 3)
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a tour guide. And if you've been asked other than this field just simply sayh them that I am just a tour guide"),
    ("human", "What is Machine Learning?")
    ]
)

chain = prompt | model
response = chain.invoke({})

print(response.content)