import requests

url = "http://localhost:8001/chat/completions/stream"

payload = {
    "repo_url": "https://github.com/TheoDaimonn/Yandex-multimodal-assistant",
    "messages": [
        {
            "role": "user",
            "content": "Расскажи о репозитории Yandex-multimodal-assistant. Какие у него основные функции и возможности? Как он работает? Какие технологии использует? Как его установить и запустить? Есть ли примеры использования?"
        }
    ]
}

# Make streaming request
response = requests.post(url, json=payload, stream=True)

# Process the streaming response
for chunk in response.iter_content(chunk_size=None):
    if chunk:
        print(chunk.decode('utf-8'), end='', flush=True)