from utils.runner import run_multiple_times, test_cold_start
from utils.logger import log_cold_start, init_csv
from datetime import datetime

CSV_PATH = 'data/results.csv'

def main():
    model = "gemma3:1b"
    prompt = "Explain the concept of gravity in one paragraph."
    count = 5

    session_ts = datetime.now().isoformat()

    init_csv(CSV_PATH)

    print(f"\n--- Cold-Start Benchmark for '{model}' ---")
    cold_time = test_cold_start(model, prompt)
    print(f"Cold start elapsed: {cold_time:.2f}s")

    log_cold_start(CSV_PATH, session_ts, model, prompt, cold_time)

    print(f"\n--- Warm_Start Repeated Runs for '{model}' ---")
    run_multiple_times(prompt, model, count, CSV_PATH)

if __name__ == "__main__":
    main()