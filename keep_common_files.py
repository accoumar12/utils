from __future__ import annotations

import shutil
from pathlib import Path
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    import os


def find_common_ids(
    directories: list[str | os.PathLike],
) -> set[str]:
    directories = [Path(dir) for dir in directories]

    # Create a list of dictionaries, each containing the file IDs in one directory
    ids_list = [
        {file.name.split(".")[0]: file for file in dir.iterdir() if file.is_file()}
        for dir in directories
    ]

    for i, ids in enumerate(ids_list, start=1):
        print(f"Found {len(ids)} files in directory {i}")

    # Find the common files
    common_keys = set.intersection(*[set(ids.keys()) for ids in ids_list])
    print(f"Found {len(common_keys)} common files")

    common_files = {key: ids_list[0][key] for key in common_keys}

    return common_keys, common_files


def move_common_files(
    directories: list[str | os.PathLike],
    destination_directory: str | os.PathLike,
) -> None:
    directories = [Path(dir) for dir in directories]
    destination_directory = Path(destination_directory)

    common_keys, common_files = find_common_ids(directories)

    # Retrieve in a csv file the missing ids
    # missing_ids = set(common_keys[0].keys()) - common_keys
    # print(f"Found {len(missing_ids)} missing files")

    # with open(destination_directory / "missing_ids.csv", "w") as f:
    #     writer = csv.writer(f)
    #     for id in missing_ids:
    #         writer.writerow([id])
    destination_directory.mkdir(parents=True, exist_ok=True)

    # Copy the common files to the destination directory
    for key, file_path in common_files.items():
        shutil.copy(file_path, destination_directory)


def keep_common_files(directories: list[str | os.PathLike]) -> None:
    directories = [Path(dir) for dir in directories]
    common_keys = find_common_ids(directories)
    for dir in directories:
        for file in dir.iterdir():
            if file.is_file() and file.name.split(".")[0] not in common_keys:
                file.unlink()


def main() -> None:
    directories = [
        "/home/share/deep-mesh/database/airbus/stl_brep_low",
        "/home/maccou/Bureau/stage-maccou/data/mv/old/stl_old_mesher",
    ]

    destination_directory = "/home/maccou/Bureau/stage-maccou/data/mv/stl"
    # find_common_ids(directories)
    move_common_files(directories, destination_directory)
    # keep_common_files(directories)


if __name__ == "__main__":
    main()
