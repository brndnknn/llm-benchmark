from utils.runner import run_multiple_times, test_cold_start
from utils.logger import log_cold_start, init_csv
from datetime import datetime

CSV_PATH = 'data/results.csv'

def main():
    model = "gemma3:1b"
    prompts = [
        "Define artificial intelligence in one clear, concise sentence.",
        "Briefly explain artificial intelligence in one paragraph.",
        "Explain the main differences between artificial intelligence, machine learning, and deep learning. Provide a brief, clear definition of each term, and illustrate with simple examples.",
        "Provide a clear explanation of artificial intelligence, emphasizing the distinction between narrow (weak) AI and general (strong) AI. Discuss several examples of narrow AI that are commonly used in everyday technologies, such as digital assistants, recommendation systems, and image recognition. Then, briefly outline the challenges researchers face in developing general AI, explaining why it remains theoretical and has not yet been fully realized.",

    ]
    count = 5

    session_ts = datetime.now().isoformat()

    init_csv(CSV_PATH)

    for prompt in prompts:

        print(f"\n--- Cold-Start Benchmark for '{model}' ---")
        cold_time = test_cold_start(model, prompt)
        print(f"Cold start elapsed: {cold_time:.2f}s")

        log_cold_start(CSV_PATH, session_ts, model, prompt, cold_time)

        print(f"\n--- Warm_Start Repeated Runs for '{model}' ---")
        run_multiple_times(prompt, model, count, CSV_PATH)

if __name__ == "__main__":
    main()