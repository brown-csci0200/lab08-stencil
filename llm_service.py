import requests
import json

BROWN_LLM_URL = "http://llmserver:37090"
MODEL_NAME = "meta-llama/Meta-Llama-3.1-8B-Instruct"
CHAT_COMPLETIONS_ENDPOINT = "v1/chat/completions"

def get_chat_completion(messages):
    url = f"{BROWN_LLM_URL}/{CHAT_COMPLETIONS_ENDPOINT}"
    response = requests.post(url, json={
        "messages": messages,
        "model": MODEL_NAME
        })

    if response.status_code != 200:
        return response.text
    return response.json()

def get_date_conversion_messages(msg):
    return [
        {
            "role": "user",
            "content": msg,
        },
    ]

def extract_chat_completion_answer(response_json):
    return response_json["choices"][0]["message"]["content"]

def ask_llm(prompt):
    messages = get_date_conversion_messages(prompt)
    raw_response = get_chat_completion(messages)
    response = extract_chat_completion_answer(raw_response)
    return response

#if __name__ == "__main__":
#    print(convert_date("September 3rd"))
#Collapse












