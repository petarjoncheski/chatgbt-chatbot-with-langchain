import os
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv(),override=True)

# print(os.environ.get("OPENAI_API_KEY")) #print the OPENAI_API_KEY

from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(model_name = 'gpt-3.5-turbo', temperature = 1)

prompt = ChatPromptTemplate.from_template("You are a chatbot having a conversation with a human about the following {content}")

chain = prompt | llm | StrOutputParser()

while True:
    content = input('Your prompt ')
    if content.lower() in ['quit', 'exit', 'bye']:
        print('Goodbye!')
        break
    response = chain.invoke({"content":content})
    print(response)
    print('-' * 50)







