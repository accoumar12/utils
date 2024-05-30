import csv
import itertools

def read_interval_from_csv(file_path: str, start: int, end: int) -> list:
    with open(file_path, 'r') as f:
        reader = csv.reader(f)
        header = next(reader)  
        # We use itertools.islice to skip the first `start - 1` rows
        rows = list(itertools.islice(reader, start - 2, end - 1))  # adjust the indices because we've already read one line
    return [header] + rows  

def write_rows_to_csv(file_path: str, rows: list) -> None:
    with open(file_path, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(rows)

def main() -> None:
    input_file_path = '/home/maccou/Bureau/stage-maccou/data/labelizer_data/to_upload_data/old/data/triplets.csv'  
    output_file_path = '/home/maccou/Bureau/stage-maccou/data/labelizer_data/to_upload_data/old/data/triplets_new.csv'
    start = 4000
    end = 7000 

    interval_rows = read_interval_from_csv(input_file_path, start, end)
    write_rows_to_csv(output_file_path, interval_rows)

if __name__ == "__main__":
    main()