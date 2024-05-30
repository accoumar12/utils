from __future__ import annotations

import os

from Pathlib import Path


def search_folders(
    root_folder: str | os.PathLike,
    file_name: str,
    search_string: str,
) -> list[str]:
    matching_folders = []

    for file_path in Path(root_folder).rglob(file_name):
        with file_path.open() as f:
            if search_string in f.read():
                matching_folders.append(file_path.parent)

    return matching_folders


def main() -> None:
    root_folder = "/path/to/root/folder"
    file_name = "log.log"
    target_string = "HardSemiHardTripletMarginWithDistanceLoss"
    matching_folders = search_folders(root_folder, file_name, target_string)

    for folder in matching_folders:
        print(folder)


if __name__ == "__main__":
    main()
