from langchain_core.tools import Tool
from langchain_community.tools import DuckDuckGoSearchRun
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

ddgo = DuckDuckGoSearchRun()

llm = ChatGoogleGenerativeAI(model = "gemini-2.5-flash").bind_tools([ddgo])

print(llm.invoke("Current Gold price in Hyderabad").tool_calls)