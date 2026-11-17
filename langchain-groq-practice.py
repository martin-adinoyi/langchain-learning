"""
This is a simple example of a multi-turn chat application using the LangChain Groq integration.

For more information on the software engineer behind this project, please visit: https://www.linkedin.com/in/martin-adinoyi
"""

import os
from langchain_core.messages import HumanMessage

from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

from dotenv import load_dotenv
from langchain_groq import ChatGroq

load_dotenv()

groq_api_key = os.getenv("GROQ_API_KEY")

if not groq_api_key:
    raise RuntimeError("GROQ_API_KEY was not found.")


# Instantiate/create the chat model object.
chat_model = ChatGroq(model="openai/gpt-oss-20b", temperature=0.2, api_key=groq_api_key)

# The sequence of messages that should be sent on every turn.
prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "You are Martosky AI, talk like a psychologist. Don't say more than 3 statement, and one statement should not be up to 10 words and there should be no big grammer words. Be simple like you are talking to a 10year old",
        ),
        MessagesPlaceholder(
            variable_name="history"
        ),  # Insert previous user and assistand messages to give the model context.
        (
            "human",
            "{input}",
        ),  # Insert the currnt user message at the end of the prompt.
    ]
)

chat_chain = (
    prompt | chat_model
)  # The pipe operator connects prompt formatting to the model call.

# Keep conversation messages in a Python list while this program is running.
# In-memory chat history for this session. It is cleared when the program exits.
history = []


# Repeatedly ask for input so the user can have a multi-turn conversation.
while True:
    user_input = input("You: ")

    # Let the user end the loop by typing either command.
    if user_input.lower() in ["exit", "quit"]:
        print("Exiting the chat. Goodbye!")
        break

    # Ignore blank input instead of sending an empty request to the model.
    if not user_input.strip():
        continue

    # Run the prompt and model with the current user input and the chat history.

    response = chat_chain.invoke(
        {
            # Supply text for the {input} placeholder in the prompt.
            "input": user_input,
            # Supply earlier turns for the MessagesPlaceholder in the prompt.
            "history": history,
        }
    )

    response = chat_chain.invoke({"input": user_input, "history": history})

    print(f"Martosky AI: {response.content}")

    history.append(HumanMessage(content=user_input))
    history.append(response)
