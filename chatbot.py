import openai
from dotenv import dotenv_values
import argparse

config = dotenv_values(".env")
openai.api_key = config["OPENAI_API_KEY"]


# helper functions to colorize the chat history:
def bold(text):
    bold_start = "\033[1m"
    bold_end = "\033[0m"
    return bold_start + text + bold_end

def blue(text):
    blue_start = "\033[34m"
    blue_end = "\033[0m"
    return blue_start + text + blue_end

def red(text):
    red_start = "\033[31m"
    red_end = "\033[0m"
    return red_start + text + red_end

# print("\033[31mHELLO\033[0m")  # "HELLO" in red


def main():
  parser = argparse.ArgumentParser(description="Simple command line chatbot")
  parser.add_argument("--personality", type=str, help="A brief summary of the chatbot's personality or its main function", default="friendly and helpful")
  args = parser.parse_args()

  # print(args.personality)  # "silly and goofy"
  initial_prompt = f"You are a conversational chatbot. Your personality is: {args.personality}."
  messages = [{"role": "system", "content": "initial_prompt"}]

  # list of messages:
  while True:
    try:
      # user's input:
      user_input = input(bold(red("User: ")))
      messages.append({"role": "user", "content": user_input})

      # assistant's response:
      res = openai.ChatCompletion.create(
          model="gpt-3.5-turbo",
          messages=[{"role": "user", "content": user_input}],
          max_tokens=200,
      )
      messages.append(res.choices[0].message.to_dict())
      print(bold(blue("Assistant: ")), res.choices[0].message.content)

      # # complete message history:
      # print("All messages: ", messages)

    except KeyboardInterrupt: # Ctrl + C
      print("Exiting ...")
      break

if __name__ == "__main__":
  main()
