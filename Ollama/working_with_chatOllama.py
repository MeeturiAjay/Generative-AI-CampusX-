from langchain_ollama import ChatOllama
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate

llm = ChatOllama(model = "llama3.2:latest")
parser = StrOutputParser()

prompt = ChatPromptTemplate.from_template("""
            You are an helpful cricket expert assistant.
            You need to answer to queries asked by the user.
            Always answer according to your cutoff date.
            If you don't know the answer to the query asked, then simply reply 'I DON'T KNOW!'               
                            
            'Question': {question}
""")

chain = prompt | llm | parser

print(chain.invoke({"question": "What is the 2023 result for Team India in an ICC tournament?"}))