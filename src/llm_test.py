from langchain_ollama import ChatOllama


llm = ChatOllama(
    model="qwen3:4b",
    temperature=0
)

response = llm.invoke(
    "Write a Snowflake SQL query to calculate total spending "
    "by vendor from FACT_TRANSACTIONS using VENDOR and AMOUNT."
)

print(response.content)