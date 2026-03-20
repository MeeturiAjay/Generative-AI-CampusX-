from langchain_ollama import OllamaEmbeddings

embedding_model = OllamaEmbeddings(model = "mxbai-embed-large:latest")

print(len(embedding_model.embed_query("Hyderabad")))
# print(embedding_model.temperature)