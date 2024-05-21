from __future__ import annotations

import shutil
from pathlib import Path
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    import os


def find_common_files(
    dir1: str | os.PathLike,
    dir2: str | os.PathLike,
) -> set[str]:
    # Convert string paths to Path objects
    dir1 = Path(dir1)
    dir2 = Path(dir2)
    ids_1 = {file.name.split(".")[0]: file for file in dir1.iterdir() if file.is_file()}
    ids_2 = {file.name.split(".")[0]: file for file in dir2.iterdir() if file.is_file()}
    common_keys = set(ids_1.keys()) & set(ids_2.keys())
    print("Found %s common files" % len(common_keys))

    return common_keys


def keep_common_files(
    dir1: str | os.PathLike,
    dir2: str | os.PathLike,
    destination_directory: str | os.PathLike,
) -> None:
    # Convert string paths to Path objects
    dir1 = Path(dir1)
    dir2 = Path(dir2)
    destination_directory = Path(destination_directory)

    ids_1 = {file.name.split(".")[0]: file for file in dir1.iterdir() if file.is_file()}
    print("Found %s files in the first directory" % len(ids_1))
    ids_2 = {file.name.split(".")[0]: file for file in dir2.iterdir() if file.is_file()}
    print("Found %s files in the second directory" % len(ids_2))

    # Find the common files
    common_keys = set(ids_1.keys()) & set(ids_2.keys())
    print("Found %s common files" % len(common_keys))

    destination_directory.mkdir(parents=True, exist_ok=True)

    # Copy the common files to the destination directory
    for key in common_keys:
        shutil.copy(ids_2[key], destination_directory)


def main() -> None:
    dir1 = "/home/maccou/Bureau/stage-maccou/data/mv/old/stl_old_mesher"
    dir2 = "/home/share/deep-mesh/database/airbus/stl_brep"

    destination_directory = "/home/maccou/Bureau/stage-maccou/data/mv/stl"
    keep_common_files(dir1, dir2, destination_directory)
    # find_common_files(dir1, dir2)


if __name__ == "__main__":
    main()
