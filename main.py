import openai
import os

openai.api_key = os.environ['API_KEY']
name = input("Who do you want to talk with?\n")

messages = [
  {
    "role": "user",
    "content": "Pretend as if you are {}. Do not reveal your identity or say the words {}. Do not reference you are an AI.".format(name, name)
  },
]

while(True):
  prompt = input("\nWhat do you want to ask {}? Type q to break\n".format(name))
  
  if(prompt == 'q'):
    break;

  messages.append({
    "role": "user",
    "content": prompt
  })
  
  completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages)

  response = completion['choices'][0]["message"]["content"]

  print(response)

  messages.append(
    {
      "role": "assistant",
      "content": response
    }
  )
