from flask import Flask, request, jsonify
from langchain import OpenAI, SQLDatabase, SQLDatabaseChain
import json
import pymysql

# Create Flask app
app = Flask(__name__)

# Specify OpenAI API key
openai_api_key = 'api-key'

# Create OpenAI instance
openai = OpenAI(openai_api_key=openai_api_key, temperature=0)

# Connect to MySQL database
db = SQLDatabase.from_uri("mysql+pymysql://root:rootroot@localhost:3306/fang")

# Create SQLDatabaseChain instance
db_chain = SQLDatabaseChain(llm=openai, database=db, verbose=True)


# Define API route and request method
@app.route('/query', methods=['POST'])
def process_query():
    # Get query string from request body
    query_string = request.json.get('query')

    # Check if the query is medical related
    if '中医药' not in query_string and '治疗' not in query_string and '成分' not in query_string:
        response = {
            'message': '这个API只能处理与传统中药、治疗方法和中药成分相关的查询。'
        }
        return jsonify(response)

    # Process the query
    result = db_chain.run(query_string)

    # Return the response as JSON
    return result


if __name__ == '__main__':
    # Run the Flask app on localhost:5000
    app.run()