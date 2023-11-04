import cohere 
co = cohere.Client('MB5Tg4Xti81PqzLjKC24GqCn2IAocX3NRLLVi7TE') # This is your trial API key
response = co.summarize( 
  text='{text}',
  length='auto',
  format='auto',
  model='command',
  additional_command='',
  temperature=0.3,
) 
print('Summary:', response.summary)
