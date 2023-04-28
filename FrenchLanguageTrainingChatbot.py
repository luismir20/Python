# pip install openai

import openai
import requests
from typing import Tuple

# Replace with your OpenAI API key
openai.api_key = "your_openai_api_key_here"

def detect_language(text: str) -> str:
    response = requests.get(f"https://translate.googleapis.com/translate_a/single?client=gtx&sl=auto&tl=en&dt=t&q={text}")
    return response.json()[2]

def translate_text(text: str, target_language: str = "fr") -> str:
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=f"Translate the following English text to {target_language}: {text}",
        temperature=0.5,
        max_tokens=100,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    return response.choices[0].text.strip()

def correct_typo(text: str) -> str:
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=f"Correct the following French text with typos: {text}",
        temperature=0.5,
        max_tokens=100,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    return response.choices[0].text.strip()

def chatbot_response(text: str) -> Tuple[str, str]:
    language = detect_language(text)
    
    if language == "en":
        translated_text = translate_text(text)
        response = correct_typo(translated_text)
    else:
        response = correct_typo(text)
    
    return response, language

while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        break
    response, language = chatbot_response(user_input)
    print(f"Bot ({language}): {response}")

# Script was made to:
# Detect the language of the input text using Google Translate API (this is a simple way to determine if the input is in English or French).
# If the input is in English, it will translate the text to French using the OpenAI API.
# Correct any typos in the French text.
# Provide a dynamic conversation by allowing you to input text in an interactive loop.
