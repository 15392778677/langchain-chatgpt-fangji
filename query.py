import json

from langchain import OpenAI, SQLDatabase, SQLDatabaseChain
import pymysql
def process_query(query_string):
    # 连接到MySQL数据库
    db = SQLDatabase.from_uri("mysql+pymysql://root:rootroot@localhost:3306/fang")

    # 指定OpenAI API密钥
    openai_api_key = 'api-key'

    # 创建OpenAI实例
    openai = OpenAI(openai_api_key=openai_api_key, temperature=0)

    # 创建SQLDatabaseChain实例
    db_chain = SQLDatabaseChain(llm=openai, database=db, verbose=True)

    # 处理查询
    result = db_chain.run(query_string)
    # 返回结果
    return result

while(1):
    user_input = input("请输入一段话: ")
    if(user_input=="q"):
        break
    print(process_query(user_input))




