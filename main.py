import cohere
from google.cloud import vision
from google.oauth2 import service_account

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

def detect_text_uri(uri):

    service_account_key_path = 'daring-spirit-404120-e0243e440d8a.json'
    #Initialize the Vision client
    credentials = service_account.Credentials.from_service_account_file(service_account_key_path)
    client = vision.ImageAnnotatorClient(credentials=credentials)

    """Detects text in the file located in Google Cloud Storage or on the Web."""

    client = vision.ImageAnnotatorClient()
    image = vision.Image()
    image.source.image_uri = uri

    response = client.text_detection(image=image)
    texts = response.text_annotations
    print("Texts:")

    for text in texts:
        print(f'\n"{text.description}"')

        vertices = [
            f"({vertex.x},{vertex.y})" for vertex in text.bounding_poly.vertices
        ]

        print("bounds: {}".format(",".join(vertices)))

    if response.error.message:
        raise Exception(
            "{}\nFor more info on error messages, check: "
            "https://cloud.google.com/apis/design/errors".format(response.error.message)
        )


if __name__ == '__main__':
    # Replace 'dummy text' with the converted text needed to be summarized
    pre_processed_text = "Your converted text goes here."
    
    # Call the function to summarize and print the text
    summarize_text(pre_processed_text)
