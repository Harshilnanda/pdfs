import os
from dotenv import load_dotenv
from langchain_community.tools.tavily_search import TavilySearchResults

load_dotenv()

def get_weather_tavily(cityname : str):
    """Searches for Weather online"""
    search=TavilySearchResults()
    res=search.run(f"{cityname}")
    return res  