import requests

API_KEY = 'sk-d2Z3OKasaE2bNbH7U2kCadmpGrdOJOI095dBgRGtoYPHivzq'

def call_model(messages, model="minimax-m2.5", temperature=0.7, stream=False):
    url = "https://tokenhub.tencentmaas.com/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    data = {
        "model": model,
        "messages": messages,
        "temperature": temperature,
        "stream": stream
    }
    response = requests.post(url, headers=headers, json=data)
    return response.json()
