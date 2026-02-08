from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnableParallel
from langchain_core.output_parsers import StrOutputParser
from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
 
load_dotenv()

llm = HuggingFaceEndpoint(repo_id = "Qwen/Qwen3-Coder-Next")
model = ChatHuggingFace(llm = llm)

prompt1 = ChatPromptTemplate.from_template("Give notes on History of Hyderabad.")
prompt2 = ChatPromptTemplate.from_template("Give quiz questions on History of Hyderabad.")
prompt3 = ChatPromptTemplate.from_template("Answer all the (quiz) '{chain2}' questions on the History of Hyderabad.")

parallel_chain = RunnableParallel({
    "chain1": prompt1 | model | StrOutputParser(),
    "chain2": prompt2 | model | StrOutputParser()
})

down_chain = prompt3 | model | StrOutputParser()

final_chain = parallel_chain | down_chain | StrOutputParser()

response = final_chain.invoke({})

# print(response)
final_chain.get_graph().print_ascii()

# chained like:
#     A   B 
#       |
#       V 
#       C 