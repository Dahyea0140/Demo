from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI
from langchain.tools import tool
from langgraph.prebuilt import create_react_agent
from dotenv import load_dotenv
import os

load_dotenv()
print("DEBUG: API KEY =", os.getenv("OPENAI_API_KEY"))


@tool
def calculator(a: float, b: float) -> str:
    """Useful for performing basic arithmatic calculations with numbers"""
    print("Tool has been called.")
    return f"The sum of {a} and {b} is {a + b}"


def main():
    model = ChatOpenAI(temperature=0)

    # Tools for the model like calculator or somthing """
    tools = [calculator]
    # creat-react_agent is a prebuilt aggent
    # that automatically handels by taking somekind of model and tool and how to use it
    agent_executor = create_react_agent(model, tools)

    print("Welcome!I'm an AI.Type 'quit' to exit.")
    print("You can ask me to perform a task. Or simply you can chat with me.")

    while True:
        user_input = input("\nYou: ").strip()

        if user_input == "quit":
            break

        print("\n Assistant: ", end="")
        for chunk in agent_executor.stream(
            {"messages": [HumanMessage(content=user_input)]}
        ):
            if "agent" in chunk and "messages" in chunk["agent"]:
                for message in chunk["agent"]["messages"]:
                    print(message.content, end="")
        print()


if __name__ == "__main__":
    main()
