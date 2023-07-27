def genCaption(prompt):
  import openai
  openai.api_key = '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'
  messages=[{"role": "system", "content": "keep the conversation respectful and non controvertial"},{"role": "user", "content": prompt}]
  completion = openai.ChatCompletion.create(model="gpt-3.5-turbo",messages=messages)
  return(str(completion.choices[0].message["content"]))