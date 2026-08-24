import os
from dotenv import load_dotenv
from langchain_core.tools import tool
from langchain_openai import ChatOpenAI


@tool
def tools1() -> str:
    """获取今天的天气情况"""
    return "今天天气真好"


load_dotenv()
llm = ChatOpenAI(
    model="deepseek-v4-flash",
    api_key=os.getenv("DEEPSEEK_API_KEY"),
    base_url=os.getenv("DEEPSEEK_BASE_URL"),
)
tool_bind_llm= llm.bind_tools([tools1])
responce1= tool_bind_llm.invoke("北京天气怎么样")
print(responce1)
print(type(responce1))
print("***--"*10)
responce2=llm.invoke("你好")
print(responce2)
print(type(responce2))