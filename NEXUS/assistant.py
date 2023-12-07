import json
from openai import OpenAI


try:
    with open("secrets.json") as f:
        secrets = json.load(f)
        api_key = secrets["api_key"]
    client = OpenAI(api_key=api_key)
except FileNotFoundError:
    print("The file 'secrets.json' was not found.")
except KeyError:
    print("The 'api_key' was not found in 'secrets.json'.")


def get_chat_response(messages: list[dict]):
    response = client.chat.completions.create(
        model = "gpt-4", # or "gpt-3.5-turbo"
        messages=messages,
        temperature = 1.0 # 0.0 - 2.0
    )
    return response.choices[0].message


if __name__ == "__main__":
    assistant_name = "Joi"
    messages = [
        {
            "role": "system", 
            "content": f"Sei un assistente virtuale chiamata {assistant_name} e parli italiano."
        }
    ]
    try:
        while True:
            user_input = input("\nTu: ")
            messages.append({"role": "user", "content": user_input})
            new_message = get_chat_response(messages=messages)
            print(f"\n{assistant_name}: {new_message.content}")
            messages.append(new_message)
    except KeyboardInterrupt:
        print("A presto!")