import os
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv(),override=True)

# print(os.environ.get("OPENAI_API_KEY")) #print the OPENAI_API_KEY

from langchain_core.prompts import ChatPromptTemplate, HumanMessagePromptTemplate, MessagesPlaceholder
from langchain_openai import ChatOpenAI
from langchain.globals import set_verbose # to remove the warning in console

set_verbose(False) # uncomment to see what is happening in the background

from langchain_core.messages import SystemMessage
from langchain.memory import ConversationBufferMemory
from langchain_community.chat_message_histories import FileChatMessageHistory

history = FileChatMessageHistory('.chat_history.json')

memory: ConversationBufferMemory = ConversationBufferMemory(
    memory_key='chat_history',
    chat_memory=history,
    return_messages=True
)

llm = ChatOpenAI(model_name = 'gpt-3.5-turbo', temperature = 1)

prompt = ChatPromptTemplate(
    input_variables = ['content'],
    messages = [
        SystemMessage(content = 'You are a chatbot having a conversation with a human.'),
        MessagesPlaceholder(variable_name = 'chat_history'), #Where the memory will be stored
        HumanMessagePromptTemplate.from_template('{content}')
    ]
)
sequence = prompt | llm

while True:
    content = input('Your prompt ')
    if content.lower() in ['quit', 'exit', 'bye']:
        print('Goodbye!')
        break
        # Get the chat history from memory
    chat_history = memory.load_memory_variables({})['chat_history']

    # Run the sequence
    response = sequence.invoke({
        "content": content,
        "chat_history": chat_history
    })

    # Update the memory with the new input and response
    memory.save_context({"content": content}, {"content": response.content})

    print(response.content)
    print('-' * 50)







