import re
from langchain.prompts.prompt import PromptTemplate
from langchain_ollama import ChatOllama
from langchain_core.tools import Tool
from langchain import hub
from langchain_core.output_parsers import StrOutputParser
from langchain.agents import (
    create_react_agent,
    AgentExecutor,
)



def remove_think_tags(text):
    return re.sub(r"<think>.*?</think>", "", text, flags=re.DOTALL).strip()

def main():
    # Initialize the Ollama LLM
    llm = ChatOllama(model="deepseek-r1:8b",temperature=0)

    # Define a prompt template
    template = """
    You are a helpful assistant. You are to answer each question formally. Here is a question:
    {question}
    Provide a short answer.
    """
    prompt = PromptTemplate(template=template, input_variables=["question"])

    # Example input question
    question = "What is 2+5?"

    # Run the chain and get the output
    chain = prompt | llm | StrOutputParser()
    response = chain.invoke(input={'question':question})

    # Print the response
    print("Response:", remove_think_tags(response))

if __name__ == "__main__":
    main()