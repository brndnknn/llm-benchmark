import requests
import time
import subprocess
from datetime import datetime
from utils.tokenizer import count_tokens
from utils.logger import init_csv, log_run, log_summary


def test_cold_start(model: str, prompt: str) -> float:
    """
    Measures cold-start time: stops Ollama, then runs the model from scratch. Returns elapsed seconds.
    """

    # Stops Ollama server
    subprocess.run(["ollama", "stop"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    # Time the cold start load + generate
    start = time.time()
    _ = run_model(prompt, model)
    
    return time.time() - start



def run_multiple_times(prompt: str, model: str, count: int, csv_path: str):
    run_times = []
    session_ts = datetime.now().isoformat()

    for i in range(count):
        print(f"\nRun {i+1}/{count}...")
        start = time.time()
        output = run_model(prompt, model)
        elapsed = time.time() - start
        run_times.append(elapsed)
        tokens = count_tokens(output)
        tok_per_sec = tokens / elapsed

        print(f"Response Time: {elapsed:.2f}s")
        print(f"{tokens} tokens in {elapsed:.2f}s -> {tok_per_sec:.1f} tok/s")
        log_run(csv_path, model, prompt, i, elapsed, tokens, tok_per_sec)
    
    total_time = sum(run_times)
    avg_time = total_time / len(run_times)

    print(f"\nSession Summary for {model} @ {session_ts}:")
    print(f"   - Average run: {avg_time:.2f}s")
    print(f"   - Total time:  {total_time:.2f}s")

    log_summary(csv_path, model, prompt, avg_time, total_time)


def run_model(prompt: str, model: str) -> str:
    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": model,
            "prompt": prompt,
            "stream": False
        }, 
        timeout=180
    )

    response.raise_for_status()
    return response.json()["response"]

