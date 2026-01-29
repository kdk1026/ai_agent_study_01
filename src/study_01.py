from dotenv import load_dotenv
import os
from tavily import TavilyClient

load_dotenv()

_TAVILY_API_KEY = os.environ.get('TAVILY_API_KEY')
import os

tavily_client = TavilyClient(api_key=_TAVILY_API_KEY)

_QUERY = "AI Agent가 뭐야?"

response = tavily_client.search(_QUERY, max_results=3) # , topic="news", days = 10
print(response) # return dict, 웹 검색 전체

print(' ')

context = tavily_client.get_search_context(query=_QUERY)
decode_context = context.encode('utf-8').decode('unicode_escape')
print(decode_context)   # reutrn str, 웹 검색 결과만

print(' ')

answer = tavily_client.qna_search(query=_QUERY)
print(answer)   # return str, 간단한 답변, 영어로 나옴