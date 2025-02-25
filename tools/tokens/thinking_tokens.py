#from together import Together
#client = Together(api_key = TOGETHER_API_KEY) # Replace with whichever API you are using
client = InferenceClient("model_name")
question = "Ask question here"

output = client.chat.completions.create(
  messages=[{"role": "user", "content": question}],
  stop = ['</think>']
)

PROMPT_TEMPLATE = """
Thought process: {thinking_tokens} </think>
Question: {question}
Answer:
"""
"""
answer = client.chat.completions.create(
  model="meta-llama/Meta-Llama-3.1-8B-Instruct-Turbo",
  messages=[{"role": "user", 
             "content": PROMPT_TEMPLATE.format(thinking_tokens=thought.choices[0].message.content, question = question) }],
)
"""
# Grab the thinking tokens
print(output.choices[0].message.content)