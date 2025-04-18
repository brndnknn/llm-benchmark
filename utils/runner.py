import requests
import time

def run_multiple_times(prompt: str, model: str, count: int):
    run_times = []

    for i in range(count):
        print(f"\nRun {i+1}/{count}...")
        start = time.time()
        output = run_model(prompt, model)
        elapsed = time.time() - start
        run_times.append(elapsed)

        print(f"Response Time: {elapsed:.2f}s")
    
    avg_time = sum(run_times) / len(run_times)
    print(f"\n--- Summary for {model} ---\n")
    print(f"Average Time: {avg_time:.2f}s over {count} runs")


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