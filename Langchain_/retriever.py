from langchain_community.retrievers import WikipediaRetriever

retriever = WikipediaRetriever(top_k_results = 2)
print(retriever.invoke("When & Where the 1st intl cricket match held?").content)