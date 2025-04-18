from utils.runner import run_model
import time

def main():
    model = "gemma3:1b"
    prompt = "Explain the concept of gravity in one paragraph."

    print(f"Running model '{model}'...")

    start_time = time.time()
    output = run_model(prompt, model)
    elapsed = time.time() - start_time

    print("\n--- Response --- \n")
    print(output)
    print(f"\nTime taken: {elapsed:.2f} seconds")

if __name__ == "__main__":
    main()