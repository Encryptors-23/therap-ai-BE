from openai import OpenAI

client = OpenAI()

def test_response(prompt):
    print(f"Prompt: {prompt}")

    response = {
    "response": "It sounds like you're feeling overwhelmed with the amount of homework you have and the limited time you have to complete it. School-related anxiety is a common issue, and it's important to remember that you're not alone in feeling this way. Here are a few strategies that may help:\n\n1. Prioritize: Break down your tasks into smaller, manageable chunks. Prioritize your assignments based on their due dates and importance.\n\n2. Time management: Create a schedule or use a planner to allocate specific time slots for each task. This can help you stay organized and ensure you're making progress on each assignment.\n\n3. Reach out for support: Don't hesitate to seek help and support from your teachers, classmates, or even a school counselor. They may be able to provide guidance or extra resources to assist you.\n\n4. Take breaks: It's essential to take regular breaks to recharge and avoid burnout. Engaging in activities you enjoy during these breaks can help reduce stress and improve focus when you return to your work.\n\nRemember, it's also important to maintain a healthy work-life balance. Be kind to yourself and practice self-care. You got this!"
    }
    
    return response

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