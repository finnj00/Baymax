from openai import OpenAI

client = OpenAI()

# Function for sending a request to the OpenAI API and returns the ChatGPT output
def openAI_api_request(messages, model="gpt-3.5-turbo"):

    response = client.chat.completions.create(
        model=model,
        messages=messages,
        max_tokens=100, # upper bound on max length of ChatGPT's response
        n=1,
        stop=None,
        temperature=0.5
    )

    message = response.choices[0].message.content
    messages.append(response.choices[0].message)
    
    # temp
    print(message)
    return message