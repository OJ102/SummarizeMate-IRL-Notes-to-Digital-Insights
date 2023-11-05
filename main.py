import cohere
from google.cloud import vision
from google.oauth2 import service_account

def summarize_text(text):
    # Initialize the Cohere client with your API key
    co = cohere.Client('MB5Tg4Xti81PqzLjKC24GqCn2IAocX3NRLLVi7TE')  # This is your trial API key

    # Use f-strings for string formatting
    try:    
        response = co.summarize(
            text=text,
            length='auto',
            format='auto',
            model='command',
            additional_command='',
            temperature=0.3,
        )
    except cohere.error.CohereAPIError as e:
        ERROR_MESSAGE="Error: invalid request - text must be longer than 250 characters"
        print(ERROR_MESSAGE)
        return ERROR_MESSAGE

    # Print the summarized text
    print('Summary:', response.summary)

def detect_text_uri(uri):

    service_account_key_path = 'daring-spirit-404120-e0243e440d8a.json'
    #Initialize the Vision client
    credentials = service_account.Credentials.from_service_account_file(service_account_key_path)
    client = vision.ImageAnnotatorClient(credentials=credentials)

    """Detects text in the file located in Google Cloud Storage or on the Web."""
    image = vision.Image()
    image.source.image_uri = uri

    response = client.text_detection(image=image)
    texts = response.text_annotations
    print("Texts:")
    
    #optimize this part
    i=0
    for text in texts:
        if i==1:
            break
        print(f'\n"{text.description}"')
        result=text.description
        return result
        i+=1

    if response.error.message:
        raise Exception(
            "{}\nFor more info on error messages, check: "
            "https://cloud.google.com/apis/design/errors".format(response.error.message)
        )


if __name__ == '__main__':
    
    # Enter your URI under here
    uri="https://marcellapurnama.files.wordpress.com/2011/10/scan-4.jpg"

    # Replace 'dummy text' with the converted text needed to be summarized
    pre_processed_text=detect_text_uri(uri)
    
    # Output read file
    print(pre_processed_text)
    print(type(pre_processed_text))
    # Call the function to summarize and print the text
    summarize_text(pre_processed_text)