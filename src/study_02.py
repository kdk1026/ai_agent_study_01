from dotenv import load_dotenv
import os
import json
from langchain_tavily import TavilySearch

load_dotenv()

_TAVILY_API_KEY = os.environ.get('TAVILY_API_KEY')
os.environ["TAVILY_API_KEY"] = _TAVILY_API_KEY

_QUERY = "LangGraph가 뭐야?"

tool = TavilySearch(max_results=2)
results = tool.invoke(_QUERY)

print(json.dumps(results, indent=2, ensure_ascii=False))