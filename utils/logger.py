import csv
import os

def init_csv(csv_path: str):
    os.makedirs(os.path.dirname(csv_path), exist_ok=True)
    if not os.path.isfile(csv_path):
        with open(csv_path, "w", newline="") as f: 
            writer = csv.writer(f)
            writer.writerow([
                "model",
                "prompt",
                "run_index",
                "response_time_s",
                "token_count",
                "token_per_second"
            ])

def append(csv_path: str, row: list[str]):
    with open(csv_path, "a", newline="") as f:
        csv.writer(f).writerow(row)

def log_cold_start(
        csv_path: str,
        model: str,
        prompt: str,
        cold_start_time: float
):
    """
    Append a row indicating the cold-start time for a session.
    """
    append(csv_path, [model, prompt, "COLD_START", f"{cold_start_time:.4f}"])

def log_run(
    csv_path: str,
    model: str,
    prompt: str,
    run_index: int,
    response_time: float,
    token_count: int,
    tokens_per_second: float
):
    append(csv_path, [
            model,
            prompt,
            run_index + 1,
            f"{response_time:.4f}",
            token_count,
            f"{tokens_per_second:.2f}"
        ])

def log_summary(
    csv_path: str,
    model: str,
    prompt: str,
    average_time: float,
    total_time: float
):
    """Append two summary rows: one for the average, one for the total."""
    append(csv_path, [
            model,
            prompt,
            "AVERAGE",
            f"{average_time:.4f}",
        ])
    append(csv_path, [
            model,
            prompt,
            "TOTAL",
            f"{total_time:.4f}",
        ])