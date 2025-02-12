from tools.tools import get_weather_tavily

from langchain.prompts.prompt import PromptTemplate
from langchain_ollama import ChatOllama
from langchain_core.tools import Tool
from langchain import hub
from langchain.agents import (
    create_react_agent,
    AgentExecutor,
)



def lookup(cityname:str) -> str:
    llm = ChatOllama(model="deepseek-r1:8b",temperature=0)
    template = "Given the city name {city}, tell me its weather. Your answer should only contain the weather."
    prompt_template=PromptTemplate(template=template, input_variables=["city"])

    tools_for_agent = [
        Tool(
            name="Search City Weather",
            func=get_weather_tavily,
            description="useful when needed to find the weather of a city",
        )
    ]

    reactprompt= hub.pull("hwchase17/react")
    #print(reactprompt.template)
    agent = create_react_agent(llm=llm, tools= tools_for_agent, prompt= reactprompt)

    agent_executor = AgentExecutor(agent=agent, tools=tools_for_agent, verbose=True)

    result= agent_executor.invoke(
        input={"input":prompt_template.format(city=cityname)}
    )

    final_result=result["output"]

    return final_result

if __name__=="__main__":
    w=lookup(cityname="Delhi")
    print(w)