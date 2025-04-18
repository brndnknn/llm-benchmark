from utils.runner import run_multiple_times
import time

CSV_PATH = 'data/results.csv'

def main():
    model = "gemma3:1b"
    prompt = "Explain the concept of gravity in one paragraph."
    count = 5

    print(f"Running model '{model}'...")


    run_multiple_times(prompt, model, count, CSV_PATH)

if __name__ == "__main__":
    main()