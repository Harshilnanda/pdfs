import os
from dotenv import load_dotenv
from langchain_community.tools.tavily_search import TavilySearchResults
import requests
import trafilatura
from googlesearch import search

def get_webpage_content(url):
    try:
        downloaded = trafilatura.fetch_url(url)
        if downloaded:
            extracted_text = trafilatura.extract(downloaded)
            return extracted_text[:5000] if extracted_text else "No readable content found"
        else:
            return "Failed to fetch content"
    except Exception as e:
        return f"Error fetching {url}: {str(e)}"

# Example: Get top 5 search results for "AI"



load_dotenv()

def get_linkurl_tavily(name : str):
    #"""Searches for Linkedin or Twitter Profile Page."""
    #search = TavilySearchResults()
    #res = search.run(f"{name+"LinkedIn"}")
    #return res
    return """[{'url': 'https://in.linkedin.com/in/harshil-nanda', 'content': 'Harshil Nanda\nOracle Analyst Intern @ Deloitte India || Generative AI - LLMs - LangChain - AI/ML\nChennai, India\n118 connections, 122 followers\n\n\nAbout:\nHighly motivated and eager to learn 20 y/o studying at Vellore Institute of Technology, Vellore. Coming from a Defence Background, I possess qualities such as Socialability, Adaptability, Teamwork,etc. Worked as an Intern in Tata Consulatancy Services, Chennai on Gen AI capabilities.\n\n\nExperience:\nOracle Analyst Intern at Deloitte (https://www.linkedin.com/company/deloitte)\nJan 2025 - Present\nChennai, Tamil Nadu, India\n\n\nEducation:\nVellore Institute of Technology\nBachelor of Technology - BTech, Computer Science\nJan 2021 - Dec 2025\nGrade: N/A\nActivities and societies: N/A'}, {'url': 'https://www.linkedin.com/in/harshilchahal', 'content': "Harshil Chahal - Instacart - University of Minnesota - Carlson School of Management - About - Key Transactions: General Mills' acquisition of Blue Buffalo ($8B)"}]"""

def web_query(query:str):
    nums = 1
    urls = list(search(query,num_results=nums))
    print(urls)
    # Extract text from each URL
    dic=[]
    for url in urls:
        print(f"\nExtracting content from: {url}")
        content = get_webpage_content(url)
        dic.append(content)
        print(content[:300], "\n...")
    return dic

#print(get_linkurl_tavily("Harshil Nanda VIT"))