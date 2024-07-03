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


def keep_csv_lines_by_index(file_path: str, indices: list) -> list:
    with Path(file_path).open() as f:
        reader = csv.reader(f)
        header = next(reader)
        rows = [row for i, row in enumerate(reader) if i in indices]
    return [header, *rows]


def write_rows_to_csv(file_path: str, rows: list) -> None:
    with Path(file_path).open("w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(rows)


def main() -> None:
    input_file_path = "/home/maccou/stage_maccou/deep_mesh/models/find_triplets/20240703-0934/20240703-0934_results_labelizer_data_0.001_0.06_0.5_0.1.csv"
    output_file_path = "/home/maccou/stage_maccou/deep_mesh/models/find_triplets/20240703-0934/filtered_results.csv"
    start = 4000
    end = 7000

    # Keep only the columns "anchor" and "negative"

    # interval_rows = keep_csv_lines_interval(input_file_path, start, end)
    kept_indices = [
        19,
        34,
        71,
        76,
        87,
        163,
        166,
        179,
        261,
        310,
        353,
        474,
        493,
        572,
        609,
        643,
        754,
        783,
        880,
    ]
    rows = keep_csv_lines_by_index(input_file_path, kept_indices)

    write_rows_to_csv(output_file_path, rows)


if __name__ == "__main__":
    main()
