import requests

def run_model(prompt: str, model: str) -> str:
    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": model,
            "prompt": prompt,
            "stream": False
        }, 
        timeout=60
    )

    response.raise_for_status()
    return response.json()["response"]