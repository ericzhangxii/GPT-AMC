import os
import openai
openai.api_key = "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"
prompt = "Who was the first president of the United States?"

c = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Who won the world series in 2020?"},
        {"role": "assistant", "content": "The Los Angeles Dodgers won the World Series in 2020."},
        {"role": "user", "content": "Where was it played?"}
    ]
)

print(c)