from openai import OpenAI

client = OpenAI()

# Function for sending a request to the OpenAI API and returns the ChatGPT output
def openAI_api_request(messages, model="gpt-4o-2024-05-13"): # October 2023 knowledge cutoff

    response = client.chat.completions.create(
        model=model,
        messages=messages,
        max_tokens=60, # upper bound on max length of ChatGPT's response
        n=1,
        stop=None,
        temperature=0.5
    )

    message = response.choices[0].message.content
    messages.append(response.choices[0].message)
    
    print(message)
    return message