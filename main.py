import cohere

def summarize_text(text):
    # Initialize the Cohere client with your API key
    co = cohere.Client('MB5Tg4Xti81PqzLjKC24GqCn2IAocX3NRLLVi7TE')  # This is your trial API key

    # Use f-strings for string formatting
    response = co.summarize(
        text=text,
        length='auto',
        format='auto',
        model='command',
        additional_command='',
        temperature=0.3,
    )

    # Print the summarized text
    print('Summary:', response.summary)

if __name__ == '__main__':
    # Replace 'dummy text' with the converted text needed to be summarized
    pre_processed_text = "Your converted text goes here."
    
    # Call the function to summarize and print the text
    summarize_text(pre_processed_text)
