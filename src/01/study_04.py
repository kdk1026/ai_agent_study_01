from dotenv import load_dotenv
import os
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_tavily import TavilySearch


load_dotenv()

google_api_key = os.getenv('GOOGLE_API_KEY')

tool = TavilySearch(max_results=2)
tools = [tool]

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    google_api_key=google_api_key
)
llm_with_tools = llm.bind_tools(tools)

query = "안녕?"

try:
    result = llm_with_tools.invoke(query)
    if result.tool_calls:
        print("도구 호출 정보:", result.tool_calls)
    else:
        print("모델 응답 내용:", result.content)
except Exception as e:
    print(f"에러 발생: {e}")


