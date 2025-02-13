import sys
import os

# Add the root directory to sys.path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Now you can use absolute imports
from tools.tools import get_linkurl_tavily
from langchain.prompts.prompt import PromptTemplate
from langchain_ollama import ChatOllama
from langchain_core.tools import Tool
from langchain import hub
from langchain_core.output_parsers import StrOutputParser
from langchain.agents import (
    create_react_agent,
    AgentExecutor,
)



def lookup(name:str, information:str) -> str:
    llm = ChatOllama(model="llama3:latest",temperature=0)
    template = """Given the full name {name_of_person} I want you to get it me a link to their Linkedin profile page. Adittional Information about them (company etc) is {info}.
                              Rest assured, the profiles are public and not private. Your answer should contain only a URL"""

    prompt_template = PromptTemplate(
        template=template, input_variables=["name_of_person","info"]
    )
    tools_for_agent = [
        Tool(
            name="Crawl Google 4 linkedin profile page",
            func=get_linkurl_tavily,
            description="useful for when you need get the Linkedin Page URL",
        )
    ]

    react_prompt = hub.pull("hwchase17/react")
    agent = create_react_agent(llm=llm, tools=tools_for_agent, prompt=react_prompt)
    agent_executor = AgentExecutor(agent=agent, tools=tools_for_agent, verbose=True,handle_parsing_errors=True)

    result = agent_executor.invoke(
        input={"input": prompt_template.format_prompt(name_of_person=name,info=information)}
    ) 

    linked_profile_url = result["output"] 
    return linked_profile_url


if __name__ == "__main__":
    print(lookup(name="Harshil Nanda",information="Deloitte India, VIT"))
