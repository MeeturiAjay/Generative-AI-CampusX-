from langchain_community.tools import DuckDuckGoSearchRun
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
from dotenv import load_dotenv
from pydantic.v1.fields import FieldInfo as FieldInfoV1

load_dotenv()

# search = DuckDuckGoSearchRun()
# # context = ddgo.invoke("Give the latest Gold rate in hyderabad")

# llm = ChatGoogleGenerativeAI(model = "gemini-2.5-flash").bind_tools([search])

# prompt = ChatPromptTemplate.from_template("""
#         You are an helpful assistant.
#         You need to answer to the user question ONLY using the context provided and also provide
#         the citation from which you are referring to answer the query.
#         If the context is insufficient, answer as you don't know.
        
#         'Context': {context}
#         'question': {question}
# """)

# parser = StrOutputParser()

# chain = {"context": RunnablePassthrough() | search , "question": RunnablePassthrough()} | prompt | llm 

# print(chain.invoke("Temperature in  kukatpally, hyderabad"))

from langchain_community.tools import DuckDuckGoSearchRun
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

# Tool
search = DuckDuckGoSearchRun()

# LLM with tool binding
llm = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash"
).bind_tools([search])

# Ask question
response = llm.invoke("Give summary of virat kohli? ")

print(response)
print("\nTOOL CALLS:")
print(response.tool_calls)