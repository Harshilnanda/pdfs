import sys
import os

# Add the root directory to sys.path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Now you can use absolute imports
from tools.tools import get_linkurl_tavily, web_query
from langchain.prompts.prompt import PromptTemplate
from langchain_ollama import ChatOllama
from langchain_core.tools import Tool
from langchain import hub
from langchain_core.output_parsers import StrOutputParser
from langchain.agents import (
    create_react_agent,
    AgentExecutor,
)



def lookup(topic:str) -> str:
    llm = ChatOllama(model="llama3:latest",temperature=0)
    template = """Adhere to the format of answer given earileir.Given the question {topic_name}, answer it by browsing the internet. 
                    Your Answer should only contain the answer relevant to question and nothing else. No extra infomation is needed."""

    prompt_template = PromptTemplate(
        template=template, input_variables=["topic_name"]
    )
    tools_for_agent = [
        Tool(
            name="Crawl Google 4 for information on the topic",
            func=web_query,
            description="useful for when you need get information not provided to you or requires browsing the internet",
        )
    ]

    react_prompt = hub.pull("hwchase17/react")
    agent = create_react_agent(llm=llm, tools=tools_for_agent, prompt=react_prompt)
    agent_executor = AgentExecutor(agent=agent, tools=tools_for_agent, verbose=True,handle_parsing_errors=True)

    result = agent_executor.invoke(
        input={"input": prompt_template.format_prompt(topic_name=topic)}
    ) 

    res = result["output"] 
    return res


if __name__ == "__main__":
    print(lookup(topic="Who performed at halftime in superbowl 2025?"))
