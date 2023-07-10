from langchain import OpenAI, SQLDatabase, SQLDatabaseChain
import pymysql
db = SQLDatabase.from_uri("mysql+pymysql://root:rootroot@localhost:3306/fang")
openai_api_key = 'api-key'  # Remember to replace this with your new API key

llm = OpenAI(openai_api_key='api-key', temperature=0)
db_chain = SQLDatabaseChain(llm=llm, database=db, verbose=True)
db_chain.run("咳嗽、咳血、肚子疼应该用什么方治疗?")
