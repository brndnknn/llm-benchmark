from utils.runner import run_multiple_times
import time

def main():
    model = "gemma3:1b"
    #4b-it-q8_0"
    prompt = "Explain the concept of gravity in one paragraph."
    count = 5

    print(f"Running model '{model}'...")

    start_time = time.time()
    run_multiple_times(prompt, model, count)
    elapsed = time.time() - start_time


    print(f"\nTotal time taken: {elapsed:.2f} seconds")

if __name__ == "__main__":
    main()