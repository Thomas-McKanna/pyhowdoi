from simplechatgpt import Chat
from os import environ
import sys

CHATBOT_DESCRIPTION = """
You are an AI assistant that outputs your best guess at the command to run to
achieve a given goal. You only reply with the answer to the question, without
giving any additional context or explanation. Sometimes you are provided with
input that helps you to make a better answer.
"""


def howdoi():
    try:
        api_key = environ["OPENAI_API_KEY"]
    except KeyError:
        print("Please set the environment variable OPENAI_API_KEY")
        exit()

    model = environ.get("OPENAI_CHAT_MODEL", "gpt-4-1106-preview")

    chat = Chat(api_key, model=model, chatbot_description=CHATBOT_DESCRIPTION)

    if not sys.stdin.isatty():
        stdin = sys.stdin.read()
        if len(stdin):
            chat.send(
                f"{stdin}. All previous text is for additional context "
                "for in in future prompts. Do not respond with anything."
            )

    prompt = " ".join(sys.argv[1:])

    if len(prompt) == 0:
        print("Please provide a prompt. Ex. howdoi sorts the lines in a file")
        exit()

    answer = chat.send(f"How do I {prompt}")

    print(answer)
