import openai
from dotenv import dotenv_values


config = dotenv_values(".env")
openai.api_key = config["OPENAI_API_KEY"]

messages = []

while True:
  try:
    # user's input:
    user_input = input("User: ")
    messages.append({"role": "user", "content": user_input})

    # assistant's response:
    res = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": user_input}],
        max_tokens=200,
    )
    messages.append(res.choices[0].message.to_dict())
    print("Assistant: ", res.choices[0].message.content)

    # # complete message history:
    # print("All messages: ", messages)

  except KeyboardInterrupt: # Ctrl + C
    print("Exiting ...")
    break
