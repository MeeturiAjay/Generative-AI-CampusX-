from langchain_groq import ChatGroq
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain.messages import AIMessage, HumanMessage, SystemMessage
from dotenv import load_dotenv
import os

load_dotenv()
# os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")

model = ChatGroq(model = "llama-3.3-70b-versatile", max_retries = 3)
prompt_template = ChatPromptTemplate.from_messages([
    SystemMessage(content = "You are a cricket expert. Else just say since you are so, you cannot answer for the user query."),
    HumanMessage(content = "What is the dimensions of the cricketing pitch?")
])

chain = prompt_template | model | StrOutputParser()

response = chain.invoke({})
# response = chain.invoke({"human":"What is Machine Learning"})
print(response)