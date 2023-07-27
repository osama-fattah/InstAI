def genImage(image_prompt):
  import openai
  openai.api_key = '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'
  response = openai.Image.create(
    prompt=image_prompt,
    n=1,
    size="1024x1024"
  )
  return(response['data'][0]['url'])