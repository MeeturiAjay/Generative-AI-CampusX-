from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser, JsonOutputParser
from dotenv import load_dotenv

load_dotenv()

llm = HuggingFaceEndpoint(
                    repo_id = "Qwen/Qwen3-Coder-Next",
                    # task = "text-generation"
                )

model = ChatHuggingFace(llm = llm)

template1 = ChatPromptTemplate.from_template("Give the detailed report on the '{topic}' given.")
template2 = ChatPromptTemplate.from_template("Give the 5 lines summary on the provided '{text}'")

# Way-1
# chain1 = template1 | model | StrOutputParser()
# text = chain1.invoke({"topic": "Hyderabad"})

# chain2 = template2 | model | StrOutputParser()
# result = chain2.invoke({"text": text})

# Way-2
chain = template1 | model | StrOutputParser() | template2 | model | StrOutputParser()
result = chain.invoke({"topic": "Hyderabad History"})
# chain.get_graph().print_ascii() -> Prints chain steps as graph
print(result)