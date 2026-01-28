from dotenv import load_dotenv
import os

from .study_tool import tools
from langchain_google_genai import ChatGoogleGenerativeAI


load_dotenv()

# OPENAI는 무조건 충전해야 해서 제미나이로 변경
google_api_key = os.getenv('GOOGLE_API_KEY')

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    google_api_key=google_api_key
)
llm_with_tools = llm.bind_tools(tools)

query = "What is 3 * 12? Also, what is 11 + 49?"
# query = "What is 12 % 2?"

try:
    result = llm_with_tools.invoke(query)
    if result.tool_calls:
        print("도구 호출 정보:", result.tool_calls)
    else:
        print("모델 응답 내용:", result.content)
except Exception as e:
    print(f"에러 발생: {e}")


