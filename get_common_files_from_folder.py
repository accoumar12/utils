from pathlib import Path
import shutil


def keep_common_files(dir1, dir2, dir3, destination_directory):
    # Convert string paths to Path objects
    dir1 = Path(dir1)
    dir2 = Path(dir2)
    dir3 = Path(dir3)
    destination_directory = Path(destination_directory)

    ids_1 = {file.name.split(".")[0]: file for file in dir1.iterdir() if file.is_file()}
    ids_2 = {file.name.split(".")[0]: file for file in dir2.iterdir() if file.is_file()}
    ids_3 = {file.name.split(".")[0]: file for file in dir3.iterdir() if file.is_file()}

    # Find the common files
    common_keys = set(ids_1.keys()) & set(ids_2.keys()) & set(ids_3.keys())

    destination_directory.mkdir(parents=True, exist_ok=True)

    # Copy the common files to the destination directory
    for key in common_keys:
        shutil.copy(ids_3[key], destination_directory)


def main() -> None:
    dir1 = "/home/maccou/Bureau/stage-maccou/data/airbus/imgs"
    dir2 = "/home/maccou/Bureau/stage-maccou/data/airbus/imgs_can"
    dir3 = "/home/maccou/Bureau/stage-maccou/data/airbus/stl"
    destination_directory = "/home/maccou/Bureau/stage-maccou/data/airbus/stls"
    keep_common_files(dir1, dir2, dir3, destination_directory)


if __name__ == "__main__":
    main()
