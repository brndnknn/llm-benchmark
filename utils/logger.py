import csv
import os

def init_csv(csv_path: str):
    os.makedirs(os.path.dirname(csv_path), exist_ok=True)
    if not os.path.isfile(csv_path):
        with open(csv_path, "w", newline="") as f: 
            writer = csv.writer(f)
            writer.writerow([
                "session_timestamp",
                "model",
                "prompt",
                "run_index",
                "response_time_s",
                "token_count",
                "token_per_second"
            ])

def log_run(
    csv_path: str,
    session_timestamp: str,
    model: str,
    prompt: str,
    run_index: int,
    response_time: float,
    token_count: int,
    tokens_per_second: float
):
    with open(csv_path, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([
            session_timestamp,
            model,
            prompt,
            run_index + 1,
            f"{response_time:.4f}",
            token_count,
            f"{tokens_per_second:.2f}"
        ])

def log_summary(
    csv_path: str,
    session_timestamp: str,
    model: str,
    prompt: str,
    average_time: float,
    total_time: float
):
    """Append two summary rows: one for the average, one for the total."""
    with open(csv_path, "a", newline="") as f:
        writer = csv.writer(f)
        # blank out columns we don't need in summary
        writer.writerow([
            session_timestamp,
            model,
            prompt,
            "AVERAGE",
            f"{average_time:.4f}",
            "",
            ""
        ])
        writer.writerow([
            session_timestamp,
            model,
            prompt,
            "TOTAL",
            f"{total_time:.4f}",
            "",
            ""
        ])