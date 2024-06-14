import csv
import itertools
from pathlib import Path


def keep_csv_lines_interval(file_path: str, start: int, end: int) -> list:
    with Path(file_path).open() as f:
        reader = csv.reader(f)
        header = next(reader)
        # We use itertools.islice to skip the first `start - 1` rows
        rows = list(
            itertools.islice(reader, start - 2, end - 1),
        )  # adjust the indices because we've already read one line
    return [header, *rows]


def keep_csv_columns(file_path: str, kept_columns: list) -> list:
    with Path(file_path).open() as f:
        reader = csv.reader(f)
        header = next(reader)
        indices = [header.index(column) for column in kept_columns]
        new_header = [header[i] for i in indices]  # Adjusted header
        rows = [[row[i] for i in indices] for row in reader]
    return [new_header, *rows]  # Return new_header instead of header


def write_rows_to_csv(file_path: str, rows: list) -> None:
    with Path(file_path).open("w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(rows)


def main() -> None:
    input_file_path = "/home/maccou/Bureau/stage-maccou/data/mv_custom_2/triplets.csv"
    output_file_path = (
        "/home/maccou/Bureau/stage-maccou/data/mv_custom_2/triplets_new.csv"
    )
    start = 4000
    end = 7000

    # Keep only the columns "anchor" and "negative"
    kept_columns = ["anchor", "negative"]
    columns = keep_csv_columns(input_file_path, kept_columns)
    write_rows_to_csv(output_file_path, columns)

    # interval_rows = keep_csv_lines_interval(input_file_path, start, end)
    # write_rows_to_csv(output_file_path, interval_rows)


if __name__ == "__main__":
    main()
