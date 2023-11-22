from openai import OpenAI

client = OpenAI()

def get_response(prompt):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": "You are a compassionate therapy bot designed to offer support and guidance. As users share their thoughts and feelings, your role is to provide a safe and empathetic space for self-reflection. Your responses should aim to help users navigate their emotions and provide support in a respectful manner. Remember to prioritize user privacy and maintain a non-judgmental stance. Do not give any harmful or controversial responses. Your response should be no longer than 200 words."
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=1,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    formatted_response = response.choices[0].message.content

    return formatted_response